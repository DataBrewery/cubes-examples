import sqlalchemy
import cubes
import cubes.tutorial.sql as tutorial

def print_cross_table(onrows, oncolumns, table):
    # Print column header:
    out = "<html><body><table>"

    out += "<th></th>" * len(onrows) + "".join(["<th>%s</th>" % c for c in table.columns])

    measure = "amount_sum"

    for row_hdr, row in zip(table.rows, table.data):
        row_label = "".join(["<th>%s</th>" % h for h in tuple(row_hdr)])
        values_str = "".join(["<td>%s</td>" % (value[0] if value else 0) for value in row])
        row_string = "<tr>%s%s</tr>" % (row_label, values_str)
        out += row_string + "\n"
        
    out += "</table></body></html>"
    
    with open("table.html", "w") as f:
        f.write(out)
     
########################################################################
# Create browsing context
        
model = cubes.load_model("vvo_model.json")
cube = model.cube("contracts")
workspace = cubes.create_workspace("sql", model, url="sqlite:///vvo_data.sqlite",
                                    dimension_prefix="dm_",
                                    fact_prefix="ft_")
browser = workspace.browser(cube)
cell = cubes.Cell(cube)

########################################################################
# Create cross-table (written to table.html in current directory)

result = browser.aggregate(cell, drilldown=["process_type", "date"])

rows=["process_type.description"]
columns=["date.year"]

table = result.cross_table(rows, columns, ["contract_amount_sum"])
print_cross_table(rows, columns, table)

print "Created file: table.html"
