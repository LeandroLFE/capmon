from auth.auth import db_location, db_name

from db.connect.db_classes.conectaSQLite import ConectaSQLite
from db.default_data.dados_parametros import script_create_table_parametros_aventureiros, script_create_table_parametros_buddies, script_create_table_parametros_capboard, script_create_table_parametros_hordas, script_create_table_parametros_criaturas, script_insert_table_parametros_criaturas, dados_padrao_tabela_parametros_criaturas, script_insert_table_parametros_aventureiros, script_insert_table_parametros_buddies, script_insert_table_parametros_capboard, script_insert_table_parametros_hordas, dados_padrao_tabela_parametros_aventureiros, dados_padrao_tabela_parametros_buddies, dados_padrao_tabela_parametros_capboard, dados_padrao_tabela_parametros_hordas, script_create_table_parametros_gerais, script_insert_table_parametros_gerais, dados_padrao_tabela_parametros_gerais
from db.default_data.dados_vantagens_subs_perfis import script_create_table_vantagens_subs, script_insert_table_vantagens_subs, dados_padrao_tabela_vantagens_subs
from db.default_data.dados_tipos import script_create_table_tipos, script_insert_table_tipos, dados_padrao_tabela_tipos
from db.default_data.dados_idiomas import script_create_table_idiomas, script_insert_table_idiomas, dados_padrao_tabela_idiomas
from db.default_data.dados_tipo_itens import script_create_table_tipo_itens
from db.default_data.dados_custos import script_create_table_custos, script_insert_table_custos, dados_padrao_tabela_custos
from db.default_data.dados_comandos_uso_itens_capshop import script_create_table_comandos_uso_itens_capshop, script_insert_table_comandos_uso_itens_capshop, dados_padrao_tabela_comandos_uso_itens_capshop
from db.default_data.dados_itens_capshop import script_create_table_itens_capshop, script_insert_table_itens_capshop, dados_padrao_tabela_itens_capshop
from db.default_data.dados_itens_capraid import script_create_table_itens_capraid, script_insert_table_itens_capraid, dados_padrao_tabela_itens_capraid
from db.default_data.dados_tipo_hordas import script_create_table_tipo_hordas, script_insert_table_tipo_hordas, dados_padrao_tabela_tipo_hordas
from db.default_data.dados_atributos import script_create_table_atributos, script_insert_table_atributos, dados_padrao_tabela_atributos
from db.default_data.dados_efetividades import script_create_table_efetividades, script_insert_table_efetividades, dados_padrao_tabela_efetividades
from db.default_data.dados_criaturas import script_create_table_criaturas, script_insert_table_criaturas, dados_padrao_tabela_criaturas
from db.default_data.dados_canais import script_create_table_canais
from db.default_data.dados_mensagens import script_create_table_msg


class Setup():
    
    db = ConectaSQLite(f"{db_location}{db_name}")

    @db.create_or_drop_table
    def create_table_idiomas(self, dados : str = ""): 
        return script_create_table_idiomas(dados)

    @db.insert_table_many_lines
    def insert_table_idiomas(self, dados : dict = {}):
        return script_insert_table_idiomas(dados)

    '''----------------------------------------------------------------'''

    @db.create_or_drop_table
    def create_table_tipo_itens(self, dados ={}):
        return script_create_table_tipo_itens(dados)

    @db.create_or_drop_table
    def create_table_tipo_hordas(self, dados={}):
        return script_create_table_tipo_hordas(dados)

    @db.insert_table_many_lines
    def insert_table_tipo_hordas(self, dados : dict = {}):
        return script_insert_table_tipo_hordas(dados)

    '''----------------------------------------------------------------'''

    @db.create_or_drop_table
    def create_table_comandos_uso_itens_capshop(self, dados={}):
        return script_create_table_comandos_uso_itens_capshop(dados)

    @db.insert_table_many_lines
    def insert_table_comandos_uso_itens_capshop(self, dados : dict = {}):
        return script_insert_table_comandos_uso_itens_capshop(dados)

    @db.create_or_drop_table
    def create_table_itens_capshop(self, dados={}):
        return script_create_table_itens_capshop(dados)

    @db.insert_table_many_lines
    def insert_table_itens_capshop(self, dados : dict = {}):
        return script_insert_table_itens_capshop(dados)

    @db.create_or_drop_table
    def create_table_itens_capraid(self, dados={}):
        return script_create_table_itens_capraid(dados)

    @db.insert_table_many_lines
    def insert_table_itens_capraid(self, dados : dict = {}):
        return script_insert_table_itens_capraid(dados)

    '''----------------------------------------------------------------'''

    @db.create_or_drop_table
    def create_table_vantagens_subs_perfis(self, dados={}):
        return script_create_table_vantagens_subs(dados)

    @db.insert_table_one_line
    def insert_table_vantagens_subs_perfis(self, dados : dict = {}):
        return script_insert_table_vantagens_subs(dados)

    '''
    Parametros:
    '''

    @db.create_or_drop_table
    def create_table_parametros_capboard(self, dados={}):
        return script_create_table_parametros_capboard(dados)

    @db.insert_table_one_line
    def insert_table_parametros_capboard(self, dados : dict = {}):
        return script_insert_table_parametros_capboard(dados)

    @db.create_or_drop_table
    def create_table_parametros_buddies(self, dados={}):
        return script_create_table_parametros_buddies(dados)

    @db.insert_table_one_line
    def insert_table_parametros_buddies(self, dados : dict = {}):
        return script_insert_table_parametros_buddies(dados)
    
    @db.create_or_drop_table
    def create_table_parametros_aventureiros(self, dados={}):
        return script_create_table_parametros_aventureiros(dados)

    @db.insert_table_one_line
    def insert_table_parametros_aventureiros(self, dados : dict = {}):
        return script_insert_table_parametros_aventureiros(dados)

    @db.create_or_drop_table
    def create_table_parametros_hordas(self, dados={}):
        return script_create_table_parametros_hordas(dados)

    @db.insert_table_one_line
    def insert_table_parametros_hordas(self, dados : dict = {}):
        return script_insert_table_parametros_hordas(dados)

    @db.create_or_drop_table
    def create_table_parametros_gerais(self, dados={}):
        return script_create_table_parametros_gerais(dados)

    @db.insert_table_one_line
    def insert_table_parametros_gerais(self, dados={}):
        return script_insert_table_parametros_gerais(dados)

    @db.create_or_drop_table
    def create_table_parametros_criaturas(self, dados={}):
        return script_create_table_parametros_criaturas(dados)

    @db.insert_table_one_line
    def insert_table_parametros_criaturas(self, dados={}):
        return script_insert_table_parametros_criaturas(dados)

    '''
        ---------------------------------------------------------------------   
    '''

    @db.create_or_drop_table
    def create_table_tipos(self, dados : str = ""): 
        return script_create_table_tipos(dados)

    @db.insert_table_many_lines
    def insert_table_tipos(self, dados : str = ""):
        return script_insert_table_tipos(dados)

    
    '''----------------------------------------------------------------'''

    @db.create_or_drop_table
    def create_table_atributos(self, dados : str = ""): 
        return script_create_table_atributos(dados)

    @db.insert_table_many_lines
    def insert_table_atributos(self, dados : str = ""):
        return script_insert_table_atributos(dados)

    
    '''----------------------------------------------------------------'''

    @db.create_or_drop_table
    def create_table_efetividades(self, dados : str = ""): 
        return script_create_table_efetividades(dados)

    @db.insert_table_many_lines
    def insert_table_efetividades(self, dados : str = ""):
        return script_insert_table_efetividades(dados)

    
    '''----------------------------------------------------------------'''

    @db.create_or_drop_table
    def create_table_custos(self, dados : str = ""): 
        return script_create_table_custos(dados)

    @db.insert_table_many_lines
    def insert_table_custos(self, dados : str = ""):
        return script_insert_table_custos(dados)

    
    '''----------------------------------------------------------------'''


    @db.create_or_drop_table
    def create_table_criaturas(self, dados : str = ""): 
        return script_create_table_criaturas(dados)

    @db.insert_table_many_lines
    def insert_table_criaturas(self, dados : str = ""):
        return script_insert_table_criaturas(dados)

    
    '''----------------------------------------------------------------'''

    @db.create_or_drop_table
    def create_table_canais(self, dados : str = ""):
        return script_create_table_canais(dados)

    
    '''----------------------------------------------------------------'''

    @db.create_or_drop_table
    def create_table_msg(self, dados : str = ""): 
        return script_create_table_msg(dados)

if __name__ == "__main__":
    setup_obj = Setup()

    setup_obj.create_table_idiomas()
    setup_obj.insert_table_idiomas(dados_padrao_tabela_idiomas())

    setup_obj.create_table_tipo_itens()

    setup_obj.create_table_tipo_hordas()
    setup_obj.insert_table_tipo_hordas(dados_padrao_tabela_tipo_hordas())

    setup_obj.create_table_comandos_uso_itens_capshop()
    setup_obj.insert_table_comandos_uso_itens_capshop(dados_padrao_tabela_comandos_uso_itens_capshop())
    
    setup_obj.create_table_itens_capshop()
    setup_obj.insert_table_itens_capshop(dados_padrao_tabela_itens_capshop())

    setup_obj.create_table_itens_capraid()
    setup_obj.insert_table_itens_capraid(dados_padrao_tabela_itens_capraid())

    setup_obj.create_table_vantagens_subs_perfis()
    setup_obj.insert_table_vantagens_subs_perfis(dados_padrao_tabela_vantagens_subs())


    '''
    Parametros:
    '''

    setup_obj.create_table_parametros_capboard()
    setup_obj.insert_table_parametros_capboard(dados_padrao_tabela_parametros_capboard())

    setup_obj.create_table_parametros_buddies()
    setup_obj.insert_table_parametros_buddies(dados_padrao_tabela_parametros_buddies())

    setup_obj.create_table_parametros_aventureiros()
    setup_obj.insert_table_parametros_aventureiros(dados_padrao_tabela_parametros_aventureiros())

    setup_obj.create_table_parametros_criaturas()
    setup_obj.insert_table_parametros_criaturas(dados_padrao_tabela_parametros_criaturas())

    setup_obj.create_table_parametros_hordas()
    setup_obj.insert_table_parametros_hordas(dados_padrao_tabela_parametros_hordas())

    setup_obj.create_table_parametros_gerais()
    setup_obj.insert_table_parametros_gerais(dados_padrao_tabela_parametros_gerais())

    '''
        ----------------------------------------------------------------------------------------- 
    '''

    setup_obj.create_table_tipos()
    setup_obj.insert_table_tipos(dados_padrao_tabela_tipos())
    
    setup_obj.create_table_atributos()
    setup_obj.insert_table_atributos(dados_padrao_tabela_atributos())
    
    setup_obj.create_table_efetividades()
    setup_obj.insert_table_efetividades(dados_padrao_tabela_efetividades())

    setup_obj.create_table_custos()
    setup_obj.insert_table_custos(dados_padrao_tabela_custos())

    setup_obj.create_table_criaturas()
    setup_obj.insert_table_criaturas(dados_padrao_tabela_criaturas())

    setup_obj.create_table_canais()

    setup_obj.create_table_msg()
    