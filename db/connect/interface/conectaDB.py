from abc import ABCMeta, abstractmethod

class ConectaDB(metaclass=ABCMeta):

    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def create_or_drop_table(self, func : object)->object:
        botPatch = self.path
        def _create_table(self: object, dados = "")->None:
            script = func(self, dados) #função deve retornar o script SQL
            #executar script com os dados como parâmetro se necessário
            #salvar alterações no BD
        return _create_table
    
    @abstractmethod
    def insert_table_one_line(self, func : object)->object:
        botPatch = self.path
        def _insert_table(self: object, dados = "")->None:
            script = func(self, dados) #função deve retornar o script SQL
            #executar script com os dados como parâmetro se necessário
            #salvar alterações no BD
        return _insert_table

    @abstractmethod
    def insert_table_many_lines(self, func : object)->object:
        botPatch = self.path
        def _insert_table(self: object, dados = "")->None:
            script = func(self, dados) #função deve retornar o script SQL
            #executar script com os dados como parâmetro se necessário
            #salvar alterações no BD
        return _insert_table

    @abstractmethod
    def update_table(self, func : object)->object:
        botPatch = self.path
        def _update_table(self: object, dados = "") -> None:
            script = func(self, dados) #função deve retornar o script SQL
            #executar script com os dados como parâmetro se necessário
            #salvar alterações no BD
        return _update_table

    @abstractmethod
    def delete_table(self, func : object)->object:
        botPatch = self.path
        def _delete_table(self: object, dados = "") -> None:
            script = func(self, dados) #função deve retornar o script SQL
            #executar script com os dados como parâmetro se necessário
            #salvar alterações no BD
        return _delete_table

    @abstractmethod
    def select_table_many_data(self, func : object)->object:
        botPatch = self.path
        def _select_table_many_data(self: object, dados = ""):
            script = func(self, dados) #função deve retornar o script SQL
            #executar script com os dados como parâmetro se necessário
            #Retornar seleção para utilização
        return _select_table_many_data

    @abstractmethod
    def select_table_one_data(self, func : object)->object:
        botPatch = self.path
        def _select_table_one_data(self: object, dados = ""):
            script = func(self, dados) #função deve retornar o script SQL
            #executar script com os dados como parâmetro se necessário
            #Retornar seleção para utilização
        return _select_table_one_data