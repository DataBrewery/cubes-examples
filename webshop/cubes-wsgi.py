# Sample file to deploy Cubes slicer as a WSGI application,
# using a virtual environment.

import sys
import os
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/srv/cubes/env/lib/python3.4/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/srv/cubes')

# Activate virtual env
activate_env=os.path.expanduser("/srv/cubes/env/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

os.chdir('/srv/cubes-examples/webshop')

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(CURRENT_DIR, "slicer.ini")

from cubes.server.base import create_server
application = create_server(CONFIG_PATH)




