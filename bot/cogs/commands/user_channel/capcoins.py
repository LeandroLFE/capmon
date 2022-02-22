from twitchio.ext.commands import Cog, command
from bot.cogs.commands.user_channel.capcoins_aux.capcoins_db_connect import Capcoins_DB_Connect

class Capcoins(Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.db = Capcoins_DB_Connect()
        self.envia_msg_with_context = self.bot.cogs['Envia_Msg'].envia_msg_with_context

    @command(name='capcoins')
    async def command_capcoins(self, ctx, pessoa=''):
        if ctx.channel.name == self.bot.nick:
            return

        _canal_id = ctx.message.tags["room-id"]
        _dados_horda = self.bot.dados_horda[_canal_id]
        _nome_idioma = _dados_horda["nome_idioma"]

        _aventureiro_id = ctx.author.id
        _aventureiro_nome = ctx.author.name

        if ctx.author.is_mod and pessoa != '':
            pessoa = pessoa[1:] if pessoa.startswith('@', 0, 1) else pessoa
            _aventureiro_nome = self.bot.remover_acentos(pessoa)
            _aventureiro = await self.db.consulta_aventureiro({
                "canal_id" : _canal_id,
                "aventureiro_nome" : _aventureiro_nome
            })

            if _aventureiro is None:
                self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capcoins_messages", "person_not_found",
                                                                {})
                await self.envia_msg_with_context(ctx, self.message)
                return
                
            _aventureiro_id = _aventureiro["aventureiro_id"]
            _capcoins = {
                "capcoins" : _aventureiro["capcoins"],
            }

        else:
            _capcoins = await self.db.consulta_capcoins({
                "canal_id" : _canal_id,
                "aventureiro_id" : _aventureiro_id
            })

            if _capcoins is None:
                await self.db.insert_aventureiro({
                    "canal_id": _canal_id,
                    "aventureiro_id": _aventureiro_id,
                    "aventureiro_nome": _aventureiro_nome,
                })
                _capcoins = await self.db.consulta_capcoins({
                    "canal_id" : _canal_id,
                    "aventureiro_id" : _aventureiro_id
                })  

        _itens_obtidos_capshop = await self.db.consulta_itens_obtidos_capshop({
            "canal_id" : _canal_id,
            "aventureiro_id" : _aventureiro_id,
            "nome_idioma" : _nome_idioma,
        })

        _itens_obtidos_capraid = await self.db.consulta_itens_obtidos_capraid({
            "canal_id" : _canal_id,
            "aventureiro_id" : _aventureiro_id,
            "nome_idioma" : _nome_idioma,
        })
        
        if _itens_obtidos_capshop == [] and _itens_obtidos_capraid == []:
            _itens_obtidos = []
        elif _itens_obtidos_capshop != [] and _itens_obtidos_capraid != []:
            _itens_obtidos = _itens_obtidos_capshop + _itens_obtidos_capraid
        elif _itens_obtidos_capshop != []:
            _itens_obtidos = _itens_obtidos_capshop
        else:
            _itens_obtidos = _itens_obtidos_capraid

        if _dados_horda["nome_horda"] != "" and _dados_horda["nome_horda"] != "capraid":
            _aventureiro_tabela = [a for a in _dados_horda["aventureiros"] if a["aventureiro_id"] == _aventureiro_id]  
            if _aventureiro_tabela != []:
                _aventureiro_tabela = _aventureiro_tabela[0]
                _capcoins["capcoins"] = _aventureiro_tabela["capcoins"]

        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capcoins_messages", "msg_capcoins",
                                                                {
                                                                    "aventureiro_nome" : _aventureiro_nome,
                                                                    "capcoins": _capcoins["capcoins"],
                                                                    "itens_obtidos": _itens_obtidos,
                                                                })
        await self.envia_msg_with_context(ctx, self.message)

    @command(name='capcoins+')
    async def command_capcoins_plus(self, ctx, pessoa='', qtde=''):
        if ctx.channel.name == self.bot.nick:
            return

        _canal_id = ctx.message.tags["room-id"]
        _dados_horda = self.bot.dados_horda[_canal_id]
        _nome_idioma = _dados_horda["nome_idioma"]
        _aventureiro_nome = ctx.author.name

        try:
            qtde = int(qtde)
        except ValueError as e:
            try:
                pessoa = int(pessoa)
            
            except ValueError as e:
                self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                        "user_channel", "capcoins_messages", "invalid_amount",
                                                                        {})
                await self.envia_msg_with_context(ctx, self.message)
                return

            else:
                pessoa, qtde = qtde, pessoa

        if not ctx.author.is_mod:
            self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                    "user_channel", "capcoins_messages", "not_allowed",
                                                                    {"moderador" : ctx.author.name})
            await self.envia_msg_with_context(ctx, self.message)
            return

        pessoa = pessoa[1:] if pessoa.startswith('@', 0, 1) else pessoa
        
        _aventureiro_nome = self.bot.remover_acentos(pessoa)
        _aventureiro_tabela = []

        if _dados_horda["nome_horda"] != "" and _dados_horda["nome_horda"] != "capraid":
            _aventureiro_tabela = [a for a in _dados_horda["aventureiros"] if a["nome"] == _aventureiro_nome]  
            if _aventureiro_tabela != []:
                _aventureiro = _aventureiro_tabela[0]
            else:
                _aventureiro = await self.db.consulta_aventureiro({
                    "canal_id" : _canal_id,
                    "aventureiro_nome" : _aventureiro_nome
                })
                if _aventureiro is None:
                    self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                    "user_channel", "capcoins_messages", "person_not_found",
                                                                    {})
                    await self.envia_msg_with_context(ctx, self.message)
                    return
        else:
            _aventureiro = await self.db.consulta_aventureiro({
                    "canal_id" : _canal_id,
                    "aventureiro_nome" : _aventureiro_nome
                })

            if _aventureiro is None:
                self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capcoins_messages", "person_not_found",
                                                                {})
                await self.envia_msg_with_context(ctx, self.message)
                return
        
        _aventureiro["capcoins"] += qtde

        if _aventureiro_tabela == []:
            _aventureiro["canal_id"] = _canal_id
            await self.db.update_capcoins_aventureiro(_aventureiro)

        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capcoins_messages", "msg_add_capcoins",
                                                                {
                                                                    "moderador" : ctx.author.name,
                                                                    "aventureiro_nome" : _aventureiro_nome,
                                                                    "capcoins": qtde,
                                                                })
        await self.envia_msg_with_context(ctx, self.message)
