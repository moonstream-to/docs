---
tags:
  - alpha
  - api
  - data
---

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
