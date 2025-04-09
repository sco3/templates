
Testing template compilation + rendering performance (1 invocation(s)):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |          1 |        0.002725 |                  0.002725 |
| Cheetah3   |          1 |        0.003355 |                  0.003355 |
| Jinja2     |          1 |        0.002363 |                  0.002363 |
| Minijinja  |          1 |        0.000254 |                  0.000254 |

Testing template compilation + rendering performance (10 invocation(s)):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |         10 |        0.007421 |                  0.000742 |
| Cheetah3   |         10 |        0.001108 |                  0.000111 |
| Jinja2     |         10 |        0.012765 |                  0.001277 |
| Minijinja  |         10 |        0.001370 |                  0.000137 |

Testing template compilation + rendering performance (100 invocation(s)):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |        100 |        0.072831 |                  0.000728 |
| Cheetah3   |        100 |        0.008919 |                  0.000089 |
| Jinja2     |        100 |        0.129571 |                  0.001296 |
| Minijinja  |        100 |        0.012954 |                  0.000130 |

Testing template compilation + rendering performance (1000 invocation(s)):
---

| Name       | Iterations |  Total Time (s) |   Avg Time per Render (s) |
|------------|------------|-----------------|---------------------------|
| Mako       |       1000 |        0.731535 |                  0.000732 |
| Cheetah3   |       1000 |        0.087500 |                  0.000087 |
| Jinja2     |       1000 |        1.296226 |                  0.001296 |
| Minijinja  |       1000 |        0.126493 |                  0.000126 |
