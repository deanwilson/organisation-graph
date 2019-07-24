import argparse
import os

from pathlib import PurePath
from py2neo import Graph, NodeMatcher
from py2neo.data import Node, Relationship
from sys import exit
from yaml import load, SafeLoader


def _inflate_yaml(file_name):
    yaml = None

    with open(file_name, 'r') as yaml_file:
        yaml = yaml_file.read()

    inflated_yaml = load(yaml, Loader=SafeLoader)
    return inflated_yaml


def load_staff(staff_file):
    staff = _inflate_yaml(staff_file)

    return staff


def load_services(service_file):
    services = _inflate_yaml(service_file)
    return services


def _get_neo_pass():
    """ Get the current Neo4J password or kill the process """
    try:
        "ORG_GRAPH_NEO_PASSWORD" in os.environ
    except KeyError:
        print("Please set the environment variable ORG_GRAPH_NEO_PASSWORD")
        exit(1)

    return os.environ["ORG_GRAPH_NEO_PASSWORD"]


def main(args):

    staff = load_staff(PurePath(args.data, args.staff))
    services = load_services(PurePath(args.data, args.services))

    neo_password = _get_neo_pass()
    graph = Graph(host="localhost", password=neo_password)

    ## Extract the data
    people = set()
    # make these comprehensions?
    roles = set()
    departments = set()
    teams = set()

    for name in staff:
        people.add(name)

        person = staff[name]

        roles.add(person['is_a'])

        if 'manages' in person:
            reports = person['manages']

            for report in reports:
                people.add(report)

        if 'member_of' in person:
            departments.add(person['member_of'])

        if 'assigned_to' in person:
            for team in person['assigned_to']:
                teams.add(team)

    ## Add the base nodes

    for person in people:
        node = Node("Person", name=person)
        graph.create(node)

    for team in teams:
        node = Node("Team", name=team)
        graph.create(node)

    for role in roles:
        node = Node("Role", name=role)
        graph.create(node)

    for department in departments:
        node = Node("Department", name=department)
        graph.create(node)

    ## Build the relationships
    ### People
    for person in staff:
        matcher = NodeMatcher(graph)
        # person is a string, person_node is a graph object
        person_node = matcher.match("Person", name=person).first()

        ## Management relationships
        manages = staff[person].get('manages', [])
        for report in manages:
            # inefficient to do this lookup everytime? Cache on node creation?
            report_node = matcher.match("Person", name=report).first()
            manage_rel = Relationship(person_node, "manages", report_node)
            graph.create(manage_rel)

        ## Role relationships
        role = staff[person]['is_a']
        role_node = matcher.match("Role", name=role).first()
        role_rel = Relationship(person_node, "is a", role_node)
        graph.create(role_rel)

        ## Team relationships
        teams = staff[person].get('assigned_to', [])
        for team in teams:
            team_node = matcher.match("Team", name=team).first()
            team_rel = Relationship(person_node, "assigned to", team_node)
            graph.create(team_rel)

        ## Tech leads
        leads = staff[person].get('tech lead', [])
        for team in leads:
            team_node = matcher.match("Team", name=team).first()
            lead_rel = Relationship(person_node, "tech leads", team_node)
            graph.create(lead_rel)



    ## Services
    for service_name in services["services"]:
        service = services["services"][service_name]

        service_node = Node("Service", name=service_name)
        graph.create(service_node) # TODO: might be redundent due to graph.create(owner_rel)

        matcher = NodeMatcher(graph)

        owner = service['owner']
        team_node = matcher.match("Team", name=owner).first()
        owner_rel = Relationship(team_node, "owns", service_node)
        graph.create(owner_rel)


## TODO
### Abstract out the addition of the node and relationship and call it once in
### the main loop? "


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Build the organisations graph')

    parser.add_argument('--data', type=str, default='data',
                        help='A directory containing your yaml data files')
    parser.add_argument('--services', type=str, default='services.yaml',
                        help='A valid yaml file containing your service information')
    parser.add_argument('--staff', type=str, default='staff.yaml',
                        help='A valid yaml file containing your staff information')

    args = parser.parse_args()


    main(args)
