---
tags:
  - library
  - mechanics
  - EIP-2535
  - smart contracts
  - on-chain
---

# Game mechanics

Moonstream Engine contains an open library of game mechanics that anyone can compose together to create
fully on-chain games.

### Composability

Our mechanics are implemented to be mounted as facets on [EIP-2535 Diamond proxy contracts](https://eips.ethereum.org/EIPS/eip-2535).
This is what makes them composable. If you would like to create an on-chain game using Moonstream mechanics,
it is important to first familiarize yourself with EIP-2535.

### Existing mechanics

- [Lootbox](./lootbox.md) - random reward distribution
- [Garden of Forking Paths](./garden-of-forking-paths.md) - multiplayer choose your own adventure

### Upcoming mechanics

- Exploration - NFT staking
- 1v1 Autobattler
- Racer
