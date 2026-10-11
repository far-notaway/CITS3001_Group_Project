#!/usr/bin/env python3

# Incorrect because it requires the chosen profiles to use exactly B minutes.

import sys


input = sys.stdin.readline
server_count, budget = map(int, input().split())
previous = [-1] * (budget + 1)
previous[0] = 0

for _ in range(server_count):
    profile_count = int(input())
    profiles = [tuple(map(int, input().split())) for _ in range(profile_count)]
    current = previous.copy()

    for duration, reduction in profiles:
        for time in range(duration, budget + 1):
            if previous[time - duration] != -1:
                current[time] = max(
                    current[time], previous[time - duration] + reduction
                )

    previous = current

print(max(0, previous[budget]))

