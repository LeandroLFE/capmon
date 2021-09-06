async def capaventura_stop(self, ctx):
    _aventureiro = self.bot.remover_acentos(ctx.author.name)
    _canal_id = ctx.message.tags["user-id"]

    aventureiro = await self.db.consulta_canal_dado_um_id({
        "canal_id" : _canal_id
    })

    if aventureiro == None or aventureiro["ativo"] == 0:
        self.error_messages = self.bot.import_message_language_by_one("english", 
            "bot_channel", "capmon_channel_messages", "capmon_channel_messages_error", 
            {
                "aventureiro":_aventureiro,
                "idiomas": [i["nome"] for i in self.idiomas],
                "comandos": self.start_parameter_list() + self.language_parameter_list() + self.stop_parameter_list()    
            })

        if aventureiro == None:
            await self.bot.cogs['Envia_Msg'].envia_msg_with_context(ctx, self.error_messages["stop_not_start"])
        else:
            await self.bot.cogs['Envia_Msg'].envia_msg_with_context(ctx, self.error_messages["stop_inactive"])
        return

    dados = {
        "nome_idioma": aventureiro["nome_idioma"], 
        "ativo": 0, 
        "nome_canal" : _aventureiro, 
        "aventureiro_nome" : _aventureiro,
        "canal_id" : _canal_id
    }

    _messages = self.bot.import_message_language_by_one(dados["nome_idioma"], 
    "bot_channel", "capmon_channel_messages", "capmon_channel_messages_normal", 
    {"aventureiro":_aventureiro})

    _tasks = self.bot.asyncio_all_tasks(self.bot.loop)  

    for task in _tasks:
        if dados["canal_id"] in task.get_name():
            task.cancel()

    await self.db.drop_tables_with_underline_adventurer_name(dados)
    await self.db.update_canais(dados)
    await self.bot.cogs['Envia_Msg'].envia_msg_with_context(ctx, _messages["stop"])