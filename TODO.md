# OrgGraph TODO

## Documentation

  * Doc page of the contents of `bin/`

## Extract the Person class

 * Convert the person hash to a collection of objects #class Person: def __init__(self): in the graph building script

## Migrate build graph script to objects

 * Add node caching to the objects
 * remove all the YAML literal / dict focus code

## Move to the official neo4j driver?

 * Should I move to https://github.com/neo4j/neo4j-python-driver ?
  * [Example of relationships](https://github.com/neo4j/neo4j-python-driver/blob/963936fab6216840c63877114150426badde97cb/tests/examples/pass_bookmarks_example.py)
 * GOV.UK use neo4j-driver==1.7.4

Is this better for the querying aspect?

## Roles

 * Update the Role objects to add the salary ranges
 * Document some queries around this.
  * median quarterly cost

## Add Tox

 * run tests under multiple python versions

# Undecided

## Add a flake plugin

 * Add pydocstyle
 * https://pypi.org/project/flake8-docstrings/
 * Finds lots of issues. Unsure about the value

## Unsorted

 * Leavers? - Which services will be impacted? Sample query
 * Teams
  * Should Teams be a seperate entity so they can have additional metadata added
  * Or should all metadata be added as relationships from the other source?
 * Tie services to skills matrix and have staff complete a matrix
 * Add test matchers for relationships
  - person node 'Dean' is 'relationship name' to person node 'Jo'
 * Document running the tests
  * pytest -v --ignore=tests/test_graph_contents.py
 * GitHub
  * Look for different teams with identical memberships

### Temporal relationships

The current graph is completely point in time and allows no history or versioning
outside of keeping the configs inside git

 * Add multiple relationships
 * one with current
 * one per time period
