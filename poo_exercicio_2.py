class Animal:
    def __init__(self, nome, cor, patas):
        self.nome = nome
        self.cor = cor
        self.patas = patas
        
    def exibir_dados(self):
        print(nome)
        print(cor)
        print(patas)

class Cachorro(Animal):
    def __init__ (self, nome, cor, numero_patas, raca):
        super().__init__(raca)
        self.raca = raca

animal = Animal("Passarinho", "Azul", 2)
animal.exibir_dados() # exibe os atributos do animal
dog = Cachorro("Rex", "Marrom", 4, "Vira lata")
dog.exibir_dados() # exibe os atributos do cachorro