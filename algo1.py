from collections import deque

def levit_algorithm(graph, start):
    inf = float('inf')
    dist = {v: inf for v in graph}
    dist[start] = 0

    m0 = set(graph.keys())  # Непосещённые вершины
    m1 = deque([start])     # Граница
    m2 = set()              # Обработанные вершины

    while m1:
        u = m1.popleft()
        for v, weight in graph[u]:
            if v in m0 or v in m1:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    if v in m0:
                        m1.append(v)
                        m0.remove(v)
            elif v in m2:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    m1.append(v)
                    m2.remove(v)
        m2.add(u)

    return dist