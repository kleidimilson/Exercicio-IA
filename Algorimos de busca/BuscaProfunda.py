import Estruturas

class BuscaEmProfundidade:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True 
        self.objetivo = objetivo
        Estrutura = Estruturas.Pilha
        self.fronteira = Estrutura(1000) 
        self.fronteira.empilhar(inicio) 
        self.achou = False

    def buscar(self):
        topo = self.fronteira.getTopo() 
        if topo == self.objetivo:
            self.achou = True
            print("Objetivo {}".format(self.objetivo.nome), "foi alcançado apartir de {}".format(self.inicio.nome))
        else: 
            print("Topo: {}".format(topo.nome))
            for adjacente in topo.adjacentes:
                if self.achou == False:
                    print("Já foi visitado? ", adjacente.cidade.nome)
                    if adjacente.cidade.visitado == False:
                        adjacente.cidade.visitado == True 
                        self.fronteira.empilhar(adjacente.cidade) 
                        BuscaEmProfundidade.buscar(self) 
        print("Desempilhou: {}".format(self.fronteira.desempilhar().nome))

class BuscaEmProfundidadeVisitados:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        estrutura = Estruturas.Pilha
        self.fronteira = estrutura(1000)
        self.fronteira.empilhar(inicio)
        self.achou = False

    def buscar(self):
        topo = self.fronteira.getTopo()
        print("Topo: {}".format(topo.nome))

        if topo == self.objetivo:
            print("Objetivo {}".format(self.objetivo.nome), "foi alcançado apartir de {}".format(self.inicio.nome))
            self.achou = True
        else:
            for adjacente in topo.adjacentes:
                if self.achou == False:
                    print("Verificando se ja visitado: {}".format(adjacente.cidade.nome))
                    if adjacente.cidade.visitado == False:
                        adjacente.cidade.visitado = True
                        self.fronteira.empilhar(adjacente.cidade)
                        BuscaEmProfundidadeVisitados.buscar(self)


