#!/usr/bin/env -S uv run

import time
from mako.template import Template as MakoTemplate
from Cheetah.Template import Template as CheetahTemplate
from jinja2 import Template as Jinja2Template, StrictUndefined
from minijinja import Environment

# Sample data
products = [
    {"name": "Laptop", "price": 999.99, "on_sale": True},
    {"name": "Smartphone", "price": 499.99, "on_sale": False},
    {"name": "Headphones", "price": 199.99, "on_sale": True},
]

# 1. Mako Template
mako_template_code = """
<%!
    def format_price(price):
        return "${:,.2f}".format(price)
%>
<ul>
% for product in products:
    <li>
        ${product["name"]} - ${format_price(product["price"])}
        % if product["on_sale"]:
            <strong>On Sale!</strong>
        % endif
    </li>
% endfor
</ul>
"""

# 2. Cheetah3 Template
cheetah_template_code = """
#def format_price(price)
    #return "${:,.2f}".format(price)
#end def
<ul>
#for $product in $products
    <li>
        $product.name - $format_price($product.price)
        #if $product.on_sale
            <strong>On Sale!</strong>
        #end if
    </li>
#end for
</ul>
"""

# 3. Jinja2 Template
jinja2_template_code = """
{% macro format_price(price) %}
    {{ "${:,.2f}".format(price) }}
{% endmacro %}
<ul>
{% for product in products %}
    <li>
        {{ product.name }} - {{ format_price(product.price) }}
        {% if product.on_sale %}
            <strong>On Sale!</strong>
        {% endif %}
    </li>
{% endfor %}
</ul>
"""

minijinja_template_code = """
{% macro format_price(price) %}
    {{ price  }}
{% endmacro %}
<ul>
{% for product in products %}
    <li>
        {{ product.name }} - {{ format_price(product.price) }}
        {% if product.on_sale %}
            <strong>On Sale!</strong>
        {% endif %}
    </li>
{% endfor %}
</ul>
"""



# Rendering and timing functions
def render_mako():
    template = MakoTemplate(mako_template_code)
    return template.render(products=products)

def render_cheetah():
    template = CheetahTemplate(cheetah_template_code, searchList=[{'products': products}])
    return str(template)

def render_jinja2():
    template = Jinja2Template(jinja2_template_code, undefined=StrictUndefined)
    return template.render(products=products)

def currency(value):
    return "${:,.2f}".format(value)

def render_minijinja():
    t_name = "test"
    env = Environment(templates={
        t_name:minijinja_template_code,
    }
    )

    return env.render_template(t_name, products=products)



# Measure execution times for 1000 invocations
def measure_execution_time(render_func, name, iterations=1000):
    start_time = time.time()
    for _ in range(iterations):
        render_func()
    end_time = time.time()
    duration = end_time - start_time
    avg_time = duration / iterations
    print(f"* {name} Rendered {iterations} times in: {duration:.6f} seconds (Avg: {avg_time:.6f} seconds per render)")


print("\nTesting template rendering performance (1 invocations):\n---\n")
measure_execution_time(render_mako, "Mako", iterations=1)
measure_execution_time(render_cheetah, "Cheetah3", iterations=1)
measure_execution_time(render_jinja2, "Jinja2", iterations=1)
measure_execution_time(render_minijinja, "Minijinja", iterations=1)

print("\nTesting template rendering performance (10 invocations):\n---\n")
measure_execution_time(render_mako, "Mako", iterations=10)
measure_execution_time(render_cheetah, "Cheetah3", iterations=10)
measure_execution_time(render_jinja2, "Jinja2", iterations=10)
measure_execution_time(render_minijinja, "Minijinja", iterations=10)

print("\nTesting template rendering performance (100 invocations):\n---\n")
measure_execution_time(render_mako, "Mako", iterations=100)
measure_execution_time(render_cheetah, "Cheetah3", iterations=100)
measure_execution_time(render_jinja2, "Jinja2", iterations=100)
measure_execution_time(render_minijinja, "Minijinja", iterations=100)

print("\nTesting template rendering performance (1000 invocations):\n---\n")
measure_execution_time(render_mako, "Mako")
measure_execution_time(render_cheetah, "Cheetah3")
measure_execution_time(render_jinja2, "Jinja2")
measure_execution_time(render_minijinja, "Minijinja")
