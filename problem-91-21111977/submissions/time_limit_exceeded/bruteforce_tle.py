#!/usr/bin/env python3

# Correct on small inputs, but too slow for large inputs.

import sys


def search(servers, index, remaining):
    if index == len(servers):
        return 0

    best = search(servers, index + 1, remaining)

    for duration, reduction in servers[index]:
        if duration <= remaining:
            best = max(
                best,
                reduction + search(servers, index + 1, remaining - duration),
            )

    return best


input = sys.stdin.readline
server_count, budget = map(int, input().split())
servers = []

for _ in range(server_count):
    profile_count = int(input())
    profiles = [tuple(map(int, input().split())) for _ in range(profile_count)]
    servers.append(profiles)

print(search(servers, 0, budget))

