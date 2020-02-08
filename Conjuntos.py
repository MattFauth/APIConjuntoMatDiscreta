class Conjuntos:
    def __init__(self):
        self.elementos = []
        self.nome = None
        self.tamanho = None

    def adicionar(self, valor):
        self.elementos.append(valor)

    def nomeConjunto(self, nome):
        self.nome = nome
    
    def medirTamanho(self):
        return len(self.elementos)

    def imprimir(self):
        print(self.elementos)