# Welcome!

## What is Moonstream?

Moonstream is an open source web3 game engine. It makes it easy for game developers and game
designers to integrate their games with blockchains.

Designing a game is hard enough. Designing a web3 game is *even harder*. One of the biggest challenges
for web3 game designers and game developers is that putting your game economy on-chain turns it into
a real economy. This takes control of your game economy away from you, the game designer, and transfers this control
to your players and to the web3 community at large.

If you are building a web3 game, the Moonstream engine provides you the tools you need to integrate your game
with the blockchain, manage your on-chain economy, and keep your players entertained.


## Terminus

The [Terminus](./terminus.md) smart contract standard is an improvement of the [EIP1155 Multi-Token Standard](https://eips.ethereum.org/EIPS/eip-1155)
designed to represent items, achievements, and experience in web3 game economies.

Terminus modifies EIP1155 by allowing game designers and game developers to define *transferability*,
*burnability*, and even supply limits at the level of token IDs.

It also allows game designers and game developers to delegate minting and burning capabilities on individual
token IDs to other accounts or to other smart contracts.

This is useful as game developers can represent all of the following types of assets using a single smart contract:
1. Badges: Non-transferable tokens which can be minted by a game server or other game contract
1. Items: Transferable tokens with a high maximum supply
1. Consumable tokens: Transferable tokens which are burned by the game contract on use
1. Artifacts: Transferable tokens with a low maximum supply

Terminus is compatible with any marketplace that supports the EIP1155 Multi-Token Standard, such as
[Open Sea](https://opensea.io).
The largest Terminus marketplace on Open Sea is currently [Crypto Unicorns: Item Marketplace](https://opensea.io/collection/crypto-unicorns-items-marketplace),
with over 2000 ETH in transaction volume.

## The Moonstream Engine

The Moonstream Engine provides:

1. [Mechanics]() - A library of game mechanics that game developers and game designers can compose to build fully on-chain game experiences for their player community.
1. [Crafting]() - An on-chain crafting system that web3 games can use to represent the workings of their economies directly on the blockchain.
1. [Dropper]() - A tool which allows game designers and game developers to reward their players for in-game activities with on-chain items, experience, and game currencies. Game designers can specify rewards using spreadsheets. Game developers can POST rewards to the Moonstream Engine API.
1. [Leaderboards]() - An API that makes it easy for game developers to combine on- and off-chain game activity to assign points to players.
1. [Query API]() - A REST API that allows game developers and game designers to monitor their on-chain game economy in real time.


## Tooling

In addition to the Moonstream web3 game engine, Moonstream also maintains several tools for the benefit of the web3 developer community:

1. [`moonworm`]() - A code generator which makes it easy for anyone to analyze and interact with Ethereum smart contracts.

1. [Inspector Facet]() - A tool which makes it easy for anyone to inspect upgradable smart contracts implementing the [EIP2535 Diamond](https://eips.ethereum.org/EIPS/eip-2535) standard, which is very useful for web3 game projects.


## Supported blockchains

Moonstream currently supports any [EVM-based blockchain](https://ethereum.org/en/developers/docs/evm/),
such as [Ethereum](https://ethereum.org), [Polygon](https://polygon.technology/), [Gnosis Chain](https://docs.gnosischain.com/), and more.



## Open source software

The Moonstream community believes firmly in the principles of [Free Software](https://www.gnu.org/philosophy/free-sw.en.html).

Moonstream is completely open source software, free for anyone to use and modify as they please.

Moonstream.to also offers the Moonstream game engine as a hosted service, available at [Moonstream.to](https://moonstream.to).

We do *not* believe in forcing our views upon our users. We do not use [copyleft licenses](https://en.wikipedia.org/wiki/Copyleft). We favor the
much more permissive [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

We do *not* believe in the [open core business model](https://en.wikipedia.org/wiki/Open-core_model). Every feature available on Moonstream.to is
also freely available to anyone who chooses to host their own instance of the Moonstream Engine.

The only code that we write that is *not* open source is the code related to our security operations. You can read more about this decision in our
policy document: [Open tooling. Hidden Operations.](https://medium.com/@moonstream/open-tooling-hidden-operations-c2033f17b33e)

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

All our technology is designed to be deployed on Linux servers, with little preference on where those servers are hosted.
We do not use docker in production, and only use it to run integration tests of our services.
