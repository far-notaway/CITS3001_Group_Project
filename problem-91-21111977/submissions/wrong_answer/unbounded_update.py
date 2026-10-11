#!/usr/bin/env python3

# Incorrect because updating forwards in one array can reuse a profile.

import sys


input = sys.stdin.readline
server_count, budget = map(int, input().split())
best = [0] * (budget + 1)

for _ in range(server_count):
    profile_count = int(input())

    for _ in range(profile_count):
        duration, reduction = map(int, input().split())

        for time in range(duration, budget + 1):
            best[time] = max(best[time], best[time - duration] + reduction)

print(best[budget])

