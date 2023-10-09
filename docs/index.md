# Welcome!

## What is Moonstream?

Moonstream is economic infrastructure for web3 games. It makes it easy to manage blockchain game economies.

One of the biggest challenges for web3 game designers and game developers is that putting your game economy on-chain turns it into
a real economy. This takes control of your game economy away from you, the game designer. Your community is in charge now:

<center>![Meme: Look at me. I'm the captain now.](https://s3.amazonaws.com/static.simiotics.com/memes/im-the-captain-now.gif)</center>

This means that you can no longer freely manipulate your game economy to improve your game.

Moonstream gives you the mechanisms you need to keep your economy healthy and sustainable. And to make sure your players are having fun.

## Supported blockchains

Moonstream currently supports any [EVM-based blockchain](https://ethereum.org/en/developers/docs/evm/) and testnets,
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
