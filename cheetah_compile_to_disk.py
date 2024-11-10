from Cheetah.Template import Template
import os

# Cheetah Template code
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

# Save Cheetah template to disk
cheetah_template_path = "cheetah_template.py"

if not os.path.exists(cheetah_template_path):
    template = Template(cheetah_template_code, searchList=[{'products': [{"name": "Laptop", "price": 999.99, "on_sale": True}]}])
    template.compile()
    with open(cheetah_template_path, "w") as f:
        f.write(str(template))

# Load and render the precompiled Cheetah template
compiled_template = Template(file=cheetah_template_path)
print(str(compiled_template))
