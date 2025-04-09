
Testing template rendering performance (1 invocation):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |          1 |        0.002588 |        0.002588 |
| Cheetah3   |          1 |        0.003116 |        0.003116 |
| Jinja2     |          1 |        0.002161 |        0.002161 |
| Minijinja  |          1 |        0.000170 |        0.000170 |

Testing template rendering performance (10 invocation):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |         10 |        0.007314 |        0.000731 |
| Cheetah3   |         10 |        0.000412 |        0.000041 |
| Jinja2     |         10 |        0.011948 |        0.001195 |
| Minijinja  |         10 |        0.000380 |        0.000038 |

Testing template rendering performance (100 invocation):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |        100 |        0.071263 |        0.000713 |
| Cheetah3   |        100 |        0.002166 |        0.000022 |
| Jinja2     |        100 |        0.119816 |        0.001198 |
| Minijinja  |        100 |        0.003049 |        0.000030 |

Testing template rendering performance (1000 invocation):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |       1000 |        0.714236 |        0.000714 |
| Cheetah3   |       1000 |        0.020726 |        0.000021 |
| Jinja2     |       1000 |        1.199730 |        0.001200 |
| Minijinja  |       1000 |        0.029146 |        0.000029 |
