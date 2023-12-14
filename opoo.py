from collections import deque
import itertools


class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, coordenada, vizinhos):
        if coordenada not in self.vertices:
            self.vertices[coordenada] = set(vizinhos)

    def adicionar_proibido(self, ponto_proibido):
        # Adiciona um ponto proibido removendo todas as arestas associadas a ele
        if ponto_proibido in self.vertices:
            del self.vertices[ponto_proibido]
            for vertice in self.vertices:
                self.vertices[vertice] = {
                    vizinho for vizinho in self.vertices[vertice] if vizinho != ponto_proibido}

    def imprimir_grafo(self):
        for vertice, vizinhos in self.vertices.items():
            print(f"{vertice}: {vizinhos}")

    def bfs(self, ponto_inicial, ponto_destino):
        fila = deque([ponto_inicial])
        visitados = set()
        antecessores = {ponto_inicial: None}

        while fila:
            atual = fila.popleft()

            if atual == ponto_destino:
                print(
                    f"Caminho encontrado de {ponto_inicial} para {ponto_destino}")
                self.mostrar_caminho(
                    ponto_inicial, ponto_destino, antecessores)
                return antecessores

            if atual not in visitados:
                visitados.add(atual)
                fila.extend(
                    vizinho for vizinho in self.vertices[atual] if vizinho not in visitados)
                for vizinho in self.vertices[atual]:
                    if vizinho not in antecessores:
                        antecessores[vizinho] = atual

        print(
            f"Nenhum caminho encontrado de {ponto_inicial} para {ponto_destino}")
        return None

    def mostrar_caminho(self, ponto_inicial, ponto_destino, antecessores):
        caminho = [ponto_destino]
        atual = ponto_destino

        while atual and atual != ponto_inicial:
            atual = antecessores[atual]
            caminho.insert(0, atual)

        print(f"Caminho percorrido: {caminho}")

    def floyd_warshall(self):
        # Implementação do algoritmo de Floyd-Warshall
        vertices = list(self.vertices.keys())
        num_vertices = len(vertices)

        # Inicializando a matriz de distâncias
        distancias = {par: float('inf')
                      for par in itertools.product(vertices, repeat=2)}
        for vertice in vertices:
            distancias[(vertice, vertice)] = 0
            for vizinho in self.vertices[vertice]:
                distancias[(vertice, vizinho)] = 1

        # Atualizando a matriz de distâncias
        for k in vertices:
            for i in vertices:
                for j in vertices:
                    if distancias[(i, j)] > distancias[(i, k)] + distancias[(k, j)]:
                        distancias[(i, j)] = distancias[(i, k)] + \
                            distancias[(k, j)]

        return distancias


# Criando um grafo com coordenadas de 0,0 até 8,11
grafo = Grafo()

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

# Adicionando pontos proibidos - São os grafos pretos na imagem da questão, aqueles que não tem ligação com o caminho percorrível.
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
    (2, 8),
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

# Aplicando o algoritmo de Floyd-Warshall
resultados = grafo.floyd_warshall()

# Imprimindo os resultados
print("\nDistâncias entre todos os pares de vértices:")
for par, distancia in resultados.items():
    print(f"{par}: {distancia}")

# Obtendo e imprimindo o caminho de

print("Digite as cordenadas do primeiro ponto: ")
x = int(input("Primeiro numero: "))
y = int(input("Segundo numero: "))
print("Digite para qual ponto deseja ir: ")
z = int(input("Primeiro numero: "))
w = int(input("Segundo numero: "))

ponto_inicial = (x, y)
ponto_destino = (z, w)

antecessores = grafo.bfs(ponto_inicial, ponto_destino)

if antecessores and ponto_destino in antecessores:
    if ponto_inicial in resultados and ponto_destino in resultados[ponto_inicial]:
        distancia = resultados[ponto_inicial][ponto_destino]
        if distancia != float('inf'):
            print(
                f"\nDistância de {ponto_inicial} até {ponto_destino}: {distancia}")

            # Reconstruindo o caminho
            caminho = [ponto_destino]
            atual = ponto_destino

            while antecessores[atual] is not None:
                caminho.append(antecessores[atual])
                atual = antecessores[atual]

            caminho.reverse()

            print(f"Caminho de {ponto_inicial} até {ponto_destino}: {caminho}")
        else:
            print(f"\nNão há caminho de {ponto_inicial} até {ponto_destino}")

else:
    print(f"\nNão há caminho de {ponto_inicial} até {ponto_destino}")
