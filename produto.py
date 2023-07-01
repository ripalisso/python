

class Produto:

    #construtor da class
    def __init__(self, descricao, preco,quantidade, id = None):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade = quantidade

    def __str__(self):
        return f'Código:{self.__id} \tDescrição: {self.__descricao} ' \
               f'\tPreço unitário: R$ {self.__preco:.2f} ' \
               f'\tQuantidade em estoque: {self.__quantidade}'

    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

        # função somente para ler a variável
    @property
    def quantidade(self):
        return self.__quantidade

        # função somente para alterar a variável
    @id.setter
    def id(self, id):
        self.__id = id

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade