#!/usr/bin/env python3

# Incorrect because choosing the best reduction per minute is not always optimal.

import sys


input = sys.stdin.readline
server_count, budget = map(int, input().split())
profiles = []

for server in range(server_count):
    profile_count = int(input())
    for _ in range(profile_count):
        duration, reduction = map(int, input().split())
        ratio = reduction / duration
        profiles.append((ratio, reduction, duration, server))

profiles.sort(reverse=True)
used_servers = set()
remaining = budget
answer = 0

for _, reduction, duration, server in profiles:
    if server not in used_servers and duration <= remaining:
        used_servers.add(server)
        remaining -= duration
        answer += reduction

print(answer)

