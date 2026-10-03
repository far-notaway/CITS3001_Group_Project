#!/usr/bin/env python3
"""Too slow: try every trail and run Dijkstra each time."""

from heapq import heappop, heappush
import sys


def shortest_path(graph, free_edge):
    n = len(graph)
    inf = 10**30
    distance = [inf] * n
    distance[0] = 0
    queue = [(0, 0)]
    while queue:
        current, node = heappop(queue)
        if current != distance[node]:
            continue
        for neighbour, weight, edge_id in graph[node]:
            candidate = current + (0 if edge_id == free_edge else weight)
            if candidate < distance[neighbour]:
                distance[neighbour] = candidate
                heappush(queue, (candidate, neighbour))
    return distance[-1]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n, m = next(it), next(it)
    graph = [[] for _ in range(n)]
    for edge_id in range(m):
        u, v, w = next(it) - 1, next(it) - 1, next(it)
        graph[u].append((v, w, edge_id))
        graph[v].append((u, w, edge_id))

    answer = min(shortest_path(graph, edge_id) for edge_id in range(m))
    print(answer)


if __name__ == "__main__":
    main()
