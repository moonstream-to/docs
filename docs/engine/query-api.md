# Query API

Moonstream's Query API makes it possible to query blockchain events, transactions, method calls, and
state using SQL queries.

The Query API allows you to make joins across different types of data and get the results in a single step.

Ours is the only API which allows you to join events and transactions to smart contract state and off-chain
metadata.

The production Query API is currently in closed alpha. If you would like to use the Query API, please
contact the `#moonstream` team on [Moonstream Discord](https://discord.gg/w7wrqrAswq).

## Implementation

The Query API is implemented in the following repository:

> [github.com/bugout-dev/moonstream](https://github.com/bugout-dev/moonstream)

## Workflow

To use the Query API, a user must first:

1. Create a subscription using the Moonstream API

1. Create a Postgres SQL query that returns the information they want. They can use Postgres variables
in the query, and pass in values for those variables from the API.

1. Make an HTTP request:

```
POST https://api.moonstream.to/queries/{query_name}/update_data
Content-Type: application/json
Authorization: bearer <token>
{
    "params": {
        "<variable name>": "<variable value>"
    }
}
```

## Why closed alpha?

We have a lot of work to do before the Query API is ready for public consumption. You can track this work
on the [Query API Beta Release milestone on GitHub](https://github.com/bugout-dev/moonstream/milestone/33).

If you would like to help us get there, either by giving us feedback in the closed alpha or by contributing
code, please message the `#moonstream` team on [Moonstream Discord](https://discord.gg/w7wrqrAswq).
