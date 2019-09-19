# OrgGraph Ideas

## Road to 0.1.0

 * Seperate staff into a staff ID based dictionary
 * Build pages for some basic nodes
  * People
  * Teams
 * Allow scripts to be run more than once.
  * Nodes should only be added once.
  * Relationships should be additive. This allows things to be run more
    than once and add new relationships as additional sources appear
 * Link people to their GitHub IDs. Shows some value in the relationships

## Data Sources 

### Enrichers

Document and add tests for the new enrichers

 * Jobs
 * Employees
 * Services

Ensure the graph looks correct when they are run.

#### Document adding a new loader

Enricher runs and puts its YAML in generated-data
generated-data is loaded into graph

Create a subdirectory under `enrichers` with the new datasources name.
The structure should look like this:

    enrichers/jobs/
    enrichers/jobs/README.MD  # Document your new enricher here
    enrichers/jobs/generator  # The script that generates the intermedite YAML
    enrichers/jobs/tests/     # You should have tests to ensure


### PyPi

Add the PyPi projects and owners to the graph.

 * Link the projects to their GitRepos
 * Use the relationships mapper to link owners to staff

### Rubygems

Add the Rubygems projects and owners to the graph.

 * Link the projects to their GitRepos
 * Use the relationships mapper to link owners to staff

### Pingdom

Does adding the people and tests benefit the graph?

 * Add people to show access
 * Show tests and link to services?

### Puppetforge

Show the puppet projects we own from gds-operations

 * Link the projects to their github repo
 * one shared users so not much value there
 * Add the projects and their version and score as node properties

[API client](https://github.com/puppetlabs/forge-ruby)

### Pagerduty

Add the users, rotatas / schedules.

 * link this to teams
 * link to services

### Staff

Rework this to key the data from a staff ID to allow two people with the same name?

 * makes mapping other systems in more convoluted but ensures a unique ID at the base
 * probably a hash of users.
  * move the name to be a property
  * use id as the key

### TravisCI

Link the public travis projects to the github repos / puppetforge etc that they become

 * add travis build configs
 * link to the source github repo
 * link to the uploaded artifacts - map this how? file from the repo detection?

### Dockerhub / Docker registery

Add docker data to the graph.

Node types
 * Users
 * Orgs
 * Repos

### AWS

Add an organization walking data grabber.

 * Start with the specified org
 * List all the associated accounts
 * Get all the IAM users in those accounts

Should result in nodes and relationships between Org, account and users.
This would then need to be mapped to the staff id

### GitHub

 * Add repo labels as node properties to allow better querying

### Fastly

Add fastly services and users to the graph.

Link the config to a service node.

### Zendesk

Add users and queues

 * Map users to staff ID
 * Map queues to teams or services?

### Icinga

Add Icinga data to the graph

 * Hosts
 * Services
  * Properties for acknolwdged and status
 * Periods

Allow more than one environment how?

Link the periods to pagerduty?

## UI

### Pages

 * Team page
 * Staff page
 * Enriched data page
  * GitHub for example

#### Team

 * Description
 * Members
 * Tech lead
 * Services it owns
 * Cost of the team

Each of these sections should be dynamic and built by exploring the relationships to
the Team node.

#### Employee

 * Bio
 * Role
 * Relationship links to all the other nodes
  * Team
  * GitHub

## OrgChart

 * ~Make `bin/build-org-chart` work with the new staff hash format~
 * Convert the orgchart to use Employee IDs for linkage

## YAML Loader Format

A generic loader that could be used to load the enriched data gathered
by any script in a consistent way and allow testing of sample datasets
without requiring any custom code. The format could be something like:

    nodes:
    - unique_name:
      node_type:
      properties:
        key: value
      relationships:
      - relationship_type: NodeType[Nodename]
        properties:
          key: value
    
    relationships:
    - unique_name:
      relationship_type:
      properties:
        key: value
      source_node: NodeType[Nodename]
      destination_node: NodeType[Nodename]
    
The relationships YAML could be used to link all the IDs together



The loader can load one or more files.
You can point it at one file or a directory and each file should be idempotent

Nodes are being created more than once.

 * ensure they only get created if new
 * ensure properties are added to existing nodes
 * ensure relationships are added to existing nodes


## Testing

For employee pytests convert the test case from a hash to a loaded fixture file
https://pypi.org/project/pytest-datadir/ might be good for per enricher fixtures

