import os
from mako.lookup import TemplateLookup
from mako.template import Template

# Path where templates will be stored
template_dir = "templates"
if not os.path.exists(template_dir):
    os.makedirs(template_dir)

# Mako Template code
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

# Save Mako template to disk
template_name = "product_template.mako"
template_file = os.path.join(template_dir, template_name)

if not os.path.exists(template_file):
    with open(template_file, 'w') as f:
        f.write(mako_template_code)

# Set up Mako TemplateLookup for caching (you can specify a cache directory here)
lookup = TemplateLookup(directories=[template_dir])

# Pre-compile the template and render it
template = lookup.get_template(template_name)
print(template.render(products=[{"name": "Laptop", "price": 999.99, "on_sale": True}]))
