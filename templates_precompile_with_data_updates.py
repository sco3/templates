#!/usr/bin/env -S uv run

import time
from mako.template import Template as MakoTemplate
from Cheetah.Template import Template as CheetahTemplate
from jinja2 import Template as Jinja2Template

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


def upd_products(p: dict, i: int) -> None:
    products[0]["price"] = i
    products[1]["price"] = i * 2
    products[2]["price"] = i * 3
    # print (products)


# Pre-compilation functions for each engine
def pre_compile_mako():
    # Pre-compile Mako template into a module.
    return MakoTemplate(mako_template_code)

def pre_compile_cheetah():
    # Compile Cheetah template (Cheetah has a compile method)
    return CheetahTemplate(cheetah_template_code, searchList=[{'products': products}])

def pre_compile_jinja2():
    # Pre-compile Jinja2 template
    return Jinja2Template(jinja2_template_code)

# Rendering and timing functions
def render_mako(template):
    return template.render(products=products)

def render_cheetah(template):
    return str(template)

def render_jinja2(template):
    return template.render(products=products)

# Measure execution times for 1000 invocations
def measure_execution_time(render_func, template, name, iterations=1000):
    start_time = time.time()
    for _ in range(iterations):
        render_func(template)
    end_time = time.time()
    duration = end_time - start_time
    avg_time = duration / iterations
    print(f"{name} Rendered {iterations} times in: {duration:.6f} seconds (Avg: {avg_time:.6f} seconds per render)")

# Pre-compiling templates
print("Pre-compiling templates...\n")
mako_template = pre_compile_mako()
cheetah_template = pre_compile_cheetah()
jinja2_template = pre_compile_jinja2()

# Running and timing each template engine for 1000 invocations
print("\nTesting template rendering performance (1000 invocations):\n")
measure_execution_time(render_mako, mako_template, "Mako")
measure_execution_time(render_cheetah, cheetah_template, "Cheetah3")
measure_execution_time(render_jinja2, jinja2_template, "Jinja2")
