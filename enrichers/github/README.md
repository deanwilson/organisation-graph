# GitHub Enricher

Add additional GitHub related nodes and relationships to the OrgGraph

![A GitHub User, Team and Repo Graph](/images/github-graph.png "Neo4J node browser with sample GitHub")

## Running the enricher

The GitHub Enricher runs in two seperate stages. The first script,
[GitHub Gatherer](/enrichers/github/github-gatherer) queries GitHub and creates
an intermedia YAML representation that can be stored in version control
or simply used as a cache. The second stage,
[GitHub Loader](/enrichers/github/github-loader) adds the data to
the Neo4J database itself.

### Running the Gatherer

Assuming you've followed the [Getting Started guide](/README.md#getting-started)
the only additional steps you will require is to request an auth token from
GitHub and export it into the shell you want to run the commands from 

    export GITHUB_AUTH_TOKEN=asd38d97a7fdg453grgt45grtg54

    ./enrichers/github/github-gatherer -o GITHUB_ORGANIZATION_NAME

You can view the gathered data in the `enriched-data` directory

### Running the loader

After the Gatherer has run `github-loader` can be invoked to add
the actual nodes and relationships to the graph. This stage works from the
local file and does not call GitHub.

    enrichers/github/github-loader

Once this is complete you should be able to see the data inside Neo4J

## Useful Queries

## Find all GitHub teams with less than four members.

    MATCH (t:GitHubTeam)
    OPTIONAL MATCH (t)-[:in_team]-(u:GitHubUser)
    WITH t, count(u) AS memberCount
    WHERE memberCount < 4
    RETURN t.name, t.organization, memberCount

### Which users are in the most teams?

    MATCH (u:GitHubUser)
    OPTIONAL MATCH (u)-[:in_team]-(t:GitHubTeam)
    WITH u, count(t) AS teamCount
    RETURN u.name, u.organization, teamCount
    ORDER BY teamCount DESC
    LIMIT 5

### And which teams contains the specified user?

Specify the username inplace of `GITHUB_USER_NAME` to list a users teams

    MATCH (u:GitHubUser { name: 'GITHUB_USER_NAME' })
    OPTIONAL MATCH (u)-[:in_team]-(t:GitHubTeam)
    RETURN t.name
    ORDER BY t.name

### Which user has access to the most repos?

    MATCH (u:GitHubUser { name: 'GITHUB_USER_NAME' })
    OPTIONAL MATCH (u)-[:in_team]-(t:GitHubTeam)-[:repo_permission]-(r:GitHubRepo)
    WITH count(r) as repoCount
    RETURN repoCount

### And which repos do they have access to?

    MATCH (u:GitHubUser { name: 'GITHUB_USER_NAME' })
    OPTIONAL MATCH (u)-[:in_team]-(t:GitHubTeam)-[:repo_permission]-(r:GitHubRepo)
    RETURN r.name
    ORDER BY u.name
