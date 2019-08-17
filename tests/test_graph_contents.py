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
    """Ensure the graph contains Person nodes."""
    with graph_connect.session() as session:
        result = session.run("MATCH (Person { name: 'Leo Fitz' }) return (Person)")

    person = result.single()

    assert person.values()[0]["name"] == "Leo Fitz"
    # print(f"Node id is {person.values()[0].id}")
