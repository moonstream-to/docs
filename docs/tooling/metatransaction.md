---
tags:
  - tooling
---


# Metatransaction

The Metatransaction API provides endpoints for interacting with user registered contracts. This includes retrieving available contract types, registering new contracts, and managing call requests for a given contract.

## API Endpoints

### Get Contract Types

Describes the contract types that users can register contracts as against this API.

Request:

```bash
GET https://engineapi.moonstream.to/metatx/contracts/types
```

Response Example:

```json
{
    "raw": "A generic smart contract. You can ask users to submit arbitrary calldata to this contract.",
    "dropper-v0.2.0": "A Dropper contract. You can authorize users to submit claims against this contract."
}
```
### Get User Registered Contracts

Users can use this endpoint to look up the contracts they have registered against this API. Authentication is required.

Request:

```bash
GET https://engineapi.moonstream.to/contracts/ 
Authorization: Bearer <moonstream_token>
```

Response Example:

```json
[
    {
        "id": "daa1b046-9557-4038-a035-4dc2bc7179fd",
        "blockchain": "mumbai",
        "address": "0x83c9070563b94392e03e87B804c35cc912d7Fe57",
        "contract_type": "dropper-v0.2.0",
        "moonstream_user_id": "d2b4185e-5cf3-4bdd-a16e-92749fb5ce33",
        "title": "This is my contract.",
        "description": "This is my contract. It is awesome.",
        "image_uri": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Example_image.svg/600px-Example_image.svg.png",
        "created_at": "2023-04-10T12:10:38.076704+03:00",
        "updated_at": "2023-04-10T12:10:38.076704+03:00"
    }
]
```

### Register a New Contract

Allows users to register contracts. Authentication is required.

Request:

```bash
POST https://engineapi.moonstream.to/contracts/register
Authorization: Bearer <moonstream_token>
```

Request Body:

```json
{
    "blockchain": "mumbai",
    "address": "0x83c9070563b94392e03e87B804c35cc912d7Fe58",
    "contract_type": "dropper-v0.2.0",
    "title": "This is my contract.",
    "description": "This is my contract. It is awesome.",
    "image_uri": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Example_image.svg/600px-Example_image.svg.png"
}
```

Response Example:

```json
{
    "blockchain": "mumbai",
    "address": "0x83c9070563b94392e03e87B804c35cc912d7Fe58",
    "contract_type": "dropper-v0.2.0",
    "title": "This is my contract.",
    "description": "This is my contract. It is awesome.",
    "image_uri": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Example_image.svg/600px-Example_image.svg.png"
}
```

### Delete a Registered Contract

Allows users to delete a registered contract. Authentication is required.

Request:

```bash
DELETE http://127.0.0.1:7191/contracts/39b928f1-13d5-4261-9efb-86b79cd5b629
Authorization: Bearer <moonstream_token>
```

### Get Unexpired Call Requests

Allows API users to see all unexpired call requests for a given caller against a given contract.

Request:

```bash
GET http://127.0.0.1:7191/contracts/requests?contract_id=daa1b046-9557-4038-a035-4dc2bc7179fd&caller=0xB5A4B925005B59C9C04fBf2742aee3b80834089F
```

Response Example:

```json
[
    {
        "id": "0e535d1d-3608-44a9-be3e-d9cee63db1b4",
        "registered_contract_id": "daa1b046-9557-4038-a035-4dc2bc7179fd",
        "moonstream_user_id": "d2b4185e-5cf3-4bdd-a16e-92749fb5ce33",
        "caller": "0xB5A4B925005B59C9C04fBf2742aee3b80834089F",
        "method": "claim",
        "parameters": {
            "amount": "2",
            "dropId": "2",
            "signer": "0xB5A4B925005B59C9C04fBf2742aee3b80834089F",
            "requestID": "2",
            "signature": "0x2",
            "blockDeadline": "2"
        },
        "expires_at": "2023-04-11T16:20:27.202413+03:00",
        "created_at": "2023-04-10T13:20:27.234896+03:00",
        "updated_at": "2023-04-10T13:20:27.234896+03:00"
    }
]
```

### Register Call Requests

Allows API users to register call requests from given call specifications.

Request:
```bash
POST http://127.0.0.1:7191/contracts/daa1b046-9557-4038-a035-4dc2bc7179fd/requests
Authorization: Bearer <moonstream_token>
```

Request Body:

```json
{
    "specifications": [
        {
            "caller": "0xB5A4B925005B59C9C04fBf2742aee3b808340894",
            "method": "claim",
            "parameters": {
                "dropId": "2",
                "requestID": "2",
                "blockDeadline": "2",
                "amount": "2",
                "signer": "0xB5A4B925005B59C9C04fBf2742aee3b80834089F",
                "signature": "0x2"
            }
        }
    ],
    "ttl_days": 1
}
```

Response Example:

```json
1
```

This response indicates that 1 request has been registered.