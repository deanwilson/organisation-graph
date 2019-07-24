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

Now we have the server running we will install the python environment
used to load data into it. I'm using `python 3` and a `venv` to ensure this
experiment stays isolated.

    # Create the python venv
    $ python3 -mvenv venv

    # Active it
    $ source venv/bin/activate

    # Install the required modules
    $ pip install -r requirements.txt
    Successfully installed ...snip... py2neo-4.3.0 pyyaml-5.1.1 ...snip...

Dependencies done you can now run `python3 build-graph.py` from the shell you
activated the `venv` in and exported the Neo4J password. Once this has
completed, open a web browser to <http://127.0.0.1:7474/browser/>, login and run
a query to show all results:

    MATCH (n) return n

You should now see all the nodes and relationships you've created and be able to
explore the data.

![A Graph screenshot](/images/organisation-graph-data.png "Neo4J node browser with sample data")

