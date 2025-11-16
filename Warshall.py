def warshall(reach):
    n = len(reach)
    R = [fila[:] for fila in reach]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                R[i][j] = R[i][j] or (R[i][k] and R[k][j])

    return R


# EJEMPLO
reach = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]

res = warshall(reach)
print("Warshall (alcanzabilidad):")
for fila in res:
    print(fila)
