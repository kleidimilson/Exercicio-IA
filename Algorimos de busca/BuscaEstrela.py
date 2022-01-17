import VetorOrdenadoAdjacente


class BuscaAEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False

    def achar(self, atual):
        print("\n ".format(atual.nome))
        atual.visitado = True

        if atual == self.objetivo:
            print(.format(self.objetivo.nome))
            self.achou = True
        else:
            self.fronteira = VetorOrdenadoAdjacente(len(atual.adjacentes))
           
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    
                    self.fronteira.inserir(a)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                BuscaAEstrela.buscar(self, self.fronteira.getPrimeiro())
