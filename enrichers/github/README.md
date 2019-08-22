# GitHub Enricher

Add additional GitHub related nodes and relationships to the OrgGraph

## Running the enricher

The GitHub Enricher runs in two seperate stages. The first script,
[GitHub Gatherer](/enrichers/github/github-gatherer) queries GitHub and creates
an intermedia YAML representation that can be stored in version control
or simply used as a cache. The second stage,
[GitHub Loader](/enrichers/github/github-loader) adds the data to
the Neo4J database itself.

### Running the Gatherer

Assuming you've followed the [Getting Started guide](/README.md#getting-started)
the only additional steps you will require is to request a auth token from the
GitHub site and export it into the shell you want to run the commands from 

    export GITHUB_AUTH_TOKEN=asd38d97a7fdg453grgt45grtg54

    ./enrichers/github/github-gatherer -o GITHUB_ORGANIZATION_NAME

You can view the gathered data in the `enriched-data` directory
