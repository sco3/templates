
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
