#!/usr/bin/env -S uv run

import time
from pathlib import Path
from mako.template import Template as MakoTemplate
from Cheetah.Template import Template as CheetahTemplate
from jinja2 import Template as Jinja2Template, StrictUndefined
from minijinja import Environment

# Sample data
products = [
    {"name": "Laptop", "price": 999.99, "on_sale": True},
    {"name": "Smartphone", "price": 499.99, "on_sale": False},
    {"name": "Headphones", "price": 199.99, "on_sale": True},
    {"name": "Tablet", "price": 299.99, "on_sale": False},
    {"name": "Smartwatch", "price": 149.99, "on_sale": True},
    {"name": "Keyboard", "price": 89.99, "on_sale": False},
    {"name": "Mouse", "price": 29.99, "on_sale": True},
    {"name": "Monitor", "price": 349.99, "on_sale": False},
    {"name": "Printer", "price": 129.99, "on_sale": True},
    {"name": "Charger", "price": 19.99, "on_sale": False},
    {"name": "Bluetooth Speaker", "price": 79.99, "on_sale": True},
    {"name": "USB Cable", "price": 5.99, "on_sale": False},
    {"name": "Camera", "price": 249.99, "on_sale": True},
    {"name": "Hard Drive", "price": 59.99, "on_sale": False},
    {"name": "Flash Drive", "price": 15.99, "on_sale": True},
    {"name": "Graphics Card", "price": 799.99, "on_sale": False},
    {"name": "Webcam", "price": 49.99, "on_sale": True},
    {"name": "Router", "price": 69.99, "on_sale": False},
    {"name": "External SSD", "price": 129.99, "on_sale": True}
]

# Read templates into string variables once
mako_template_code      = Path("t.mako").read_text()
cheetah_template_code   = Path("t.cheetah3").read_text()
jinja2_template_code    = Path("t.jinja2").read_text()
minijinja_template_code = Path("t.minijinja").read_text()

# Rendering functions (compile + render per iteration)
def render_mako():
    template = MakoTemplate(mako_template_code)
    return template.render(products=products)

def render_cheetah():
    template = CheetahTemplate(cheetah_template_code, searchList=[{'products': products}])
    return str(template)

def render_jinja2():
    template = Jinja2Template(jinja2_template_code, undefined=StrictUndefined)
    return template.render(products=products)

def render_minijinja():
    env = Environment()
    env.add_filter("currency", lambda v: "${:,.2f}".format(v))
    env.add_template("template", minijinja_template_code)
    return env.render_template("template", products=products)

# Benchmark
def measure_execution_time(render_func, name, iterations=1000):
    start_time = time.time()
    for _ in range(iterations):
        render_func()
    duration = time.time() - start_time
    avg_time = duration / iterations
    print(f"| {name:<10} | {iterations:>10} | {duration:>15.6f} | {avg_time:>25.6f} |")

def header(n):
    print(f"\nTesting compilation + rendering performance ({n} invocation(s)):\n---\n")
    print(f"| {'Name':<10} | {'Iterations':>10} | {'Total Time (s)':>15} | {'Avg Time per Render (s)':>25} |")
    print(f"|{'-'*12}|{'-'*12}|{'-'*17}|{'-'*27}|")

# Run benchmarks
for i in [1, 10, 100, 1000]:
    header(i)
    measure_execution_time(render_mako, "Mako", iterations=i)
    measure_execution_time(render_cheetah, "Cheetah3", iterations=i)
    measure_execution_time(render_jinja2, "Jinja2", iterations=i)
    measure_execution_time(render_minijinja, "Minijinja", iterations=i)
