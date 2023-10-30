---
tags:
  - terminus
  - EIP-1155
  - smart contract
  - standard
---

# Terminus

## What is Terminus?

Terminus is a protocol for managing access to decentralized applications deployed to Ethereum or other blockchains which utilize the Ethereum Virtual Machine.

Terminus extends the [EIP-1155 Multi-Token Standard](https://eips.ethereum.org/EIPS/eip-1155) with rules defining who can mint and burn tokens with a given token ID.

In Terminus, each ERC-1155 token ID represents a pool of tokens which grant their bearers permission to take a specific set of actions.

Each Terminus pool has a controller address which can:
1. Mint tokens from that pool to any address they like.
2. Burn tokens from that pool from any address they like.

The controller can also grant and revoke the above minting and burning privileges to and from other accounts.

When a pool is created, it can be configured to be:
- **Transferable or non-transferable**: Tokens in transferable pools can be transferred freely between accounts. Tokens in non-transferable pools cannot be transferred between accounts.
- **Burnable or non-burnable**: Tokens in burnable pools can be burned by their holders. Tokens in non-burnable tools can only be burned by the pool controller or by an account that has been authorized to burn tokens in that pool by the controller.

Terminus also adds batch minting and burning functions to ERC-1155.

## Terminus in games

Terminus is useful to game developers because it allows them to represent the following types of assets using a single smart contract:

1. Badges: Non-transferable tokens which can be minted by a game server or other game contract
1. Items: Transferable tokens with a high maximum supply
1. Consumable tokens: Transferable tokens which are burned by the game contract on use
1. Artifacts: Transferable tokens with a low maximum supply

Terminus is compatible with any marketplace that supports the EIP-1155 Multi-Token Standard, such as
[Open Sea](https://opensea.io).
The largest Terminus marketplace on Open Sea is currently [Crypto Unicorns: Item Marketplace](https://opensea.io/collection/crypto-unicorns-items-marketplace),
with over 2000 ETH in transaction volume.

## Terminus for access control

Terminus useful for controlling access to smart contracts and APIs.

Smart contracts can use the `holdsPoolToken` and `spendsPoolToken` modifiers from our `TerminusPermissions`
contracts to gate access to methods.

Some portions of the Moonstream Web3 API use a configurable Terminus pool to gate access to administrative
functionality.

The advantage that Terminus-based access control has over address whitelists is that it makes it easy to
rotate accounts. Instead of submitting whitelist and blacklist transactions against multiple contracts,
administrators can simply burn and mint batches of Terminus tokens against the same Terminus contract.

## Implementation

The reference implementation of Terminus is available as [`TerminusFacet`](https://github.com/moonstream-to/web3/blob/ec4e44c536cdcc88fbcddd4628955bf607bbad82/contracts/terminus/TerminusFacet.sol).

The above implementation is also compatible with `DELEGATECALL` proxy contracts, such as those implementing the
[EIP-2535 Diamond standard](https://eips.ethereum.org/EIPS/eip-2535).
