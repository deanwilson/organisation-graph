# Interactive Testing

Some code snippets to help test Cypher queries

## Running queries from python3

```
import os
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", os.environ["ORG_GRAPH_NEO_PASSWORD"]))


with driver.session() as session:
    result = session.run(
        "MATCH (:Team { name: 'Backend' })-[r]->(rela)"
        "RETURN type(r) as relation_name, (rela.name) as remote_node_value"
    )

result.data()
```
