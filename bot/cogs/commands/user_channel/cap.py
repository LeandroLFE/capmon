from twitchio.ext.commands import Cog, command

class Cap(Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

        self.envia_msg_without_context = self.bot.cogs['Envia_Msg'].envia_msg_without_context
        

    @command(name='cap')
    async def command_cap(self, ctx, tentativas, criatura='', item=''):
        if ctx.channel.name == self.bot.nick:
            return

        _canal_id = ctx.message.tags["room-id"]
        _aventureiro = ctx.author.name
        _nome_idioma = self.bot.dados_horda[_canal_id]["nome_idioma"]

        _dados_canal = {
            "canal_id" : _canal_id,
            "nome_canal" : ctx.channel.name,
            "nome_idioma" : _nome_idioma
        }
        
        if self.bot.dados_horda[_canal_id]["nome_horda"] == "":
            _parametros_horda = self.bot.parametros_horda[_canal_id]
            self.message = self.bot.import_message_language_by_one(_nome_idioma, 
                "user_channel", "cap_messages", "error_horde_inactive", 
                {"aventureiro": _aventureiro})
            await self.envia_msg_without_context(_dados_canal, self.message)
            return

        if isinstance(tentativas, str) == isinstance(criatura, int):
            tentativas, criatura = criatura, tentativas

        _dados_horda = self.bot.dados_horda[_canal_id] 

        _nome_func_tipo_horda = f"""tipo_horda_{_dados_horda["nome_horda"]}"""
        _func_tipo_horda = getattr(self, _nome_func_tipo_horda) 
        await _func_tipo_horda(_dados_canal)  


    async def tipo_horda_normal_aleatoria(self, dados_canal):

        _criatura = await self.db.seleciona_criatura_aleatoria(dados_canal)

        _parametros_horda = self.bot.parametros_horda[dados_canal["canal_id"]] 

        _duracao = self.bot.random_randint(_parametros_horda["tempo_horda_min"], _parametros_horda["tempo_horda_max"]) 

        dados_horda = {
            "nome_idioma" : dados_canal["nome_idioma"],
            "nome_horda" : "normal_aleatoria",
            "criatura" : _criatura,
            "criaturas" : [],
            "capraid" : {},
            "duracao" : _duracao,
        }
        
        self.message = self.bot.import_message_language_by_one(dados_canal["nome_idioma"], 
                "adventure_channel", "horde_messages", "new_normal_horde_message", 
                dados_horda)
        
        await self.envia_msg_without_context(dados_canal, self.message)

        return dados_horda

    async def tipo_horda_elemental(self, dados_canal):

        _parametros_horda = self.bot.parametros_horda[dados_canal["canal_id"]]
        _duracao = self.bot.random_randint(_parametros_horda["tempo_horda_min"], _parametros_horda["tempo_horda_max"]) 

        _atributos = await self.db.seleciona_todos_atributos(dados_canal)
        _custos = await self.db.seleciona_todos_custos(dados_canal)

        _list_atributos = [a["ref"] for a in _atributos]
        _list_custos = [c["ref"] for c in _custos]

        dados_horda = {
            "nome_idioma" : dados_canal["nome_idioma"],
            "nome_horda" : "elemental",
            "capraid" : {},
            "duracao" : _duracao,
        }

        dados_horda["ref_atributo"] = self.bot.random_choice(_list_atributos)
        dados_horda["custo"] = self.bot.random_choice(_list_custos)
        _criaturas = await self.db.seleciona_criaturas_atributo(dados_horda)
        
        while _criaturas == []:
            dados_horda["ref_atributo"] = self.bot.random_choice(_list_atributos)
            dados_horda["custo"] = self.bot.random_choice(_list_custos)
            _criaturas = await self.db.seleciona_criaturas_atributo(dados_horda)

        dados_horda["nome_tipo"] = _criaturas[0]["nome_tipo"]        
        dados_horda["criaturas"] = _criaturas

        _atributo = await self.db.seleciona_atributo_por_ref(dados_horda)
        dados_horda["atributo"] = _atributo["nome"]

        self.message = self.bot.import_message_language_by_one(dados_canal["nome_idioma"], 
                "adventure_channel", "horde_messages", "new_elemental_horde_message", 
                dados_horda)
        
        await self.envia_msg_without_context(dados_canal, self.message)

        return dados_horda

    async def tipo_horda_capraid(self, dados_canal):

        _criatura = await self.db.seleciona_criatura_aleatoria_lendaria(dados_canal)

        _parametros_horda = self.bot.parametros_horda[dados_canal["canal_id"]] 

        _duracao = _parametros_horda["tempo_horda_max"]

        _capraid = {

        }

        dados_horda = {
            "nome_idioma" : dados_canal["nome_idioma"],
            "nome_horda" : "capraid",
            "criatura" : _criatura,
            "criaturas" : [],
            "capraid" : _capraid,
            "duracao" : _duracao,
        }
        
        self.message = self.bot.import_message_language_by_one(dados_canal["nome_idioma"], 
                "adventure_channel", "horde_messages", "new_capraid_message", 
                dados_horda)
        
        await self.envia_msg_without_context(dados_canal, self.message)

        return dados_horda

    async def tipo_horda_normal_especifica(self, dados_canal, criatura):

        _parametros_horda = self.bot.parametros_horda[dados_canal["canal_id"]] 

        _duracao = self.bot.random_randint(_parametros_horda["tempo_horda_min"], _parametros_horda["tempo_horda_max"]) 

        dados_horda = {
            "nome_horda" : "normal_especifica",
            "criatura" : criatura,
            "criaturas" : [],
            "capraid" : {},
            "duracao" : _duracao,
        }
        
        self.message = self.bot.import_message_language_by_one(dados_canal["nome_idioma"], 
                "adventure_channel", "horde_messages", "new_normal_horde_message", 
                dados_horda)
        
        await self.envia_msg_without_context(dados_canal, self.message)

        return dados_horda
