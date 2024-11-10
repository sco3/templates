import os
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 Environment with caching to disk
cache_dir = "jinja2_cache"
os.makedirs(cache_dir, exist_ok=True)

env = Environment(
    loader=FileSystemLoader(searchpath="./"),  # Load templates from the current directory
    auto_reload=False,  # Disable auto-reloading for faster performance
    cache_size=100,  # Number of templates to cache
)

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

template_name = "jinja2_template.html"

# Save Jinja2 template to disk
if not os.path.exists(template_name):
    with open(template_name, "w") as f:
        f.write(jinja2_template_code)

# Precompile and render the template using the Jinja2 environment
template = env.get_template(template_name)
print(template.render(products=[{"name": "Laptop", "price": 999.99, "on_sale": True}]))
