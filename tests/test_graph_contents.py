"""Test cases for loaded graph data."""
import os
import pytest

from neo4j import GraphDatabase

# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture(scope="session", autouse=True)
def graph_connect():
    """Manage the Neo4J connection used by all our tests."""
    # run before all tests
    driver = GraphDatabase.driver(
        "bolt://localhost:7687", auth=("neo4j", os.environ["ORG_GRAPH_NEO_PASSWORD"])
    )
    yield driver
    # run after all tests
    driver.close()


def test_person_nodes(graph_connect):
    """Ensure the graph contains Employee nodes."""
    with graph_connect.session() as session:
        result = session.run("MATCH (Employee { name: 'Leo Fitz' }) return (Employee)")

    person = result.single()

    assert person.values()[0]["name"] == "Leo Fitz"
    # print(f"Node id is {person.values()[0].id}")


def test_person_relationships(graph_connect):
    """Ensure the expected node relations exist."""
    with graph_connect.session() as session:
        result = session.run(
            "MATCH (:Employee { name: 'Melinda May' })-[r]->(rela)"
            "RETURN type(r) as relation_name, (rela.name) as remote_node_value"
        )

    relations = result.data()

    # the results from data are a list of dicts. This turns it into a single dict
    # TODO: this is naive code and assumes one of each relationship type. Which isn't
    # true of some, such as "manages"
    node_relations = {}
    for relation in relations:
        node_relations[relation["relation_name"]] = relation["remote_node_value"]

    # and she is a tech lead
    assert "tech_lead" in node_relations, "Node has a 'tech lead' relationship"
    assert node_relations["tech_lead"] == "Frontend"

    # and she manages
    assert "manages" in node_relations, "Node has a 'manages' relationship"
    assert node_relations["manages"] == "Piper"

    # and she is a
    assert "is a" in node_relations, "Node has a 'is a' relationship"
    assert node_relations["is a"] == "Senior SRE"

    # and she is in a team
    assert "in_team" in node_relations, "Node has a 'in_team' relationship"
    assert node_relations["in_team"] == "Frontend"

    # and she is a member of
    assert "member of" in node_relations, "Node has a 'member of' relationship"
    assert node_relations["member of"] == "Infrastructure"


def test_role_nodes(graph_connect):
    """Ensure the graph contains Role nodes."""
    with graph_connect.session() as session:
        result = session.run(
            "MATCH (Role { name: 'Head of Development' }) return (Role)"
        )

    role = result.single()

    assert role.values()[0]["name"] == "Head of Development"


def test_department_nodes(graph_connect):
    """Ensure the graph contains Department nodes."""
    with graph_connect.session() as session:
        result = session.run(
            "MATCH (Department { name: 'Technology' }) return (Department)"
        )

    department = result.single()

    assert department.values()[0]["name"] == "Technology"


def test_technology_nodes(graph_connect):
    """Ensure the graph contains Technology nodes."""
    with graph_connect.session() as session:
        result = session.run(
            "MATCH (Technology { name: 'PostgreSQL' }) return (Technology)"
        )

    technology = result.single()

    assert technology.values()[0]["name"] == "PostgreSQL"


def test_team_nodes(graph_connect):
    """Ensure the graph contains Team nodes."""
    with graph_connect.session() as session:
        result = session.run("MATCH (Team { name: 'Backend' }) return (Team)")

    team = result.single()

    assert team.values()[0]["name"] == "Backend"


def test_team_relationships(graph_connect):
    """Ensure the expected team node relations exist."""
    with graph_connect.session() as session:
        result = session.run(
            "MATCH (:Team { name: 'Backend' })-[r]->(rela)"
            "RETURN type(r) as relation_name, (rela.name) as remote_node_value"
        )

    relations = result.data()

    owned_services = [
        r["remote_node_value"] for r in relations if r["relation_name"] == "owns"
    ]

    # the team should own a service
    assert "Order System" in owned_services


def test_service_nodes(graph_connect):
    """Ensure the graph contains Service nodes."""
    with graph_connect.session() as session:
        result = session.run(
            "MATCH (Service { name: 'Order System' }) return (Service)"
        )

    service = result.single()

    assert service.values()[0]["name"] == "Order System"


def test_service_relationships(graph_connect):
    """Ensure the expected service node relations exist."""
    with graph_connect.session() as session:
        result = session.run(
            "MATCH (:Service { name: 'Order System' })-[r]->(rela)"
            "RETURN type(r) as relation_name, (rela.name) as remote_node_value"
        )

    relations = result.data()

    tech_used = [
        r["remote_node_value"] for r in relations if r["relation_name"] == "uses"
    ]

    # the service uses technologies
    assert "PostgreSQL" in tech_used
