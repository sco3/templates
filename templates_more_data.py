#!/usr/bin/env -S uv run

import time
from mako.template import Template as MakoTemplate
from Cheetah.Template import Template as CheetahTemplate
from jinja2 import Template as Jinja2Template



import random
from itertools import cycle

def products(num_records):
    """
    Generator to create a dynamic number of product records.

    Args:
        num_records (int): Total number of products to generate.

    Yields:
        dict: A product dictionary with 'name', 'price', and 'on_sale' attributes.
    """
    # Predefined values
    product_names = ["Laptop", "Smartphone", "Headphones", "Tablet", "Camera"]
    min_price = 100.00  # Minimum price
    max_price = 2000.00  # Maximum price
    name_cycle = cycle(product_names)  # Cycle through the product names

    for _ in range(num_records):
        yield {
            "name": next(name_cycle),  # Cyclic selection of names
            "price": round(random.uniform(min_price, max_price), 2),  # Random price
            "on_sale": random.choice([True, False]),  # Random on_sale status
        }



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

NREC:int=100


# Rendering and timing functions
def render_mako(i: int):
    template = MakoTemplate(mako_template_code)
    return template.render(products=products(NREC))


def render_cheetah(i: int):
    template = CheetahTemplate(
        cheetah_template_code, searchList=[{"products": products(NREC)}]
    )
    return str(template)


def render_jinja2(i: int):
    template = Jinja2Template(jinja2_template_code)
    return template.render(products=products(NREC))


# Measure execution times for 1000 invocations
def measure_execution_time(render_func, name, iterations=1000):
    start_time = time.time()
    for i in range(iterations):
        render_func(i)
    end_time = time.time()
    duration = end_time - start_time
    avg_time = duration / iterations
    print(
        f"{name} Rendered {iterations} times in: {duration:.6f} seconds (Avg: {avg_time:.6f} seconds per render)"
    )


print("Testing template rendering performance (1 invocations):\n")
measure_execution_time(render_mako, "Mako", iterations=1)
measure_execution_time(render_cheetah, "Cheetah3", iterations=1)
measure_execution_time(render_jinja2, "Jinja2", iterations=1)

print("Testing template rendering performance (1000 invocations):\n")
measure_execution_time(render_mako, "Mako")
measure_execution_time(render_cheetah, "Cheetah3")
measure_execution_time(render_jinja2, "Jinja2")
