
Testing template rendering performance (1 invocation(s)):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |          1 |        0.002533 |        0.002533 |
| Cheetah3   |          1 |        0.003086 |        0.003086 |
| Jinja2     |          1 |        0.002166 |        0.002166 |
| Minijinja  |          1 |        0.000179 |        0.000179 |

Testing template rendering performance (10 invocation(s)):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |         10 |        0.007173 |        0.000717 |
| Cheetah3   |         10 |        0.000422 |        0.000042 |
| Jinja2     |         10 |        0.011773 |        0.001177 |
| Minijinja  |         10 |        0.000384 |        0.000038 |

Testing template rendering performance (100 invocation(s)):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |        100 |        0.070550 |        0.000706 |
| Cheetah3   |        100 |        0.002162 |        0.000022 |
| Jinja2     |        100 |        0.117698 |        0.001177 |
| Minijinja  |        100 |        0.003128 |        0.000031 |

Testing template rendering performance (1000 invocation(s)):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |       1000 |        0.703843 |        0.000704 |
| Cheetah3   |       1000 |        0.020564 |        0.000021 |
| Jinja2     |       1000 |        1.168896 |        0.001169 |
| Minijinja  |       1000 |        0.029271 |        0.000029 |
