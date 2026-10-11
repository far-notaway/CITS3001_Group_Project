# Hardening Before Sunrise: Solution Description

## Overview

This problem is a variation of 0/1 knapsack. The difference is that the profiles are split into groups, with one group for each server. We can choose at most one profile from each server, or skip that server.

I use dynamic programming to store the best risk reduction available for each time limit. Let `previous[t]` be the best result after processing the earlier servers, using at most `t` minutes.

## Algorithm

The array starts with zero at every position because choosing no profiles is always allowed.

For each server, I copy `previous` into `current`. This covers the choice of skipping that server. I then consider each of its profiles. If a profile takes `duration` minutes and reduces risk by `reduction`, the transition is:

```text
current[t] = max(current[t], previous[t - duration] + reduction)
```

Every transition reads from `previous`, not `current`. This is the main detail of the solution. Reading from `current` could combine two profiles from the same server, which is not allowed.

After checking every profile for the server, `current` becomes the new `previous` array. The answer is `previous[B]` after all servers have been processed.

```text
previous[0 ... B] = 0

for each server:
    current = copy of previous

    for each profile (duration, reduction) for that server:
        for t from duration to B:
            candidate = previous[t - duration] + reduction
            current[t] = max(current[t], candidate)

    previous = current

output previous[B]
```

A greedy approach does not work because the profile with the highest reduction, or the best reduction per minute, may prevent a better combination later. Treating every profile as a separate knapsack item also fails because it could select more than one profile for the same server.

## Correctness

Before any servers are processed, every entry is zero, which is correct because no profile can be selected.

Assume `previous[t]` is correct after processing the first `i - 1` servers. For server `i`, a valid solution either skips the server or selects exactly one of its profiles. Skipping keeps the value `previous[t]`. Selecting a profile with duration `d` and reduction `r` adds `r` to the best result for the earlier servers with at most `t - d` minutes, giving `previous[t - d] + r`.

The transition checks both possibilities and every profile that fits. Because it only reads from the previous array, it cannot choose two profiles from the current server. Therefore, `current[t]` is correct after processing server `i`. By induction, `previous[B]` is the maximum risk reduction possible within the budget.

## Complexity

Let `P` be the total number of profiles and `B` the time budget. Each profile checks at most `B` positions, so the time complexity is `O(PB)`. Two arrays of length `B + 1` are stored, giving `O(B)` space complexity.

## AI use declaration

I used AI tools to help brainstorm ideas, identify suitable algorithmic approaches, generate input data, and provide suggestions when debugging.
