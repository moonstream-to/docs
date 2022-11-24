# Welcome!

## What is Moonstream?

Moonstream is economic infrastructure for web3 games. It makes it easy to manage blockchain game economies.

One of the biggest challenges for web3 game designers and game developers is that putting your game economy on-chain turns it into
a real economy. This takes control of your game economy away from you, the game designer. Your community is in charge now:

<center>![Meme: Look at me. I'm the captain now.](https://s3.amazonaws.com/static.simiotics.com/memes/im-the-captain-now.gif)</center>

This means that you can no longer freely manipulate your game economy to improve your game.

Moonstream gives you the tools you need to keep your economy healthy and sustainable. And to make sure your players are having fun.

## Terminus

The [Terminus](./terminus.md) smart contract standard is a modification of the [EIP-1155 Multi-Token Standard](https://eips.ethereum.org/EIPS/eip-1155)
designed to represent items, achievements, and experience in web3 games. Terminus is also useful as an
access control mechanism for smart contracts and APIs.

## The Moonstream Engine

The Moonstream Engine provides:

1. [Query API](engine/query-api.md) - A REST API that allows game developers and game designers to monitor their on-chain game economy in real time.
1. [Leaderboards](engine/leaderboards.md) - An API that makes it easy for game developers to combine on- and off-chain game activity to assign points to players.
1. [Dropper](engine/dropper.md) - A tool which allows game designers and game developers to reward their players for in-game activities with on-chain items, experience, and game currencies. Game designers can specify rewards using spreadsheets. Game developers can POST rewards to the Moonstream Engine API.
1. [Crafting](engine/crafting.md) - An on-chain crafting system that web3 games can use to represent the workings of their economies directly on the blockchain.
1. [Game mechanics](engine/mechanics.md) - A library of game mechanics that game developers and game designers can compose to build fully on-chain game experiences for their player community.

## Entity

The Moonstream Entity provides:

1. [Entity API](entity/entity-api.md) - Moonstream Entity API overview.

## Tooling

In addition to the Moonstream web3 game engine, Moonstream also maintains several tools for the benefit of the web3 developer community:

1. [Inspector Facet](tooling/inspector-facet.md) - A tool which makes it easy for anyone to inspect upgradable smart contracts implementing the [EIP-2535 Diamond](https://eips.ethereum.org/EIPS/eip-2535) standard, which is very useful for web3 game projects.

1. [`moonworm`](tooling/moonworm.md) - A code generator which makes it easy for anyone to analyze and interact with Ethereum smart contracts.

## Supported blockchains

Moonstream currently supports any [EVM-based blockchain](https://ethereum.org/en/developers/docs/evm/),
such as [Ethereum](https://ethereum.org), [Polygon](https://polygon.technology/), [Gnosis Chain](https://docs.gnosischain.com/), and more.

## Open source software

The Moonstream community believes firmly in the principles of [Free Software](https://www.gnu.org/philosophy/free-sw.en.html).

Moonstream is completely open source software, free for anyone to use and modify as they please.

Moonstream.to also offers the Moonstream game engine as a hosted service, available at [Moonstream.to](https://moonstream.to).

We do _not_ believe in forcing our views upon our users. We do not use [copyleft licenses](https://en.wikipedia.org/wiki/Copyleft). We favor the
much more permissive [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

We do _not_ believe in the [open core business model](https://en.wikipedia.org/wiki/Open-core_model).
Every feature available on Moonstream.to is also freely available to anyone who chooses to host their own instance of the Moonstream Engine.

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
