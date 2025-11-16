import heapq

def dijkstra(grafo, origen):
    dist = {n: float('inf') for n in grafo}
    dist[origen] = 0
    pq = [(0, origen)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, peso in grafo[u]:
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                heapq.heappush(pq, (dist[v], v))

    return dist


# EJEMPLO
grafo = {
    'A': [('B', 4), ('C', 1)],
    'B': [('D', 1)],
    'C': [('B', 2), ('D', 5)],
    'D': []
}

print("Dijkstra:", dijkstra(grafo, 'A'))
