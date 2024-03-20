.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/bracket-generator.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/bracket-generator
    .. image:: https://readthedocs.org/projects/bracket-generator/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://bracket-generator.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/bracket-generator/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/bracket-generator
    .. image:: https://img.shields.io/pypi/v/bracket-generator.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/bracket-generator/
    .. image:: https://img.shields.io/conda/vn/conda-forge/bracket-generator.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/bracket-generator
    .. image:: https://pepy.tech/badge/bracket-generator/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/bracket-generator
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/bracket-generator

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

=================
bracket-generator
=================


    This is a simple python based bracket generator for the NCAA tournament.


The odds are controlled in the src/bracket_generator/game.py class and are used
in the simulate() function to determine a winner based on seeding.

Usage:
* run the following to setup a python environment
```
python3 -m venv venv
. venv/bin/activate
```
* the from the top level run `pip install .` to setup the virtual env
* update the config/test_bracket.yaml config file for this year's tournament
* once thats done you cna simply run `bracket_generator --config config/test_bracket.yaml -vv`

To Do:
* Update the tests to be more robust
* Update the odds with something more complex and based on historicals
* Update the output so you don't have to use verbose logging and so it looks cleaner

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
