Webshop (Online shop example)
=============================

Example includes:

* Model (model.json)
* Cubes server config (slicer.ini)
* Loaded SQLite database (webshop.sqlite)


Version
-------

This sample is tested with cubes-1.0.1.


Description
-----------

This sample includes a simple model and sample data from a fictional
online shop.

It contains a fact table "sales" with information about product sales,
customer country, product and product category, and invoice amount.

It also contains a fact table "webvisits" with information about
fictional web visits (country of visitor, page views, browser...).


Slicer Usage
------------

Make sure you've installed Cubes 1.0.x and that the `slicer` command
is available (either globally or within a *virtualenv*).

Execute:

    $ slicer serve slicer.ini

Documentation: http://packages.python.org/cubes/server.html


CubesViewer
-----------

You can use a client tool like CubesViewer to inspect these cubes:

Live example: http://jjmontesl.github.io/cubesviewer/

Documentation: https://github.com/jjmontesl/cubesviewer/


You can find a tutorial for CubesViewer and Cubes using this
data at https://github.com/jjmontesl/cubesviewer/blob/master/doc/guide/cubesviewer-quickstart.md .


Generating the data
-------------------

This sample data was generated using an (experimental) tool called
CubETL, which is able to insert data into OLAP schemas and
generates Cubes model automatically.

If you are interested in the topic, check it out and get in touch:

CubETL: https://github.com/jjmontesl/cubetl
WebShop ETL Source: https://github.com/jjmontesl/cubetl/blob/master/examples/webshop.yaml

(Note you are in the wild, there is little to no documentation, but there are
a bunch of examples and I'm happy to provide assistance and fix bugs).

