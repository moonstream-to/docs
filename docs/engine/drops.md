---
tags:
  - api
  - data
  - economics
---

# Drops

Use Drops to distribute ERC20 tokens, NFTs, items, or achievements to your community. All you have to do is upload a spreadsheet listing the amount of rewards that each community member should receive.

Alternatively, you can use Drops to automate the distribution of rewards to players occupying top places in your game’s [leaderboards](leaderboards.md).

## Dropper contract

Dropper is a contract that allows you to distribute tokens to your users, with them submitting the transactions to claim those tokens.

It can distribute ERC20 tokens, ERC721 tokens, and ERC1155 tokens. It can also be used to mint Terminus tokens using an authorized claim workflow.

<table>
  <tr>
    <th>Contract name</th>
    <th>Immutable or Upgradable</th>
    <th>Deployment</th>
    <th>CLI</th>
    <th>Solidity interface</th>
    <th>ABI</th>
  </tr>
  <tr>
    <td><a href="./contracts/Dropper/DropperFacet.sol"><pre>DropperFacet</pre></a></td>
    <td>Upgradable</td>
    <td><pre>web3cli core dropper-gogogo</pre></td>
    <td><pre>web3cli dropper</pre></td>
    <td><a href="./contracts/interfaces/IDropper.sol"><pre>IDropper</pre></a></td>
    <td><a href="./abi/DropperFacet.json"><pre>abi/DropperFacet.json</pre></a></td>
  </tr>
  <tr>
    <td><a href="./contracts/Dropper.sol"><pre>Dropper (legacy version)</pre></a></td>
    <td>Immutable</td>
    <td><pre>web3cli dropper-v1 deploy</pre></td>
    <td><pre>web3cli dropper-v1</pre></td>
    <td>n/a</td>
    <td><a href="./abi/Dropper.json"><pre>abi/Dropper.json</pre></a></td>
  </tr>
</table>

## Workflow

To use drops, you will first have to deploy a Dropper contract. This can be done using the `web3cli` command line utility in [web3 repo](https://github.com/moonstream-to/web3). That's a Python program; instructions to install it are in the [README](https://github.com/moonstream-to/web3/blob/main/README.md).

The command to deploy a Dropper contract is `web3cli core dropper-gogogo`. Try `web3cli core dropper-gogogo –help` to see what parameters you need to provide.

The deployment is complex because we use the [Terminus](../terminus.md) protocol to manage role-based permissions on the Dropper contract. That means you’ll need to also deploy a Terminus contract using `web3cli core terminus-gogogo`. Reach out to us on [Discord](https://discord.gg/w7wrqrAswq) for the details of the deployment from CLI.

We are planning to build a web UI for these deployments in the future.

To manage token drops:
1. Create a free Moonstream account [here](https://moonstream.to/). 
2. Go to Moonstream [Portal](https://moonstream.to/portal/) and click [Drops](https://moonstream.to/portal/dropper/).

# Lootboxes

Before dropping tokens to players, you can bundle them into fully on-chain randomizable lootboxes. These are implemented as [Terminus](../terminus.md) tokens. Lootboxes come in two varieties - deterministic and random.

Random lootboxes use decentralized, verifiable randomness to randomize the items that players receive when they open the lootbox.

<table>
  <tr>
    <th>Contract name</th>
    <th>Immutable or Upgradable</th>
    <th>Deployment</th>
    <th>CLI</th>
    <th>Solidity interface</th>
    <th>ABI</th>
  </tr>
  <tr>
    <td><a href="./contracts/Lootbox.sol"><pre>Lootbox</pre></a></td>
    <td>Immutable</td>
    <td><pre>web3cli lootbox deploy</pre></td>
    <td><pre>web3cli lootbox</pre></td>
    <td><a href="./contracts/interfaces/ILootbox.sol"><pre>ILootbox</pre></a></td>
    <td><a href="./abi/Lootbox.json"><pre>abi/Lootbox.json</pre></a></td>
  </tr>
</table>

Deploying a Lootbox contract can be done using the `web3cli` command line utility in [web3 repo](https://github.com/moonstream-to/web3). That's a Python program; instructions to install it are in the [README](https://github.com/moonstream-to/web3/blob/main/README.md).

