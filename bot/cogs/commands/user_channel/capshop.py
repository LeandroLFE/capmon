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
        _dados_horda = self.bot.dados_horda[_canal_id]
        _nome_idioma = _dados_horda["nome_idioma"]

        _aventureiro_id = ctx.author.id
        _aventureiro_nome = ctx.author.name

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

        itens_capshop = await self.db.consulta_itens_capshop({
            "nome_idioma": _nome_idioma,
        })

        _dados_canal = {
            "canal_id": _canal_id,
            "nome_canal": ctx.channel.name,
            "nome_idioma": _nome_idioma
        }

        desconto = 0
        plus = False

        _vantagens_subs_canal = await self.db.consulta_vantagens_subs_canal(_dados_canal)
        if _vantagens_subs_canal["habilita_vantagens_subs"] and _vantagens_subs_canal["acesso_exclusivo_capshop"]:
            if ctx.author.is_subscriber == '1':
                desconto = _vantagens_subs_canal["desconto_capshop_percent"]
                for i in itens_capshop:
                    # exclui o item capcandy dos descontos
                    i["custo_em_capcoins"] *= (100 -
                                               desconto)/100 if i["id_item_capshop"] != 3 else 1

                    i["custo_em_capcoins"] = int(i["custo_em_capcoins"])

                plus = True
                self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                       "user_channel", "capshop_messages", "welcome",
                                                                       {
                                                                           "plus": plus,
                                                                       })
            else:
                itens_capshop = [
                    i for i in itens_capshop if i["item_capshop_plus"] == 0]
                self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                       "user_channel", "capshop_messages", "welcome",
                                                                       {
                                                                           "plus": plus,
                                                                       })
        else:
            self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                   "user_channel", "capshop_messages", "welcome",
                                                                   {
                                                                       "plus": plus
                                                                   })

        await self.envia_msg_whisper(ctx, self.message)

        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                               "user_channel", "capshop_messages", "capshop_items_msg",
                                                               {
                                                                   "itens": itens_capshop
                                                               })

        await self.envia_msg_whisper(ctx, self.message)

        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                               "user_channel", "capshop_messages", "wait_for_user_to_buy",
                                                               {}
                                                               )

        await self.envia_msg_whisper(ctx, self.message)
