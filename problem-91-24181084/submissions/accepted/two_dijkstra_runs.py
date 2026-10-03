#!/usr/bin/env python3
"""Another correct answer. Run Dijkstra from both ends."""

from heapq import heappop, heappush
import sys


def dijkstra(start, graph):
    infinity = 10**30
    distance = [infinity] * len(graph)
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        current, node = heappop(queue)
        if current != distance[node]:
            continue
        for neighbour, weight in graph[node]:
            candidate = current + weight
            if candidate < distance[neighbour]:
                distance[neighbour] = candidate
                heappush(queue, (candidate, neighbour))
    return distance


def main() -> None:
    values = list(map(int, sys.stdin.buffer.read().split()))
    iterator = iter(values)
    n = next(iterator)
    m = next(iterator)
    graph = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = next(iterator) - 1
        v = next(iterator) - 1
        w = next(iterator)
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v))

    # A free edge can join a shortest prefix to a shortest suffix.
    from_start = dijkstra(0, graph)
    from_finish = dijkstra(n - 1, graph)
    answer = from_start[n - 1]
    for u, v in edges:
        answer = min(answer, from_start[u] + from_finish[v])
        answer = min(answer, from_start[v] + from_finish[u])
    print(answer)


if __name__ == "__main__":
    main()
