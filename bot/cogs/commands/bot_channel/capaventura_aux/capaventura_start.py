async def capaventura_start(self, ctx, idioma_canal):
        _aventureiro = self.remover_acentos(ctx.author.name)
        _canal_id = ctx.message.tags["user-id"]
        
        _parametros_aventureiro = await self.db.consulta_parametros_aventureiros_novo_canal()

        dados = {
            "nome_idioma": idioma_canal, 
            "ativo": 1, 
            "nome_canal" : _aventureiro, 
            "aventureiro_nome" : _aventureiro,
            "canal_id" : _canal_id,
            "aventureiro_id" : _canal_id,
            "capcoins_iniciais": _parametros_aventureiro["capcoins_iniciais"]
        }

        canal = await self.db.consulta_canal_dado_um_id({
            "canal_id" : dados["canal_id"]
        })

        if canal == None or canal["ativo"] == 0:

            self.messages = self.import_message_language_by_one(dados["nome_idioma"], 
            "bot_channel", "capmon_channel_messages", "capmon_channel_messages_normal", 
            {"aventureiro":_aventureiro})

            await self.db.create_tables_with_underline_adventurer_name(dados)
            await self.db.insert_aventureiro(dados)
            await self.db.insert_canais(dados) if canal == None else await self.db.update_canais(dados)

            await self.send_msg.envia_msg_with_context(ctx, self.messages["start"])

        else:
            self.error_messages = self.import_message_language_by_one(dados["nome_idioma"], 
            "bot_channel", "capmon_channel_messages", "capmon_channel_messages_error", 
            {
                "aventureiro":_aventureiro,
                "idiomas": [i["nome"] for i in self.idiomas],
                "comandos": self.start_parameter_list() + self.language_parameter_list() + self.stop_parameter_list()    
            })
            await self.send_msg.envia_msg_with_context(ctx, self.error_messages["start"])