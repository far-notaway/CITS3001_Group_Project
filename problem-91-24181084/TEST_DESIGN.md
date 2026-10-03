# Secret tests

I made each test to catch a different mistake.

| Test | What it checks |
|---|---|
| `01_minimal` | The smallest graph. The pass makes the only trail free. |
| `02_route_change` | The pass makes a different route better. |
| `03_parallel` | Two camps can have more than one trail. |
| `04_large_weights` | Big numbers and a bad infinity value. |
| `05_keep_both_states` | The program must keep both pass states. |
| `06_equal_weights` | A long path where every trail has the same time. |
| `07_weighted_bfs_trap` | BFS is wrong because trail times are different. |
| `08_large_random` | A random connected graph at the limits: $n=200000$ and $m=300000$. |
| `09_large_path` | A path with the maximum $n$. The slow answer should time out. |

The sample tests show the input style, a route change, and the smallest graph.
