class Grafo:
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas

    def inicializar_matrizes(self):
        n = len(self.vertices)
        dist = [[float('inf')] * n for _ in range(n)]
        pred = [[None] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for i, j in self.arestas:
            dist[i][j] = 1
            pred[i][j] = i

        return dist, pred

    def floyd_warshall(self):
        dist, pred = self.inicializar_matrizes()

        n = len(self.vertices)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        pred[i][j] = pred[k][j]

        return dist, pred


# Exemplo de uso
vertices = [0, 1, 2, 3]
arestas = [(0, 1), (1, 2), (2, 3), (3, 0)]

grafo = Grafo(vertices, arestas)
distancias, predecessores = grafo.floyd_warshall()

# Exibindo resultados
print("Matriz de distâncias:")
for row in distancias:
    print(row)

print("\nMatriz de predecessores:")
for row in predecessores:
    print(row)
