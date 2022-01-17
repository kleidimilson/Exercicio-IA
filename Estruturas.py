
class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0

    def enfileirar(self, cidade):
        if self.fim == self.tamanho - 1:
            self.fim = -1
        self.fim += 1
        self.cidades[self.fim] = cidade
        self.numeroElementos += 1

    def desinfileirar(self):

        temp = self.cidades[self.inicio]
        self.inicio += 1
        if self.inicio == self.tamanho:
            self.inicio = 0
        self.numeroElementos -= 1
        return temp

    def getPrimeiro(self):
        return self.cidades[self.inicio]

    def filaVazia(self):
        return self.numeroElementos == 0

    def filaCheia(self):
        return self.numeroElementos == self.tamanho

class Pilha: 
    def __init__(self, tamanho): 
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.topo = -1

    def empilhar(self, cidade):
        if not Pilha.pilhaCheia(self):
            self.topo += 1
            self.cidades[self.topo] = cidade
        else:
            print("Pilha esta cheia")

    def desempilhar(self): 
        if not Pilha.pilhaVazia(self): 
            temporario = self.cidades[self.topo]
            self.topo -= 1 
            return temporario
        else:
            print("Pilha esta vazia")
            return None

    def getTopo(self):
        return self.cidades[self.topo]

    def pilhaVazia(self):
        return (self.topo == -1)

    def pilhaCheia(self):
        return (self.topo == self.tamanho - 1)
