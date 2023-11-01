# Welcome!

## What is Moonstream?

Moonstream provides economic infrastructure for web3 games. It makes it easy to manage blockchain game economies.

One of the biggest challenges for web3 game designers and game developers is that putting your game economy on-chain turns it into a real economy. This takes control of your game economy away from you, the game designer. Your community is in charge now.

This means that you can no longer freely manipulate your game economy to improve your game.

Moonstream gives you the mechanisms you need to keep your economy healthy and sustainable–and to make sure your players are having fun.

## Moonstream Core Tools

The main Moonstream mechanisms are:

- [Analytics](./engine/analytics.md) - the base for all our tools; provides you with data on account activity for regular addresses and smart contracts. This includes:
    - ABI Explorer
    - Query API
- [Leaderboards](./engine/leaderboards.md) - a deflationary tool; makes it easy for game developers to combine on- and off-chain game activity to assign points to players.
- [Drops](./engine/drops.md) - a tool for game designers and game developers to automate rewarding their players for in-game activities with on-chain items, experience, and game currencies. This includes:
    - Lootboxes

## Additional open source tooling

In addition to the main Moonstream web3 mechanisms, Moonstream also maintains several tools for the benefit of the web3 developer community:

- [Terminus](terminus.md) - a smart contract standard (a modification of the [EIP-1155 Multi-Token Standard](https://eips.ethereum.org/EIPS/eip-1155)) designed to represent items, achievements, and experience in web3 games. It’s also useful as an access control mechanism for smart contracts and APIs.
- [Metatransaction](./tooling/metatransaction.md) - this API provides endpoints to interact with user registered contracts.
- [Entity](entity.md) - a way to store any web3 address (including smart contract addresses and even addresses that may not have been used) together with identifying information/notes.
- [NFT Inventory](./tooling/nft-inventory.md) - functional on-chain inventory slots for NFTs so that NFTs can own and equip items.
- [Crafting](./tooling/crafting.md) - fully on-chain crafting system with customizable recipes.
- [Garden of Forking Paths](./engine/mechanics/garden-of-forking-paths.md) - an on-chain game mechanic for choosing paths in a story.
- [Inspector Facet](./tooling/inspector-facet.md) - a tool which makes it easy for anyone to inspect upgradable smart contracts implementing the [EIP-2535 Diamond](https://eips.ethereum.org/EIPS/eip-2535) standard, which is very useful for web3 game projects.
- [Moonworm](./tooling/moonworm.md) - a code generator which makes it easy for anyone to analyze and interact with Ethereum smart contracts.


## Supported blockchains

Moonstream can currently support any [EVM-based blockchain](https://ethereum.org/en/developers/docs/evm/) and **testnets**,
such as [Ethereum](https://ethereum.org), [Polygon](https://polygon.technology/), [Polygon Mumbai Testnet](https://wiki.polygon.technology/docs/tools/ethereum/remix/#deploying-to-the-mumbai-testnet), [Gnosis Chain](https://docs.gnosischain.com/), and more.

## Open source software

The Moonstream community believes firmly in the principles of [Free Software](https://www.gnu.org/philosophy/free-sw.en.html).

Moonstream is completely open source software, free for anyone to use and modify as they please.

We do _not_ believe in forcing our views upon our users. We do not use [copyleft licenses](https://en.wikipedia.org/wiki/Copyleft). We favor the
much more permissive [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

We do _not_ believe in the [open core business model](https://en.wikipedia.org/wiki/Open-core_model).
Every feature available on Moonstream.to is also freely available to anyone who chooses to host their own instance.

The only code that we write that is _not_ open source is the code related to our security operations. You can read more about this decision in our
policy document:

> [Open tooling. Hidden Operations.](https://medium.com/@moonstream/open-tooling-hidden-operations-c2033f17b33e)

## Tech stack

Moonstream is built primarily using the following programming languages:

- [Python](https://python.org)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Go](https://go.dev/)
- [Solidity](https://soliditylang.org)

Moonstream is designed with [PostgreSQL](https://www.postgresql.org/) as its primary storage mechanism.

Many features of Moonstream make heavy use of [Bugout](https://bugout.dev), an open source ontology built by the same
core team as Moonstream.

Moonstream uses the following tools to interact with blockchains:

- [web3.js](https://github.com/web3/web3.js)
- [web3.py](https://github.com/ethereum/web3.py)
- [`brownie`](https://github.com/eth-brownie/brownie)

This documentation was generated using [`mkdocs`](https://www.mkdocs.org/). It uses many packages in the `mkdocs` ecosystem, such as:

- The [Material for mkdocs](https://squidfunk.github.io/mkdocs-material/) theme
- [`mkdocstrings`](https://github.com/mkdocstrings/mkdocstrings) to autogenerate documentation from docstrings

## APIs

Moonstream favors the use of simple HTTP APIs that do not store state at the API layer. All state is stored in and accessed
from a database.

Moonstream does not natively offer websocket-based APIs or even HTTP/2-based streaming APIs. This means that
Moonstream API instances are stateless and can be managed easily even by individuals or small teams.

## Administration

All our technology is designed to be deployed on Linux servers, with little preference about where those servers are hosted.
We do not use docker in production. We only use it to run integration tests of our services.
