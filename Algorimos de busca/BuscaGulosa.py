
from Vetor import VetorOrdenado


class BuscaGulosa: 
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False

    def buscar(self, atual):
        print("\nAtual: {}".format(atual.nome))
        atual.visitado = True

        if atual == self.objetivo:
            self.achou = True
            
        else:
            self.fronteira = VetorOrdenado(len(atual.adjacentes))

            for i in atual.adjacentes:
                if i.cidade.visitado == False:
                    self.fronteira.inserir(i.cidade)
                    i.cidade.visitado = True
                   
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:

                BuscaGulosa.buscar(self, self.fronteira.getPrimeiro())
