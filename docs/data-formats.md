# Data and data formats

The example data I've included under [data](/data/) is the bare minimum required
to have a graph you can explore and run some interesting queries over. If
you want to add your own data they should be written in the formats outlined
in this document.

## Data format: Employees

The individual Employee entries should look like this:

    FirstName LastName:
      in_team:
        - Team-1
        - Team-2
      job_title: 'Role title'
      manages:
        - "FirstName LastName 1"
        - "FirstName LastName 2"
        - "FirstName LastName 3"
      department: "Department Name"

and a worked example:

    Malcolm Reynolds:
      in_team:
        - Serenity
      job_title: 'Captain'
      manages:
        - Kaylee
        - Wash
        - Jayne Cobb
      department: Independents

It's worth noting nearly every element is optional, the less you specify the
less interesting the result set.

## Data format: Jobs

The Job data is currently very bare boned. Each entry consists of a job title and a `salary`.

    jobs:
      "Director of Technology":
        salary: "120000"
      "Head of Infrastructure":
        salary: "85000-99000"

 * The job title is a free form text field.
 * `salary` can be represented as a range, stated as lowest to highest, seperated by
   a `-` or an absolute value.

## Data format: Services

Services should be used to describe a relativily self-contained system. What
that exactly means will be heavily tied to your own environment.

    services:
      "Order System":
        owner: "Backend"
        technologies:
          - Linux
          - PostgreSQL
          - Java

 * The service name is free form text
 * The `owner` should match a team specified in the `in_team` field of one of more employees
 * `technologies` is a list of free form text technology names
