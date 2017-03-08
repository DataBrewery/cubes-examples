from cubes import Workspace, Cell

# 1. Create a workspace
workspace = Workspace()
workspace.register_default_store("sql",
                                 url="sqlite:///vvo_data.sqlite",
                                 dimension_prefix="dm_",
                                 fact_prefix="ft_")
workspace.import_model("procurements.cubesmodel")

# 2. Get a browser
browser = workspace.browser("contracts")
cube = browser.cube

# workspace = cubes.create_workspace("sql", model, url="postgres://localhost/ep2012",
#                                     schema="vvo",
#                                     dimension_prefix="dm_",
#                                     fact_prefix="ft_",
#                                     denormalized_view_schema="views",
#                                     use_denormalization=False,
#                                     denormalized_view_prefix="mft_")

def drilldown(cell, dimension):
    """Drill-down and aggregate recursively through als levels of `dimension`.
    
    This function is like recursively traversing directories on a file system
    and aggregating the file sizes, for example.
    
    * `cell` - cube cell to drill-down
    * `dimension` - dimension to be traversed through all levels
    """

    if cell.is_base(dimension):
        return

    result = browser.aggregate(aggregates=["contract_amount_sum"], cell=cell, drilldown=[dimension])

    # for row in cubes.drilldown_rows(cell, result, dimension):
    for row in result.table_rows(dimension):
        indent = "    " * (len(row.path) - 1)
        print "%s%s: %d" % (indent, row.label, row.record["contract_amount_sum"])

        new_cell = cell.drilldown(dimension, row.key)
        drilldown(new_cell, dimension)

# Get whole cube
cell = Cell(cube)

print "Drill down through date hierarchy:"
drilldown(cell, cube.dimension("date"))

# print "Drill down through CPV hierarchy in 2011:"
# cell = cell.slice(cubes.PointCut("date", [2010,5]))
# drilldown(cell, cube.dimension("cpv"))

