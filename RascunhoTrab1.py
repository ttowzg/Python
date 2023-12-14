from heapq import heappop, heappush


class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, coordenada, vizinhos):
        if coordenada not in self.vertices:
            self.vertices[coordenada] = set(vizinhos)

    def adicionar_proibido(self, ponto_proibido):
        # Remove um ponto proibido sem quebrar as arestas
        if ponto_proibido in self.vertices:
            del self.vertices[ponto_proibido]

            for vertice, vizinhos in self.vertices.items():
                self.vertices[vertice] = {
                    vizinho for vizinho in vizinhos if vizinho != ponto_proibido}

    def imprimir_grafo(self):
        for vertice, vizinhos in self.vertices.items():
            print(f"{vertice}: {vizinhos}")

    def dijkstra(self, ponto_inicial, ponto_destino):
        fila = [(0, ponto_inicial)]  # (distância, vértice)
        visitados = set()

        while fila:
            distancia, atual = heapq.heappop(fila)

            if atual == ponto_destino:
                caminho = self.reconstruir_caminho(
                    ponto_inicial, ponto_destino, visitados)
                print(
                    f"Caminho mínimo de {ponto_inicial} para {ponto_destino}: {caminho}")
                return

            if atual not in visitados:
                visitados.add(atual)

                for vizinho in self.vertices[atual]:
                    if vizinho not in visitados:
                        # Peso 1 para arestas não ponderadas
                        heapq.heappush(fila, (distancia + 1, vizinho))

    def reconstruir_caminho(self, ponto_inicial, ponto_destino, visitados):
        caminho = []
        atual = ponto_destino

        while atual != ponto_inicial:
            caminho.insert(0, atual)
            for vizinho in self.vertices[atual]:
                if vizinho in visitados and vizinho not in caminho:
                    atual = vizinho
                    break

        caminho.insert(0, ponto_inicial)
        return caminho


# Criando um grafo com coordenadas de 0,0 até 8,11
grafo = Grafo()

# Adicionando vértices e arestas explicitamente
for i in range(9):  # profundidade
    for j in range(12):  # largura
        vizinhos = []
        if i > 0:
            vizinhos.append((i - 1, j))  # Vizinho acima
        if i < 8:
            vizinhos.append((i + 1, j))  # Vizinho abaixo
        if j > 0:
            vizinhos.append((i, j - 1))  # Vizinho à esquerda
        if j < 11:
            vizinhos.append((i, j + 1))  # Vizinho à direita
        grafo.adicionar_vertice((i, j), vizinhos)

# Adicionando pontos proibidos

# Lista de pontos proibidos
pontos_proibidos = [
    (6, 0),
    (6, 1),
    (5, 1),
    (4, 1),
    (3, 1),
    (2, 1),
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (0, 5),
    (1, 8),
    (2, 7),
    (2, 9),
    (3, 8),
    (8, 5),
    (7, 5),
    (6, 5),
    (5, 5),
    (5, 6),
    (5, 7),
    (5, 8),
    (6, 8),
    (7, 8),
    (8, 8),
]

# Adicionando pontos proibidos ao grafo
for ponto in pontos_proibidos:
    grafo.adicionar_proibido(ponto)

# Imprimindo o grafo
grafo.imprimir_grafo()

# Aplicando Dijkstra para encontrar um caminho mínimo entre dois pontos
ponto_inicial = (0, 0)
ponto_destino = (8, 11)
grafo.dijkstra(ponto_inicial, ponto_destino)
