class Cliente:

    #Construtor Python
    def __init__(self, nome):
        self.__nome = nome

    #Trocando o Get pelo @property
    @property
    def nome(self):
        return self.__nome.title()

    #Trocando o Set
    @nome.setter
    def nome(self, nome):
        self.__nome = nome