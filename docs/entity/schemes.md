---
tags:
  - alpha
  - data
  - entity
  - scheme
---

# Schemes

Entity could be created one by one or uploaded as `csv` or `json` files in format:

**CSV format for uploading**

```
address,name,<another fields will be added as additional (like discord,telegram,etc)>
```

**JSON format for uploading**

```
[
    {"address": "","name": "", "<another filed>": ""}
]
```

## Smartcontract

Required keys: `address`, `name`, `blockchain`, `contract_deployer`, `support_erc`, `proxy`. Other fields will be added to content as additional.

### Generated entity structure

title: `0x062BEc5e84289Da2CD6147E0e4DA402B33B8f796 -- Terminus`

tags:

-   `blockchain:polygon`
-   `address:0x062BEc5e84289Da2CD6147E0e4DA402B33B8f796`
-   `contract_deployer:0xEba757cEac281D9de85b768Ef4B9E1992C41EA7F`
-   `support_erc:1155,721`
-   `proxy:true`

content:

```json
{
	"description": "Terminus Moonstream.to smartcontract.",
    "discord": "https://discord.com/invite/K56VNUQGvA"
}
```

## Smartcontract deployer

Required keys: `address`, `name`, `blockchain`, `deployed_contract`. Other fields will be added to content as additional.

### Generated entity structure

title: `0xEba757cEac281D9de85b768Ef4B9E1992C41EA7F -- Moonstream dropper contract deployer`

tags:

-   `blockchain:polygon`
-   `address:0xEba757cEac281D9de85b768Ef4B9E1992C41EA7F`
-   `deployed_contract:0x7bbf900Ded826D5A16a27dF028018673E521B35d`
-   `deployed_contract:0xEba757cEac281D9de85b768Ef4B9E1992C41EA7F`

content:

```json
{
	"description": "Moonstream.to deployer.",
    "discord": "https://discord.com/invite/K56VNUQGvA"
}
```

## Person

Required keys: `address`, `name`, `blockchain`. Other fields will be added to content as additional.

### Generated entity structure

title: `0xE7F5ccE56814f2155F05eF6311A6De55E4189Ea5 -- Kompotkot's DarkForest Burner`

tags:

-   `blockchain:xdai`
-   `address:0xE7F5ccE56814f2155F05eF6311A6De55E4189Ea5`

content:

```json
{
	"description": "DarkForest game burner address of user kompotkot.",
    "discord": "kompotkot#0000"
}
```
