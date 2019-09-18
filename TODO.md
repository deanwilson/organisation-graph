# OrgGraph TODO

## Documentation

  * Doc page of the contents of `bin/`

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


### Links
https://medium.com/neo4j/py2neo-v4-2bedc8afef2
