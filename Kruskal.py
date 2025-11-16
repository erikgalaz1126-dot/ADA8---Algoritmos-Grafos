def kruskal(graph):
    edges = []
    num_vertices = len(graph)

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))

    edges.sort()

    parent = list(range(num_vertices))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    def union(x, y):
        parent[find(x)] = find(y)

    mst = []
    for w, u, v in edges:
        if find(u) != find(v):
            mst.append((u, v, w))
            union(u, v)

    return mst
