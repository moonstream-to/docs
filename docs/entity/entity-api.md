---
tags:
    - alpha
    - data
    - entity
    - overview
    - schemes
---

# Entity API

Entities are useful during game air drops, it's providing additional information in leaderboards, for internal usage of crypto projects who want their users to pass KYC and legal things there was a problem to bridge the blockchain and physical world.

Current document describes how to store user identity data with Moonstream infrastructure for different use cases:

-   User web3 addresses
-   Maintaining a list of deployed smart contracts (by address)
-   Maintaining a list of smart contract deployers
-   Blacklisting or whitelisting accounts by Discord id, Twitter id, email, etc.

This is not just a mapping between users (human-owned addresses) and identifying information, but any Ethereum address (including smart contract addresses and even addresses that may not have been used) and identifying information/notes. For smart contracts, it would also store things like bytecode, ABI, etc.

## Workflow

All your entities stored in collections and each new collection belongs only to you until you will provide access to you friends or team read/update/delete access.

To work with entity you need to Create an account at https://moonstream.to, and generate Bearer access token or attach your web3 address for web3_token. And store it as environment variable:

```bash
export MOONSTREAM_ACCESS_TOKEN="<your_generated_access_token>"
```

### Creating collections via API

Create collection `curl` request

```bash
curl --request POST "https://api.moonstream.to/entity/collections" \
    --header "Authorization: Bearer $MOONSTREAM_ACCESS_TOKEN" \
    --header "Content-Type: application/json" \
    --data-raw '{
        "name": "Whitelist of November"
    }'
```

Get list of your collections

```bash
curl --request GET "https://api.moonstream.to/entity/collections" \
    --header "Authorization: Bearer $MOONSTREAM_ACCESS_TOKEN"
```

### Creating entities

Set collection you are working with:

```bash
export MOONSTREAM_ENTITY_COLLECTION_ID="<your_collection_id>"
```

For each entity there are 3 permanently required fields:

-   name
-   address
-   blockchain

Depending on the use case, you can specify additional fields that will be required for your entities in certain collection. Then, you will be able to search across these fields with high precision compared to other fields.

```bash
curl --location --request POST "https://api.moonstream.to/entity/collections/$MOONSTREAM_ENTITY_COLLECTION_ID/entities" \
    --header "Authorization: Bearer $MOONSTREAM_ACCESS_TOKEN" \
    --header "Content-Type: application/json" \
    --data-raw '{
        "name": "Dark Forest burner",
        "address": "0xe7f5cce56814f2155f05ef6311a6de55e4189ea5",
        "blockchain": "xdai",
        "required_fields": {
            "discord": "https://discord.com/invite/K56VNUQGvA",
            "organization": true
        },
        "description": "Moonstream organization burner address for Dark Forest game."
    }'
```

Also you can pass a list of entities to create them in bulk mode to url `https://api.moonstream.to/entity/collections/{{collection_id}}/bulk`

Get list of entities with request:

```bash
curl --request GET "https://api.moonstream.to/entity/collections/$MOONSTREAM_ENTITY_COLLECTION_ID/entities" \
    --header "Authorization: Bearer $MOONSTREAM_ACCESS_TOKEN"
```

### Entity modifications

Set entity you are working with:

```bash
export MOONSTREAM_ENTITY_ID="<your_entity_id>"
```

Delete entity:

```bash
curl --request DELETE "https://api.moonstream.to/entity/collections/$MOONSTREAM_ENTITY_COLLECTION_ID/entities/$MOONSTREAM_ENTITY_ID" \
    --header "Authorization: Bearer $MOONSTREAM_ACCESS_TOKEN"
```

## Different use cases and schemes

### Smartcontract

Required keys: `name`, `address`, `blockchain`, `contract_deployer`, `support_erc`, `proxy`. Other fields could be added as additional.

name: `Terminus`

required fields:

```json
{
	"blockchain": "polygon",
	"address": "0x062BEc5e84289Da2CD6147E0e4DA402B33B8f796",
	"contract_deployer": "0xEba757cEac281D9de85b768Ef4B9E1992C41EA7F",
	"support_erc": [1155, 721],
	"proxy": true
}
```

additional fields:

```json
{
	"description": "Terminus Moonstream.to smartcontract.",
	"discord": "https://discord.com/invite/K56VNUQGvA"
}
```

## Smartcontract deployer

Required keys: `address`, `name`, `blockchain`, `deployed_contract`. Other fields could be added as additional.

title: `Moonstream dropper contract deployer`

required fields:

```json
{
	"blockchain": "polygon",
	"address": "0xEba757cEac281D9de85b768Ef4B9E1992C41EA7F",
	"deployed_contract": "0x7bbf900Ded826D5A16a27dF028018673E521B35d",
	"deployed_contract": "0xEba757cEac281D9de85b768Ef4B9E1992C41EA7F"
}
```

additional fields:

```json
{
	"description": "Moonstream.to deployer.",
	"discord": "https://discord.com/invite/K56VNUQGvA"
}
```
