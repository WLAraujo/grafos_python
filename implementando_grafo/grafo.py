# ALGUNS DETALHES:
# * É possível eliminar o conjunto de vértices, afinal, o dicionário de vizinhos já contém essa informação
# * No método construtor do grafo poderiamos já usar os métodos add_vertice e add_aresta

class Grafo:

    # Método construtor da classe Grafo
    def __init__(self, V, E):
        # Instanciando vértices
        self.V = set(V)
        # Instanciando arestas
        self.E = set(frozenset((u,v)) for u, v in E)
        # Criando dicionário que armazenara os vizinhos de cada vértice
        self.vizinhos_estrutura = {}
        for v in self.V:
            self.vizinhos_estrutura[v] = set()
        for u,v in self.E:
            self.vizinhos_estrutura[u].add(v)
            self.vizinhos_estrutura[v].add(u)

    # Método que devolve o grau de um vértice
    def grau(self, v):
        return sum(1 for e in self.E if v in e)
    
    # Método que retorna os vizinhos de um vértice
    def vizinhos(self, v):
        return self.vizinhos_estrutura[v]

    # Método que adiciona um vértice
    def add_vertice(self, v):
        if v not in self.V:
            self.V.add(v)
            self.vizinhos_estrutura[v] = {}
    
    # Método que adiciona uma aresta
    def add_aresta(self, e):
        if e not in self.E:
            self.E.add(e)
    
if __name__ == '__main__':
    # Grafo usado para testes
    G = Grafo([1,2,3,4], [(1,2),(2,3),(2,4),(3,4)])
    
    # Testes da função grau
    assert(G.grau(1) == 1)
    assert(G.grau(2) == 3)
    assert(G.grau(3) == 2)
    assert(G.grau(4) == 2)
    print("Função grau ok")

    #  Testes da função grau
    assert(G.vizinhos(1) == {2})
    assert(G.vizinhos(2) == {1,3,4})
    print("Função vizinhos ok")

    # Testes da função add_vertice
    G.add_vertice(5)
    assert(G.vizinhos(5) == {})
    G.add_vertice(4)
    assert(G.vizinhos(4) == {2,3})
    print("Função add_vertice ok")

    # Testes da função add_aresta
    G.add_aresta((1,4))
    assert(G.vizinhos(1) == {2,4})