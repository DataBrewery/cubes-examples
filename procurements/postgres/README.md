PostgreSQL database dump
========================

Dump of example data (same as in the SQLite database) for Postgres database.

Files:

* pg_dump.sql - schema and full data dump
* pg_dump-schema.sql - dump of schema pnly

Load the data into database, edit slicer-pg.ini (change database name).

Use:

    $ slicer serve slicer-pg.ini
    
Denormalisation
---------------

1. uncomment three denormalisation lines in the slicer-pg.ini
2. either create schema `views` or change `denormalized_view_schema`
3. execute:

    $ slicer denormalize slicer-pg.ini
    
Try also with: --force, --materialize and --index arguments.

For more information read http://packages.python.org/cubes/slicer.html#denormalize


