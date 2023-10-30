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

[!NOTE]
💡Fetching the ABI using a contract address employs the Moonstream API. A user login is mandatory for this method.

**Function Call with Metamask**: If Metamask is connected, simply click on any function. You can then proceed to fill out the form and initiate the call.
