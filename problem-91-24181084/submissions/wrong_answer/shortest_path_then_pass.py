#!/usr/bin/env python3
"""Wrong idea: pick the normal shortest path first."""

from heapq import heappop, heappush
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n, m = next(it), next(it)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = next(it) - 1, next(it) - 1, next(it)
        graph[u].append((v, w))
        graph[v].append((u, w))

    inf = 10**30
    dist = [inf] * n
    parent = [None] * n
    dist[0] = 0
    queue = [(0, 0)]
    while queue:
        current, node = heappop(queue)
        if current != dist[node]:
            continue
        for neighbour, weight in graph[node]:
            candidate = current + weight
            if candidate < dist[neighbour]:
                dist[neighbour] = candidate
                parent[neighbour] = (node, weight)
                heappush(queue, (candidate, neighbour))

    largest = 0
    node = n - 1
    while node != 0:
        node, weight = parent[node]
        largest = max(largest, weight)
    print(dist[n - 1] - largest)


if __name__ == "__main__":
    main()
