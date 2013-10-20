Public Procurements of Slovakia
===============================

Example includes:

* star schema
* mappings
* default dimension naming with prefixes
* default cube fact table naming (with explicit prefix)
* Flask (web microframework) example browser
* cross-table (see cross.py)

Slicer Use
----------

Execute:

    $ slicer serve slicer.ini

Documentation: http://packages.python.org/cubes/server.html

Cross table
-----------

    $ python cross.py
    
Result output is in table.html.

Flask Use
---------

    cd procurements
    python flask_app.py

Navigate browser to http://localhost:5000/

Source Data
-----------

http://tendre.sme.sk
