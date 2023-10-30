---
tags:
  - entity
  - API
  - python
---

# Entity

Entity is used to store web3 addresses (including smart contract addresses and even addresses that have not yet been used) accompanied by identifying information/notes.

For each entity there are 3 permanently required fields:

-   title
-   address
-   blockchain

Depending on the use case, you can specify additional required fields.

Entities are useful during game air drops, and to  provide additional information on leaderboards. They can also be used internally  by crypto projects as part of their KYC protocols, as the data they store acts as a bridge between the blockchain and physical world.

This document describes how to store user identity data with Moonstream infrastructure for several different use cases:

-   Storing users’ web3 addresses
-   Maintaining a list of deployed smart contracts (by address)
-   Maintaining a list of smart contract deployers
-   Blacklisting or whitelisting accounts by Discord id, Twitter id, email, etc.
-   Other..

This is not just a mapping between users (human-owned addresses) and identifying information, but any web3 address (including smart contract addresses and even addresses that may not have been used) and identifying information/notes. For smart contracts, the entity would also store things like bytecode, ABI, etc.

You can find detailed documentation at https://api.moonstream.to/journals/docs#tag/entities

## Different use cases and schemes

### Smartcontract

Required keys: `title`, `address`, `blockchain`, `contract_deployer`, `support_erc`, `proxy`. Other fields could be added as additional. For example:

title: `Terminus`

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

Required keys: `address`, `title`, `blockchain`, `deployed_contract`. Other fields could be added as additional. For example:

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

## Entity API

All your entities stored in journals and each new journal belongs only to you until you will provide access to you friends or team read/update/delete access.

To work with entity you need to Create an account at https://moonstream.to, and generate Bearer access token or attach your web3 address for web3_token. Then store it as an environment variable:

```bash
export MOONSTREAM_ACCESS_TOKEN="<your_access_token>"
```

### Creating journals via API

Create journal `curl` request

```bash
curl --request POST "https://api.moonstream.to/journals/" \
    --header "Authorization: Bearer $MOONSTREAM_ACCESS_TOKEN" \
    --header "Content-Type: application/json" \
    --data-raw '{
        "name": "Whitelist of November"
    }'
```

Get list of your journals

```bash
curl --request GET "https://api.moonstream.to/journals/" \
    --header "Authorization: Bearer $MOONSTREAM_ACCESS_TOKEN"
```

### Creating entities

Set journal you are working with:

```bash
export MOONSTREAM_ENTITY_JOURNAL_ID="<your_journal_uuid>"
```

For each entity there are 3 permanently required fields:

-   title
-   address
-   blockchain

Depending on the use case, you can specify additional fields that will be required for your entities in certain journal. Then, you will be able to search across these fields with high precision compared to other fields.

```bash
curl --location --request POST "https://api.moonstream.to/journals/$MOONSTREAM_ENTITY_JOURNAL_ID/entities" \
    --header "Authorization: Bearer $MOONSTREAM_ACCESS_TOKEN" \
    --header "Content-Type: application/json" \
    --data-raw '{
        "title": "Dark Forest burner",
        "address": "0xe7f5cce56814f2155f05ef6311a6de55e4189ea5",
        "blockchain": "xdai",
        "required_fields": {
            "discord": "https://discord.com/invite/K56VNUQGvA",
            "organization": true
        },
        "description": "Moonstream organization burner address for Dark Forest game."
    }'
```

Also you can pass a list of entities to create in bulk mode to the url `https://api.moonstream.to/journals/{{journal_id}}/entities/bulk`

Get list of entities with request:

```bash
curl --request GET "https://api.moonstream.to/journals/$MOONSTREAM_ENTITY_JOURNAL_ID/entities" \
    --header "Authorization: Bearer $MOONSTREAM_ACCESS_TOKEN"
```

### Entity modifications

Set entity you are working with:

```bash
export MOONSTREAM_ENTITY_ID="<your_entity_id>"
```

Delete entity:

```bash
curl --request DELETE "https://api.moonstream.to/journals/$MOONSTREAM_ENTITY_JOURNAL_ID/entities/$MOONSTREAM_ENTITY_ID" \
    --header "Authorization: Bearer $MOONSTREAM_ACCESS_TOKEN"
```
