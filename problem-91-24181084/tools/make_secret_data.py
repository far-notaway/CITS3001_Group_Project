#!/usr/bin/env python3
"""Make the secret tests and answers."""

from heapq import heappop, heappush
from pathlib import Path
import random


PROBLEM = Path(__file__).resolve().parents[1] / "quokkaexpress"
SECRET = PROBLEM / "data" / "secret"


def solve(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    inf = 10**30
    distance = [[inf, inf] for _ in range(n)]
    distance[0][0] = 0
    queue = [(0, 0, 0)]
    while queue:
        current, node, used = heappop(queue)
        if current != distance[node][used]:
            continue
        for neighbour, weight in graph[node]:
            candidate = current + weight
            if candidate < distance[neighbour][used]:
                distance[neighbour][used] = candidate
                heappush(queue, (candidate, neighbour, used))
            if used == 0 and current < distance[neighbour][1]:
                distance[neighbour][1] = current
                heappush(queue, (current, neighbour, 1))
    return min(distance[-1])


def write_case(name, n, edges):
    input_path = SECRET / f"{name}.in"
    answer_path = SECRET / f"{name}.ans"
    with input_path.open("w", encoding="ascii") as stream:
        stream.write(f"{n} {len(edges)}\n")
        stream.writelines(f"{u} {v} {w}\n" for u, v, w in edges)
    answer_path.write_text(f"{solve(n, edges)}\n", encoding="ascii")


def main():
    SECRET.mkdir(parents=True, exist_ok=True)

    write_case("01_minimal", 2, [(1, 2, 73)])
    write_case(
        "02_route_change",
        5,
        [(1, 2, 4), (2, 5, 4), (1, 3, 20), (3, 4, 1), (4, 5, 1)],
    )
    write_case(
        "03_parallel",
        4,
        [(1, 2, 50), (1, 2, 2), (2, 3, 8), (3, 4, 9), (1, 4, 100)],
    )
    write_case(
        "04_large_weights",
        4,
        [(1, 2, 10**9), (2, 3, 10**9), (3, 4, 10**9)],
    )
    write_case(
        "05_keep_both_states",
        5,
        [(1, 2, 100), (1, 3, 1), (3, 2, 1), (2, 5, 100), (3, 4, 50), (4, 5, 50)],
    )
    write_case("06_equal_weights", 1001, [(i, i + 1, 1) for i in range(1, 1001)])
    write_case(
        "07_weighted_bfs_trap",
        8,
        [(1, 2, 1000), (2, 8, 1000), (1, 3, 2), (3, 4, 2), (4, 5, 2), (5, 6, 2), (6, 7, 2), (7, 8, 2)],
    )

    rng = random.Random(3001)
    # A random connected graph at both input limits: n = 200,000 and m = 300,000.
    n = 200_000
    edges = [(i, i + 1, rng.randint(1, 10**6)) for i in range(1, n)]
    for _ in range(100_001):
        u = rng.randint(1, n)
        v = rng.randint(1, n)
        while v == u:
            v = rng.randint(1, n)
        edges.append((u, v, rng.randint(1, 10**9)))
    write_case("08_large_random", n, edges)

    n = 200_000
    edges = [(i, i + 1, 1 + (i * 1_000_003) % 10**9) for i in range(1, n)]
    write_case("09_large_path", n, edges)


if __name__ == "__main__":
    main()
