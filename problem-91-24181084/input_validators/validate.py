#!/usr/bin/env python3
"""Check that a Quokka Express input file follows the stated format."""

import sys
import re


def reject(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(43)


def read_numbers(expected: int, label: str) -> list[int]:
    line = sys.stdin.buffer.readline()
    if not line:
        reject(f"missing {label}")
    pattern = rb"[1-9][0-9]*" + rb" [1-9][0-9]*" * (expected - 1) + rb"\n"
    if re.fullmatch(pattern, line) is None:
        reject(f"{label} must contain {expected} integers with single spaces")
    return [int(part) for part in line.split()]


def find(parent: list[int], node: int) -> int:
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node


def union(parent: list[int], size: list[int], a: int, b: int) -> None:
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]


def main() -> None:
    n, m = read_numbers(2, "first line")
    if not 2 <= n <= 200_000:
        reject("n is outside the allowed range")
    if not 1 <= m <= 300_000:
        reject("m is outside the allowed range")

    parent = list(range(n))
    size = [1] * n

    for edge_number in range(1, m + 1):
        u, v, w = read_numbers(3, f"trail {edge_number}")
        if not 1 <= u <= n or not 1 <= v <= n:
            reject(f"trail {edge_number} has an invalid camp number")
        if u == v:
            reject(f"trail {edge_number} joins a camp to itself")
        if not 1 <= w <= 1_000_000_000:
            reject(f"trail {edge_number} has an invalid time")
        union(parent, size, u - 1, v - 1)

    if sys.stdin.buffer.read().strip():
        reject("extra data after the last trail")

    root = find(parent, 0)
    if any(find(parent, node) != root for node in range(1, n)):
        reject("not every camp can be reached")

    raise SystemExit(42)


if __name__ == "__main__":
    main()
