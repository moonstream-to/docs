---
tags:
  - api
  - data
---

# Analytics

A highly reliable version of web3 analytics that you can use without connecting your wallet. We run our own nodes, so it’s much better than Etherscan or Polygonscan.

## How to use

First, create a free Moonstream account [here](https://moonstream.to/). Then go to Moonstream [Portal](https://moonstream.to/portal/) and click [Analytics](https://moonstream.to/portal/analytics/).

![Portal](image.png)

From there you can create subscriptions to wallet addresses and smart contracts to watch and analyze. This works with live projects or projects that are still under development.

![Subscriptions](image-1.png)

There are two types of subscriptions you can create:

- Regular addresses
- Smart contracts

When you create a subscription to a regular wallet address, we gather all the data associated with it. You can then ask relevant questions about that data, aka make queries about it (e.g. incoming transactions for a particular time period). You can then save the results of your query as a JSON file and use it however you want.

![Regular address](image-2.png)

Subscriptions to smart contracts are more complex. You’ll need to provide an ABI, but usually it’s loaded automatically. Once you create a subscription, we begin to gather all the historical data for that smart contract. The types of queries you can make are different for smart contracts, though you can still export the results in JSON format.

![Smart Contract](image-3.png)

All query types are automatically loaded from our library, but you can specify parameters for them. If you want to add another type of query – there’s a button to request it.

![Queries](image-4.png)

# ABI Explorer

![ABI Explorer](image-5.png)

To access the ABI Explorer, use this link. This tool offers a comprehensive view of events and functions from your ABI.

Providing the ABI:
1. **Direct ABI Input**: Paste the ABI directly.
2. **From a URL**: Enter the URL of a JSON file containing the ABI. This method archives your input in your session history.
3. **Using a Verified Smart Contract Address**: Simply input the address. Not only is this method stored in your history, but it also pre-fills the function call form for convenience.

💡***Note***: Fetching the ABI using a contract address employs the Moonstream API. A user login is mandatory for this method.

**Function Call with Metamask**: If Metamask is connected, simply click on any function. You can then proceed to fill out the form and initiate the call.

# Query API

Moonstream's Query API makes it possible to query blockchain events, transactions, method calls, and state using SQL queries.

The Query API allows you to make joins across different types of data and get the results in a single step.

Ours is the only API which allows you to join events and transactions to the smart contract state and off-chain metadata.

The production Query API is currently in closed alpha. If you would like to use the Query API, please contact the @moonstream team on the [Moonstream Discord](https://discord.gg/w7wrqrAswq).

## Workflow

To use the Query API, a user must first:

1.  Create a subscription using the Moonstream API

2.  Create a Postgres SQL query that returns the information they want. They can use Postgres variables
    in the query, and pass in values for those variables from the API.

3.  Make an HTTP request in the [format below](#request-format).

4.  This request returns an [AWS S3 presigned URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) at which you can access the data from an S3 bucket.
    To work with the presigned URL:

        1. Store a `request_timestamp` before the `update_data` request.

        2. Make an HTTP request of the form of `Codeblock` and receive a `presigned_url` for S3 access.

        3. `GET presigned_url` and set an `If-Modified-Since: request_timestamp` header on your `GET` request. The possible status codes here are:

            1. `404` - means this was the first time this query was called and data has not been pushed to S3 bucket yet

            2. `304` - data older then If-Modified-Since and has not yet been updated

            3. `200` - data is updated, read response, have fun!

    See the [example below for a Python implementation of this workflow](#example-a-python-script-to-read-data-from-the-query-api).

### Request format

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

### Example: A Python script to read data from the Query API

```python
query_name = "current_owners_with_tokens"
moonstream_access_token = "<token>"

request_url = f"https://moonstream.to/queries/{query_name}/update_data"
headers = {
    "Authorization": f"Bearer {moonstream_access_token}",
    "Content-Type": "application/json",
}
request_body = {
    "params": {"address": "0xdC0479CC5BbA033B3e7De9F178607150B3AbCe1f"}
}

keep_going = True

if_modified_since_datetime = datetime.datetime.utcnow()
if_modified_since = if_modified_since_datetime.strftime("%a, %d %b %Y %H:%M:%S GMT")

# Query Moonstream request data update and get presign_url
response = requests.post(
   request_url, json=request_body, headers=headers, timeout=10
)
response_body = response.json()
data_url = response_body["url"] # S3 presign_url
while keep_going:
    data_response = requests.get(
         data_url,
         headers={"If-Modified-Since": if_modified_since},
         timeout=10,
     )
    if data_response.status_code == 200:
        json.dump(data_response.json())
        break
    else:
        # You can put a sleep in here if you want
        continue
```