# OrgGraph TODO

## Documentation

  * Doc page of the contents of `bin/`
  * Extract all the data structure information to a data structures page

## Salary Script

 * Move the script to ./bin
 * fix the imports and the script to use it

## Linting and formatting

 * add flake
  * run an example to see what it flags up.
  * https://gitlab.com/pycqa/flake8
 * add black
  * https://github.com/psf/black
  * rerun flake to view the differences

## Add PyTest for the jobs and Job classes

 * write a few small tests to ensure the job creates correctly
 * ensure a YAML file creates multiple jobs (fixtures directory?)

## Extract the Person class

 * Convert the person hash to a collection of objects #class Person: def __init__(self):
 * Extract the people class from the build org chart script
 * Add a few basic checks for it
 * Add a Person class collection wrapper
 * Add a few basic checks for it

## Add some basic graph structure tests

 * Ensure some of the sample data has nodes
 * Ensure some of the relationships are present
 * Make a pytest plugin for this?

## Migrate build graph script to objects

 * Add node caching to the objects
 * remove all the YAML literal / dict focus code

## Move to the official neo4j driver?

 * Should I move to https://github.com/neo4j/neo4j-python-driver ?
  * [Example of relationships](https://github.com/neo4j/neo4j-python-driver/blob/963936fab6216840c63877114150426badde97cb/tests/examples/pass_bookmarks_example.py)
 * GOV.UK use neo4j-driver==1.7.4

Is this better for the querying aspect?

## Add Tox

 * run tests under multiple python versions

# Undecided

## Add a flake plugin

 * Add pydocstyle
 * https://pypi.org/project/flake8-docstrings/

## Add Pyblack config if needed

```
pyproject.toml
[tool.black]
line-length = 88
```

## Unsorted

 * Leavers? - Which services will be impacted? Sample query
 * Teams
  * Should Teams be a seperate entity so they can have additional metadata added
  * Or should all metadata be added as relationships from the other source?
 * Tie services to skills matrix and have staff complete a matrix
 * Add test matchers for relationships
  - person node 'Dean' is 'relationship name' to person node 'Jo'
