# Organisation Graph example queries

The syntax for querying a graph database can be unfamiliar and quite difficult
so in this page I've included a number of queries to show you what, and more
importantly how, you can find answers in your data. As this repository is
a learning experience for me I make no guaranties that they are the best, most
efficient or idiomatic ways to achieve the results.

In some cases it's possible to change the returned results display from a text
table to the clickable graph and back. If the `RETURN` has attributes, such as
`p.name` it will be displayed as text. If instead it's returned as the raw
node `RETURN p` it will be shown as the graph. Changing the display mode may
make navigating some of the results sets easier.

## Basic Neo4J Queries

### Show all data

Show the entire data set as a clickable graph.

    MATCH (n) return n

### Delete all data

Remove all the data, including nodes and relationships.

    MATCH (n) detach delete n;

In the Python code you can achieve the same results with

      graph = Graph(host="localhost", password=neo_password)
      graph.delete_all()

## People focused queries

### Return everyone of a given role

If you want to find everyone with an exact role you can use the `role name`
attribute. In this example we return everyone who is a `Senior SRE`

    MATCH (e:Employee)-[`is a`]-(j:Job {name:'Senior SRE'}) return e.name as Employee, j.name as Job

You can also match on sub strings inside an attribute. In the next query we will
find everyone who is a Senior.

    MATCH (e:Employee)-[`is a`]-(j:Job)
    WHERE j.name STARTS WITH 'Senior'
    RETURN e as Employee, j as Job

![Graph view of all Seniors](/images/senior-graph.png "Neo4J node browser showing Seniors")

And the same query results, but represented as a table

    MATCH (e:Employee)-[`is a`]-(j:Job)
    WHERE j.name STARTS WITH 'Senior'
    RETURN e.name as Employee, j.name as Job

![Table view of all Seniors](/images/senior-table.png "Textual Table showing Seniors")

### Show the tech leads

Show the tech lead from each team.

    MATCH (e:Employee)-[:`tech_lead`]-(t:Team)
    return e.name as Employee, t.name as Team
    ORDER BY Employee

## Team focused queries

### Show team members

Show everyone in the given team as a table

    MATCH (e:Employee)-[:`in_team`]-(t:Team {name:'Frontend'}) return e.name, t.name

and as a graph. In this view you can also see the other relationships. This can
make further avenues of exploration easier.

    MATCH (e:Employee)-[:`in_team`]-(t:Team {name:'Frontend'}) return e, t

![Graph of Team relationships](/images/team-members.png
  "Neo4J node browser showing everyone in a team and their other relationships to each other")

### Show seniors and their teams

Show everyone who is a `Senior` and the team they are in.

    # TODO: shows double of two staff. Why?
    MATCH (e:Employee)-[`is a`]-(j:Job)
    WHERE j.name STARTS WITH 'Senior'
    MATCH (e)-[`in_team`]-(t:Team)
    RETURN e.name as Employee, j.name as Job, t.name as Team
    ORDER BY Team

### Show the services a team owns

Being able to determine the owner of a service is a basic but important
building block for other, more interesting, queries.

    MATCH  (t:Team)-[`owns`]-(s:Service)
    RETURN  t.name as Team, s.name as Service

Graph version

    MATCH (t:Team)-[`owns`]-(s:Service)
    RETURN  t as Team, s as Service

### Show the technical lead for services

    MATCH (s:Service)-[:`owns`]-(t:Team)
    MATCH (t:Team)-[:`tech_lead`]-(e:Employee)
    RETURN s.name as Service, t.name as Team, e.name as TechLead

And as a graph

    MATCH (s:Service)-[:`owns`]-(t:Team)
    MATCH (t:Team)-[:`tech_lead`]-(e:Employee)
    RETURN s as Service, t as Team, e as TechLead

![Graph of TechLead to Service relationships](/images/service-tech-lead.png 
  "Neo4J node browser showing the tech lead for a service")

### Show all the team members responsible for a service

Sometimes you just need to find _anyone_ involved in a service. This query
will find everyone on the owning team.

    MATCH (s:Service {name: 'Webchat'})-[:`owns`]-(t:Team)
    MATCH (t:Team)-[:`in_team`]-(e:Employee)
    RETURN s.name as Service, e.name as Owners

### Show the running cost of a team

    MATCH (e:Employee)-[:`in_team`]-(t:Team {name:'Frontend'})
    OPTIONAL MATCH (e)-[:`is a`]-(j:Job)
    RETURN SUM(toInteger(j.median_salary)) as `Annual team running cost`

## External Links

 * [Cypher Match clause](https://neo4j.com/docs/cypher-manual/current/clauses/match/)
 * [A micro blog application powered by Flask and Neo4j](http://nicolewhite.github.io/neo4j-flask/) - best self-contained Python/Neo4J demo I've found
