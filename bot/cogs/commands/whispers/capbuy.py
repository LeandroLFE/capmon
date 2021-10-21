from twitchio.ext.commands import Cog, command
from bot.cogs.commands.whispers.whispers_aux.whispers_db_connect import Whispers_DB_Connect

class Capbuy(Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.db = Whispers_DB_Connect()
        self.envia_msg_whisper = self.bot.cogs['Envia_Msg'].envia_msg_whisper

    async def listen_whisper(self, _dados_whisper):

        _aventureiro_id_test = f"""_aventureiro_id_{_dados_whisper["aventureiro_id"]}"""        
        _tasks = self.bot.asyncio_all_tasks(self.bot.loop)
        _sessao = [task for task in _tasks if _aventureiro_id_test in task.get_name()]

        if _sessao == []:
            return

        if _dados_whisper["aventureiro_id"] not in self.bot.sessao_ativa.keys():
            return

        if self.bot.sessao_ativa[_dados_whisper["aventureiro_id"]]["tipo"] != "capshop":
            return

        _dados_aventureiro = self.bot.sessao_ativa[_dados_whisper["aventureiro_id"]]["dados"]["aventureiro"]
        _nome_idioma = self.bot.sessao_ativa[_dados_whisper["aventureiro_id"]]["dados"]["nome_idioma"]
        _canal_id = _dados_aventureiro["canal_id"]
        _dados_horda = self.bot.dados_horda[_canal_id]
        
        if len(_dados_whisper["comando"]) == 1:
 
            self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                               "user_channel", "capbuy_messages", "invalid_parameter",
                                                               {}
                                                               )

            await self.envia_msg_whisper(_dados_aventureiro, self.message)
            return
        
        item_a_adquirir = [i for i in self.bot.sessao_ativa[_dados_whisper["aventureiro_id"]]["dados"]["itens"] if i["id_item_capshop"] == _dados_whisper["comando"][1]]

        if item_a_adquirir == []:
            self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                               "user_channel", "capbuy_messages", "invalid_parameter",
                                                               {}
                                                               )

            await self.envia_msg_whisper(_dados_aventureiro, self.message)
            return

        item_a_adquirir = item_a_adquirir[0]
        
        _custo_capcoins = item_a_adquirir["custo_em_capcoins"]

        if _dados_horda["nome_horda"] != "" and _dados_horda["nome_horda"] != "capraid":
            _aventureiro_tabela = [a for a in _dados_horda["aventureiros"] if a["aventureiro_id"] == _dados_whisper["aventureiro_id"]]  
            if _aventureiro_tabela != []:
                _aventureiro_tabela = _aventureiro_tabela[0]            

                if _aventureiro_tabela["capcoins"] - _custo_capcoins < 0:
                    self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                               "user_channel", "capbuy_messages", "without_capcoins",
                                                                {
                                                                    "nome_item" : item_a_adquirir["nome"],
                                                                    "custo_em_capcoins" : _custo_capcoins,
                                                                    "capcoins" : _aventureiro_tabela["capcoins"]   
                                                                })

                    await self.envia_msg_whisper(_dados_aventureiro, self.message)
                    return

                _aventureiro_tabela["capcoins"] -= _custo_capcoins  
                await self.db.insert_update_itens_obtidos({
                                            "canal_id" : _canal_id,
                                            "aventureiro_id": _aventureiro_tabela["aventureiro_id"],
                                            "tipo_item" : item_a_adquirir["tipo_capshop"],
                                            "id_item" : item_a_adquirir["id"],
                                            "qtde" : 1
                                        })
                self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capbuy_messages", "obtained_item",
                                                                {
                                                                    "aventureiro_nome" : _dados_aventureiro["aventureiro_nome"],
                                                                    "nome_item" : item_a_adquirir["nome"]
                                                                })

                await self.envia_msg_whisper(_dados_aventureiro, self.message)
                return

        _aventureiro_tabela = await self.db.consulta_aventureiro({
            "canal_id": _canal_id,
            "aventureiro_id": _dados_whisper["aventureiro_id"]
        })

        if _aventureiro_tabela["capcoins"] - _custo_capcoins < 0:
            self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                               "user_channel", "capbuy_messages", "without_capcoins",
                                                                {
                                                                    "nome_item" : item_a_adquirir["nome"],
                                                                    "custo_em_capcoins" : _custo_capcoins,
                                                                    "capcoins" : _aventureiro_tabela["capcoins"]   
                                                                })

            await self.envia_msg_whisper(_dados_aventureiro, self.message)
            return

        _aventureiro_tabela["capcoins"] -= _custo_capcoins  
        await self.db.insert_update_itens_obtidos({
                                            "canal_id" : _canal_id,
                                            "aventureiro_id": _aventureiro_tabela["aventureiro_id"],
                                            "tipo_item" : item_a_adquirir["tipo_capshop"],
                                            "id_item" : item_a_adquirir["id"],
                                            "qtde" : 1
                                        })
        _aventureiro_tabela["canal_id"] = _canal_id
        await self.db.update_capcoins_aventureiro(_aventureiro_tabela)
        self.message = self.bot.import_message_language_by_one(_nome_idioma,
                                                                "user_channel", "capbuy_messages", "obtained_item",
                                                                {
                                                                    "aventureiro_nome" : _dados_aventureiro["aventureiro_nome"],
                                                                    "nome_item" : item_a_adquirir["nome"]
                                                                })

        await self.envia_msg_whisper(_dados_aventureiro, self.message)