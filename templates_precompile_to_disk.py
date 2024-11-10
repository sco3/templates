import time
import os
from mako.template import Template as MakoTemplate
from Cheetah.Template import Template as CheetahTemplate
from jinja2 import Environment, FileSystemLoader, Template as Jinja2Template

# Sample data
products = [
    {"name": "Laptop", "price": 999.99, "on_sale": True},
    {"name": "Smartphone", "price": 499.99, "on_sale": False},
    {"name": "Headphones", "price": 199.99, "on_sale": True},
]

# Template code (same for all)
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

# Path for compiled templates
mako_compiled_path = "mako_template.py"
cheetah_compiled_path = "cheetah_template.py"
jinja2_cache_dir = "jinja2_cache"

# Pre-compiling Mako template
if not os.path.exists(mako_compiled_path):
    mako_template = MakoTemplate(mako_template_code)
    with open(mako_compiled_path, "w") as f:
        f.write(mako_template.compile())

# Pre-compiling Cheetah template
if not os.path.exists(cheetah_compiled_path):
    cheetah_template = CheetahTemplate(cheetah_template_code, searchList=[{'products': products}])
    cheetah_template.compile()
    with open(cheetah_compiled_path, "w") as f:
        f.write(str(cheetah_template))

# Set up Jinja2 cache
os.makedirs(jinja2_cache_dir, exist_ok=True)
jinja2_env = Environment(
    loader=FileSystemLoader(searchpath="./"),
    auto_reload=False,
    cache_size=100,
)
jinja2_template_name = "jinja2_template.html"

# Save Jinja2 template code if it doesn't exist
if not os.path.exists(jinja2_template_name):
    with open(jinja2_template_name, "w") as f:
        f.write(jinja2_template_code)

# Timing and rendering functions remain unchanged

# Example of rendering functions with precompiled templates...
