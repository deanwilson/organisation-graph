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

## Example Queries

Show the services and which teams own them as a table:

    MATCH (s:Service)-[:`owns`]-(t:Team)
    RETURN s.name as Service, t.name as Team

![Table of service names and the teams that own them](/images/service-owners.png "Table of service names and the teams that own them")

Or as a pretty graph

    MATCH (s:Service {name: 'Prison 42'})-[:`owns`]-(t:Team)
    MATCH (t:Team)-[:`assigned to`]-(p:Person)
    RETURN  s.name as Service, p.name as Owners

Show all the people in the team that owns a service. This can be handy for finding
people to help you in an incident.

    MATCH (s:Service {name: 'Prison 42'})-[:`owns`]-(t:Team)
    MATCH (t:Team)-[:`assigned to`]-(p:Person)
    RETURN  s.name as Service, p.name as Owners


## Data and data formats

The example data I've included under [data](/data/) is the bare minimum required
to have a graph you can click around and run some interesting queries over. If
you want to add your own data the current formats are:

### Data formats - Staff

The individual staff entries should look like this:

    FirstName LastName:
      assigned_to:
        - Team-1
        - Team-2
      is_a: 'Role title'
      manages:
      - FirstName LastName 1
      - FirstName LastName 2
      - FirstName LastName 3
    member_of: 'Department Name'

and a worked example:

    Malcolm Reynolds:
      assigned_to:
        - Serenity
      is_a: 'Captain'
      manages:
      - Kaylee
      - Wash
      - Jayne Cobb
    member_of: Independents

It's worth noting nearly every element is optional.

### Data formats - Services

    services:
      - ServiceName:
          owner: 'Team Name'

An example with less abstract values:

    services:
      - Cerebro:
          owner: 'X-Men'
      - 'Danger Room':
          owner: 'X-Men'

## Notes

This graph is all based on here and now. There are no date relationships
available, such as looking up the line manager six months ago.

### Author

  [Dean Wilson](https://www.unixdaemon.net)

### License

 * Released under the GPLv2
