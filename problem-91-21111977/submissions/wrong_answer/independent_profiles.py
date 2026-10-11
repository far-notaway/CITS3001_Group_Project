#!/usr/bin/env python3

# Incorrect because it treats profiles from the same server as separate items.

import sys


input = sys.stdin.readline
server_count, budget = map(int, input().split())
profiles = []

for _ in range(server_count):
    profile_count = int(input())
    for _ in range(profile_count):
        profiles.append(tuple(map(int, input().split())))

best = [0] * (budget + 1)

for duration, reduction in profiles:
    for time in range(budget, duration - 1, -1):
        best[time] = max(best[time], best[time - duration] + reduction)

print(best[budget])

