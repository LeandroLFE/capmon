from bot.cogs.commands.user_channel.cap_aux.cap_db_connect import Cap_DB_Connect
from twitchio.ext.commands import Cog, command

class Cap(Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.db = Cap_DB_Connect()
        self.envia_msg_with_context = self.bot.cogs['Envia_Msg'].envia_msg_with_context

    @command(name='cap')
    async def command_cap(self, ctx, tentativas='', criatura_item='', item=''):
        if ctx.channel.name == self.bot.nick:
            return

        _canal_id = ctx.message.tags["room-id"]
        _dados_horda = self.bot.dados_horda[_canal_id]
        _aventureiro_nome = ctx.author.name
        _aventureiro_id = ctx.author.id
        _nome_idioma = _dados_horda["nome_idioma"]

        _aventureiro = await self.db.consulta_aventureiro({
            "canal_id": _canal_id,
            "aventureiro_id": _aventureiro_id
        })

        if _aventureiro == None:
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

        _dados_canal = {
            "canal_id": _canal_id,
            "nome_canal": ctx.channel.name,
            "nome_idioma": _nome_idioma
        }

        if _dados_horda["nome_horda"] == "" or _dados_horda["nome_horda"] == "capraid":
            self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                   "user_channel", "cap_messages", "error_horde_inactive",
                                                                   {
                                                                       "nome_horda": _dados_horda["nome_horda"],
                                                                       "aventureiro": _aventureiro_nome
                                                                   })
            await self.envia_msg_with_context(ctx, self.message)
            return

        if not str(tentativas).isnumeric() and str(criatura_item).isnumeric():
            tentativas, criatura_item = criatura_item, tentativas

        _criatura = [c for c in _dados_horda["criaturas"]
                     if self.bot.remover_acentos(c["nome"]) == criatura_item]

        _criatura = _criatura[0] if _criatura != [] else {}

        if _dados_horda["criaturas"] != [] and _criatura == {}:

            _opcoes = [self.bot.remover_acentos(
                c["nome"]) for c in _dados_horda["criaturas"]]

            self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"],
                                                                   "user_channel", "cap_messages", "error_invalid_creature",
                                                                   {
                "aventureiro": _aventureiro_nome,
                "opcoes": _opcoes
            })
            await self.envia_msg_with_context(ctx, self.message)
            return

        elif _dados_horda["criaturas"] != []:
            _dados_horda["criatura"] = _criatura

        _custo = _dados_horda["criatura"]["custo"]

        _dados_aventureiro = {
            "aventureiro_id": _aventureiro_id,
            "nome": _aventureiro_nome,
            "ctx": ctx,
            "capcoins" : _aventureiro["capcoins"],
            "tentativas": tentativas,
            "criatura_item": criatura_item,
            "item": item,
            "capturou": False,
            "tabela": _aventureiro
        }

        _criatura_ja_capturada = None
        _capturou = False
        _capturou_especial = False

        _criatura = _dados_horda["criatura"]

        _parametros_criatura = await self.db.consulta_parametros_criatura({
            "criatura_nome": _criatura["nome"]
        })

        if not _aventureiro_novo:
            _criatura_ja_capturada = await self.db.consulta_se_ja_tem_capturada({
                "canal_id": _dados_canal["canal_id"],
                "aventureiro_id": _aventureiro_id,
                "nome_criatura":  _dados_horda["criatura"]["nome"],
            })

        _ja_capturou_antes = True

        if _criatura_ja_capturada == None:
            _ja_capturou_antes = False
            _criatura_ja_capturada = {
                "cp": 0,
                "especial": _capturou_especial
            }

        _dados_horda["criatura_ja_capturada"] = _criatura_ja_capturada
        _dados_horda["dados_aventureiro"] = _dados_aventureiro

        dados = {
            "dados_canal": _dados_canal,
            "dados_horda": _dados_horda,
        }

        _aventureiro_tabela = [a for a in _dados_horda["aventureiros"]
                               if a["aventureiro_id"] == _aventureiro["aventureiro_id"]]
        if _aventureiro_tabela != []:
            _aventureiro_tabela = _aventureiro_tabela[0]
            _dados_horda["dados_aventureiro"] = _aventureiro_tabela

            self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                   "user_channel", "cap_messages", "error_adventure_already_participated", _dados_horda)
            await self.envia_msg_with_context(ctx, self.message)
            return

        if not str(tentativas).isnumeric():
            self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"],
                                                                   "user_channel", "cap_messages", "error_invalid_attempties",
                                                                   {
                "nome_horda": _dados_horda["nome_horda"],
                "aventureiro": _aventureiro_nome,
                "custo": _custo,
                "criaturas": _dados_horda["criaturas"]
            })
            await self.envia_msg_with_context(ctx, self.message)
            return

        _capturado = {
                "aventureiro_id": _aventureiro_id,
                "id_criatura": 0,
                "cp": 0,
                "golpe": 0,
                "criatura_tipo": 0,
                "custo_capcoins": 0,
                "especial": 0,
            }

        tentativas = int(tentativas)

        _dados_aventureiro["tentativas"] = tentativas

        if tentativas < 0:
            tentativas = _parametros_criatura["num_tentativas_caso_zero_ou_negativo"]

        elif tentativas == 0:

            _dados_horda["aventureiros"].append(_dados_aventureiro)
            self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"],
                                                                   "user_channel", "cap_messages", "cap_command_skip_message",
                                                                   _dados_horda)
            await self.envia_msg_with_context(ctx, self.message)
            return

        _custo_capcoins = tentativas * _criatura["custo"]

        if _custo_capcoins > _aventureiro["capcoins"]:
            self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"],
                                                                   "user_channel", "cap_messages", "error_overload_attempties",
                                                                   {
                "aventureiro": _aventureiro_nome,
                "custo": _custo,
                "capcoins": _aventureiro["capcoins"]
            })
            await self.envia_msg_with_context(ctx, self.message)
            return

        _chance_captura = _parametros_criatura["chance_captura"]
        _chance_especial = _parametros_criatura["chance_especial"]

        if ctx.author.is_subscriber:
            _vantagens_subs_canal = await self.db.consulta_vantagens_subs_canal(_dados_canal)
            if _vantagens_subs_canal["habilita_vantagens_subs"]:
                _chance_captura += _vantagens_subs_canal["aumento_chance_captura"]
                _chance_especial += _vantagens_subs_canal["aumento_chance_especial"]

        if _dados_aventureiro["item"] != '':
            _itens_obtidos = await self.db.consulta_itens_obtidos({
                "aventureiro_id": _aventureiro_id,
                "canal_id": _dados_canal["canal_id"],
                "nome_idioma": _dados_canal["nome_idioma"],
            })

        for _ in range(tentativas):
            _sorteio_captura = self.bot.random_randint(1, 100)
            if _sorteio_captura <= _chance_captura:
                _capturou = True
                break

        _dados_aventureiro["capcoins"] -=  _custo_capcoins

        if _capturou:

            _sorteio_especial = self.bot.random_randint(1, 100)

            if _sorteio_especial <= _chance_especial:
                _capturou_especial = True

            _atributo = self.bot.random_choice([_dados_horda["criatura"]["nome_atributo1"], _dados_horda["criatura"]["nome_atributo2"]
                                                ]) if _dados_horda["criatura"]["nome_atributo2"] != None else _dados_horda["criatura"]["nome_atributo1"]

            _cp = _dados_horda["criatura_ja_capturada"]["cp"] + ( self.bot.random_randint(
                  _dados_horda["criatura"]["cp_min"] * 0.1, _dados_horda["criatura"]["cp_max"] * 0.1)) if _ja_capturou_antes else _parametros_criatura["cp_inicial"]
            _cp = _cp if _cp <= _dados_horda["criatura"]["cp_limite"] else _dados_horda["criatura"]["cp_limite"]

            _capturado = {
                "aventureiro_id": _aventureiro_id,
                "id_criatura": _dados_horda["criatura"]["num"],
                "cp": _cp,
                "golpe": _atributo,
                "criatura_tipo": _dados_horda["criatura"]["nome_tipo"],
                "custo_capcoins": _custo_capcoins,
                "especial": _capturou_especial,
            }

            _dados_horda["capturado"] = _capturado
            _dados_horda["capturados"].append(_capturado)

            _dados_aventureiro["capturou"] = True

        else:
            _capturado["custo_capcoins"] = _custo_capcoins
            _dados_horda["capturado"] = _capturado
            _dados_horda["capturados"].append(_capturado)

        _dados_horda["aventureiros"].append(_dados_aventureiro)

        self.message = self.bot.import_message_language_by_one(_dados_canal["nome_idioma"],
                                                               "user_channel", "cap_messages", "cap_command_capture_messages",
                                                               dados)
        await self.envia_msg_with_context(ctx, self.message)

    