#!/usr/bin/env python3
"""Wrong idea: act like every trail takes the same time."""

from collections import deque
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n, m = next(it), next(it)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, _ = next(it) - 1, next(it) - 1, next(it)
        graph[u].append(v)
        graph[v].append(u)

    distance = [-1] * n
    distance[0] = 0
    queue = deque([0])
    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            if distance[neighbour] == -1:
                distance[neighbour] = distance[node] + 1
                queue.append(neighbour)

    print(max(0, distance[n - 1] - 1))


if __name__ == "__main__":
    main()
