from bot.cogs.commands.user_channel.capmon_aux.capmon_db_connect import Capmon_DB_Connect
from twitchio.ext.commands import Cog, command

class Capmon(Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.db = Capmon_DB_Connect()
        self.envia_msg_with_context = self.bot.cogs['Envia_Msg'].envia_msg_with_context
        self.envia_msg_whisper = self.bot.cogs['Envia_Msg'].envia_msg_whisper

    @command(name='capmon')
    async def command_capmon(self, ctx, filtro=''):
        if ctx.channel.name == self.bot.nick:
            return

        _canal_id = ctx.message.tags["room-id"]
        _nome_canal = ctx.channel.name
        _dados_horda = self.bot.dados_horda[_canal_id]
        _aventureiro_nome = ctx.author.name
        _aventureiro_id = ctx.author.id
        _nome_idioma = _dados_horda["nome_idioma"]

        _aventureiro = await self.db.consulta_aventureiro({
            "canal_id": _canal_id,
            "aventureiro_id": _aventureiro_id
        })

        if _aventureiro is None:
            await self.db.insert_aventureiro({
                "canal_id": _canal_id,
                "aventureiro_id": _aventureiro_id,
                "aventureiro_nome": _aventureiro_nome,
            })
            _aventureiro = await self.db.consulta_aventureiro({
                "canal_id": _canal_id,
                "aventureiro_id": _aventureiro_id
            })
            _aventureiro_novo = True

        else:
            _aventureiro_novo = False

        if filtro == '':
            _lista_tipos_dict = await self.db.consulta_tipos_disponiveis({})
            _lista_tipos = [i['nome'].lower() for i in _lista_tipos_dict]
            _lista_tipos_str = ", ".join(_lista_tipos)

            self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capmon_messages", "msg_invalid_filter",
                                                                {
                                                                    "aventureiro_nome" : _aventureiro_nome,
                                                                    "lista_tipos" : _lista_tipos_str,
                                                                })
            await self.envia_msg_with_context(ctx, self.message)
            return

        if _aventureiro_novo:
            #sem criaturas
            self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capmon_messages", "msg_no_creatures",
                                                                {
                                                                    "aventureiro_nome" : _aventureiro_nome,
                                                                })
            await self.envia_msg_with_context(ctx, self.message)
            return
        
        _lista_tipos_dict = await self.db.consulta_tipos_disponiveis({})
        _lista_tipos = [i['nome'].lower() for i in _lista_tipos_dict]
        _lista_tipos_str = ", ".join(_lista_tipos)

        _lista_atributos_dict = await self.db.consulta_atributos_disponiveis({"nome_idioma" : _nome_idioma})
        _lista_atributos = [ i['nome'].lower() for i in _lista_atributos_dict]
        _lista_atributos_str = ", ".join([i['nome'].lower() for i in _lista_atributos_dict if i["nome_idioma"].lower() == _nome_idioma])

        # raridades = custos
        _lista_raridades_dict = await self.db.consulta_custos_disponiveis({"nome_idioma" : _nome_idioma})
        _lista_raridades = [i['nome'].lower() for i in _lista_raridades_dict]
        _lista_raridades_ref = set([i['ref'] for i in _lista_raridades_dict])
        _lista_raridades_str = ", ".join([i['nome'].lower() for i in _lista_raridades_dict if i["nome_idioma"].lower() == _nome_idioma])
         

        _lista_especiais_dict = await self.db.consulta_especiais_disponiveis({"nome_idioma" : _nome_idioma})
        _lista_especiais = [i['nome'].lower() for i in _lista_especiais_dict]
        _lista_especiais_str = ", ".join([i['nome'].lower() for i in _lista_especiais_dict if i["nome_idioma"].lower() == _nome_idioma])

        filtros_possiveis = _lista_tipos + _lista_atributos + _lista_raridades + _lista_especiais

        # if filtro not in _lista_tipos and filtro not in _lista_atributos and filtro not in _lista_raridades and filtro not in _lista_especiais:
        if filtro not in filtros_possiveis:
            filtro_singular = filtro[:-1] if filtro[-1] == "s" else filtro
            if filtro_singular not in filtros_possiveis:
                #filtro inválido
                self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                    "user_channel", "capmon_messages", "msg_invalid_filter",
                                                                    {
                                                                        "aventureiro_nome" : _aventureiro_nome,
                                                                        "lista_tipos" : _lista_tipos_str,
                                                                        "lista_atributos" : _lista_atributos_str,
                                                                        "lista_raridades" : _lista_raridades_str,
                                                                        "lista_especiais" : _lista_especiais_str,
                                                                    })
                await self.envia_msg_with_context(ctx, self.message)
                return
            
            else:
                filtro = filtro_singular

        if filtro in _lista_tipos:
            _tipo_filtrado = [i for i in _lista_tipos_dict if i["nome"].lower() == filtro][0]
            _capturados_filtro = await self.db.seleciona_capturados_tipo({
                "canal_id" : _canal_id,
                "aventureiro_id" : _aventureiro_id,
                "nome_idioma" : _nome_idioma,
                "tipo" : _tipo_filtrado["ref"],
            })
            _tipo_exibido = "type"

        elif filtro in _lista_atributos:
            _atributo_filtrado = [i for i in _lista_atributos_dict if i["nome"].lower() == filtro][0]
            _capturados_filtro = await self.db.seleciona_capturados_atributo({
                "canal_id" : _canal_id,
                "aventureiro_id" : _aventureiro_id,
                "nome_idioma" : _nome_idioma,
                "atributo" : _atributo_filtrado["ref"],
            })
            _tipo_exibido = "attribute"

        elif filtro in _lista_raridades:
            _raridade_filtrada = [i for i in _lista_raridades_dict if i["nome"].lower() == filtro][0]
            _capturados_filtro = await self.db.seleciona_capturados_raridade({
                "canal_id" : _canal_id,
                "aventureiro_id" : _aventureiro_id,
                "nome_idioma" : _nome_idioma,
                "raridade" : _raridade_filtrada["ref"],
            })
            _tipo_exibido = "rarity"

        else:
            # _especiais_filtrado = [i for i in _lista_especiais_dict if i["nome"].lower() == filtro][0]
            
            # especiais = outros
            _capturados_filtro = await self.db.seleciona_capturados_especial({
                "canal_id" : _canal_id,
                "aventureiro_id" : _aventureiro_id,
                "nome_idioma" : _nome_idioma,
            })
            _tipo_exibido = "other"

        if _capturados_filtro == []:
            #sem criaturas
            self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capmon_messages", "msg_no_creatures",
                                                                {
                                                                    "aventureiro_nome" : _aventureiro_nome,
                                                                })
            await self.envia_msg_with_context(ctx, self.message)
            return

        _qtde = len(_capturados_filtro)
        _qtde_especial = len([e for e in _capturados_filtro if e["especial"]])

        #imprime: Você possui {qtde} criaturas do atributo {_filtro}, sendo {_especial} especiais.
        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capmon_messages", "msg_show_captured",
                                                                {
                                                                    "aventureiro_nome" : _aventureiro_nome,
                                                                    "tipo_exibido" : _tipo_exibido,
                                                                    "qtde" : _qtde,
                                                                    "filtro" : filtro,
                                                                    "qtde_especial" : _qtde_especial,
                                                                })
        await self.envia_msg_with_context(ctx, self.message)

        _aventureiro_id_test = f"capmon_aventureiro_id_{_aventureiro_id}"
        
        _tasks = self.bot.asyncio_all_tasks(self.bot.loop)
        _sessao_task = [task for task in _tasks if _aventureiro_id_test in task.get_name()]

        if _sessao_task != []:
            return

        _parametros_gerais = await self.db.consulta_parametros_gerais({
            "canal_id" : _canal_id
        })

        _dados_aventureiro = {
            "canal_id": _canal_id,
            "nome_canal" : _nome_canal,
            "aventureiro_id": _aventureiro_id,
            "aventureiro_nome": _aventureiro_nome,
            "parametros_gerais" : _parametros_gerais
        }        

        if _aventureiro is None:
            await self.db.insert_aventureiro(_dados_aventureiro)
            _aventureiro = await self.db.consulta_aventureiro(_dados_aventureiro)
        
        self.bot.sessao_ativa[_aventureiro_id] = {
            "tipo" : "capmon",
            "dados" : {
                "aventureiro" : _dados_aventureiro,
                "criaturas_filtro" : _capturados_filtro,
                "nome_idioma" : _nome_idioma
            }
        }

        _task = self.bot.loop.create_task(self.bot.aguarda(self, _parametros_gerais["tempo_sessao_capmon"]))        
        _nome_task = self.bot.import_message_language_by_one("general",
                                                            "task_names", "nomes_tasks", "task_aguarda_expiracao_capmon",
                                                            _dados_aventureiro
                                                            )
        _task.set_name(_nome_task)
        _task.add_done_callback(self.bot.functools_partial(self.conclui_aguardo_expiracao_capmon_sync, _dados_aventureiro))  

        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capmon_messages", "msg_start_show_captured_whisper",
                                                                {"aventureiro_nome": _aventureiro_nome,}
                                                            )

        self.bot.loop.create_task(self.envia_msg_whisper(_dados_aventureiro, self.message))

        _capturados_filtro_custo = set([c["nome_custo"] for c in _capturados_filtro])
        
        _criaturas_filtradas = {}

        for criatura in _capturados_filtro:
            try:
                _criaturas_filtradas[criatura["nome_custo"]] += [criatura]
            except Exception as e:
                _criaturas_filtradas[criatura["nome_custo"]] = [criatura]

        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capmon_messages", "msg_show_captured_whisper",
                                                                {
                                                                    "aventureiro" : _dados_aventureiro,
                                                                    "criaturas" : _criaturas_filtradas,
                                                                    "raridades" :_capturados_filtro_custo,
                                                                }
                                                            )

        self.bot.loop.create_task(self.envia_msg_whisper(_dados_aventureiro, self.message))


    def conclui_aguardo_expiracao_capmon_sync(self, dados_aventureiro, future):
        if not future.done() or future.cancelled():
            return
        
        _aventureiro_id = dados_aventureiro["aventureiro_id"]
        _nome_idioma = self.bot.sessao_ativa[_aventureiro_id]["dados"]["nome_idioma"] if _aventureiro_id in self.bot.sessao_ativa.keys() else None

        if _nome_idioma is None:
            return   

        future.cancel()
        self.bot.sessao_ativa.pop(_aventureiro_id, None)

        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                               "user_channel", "capmon_messages", "end_session",
                                                               {}
                                                               )

        self.bot.loop.create_task(self.envia_msg_whisper(dados_aventureiro, self.message))



