#!/usr/bin/env python3

import sys


def main():
    input = sys.stdin.readline
    server_count, budget = map(int, input().split())
    previous = [0] * (budget + 1)

    for _ in range(server_count):
        profile_count = int(input())
        profiles = []

        for _ in range(profile_count):
            duration, reduction = map(int, input().split())
            profiles.append((duration, reduction))

        # Copying the old row represents skipping this server.
        current = previous.copy()

        for duration, reduction in profiles:
            if duration > budget:
                continue

            # Read from the previous row so only one profile from this server
            # can be selected.
            for time in range(duration, budget + 1):
                candidate = previous[time - duration] + reduction
                if candidate > current[time]:
                    current[time] = candidate

        previous = current

    print(previous[budget])


if __name__ == "__main__":
    main()
