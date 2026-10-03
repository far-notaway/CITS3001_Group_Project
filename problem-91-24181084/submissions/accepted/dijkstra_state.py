#!/usr/bin/env python3
"""My main answer. Each camp has two pass states."""

from heapq import heappop, heappush
import sys


def main() -> None:
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    iterator = iter(values)
    n = next(iterator)
    m = next(iterator)

    # Adjacency list for the undirected graph.
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = next(iterator) - 1
        v = next(iterator) - 1
        w = next(iterator)
        graph[u].append((v, w))
        graph[v].append((u, w))

    infinity = 10**30
    # distance[v][0] keeps the pass; distance[v][1] has used it.
    distance = [[infinity, infinity] for _ in range(n)]
    distance[0][0] = 0
    queue = [(0, 0, 0)]  # time, camp, pass used or not

    while queue:
        current, camp, used = heappop(queue)
        if current != distance[camp][used]:
            continue

        for neighbour, weight in graph[camp]:
            normal = current + weight
            if normal < distance[neighbour][used]:
                distance[neighbour][used] = normal
                heappush(queue, (normal, neighbour, used))

            # Use the pass on this trail, so its added cost is zero.
            if used == 0 and current < distance[neighbour][1]:
                distance[neighbour][1] = current
                heappush(queue, (current, neighbour, 1))

    print(min(distance[n - 1]))


if __name__ == "__main__":
    main()
