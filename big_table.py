import time
from mako.template import Template as MakoTemplate
from Cheetah.Template import Template as CheetahTemplate
from jinja2 import Template as Jinja2Template

# Create the table data (100x100 cells)
table_data = [[f"Cell {row * 100 + col}" for col in range(100)] for row in range(100)]

# Mako Template code
mako_template_code = """
<%!
    def format_cell(cell):
        return f"Cell {cell}"
%>
<table>
% for row in table:
    <tr>
    % for col in row:
        <td>${format_cell(col)}</td>
    % endfor
    </tr>
% endfor
</table>
"""

# Cheetah3 Template code
cheetah_template_code = """
#def format_cell(cell)
    return "Cell $cell"
#end def
<table>
#for $row in $table
    <tr>
    #for $col in $row
        <td>$format_cell($col)</td>
    #end for
    </tr>
#end for
</table>
"""

# Jinja2 Template code
jinja2_template_code = """
{% macro format_cell(cell) %}
    Cell {{ cell }}
{% endmacro %}

<table>
{% for row in table %}
    <tr>
    {% for col in row %}
        <td>{{ format_cell(col) }}</td>
    {% endfor %}
    </tr>
{% endfor %}
</table>
"""

# 1. Mako Template
def render_mako():
    template = MakoTemplate(mako_template_code)
    return template.render(table=table_data)

# 2. Cheetah3 Template
def render_cheetah():
    template = CheetahTemplate(cheetah_template_code, searchList=[{'table': table_data}])
    return str(template)

# 3. Jinja2 Template
def render_jinja2():
    template = Jinja2Template(jinja2_template_code)
    return template.render(table=table_data)

# Measure execution times for 1000 invocations
def measure_execution_time(render_func, name, iterations=1000):
    start_time = time.time()
    for _ in range(iterations):
        render_func()
    end_time = time.time()
    duration = end_time - start_time
    avg_time = duration / iterations
    print(f"{name} Rendered {iterations} times in: {duration:.6f} seconds (Avg: {avg_time:.6f} seconds per render)")

# Start the benchmarking
print("Testing template rendering performance for 100x100 table (1 invocation):\n")
measure_execution_time(render_mako, "Mako", iterations=1)
measure_execution_time(render_cheetah, "Cheetah3", iterations=1)
measure_execution_time(render_jinja2, "Jinja2", iterations=1)

print("\nTesting template rendering performance for 100x100 table (1000 invocations):\n")
measure_execution_time(render_mako, "Mako")
measure_execution_time(render_cheetah, "Cheetah3")
measure_execution_time(render_jinja2, "Jinja2")
