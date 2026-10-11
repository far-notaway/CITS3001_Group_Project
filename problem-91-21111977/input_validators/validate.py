#!/usr/bin/env python3

import sys


def read_numbers(expected):
    line = sys.stdin.readline()
    assert line.endswith("\n"), "each line must end with a newline"

    parts = line[:-1].split(" ")
    assert len(parts) == expected, "incorrect number of values on a line"
    assert all(
        part.isascii()
        and part.isdigit()
        and part[0] != "0"
        for part in parts
    ), "values must be positive integers without leading zeros"

    return [int(part) for part in parts]


n, budget = read_numbers(2)
assert 1 <= n <= 200
assert 1 <= budget <= 10_000

total_profiles = 0

for _ in range(n):
    profile_count = read_numbers(1)[0]
    assert 1 <= profile_count <= 1_000

    total_profiles += profile_count
    assert total_profiles <= 1_000

    for _ in range(profile_count):
        duration, reduction = read_numbers(2)
        assert 1 <= duration <= 1_000_000_000
        assert 1 <= reduction <= 1_000_000_000

assert sys.stdin.read() == "", "extra data after the last profile"
sys.exit(42)
