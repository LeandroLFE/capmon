from twitchio.ext.commands import Cog, command
from bot.cogs.commands.user_channel.capshop_aux.capshop_db_connect import Capshop_DB_Connect

class Capshop(Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.db = Capshop_DB_Connect()
        self.envia_msg_whisper = self.bot.cogs['Envia_Msg'].envia_msg_whisper

    @command(name='capshop')
    async def command_capshop(self, ctx, pessoa=''):
        if ctx.channel.name == self.bot.nick:
            return

        _canal_id = ctx.message.tags["room-id"]
        _nome_canal = ctx.channel.name
        _dados_horda = self.bot.dados_horda[_canal_id]
        _nome_idioma = _dados_horda["nome_idioma"]

        _aventureiro_id = ctx.author.id
        _aventureiro_nome = ctx.author.name

        _aventureiro_id_test = f"capshop_aventureiro_id_{_aventureiro_id}"
        
        _tasks = self.bot.asyncio_all_tasks(self.bot.loop)
        _sessao_task = [task for task in _tasks if _aventureiro_id_test in task.get_name()]

        if _sessao_task != []:
            return

        _aventureiro = await self.db.consulta_aventureiro({
            "canal_id": _canal_id,
            "aventureiro_id": _aventureiro_id
        })

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

        if _aventureiro == None:
            await self.db.insert_aventureiro(_dados_aventureiro)
            _aventureiro = await self.db.consulta_aventureiro(_dados_aventureiro)

        itens_capshop = await self.db.consulta_itens_capshop({
            "nome_idioma": _nome_idioma,
        })

        desconto = 0
        _plus = False

        _vantagens_subs_canal = await self.db.consulta_vantagens_subs_canal(_dados_aventureiro)
        if _vantagens_subs_canal["habilita_vantagens_subs"] and _vantagens_subs_canal["acesso_exclusivo_capshop"]:
            if ctx.author.is_subscriber == '1':
                desconto = _vantagens_subs_canal["desconto_capshop_percent"]
                for i in itens_capshop:
                    # exclui o item capcandy dos descontos
                    i["custo_em_capcoins"] *= (100 -
                                               desconto)/100 if i["id_item_capshop"] != '3' else 1

                    i["custo_em_capcoins"] = int(i["custo_em_capcoins"])

                _plus = True
                self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                       "user_channel", "capshop_messages", "welcome",
                                                                       {
                                                                           "plus": _plus,
                                                                       })
            else:
                itens_capshop = [
                    i for i in itens_capshop if i["item_capshop_plus"] == 0]
                self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                       "user_channel", "capshop_messages", "welcome",
                                                                       {
                                                                           "plus": _plus,
                                                                       })
        else:
            self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                   "user_channel", "capshop_messages", "welcome",
                                                                   {
                                                                       "plus": _plus
                                                                   })

        await self.envia_msg_whisper(_dados_aventureiro, self.message)

        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                               "user_channel", "capshop_messages", "capshop_items_msg",
                                                               {
                                                                   "itens": itens_capshop
                                                               })

        await self.envia_msg_whisper(_dados_aventureiro, self.message)

        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                               "user_channel", "capshop_messages", "wait_for_user_to_buy",
                                                               {}
                                                               )

        await self.envia_msg_whisper(_dados_aventureiro, self.message)

        self.bot.sessao_ativa[_aventureiro_id] = {
            "tipo" : "capshop",
            "dados" : {
                "aventureiro" : _dados_aventureiro,
                "itens" : itens_capshop,
                "nome_idioma" : _nome_idioma
            }
        }

        _task = self.bot.loop.create_task(self.bot.aguarda(self, _parametros_gerais["tempo_sessao_capshop"]))        
        _nome_task = self.bot.import_message_language_by_one("general",
                                                            "task_names", "nomes_tasks", "task_aguarda_expiracao_capshop",
                                                            _dados_aventureiro
                                                            )
        _task.set_name(_nome_task)
        _task.add_done_callback(self.bot.functools_partial(self.conclui_aguardo_expiracao_capshop_sync, _dados_aventureiro))     


    def conclui_aguardo_expiracao_capshop_sync(self, dados_aventureiro, future):
        if not future.done() or future.cancelled():
            return
        
        _aventureiro_id = dados_aventureiro["aventureiro_id"]
        _nome_idioma = self.bot.sessao_ativa[_aventureiro_id]["dados"]["nome_idioma"] if _aventureiro_id in self.bot.sessao_ativa.keys() else None

        if _nome_idioma == None:
            return   

        future.cancel()
        self.bot.sessao_ativa.pop(_aventureiro_id, None)

        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                               "user_channel", "capshop_messages", "end_session",
                                                               {}
                                                               )

        self.bot.loop.create_task(self.envia_msg_whisper(dados_aventureiro, self.message))