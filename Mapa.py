import Cidade 
import Adjacente
class Mapa:
 
    arad = Cidade('Arad', 366)
    zerind = Cidade('Zerind', 374)
    oradea = Cidade('Oradea', 380)
    sibiu = Cidade('Sibiu', 253)
    timisoara = Cidade('Timisoara', 329)
    lugoj = Cidade('Lugoj', 244)
    mehadia = Cidade('Mehadia', 241)
    dobreta = Cidade('Dobreta', 242)
    craiova = Cidade('Craiova', 160)
    rimnicu = Cidade('Rimnicu', 193)
    fagaras = Cidade('Fagaras', 178)
    pitesti = Cidade('Pitesti', 98)
    bucharest = Cidade('Bucharest', 0)
    giurgiu = Cidade('Giurgiu', 77)

    
    arad.addCidadeAdjacente(Adjacente(zerind, 75)) 
    arad.addCidadeAdjacente(Adjacente(sibiu, 140))
    arad.addCidadeAdjacente(Adjacente(timisoara, 118))

    zerind.addCidadeAdjacente(Adjacente(arad, 75))
    zerind.addCidadeAdjacente(Adjacente(oradea, 71))

    oradea.addCidadeAdjacente(Adjacente(zerind, 71))
    oradea.addCidadeAdjacente(Adjacente(sibiu, 151))

    sibiu.addCidadeAdjacente(Adjacente(oradea, 151))
    sibiu.addCidadeAdjacente(Adjacente(arad, 140))
    sibiu.addCidadeAdjacente(Adjacente(fagaras, 99))
    sibiu.addCidadeAdjacente(Adjacente(rimnicu, 80))

    timisoara.addCidadeAdjacente(Adjacente(arad, 118))
    timisoara.addCidadeAdjacente(Adjacente(lugoj, 111))

    lugoj.addCidadeAdjacente(Adjacente(timisoara, 111))
    lugoj.addCidadeAdjacente(Adjacente(mehadia, 70))

    mehadia.addCidadeAdjacente(Adjacente(lugoj, 70))
    mehadia.addCidadeAdjacente(Adjacente(dobreta, 75))

    dobreta.addCidadeAdjacente(Adjacente(mehadia, 75))
    dobreta.addCidadeAdjacente(Adjacente(craiova, 120))

    craiova.addCidadeAdjacente(Adjacente(dobreta, 120))
    craiova.addCidadeAdjacente(Adjacente(pitesti, 138))
    craiova.addCidadeAdjacente(Adjacente(rimnicu, 146))

    rimnicu.addCidadeAdjacente(Adjacente(craiova, 146))
    rimnicu.addCidadeAdjacente(Adjacente(sibiu, 80))
    rimnicu.addCidadeAdjacente(Adjacente(pitesti, 97))

    fagaras.addCidadeAdjacente(Adjacente(sibiu, 99))
    fagaras.addCidadeAdjacente(Adjacente(bucharest, 211))

    pitesti.addCidadeAdjacente(Adjacente(rimnicu, 97))
    pitesti.addCidadeAdjacente(Adjacente(craiova, 138))
    pitesti.addCidadeAdjacente(Adjacente(bucharest, 101))

    bucharest.addCidadeAdjacente(Adjacente(fagaras, 211))
    bucharest.addCidadeAdjacente(Adjacente(pitesti, 101))
    bucharest.addCidadeAdjacente(Adjacente(giurgiu, 90))
