def floyd_warshall(mat):
    n = len(mat)
    dist = [fila[:] for fila in mat]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# EJEMPLO: INF = 9999
INF = 9999
mat = [
    [0,   3, INF,  7],
    [8,   0,   2, INF],
    [5, INF,   0,   1],
    [2, INF, INF,  0]
]

res = floyd_warshall(mat)
print("Floyd-Warshall:")
for fila in res:
    print(fila)
