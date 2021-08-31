async def capaventura_language(self, ctx, _opt):
    _aventureiro = self.remover_acentos(ctx.author.name)
    _canal_id = ctx.message.tags["user-id"]

    aventureiro = await self.db.consulta_canal_dado_um_id({
        "canal_id" : _canal_id
    })

    _idioma_valido = [i["nome"] for i in self.idiomas if i["nome"] == _opt]

    if aventureiro == None or aventureiro["ativo"] == 0 or _idioma_valido == []:
        self.error_messages = self.import_message_language_by_one("english", 
            "bot_channel", "capmon_channel_messages", "capmon_channel_messages_error", 
            {
                "aventureiro":_aventureiro,
                "idiomas": [i["nome"] for i in self.idiomas],
                "comandos": self.start_parameter_list() + self.language_parameter_list() + self.stop_parameter_list()    
            })

        if aventureiro == None:
            await self.send_msg.envia_msg_with_context(ctx, self.error_messages["language_stop"])
        elif  aventureiro["ativo"] == 0:
            await self.send_msg.envia_msg_with_context(ctx, self.error_messages["language_inactive"])
        else:
            await self.send_msg.envia_msg_with_context(ctx, self.error_messages["language_invalid"])
        return

    dados = {
        "nome_idioma": _opt, 
        "nome_canal" : _aventureiro,
        "canal_id" : _canal_id,
        "ativo" : aventureiro["ativo"]
    }

    await self.db.update_canais(dados)
    
    self.messages = self.import_message_language_by_one(dados["nome_idioma"], 
    "bot_channel", "capmon_channel_messages", "capmon_channel_messages_normal", 
    {"aventureiro":_aventureiro})

    await self.send_msg.envia_msg_with_context(ctx, self.messages["language"])