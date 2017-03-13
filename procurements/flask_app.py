from flask import Flask, render_template, request, g
import cubes
import os.path
import sqlalchemy
from configparser import ConfigParser

import logging

logger = cubes.get_logger()
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

#
# Data we aregoing to browse and logical model of the data
#

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(APP_ROOT, "vvo_model.json")
DB_PATH = os.path.join(APP_ROOT, "vvo_data.sqlite")
DB_URL = "sqlite:///" + DB_PATH

CUBE_NAME = "contracts"

# Some global variables. We do not have to care about Flask provided thread
# safety here, as they are non-mutable.

workspace = None
model = None

@app.route("/")
@app.route("/<dim_name>")
def report(dim_name=None):
    cube = workspace.cube("contracts")
    browser = workspace.browser(cube)
    result = browser.aggregate()
    print('keys: ', result.levels)

    if not dim_name:
        return render_template('report.html', dimensions=cube.dimensions)

    # First we need to get the hierarchy to know the order of levels. Cubes
    # supports multiple hierarchies internally.
    
    dimension = cube.dimension(dim_name)
    hierarchy = dimension.hierarchy()

    # Parse the`cut` request parameter and convert it to a list of 
    # actual cube cuts. Think of this as of multi-dimensional path, even that 
    # for this simple example, we are goint to use only one dimension for
    # browsing.

    cutstr = request.args.get("cut")
    cell = cubes.Cell(browser.cube, cubes.cuts_from_string(cube,cutstr))

    # Get the cut of actually browsed dimension, so we know "where we are" -
    # the current dimension path
    cut = cell.cut_for_dimension(dimension)

    if cut:
        path = cut.path
    else:
        path = []
    
    #
    # Do the work, do the aggregation.
    #
    print("AGGREGATE %s DD: %s" % (cell, dim_name))
    result = browser.aggregate(cell, drilldown=[dim_name])

    # If we have no path, then there is no cut for the dimension, # therefore
    # there is no corresponding detail.
    if path:
        details = browser.cell_details(cell, dimension)[0]
    else:
        details = []

    # Find what level we are on and what is going to be the drill-down level
    # in the hierarchy
    
    levels = hierarchy.levels_for_path(path)
    if levels:
        next_level = hierarchy.next_level(levels[-1])
    else:
        next_level = hierarchy.next_level(None)

    # Are we at the very detailed level?

    is_last = hierarchy.is_last(next_level)
    # Finally, we render it

    return render_template('report.html',
                            dimensions=cube.dimensions,
                            dimension=dimension,
                            levels=levels,
                            next_level=next_level,
                            result=result,
                            cell=cell,
                            is_last=is_last,
                            details=details)

@app.before_first_request
def initialize_model():
    global model
    global workspace
    #model = cubes.load_model(MODEL_PATH)
    # workspace = cubes.create_workspace("sql",url=DB_URL,
    #                                                  fact_prefix="ft_",
    #                                                  dimension_prefix="dm_")
    # engine = sqlalchemy.create_engine(DB_URL)
    # connection = engine.connect()

    parser = ConfigParser()
    parser.read("slicer.ini")
    workspace = cubes.Workspace(config=parser)
    #workspace.register_default_store("sql",url=DB_URL)
    print(MODEL_PATH)
    print(DB_URL)
    #workspace.import_model(MODEL_PATH)
if __name__ == "__main__":
    app.debug = True
    app.run()
