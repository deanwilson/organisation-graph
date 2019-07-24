# organisation-graph

An experiment in representing an organisations structure in a GraphDB

## Getting started

To try out the organisation graph you'll need a neo4j instance, which
I'm going to run via `docker`, and a working python 3 install with some
additional modules.

First we'll set our chosen Neo4j password and install the `Neo4j`
container. By default this will place the persistent Neo4j server files
under `$HOME/python-neo4j`. You can change this by editing the
`bin/run-neo-docker.sh` script before running it.

    export ORG_GRAPH_NEO_PASSWORD=my_test_pass

    $ bin/run-neo-docker.sh
    0d45567uhdfdthae4731b8fc74sdff20g44740e32888ac5bd2d6438eba1d8a4d0f22e # Container ID


You can confirm the container is running with `docker ps` and the container ID
returned by our bash script above.
