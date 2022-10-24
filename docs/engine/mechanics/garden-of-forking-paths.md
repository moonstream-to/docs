---
tags:
  - library
  - mechanics
  - EIP-2535
  - smart contracts
  - on-chain
  - social
  - lore
  - terminus
---

# The Garden of Forking Paths

The Garden of Forking Paths is a multiplayer choose your own adventure mechanic.

It draws inspiration from:

1. The huge body of [traditional choose your own adventure literature](https://en.wikipedia.org/wiki/Gamebook).
2. [The story of the same name](https://en.wikipedia.org/wiki/The_Garden_of_Forking_Paths) by
[Jorge Luis Borges](https://en.wikipedia.org/wiki/Jorge_Luis_Borges).
3. [Dungeons and Dragons](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons) and other [tabletop roleplaying games](https://en.wikipedia.org/wiki/Tabletop_role-playing_game).

## Overview and definitions

### Philosophy

We care deeply about our game mechanics being *fun* for players. The Garden of Forking Paths allows
game communities to collaboratively create the lore for their game universe.

All the rules dictating what players can do are represented on the smart contract, but we place no restrictions
on game masters for how they determine the canonical path through their adventures. Game masters are free
to use any mechanism they like to resolve paths. From choosing randomly, to choosing based on player votes, to
choosing by fiat. It is not our place to impose any constraints on game masters.

In our experiences playing and running the Garden of Forking Paths, the fun has been in players creating the lore of
their game universe through play.

### Players and game masters

Garden of Forking Paths contracts have two kinds of users:

1. Players
2. Game masters

The Garden of Forking Paths allows players to experience adventures using their NFTs. Game masters
are the ones responsible for creating and running these adventures.

When a Garden of Forking Paths contract is set up, the deployer specifies a [Terminus](../../terminus.md)
badge which defines whether or not an account is a game master. Any account with that badge is treated as
a game master. Any account without that badge is treated as a player.

Garden of Forking Paths contracts do not care if a game master account represents a human, a bot, or
even a smart contract. One of our principles of composability is that this shouldn't matter. All that
matters is that they have a badge signifying their authority to run adventures for players.

### Sessions, stages, and paths

Each Garden of Forking Paths adventure is represented by a *session*.

Each *session* will involve ERC721 *player tokens*. Different *sessions* may involve different *player token* contracts.

Each *session* will consist of a series of *stages*.

Players will participate in the game using the *player tokens* they own.

Each *stage* will present a *player token* with a number of paths (can vary from stage to stage). A *player token* may choose a path for that stage or it may elect not to choose a path. At the end of that *stage*, a game master will reveal the correct choice for that *stage*. The *player tokens* that chose the correct path will progress to the next *stage*. The *player tokens* which either did not choose a path or which chose an incorrect path will not be able to progress and will remain locked in the contract until the end of the *session*.

Each *stage* *may* have an associated *stage reward.* The *stage reward*, if defined, is a [Terminus](../../terminus.md) token which will be minted to the owners of all *player tokens* that enter that *stage* after choosing the correct path in the previous stage.

*Sessions* will be initiated by game masters.

At the end of every *stage*, a game master will register the correct path for that *stage*. Once this
has been done, if the game masters have reactivated path choices, *player tokens* may be able to register their choice for
the next stage.

Whether or not *player tokens* can make a choice for a *stage* depends on whether the *session* is being
run in *forgiving* mode. In *forgiving* mode, any *player token* can make a choice for the current *stage*, even if
it chose an incorrect path at the previous *stage*. Only *player tokens* which made the correct choice
at the previous stage receive the *stage reward* for the current stage. If a session is *unforgiving*,
then *player tokens* which made an incorrect choice in the previous *stage* may not make a choice in
the current *stage* (and for the rest of the *session*).

A player may only unstake their *player tokens* from a *session* once the *session* has been marked as inactive by a game master.

## Operations

You can use the [`enginecli` command-line tool](https://github.com/bugout-dev/engine) to deploy and
interact with Garden of Forking Paths contracts.

### Deploying a Garden of Forking Paths contract

```bash
enginecli core gofp-gogogo \
    --network $BROWNIE_NETWORK \
    --sender $SENDER \
    --admin-terminus-address $GAME_MASTER_TERMINUS_ADDRESS \
    --admin-terminus-pool-id $GAME_MASTER_TERMINUS_POOL_ID
```

The variables you should define are:

1. `BROWNIE_NETWORK`: The [`brownie`](https://github.com/eth-brownie/brownie) that `enginecli` will use
to connect to your desired blockchain.
2. `SENDER`: Either a path to an Ethereum account keystore JSON file or the name of a [`brownie`](https://github.com/eth-brownie/brownie)
account. This is the Ethereum account you will use to submit the transactions that comprise the Garden of
Forking paths deployment.
3. `GAME_MASTER_TERMINUS_ADDRESS`: The address of the [Terminus](../../terminus.md) contract containing the
game master badge.
4. `GAME_MASTER_TERMINUS_POOL_ID`: The [Terminus](../../terminus.md) pool ID of the game master badge.

You can also specify other arguments on the command line, such as `--confirmations`, `--nonce`, `--max-fee-per-gas`, etc.
To see a full list of the arguments available to the deployment command, run:

```bash
enginecli core gofp-gogogo --help
```

Once this deployment is complete, a JSON object will be printed to `stdout`. The output will have the following structure:

```json
{
    "contracts": {
        "DiamondCutFacet": "0xED2E9e3a46f5e8Defa3641FA0e5AccFbd97D5b75",
        "Diamond": "0x4a0CA4D0CC883343F9499053E11812Ce469b229f",
        "DiamondLoupeFacet": "0x2D9f60a6C1CCC247bAB4207023533CF317fB3F9E",
        "OwnershipFacet": "0x8aBfB1054Dd4f4DCa16c96358B5223b62A7cAB90",
        "GOFPFacet": "0xE7963a151Ea40A3D7256724C630B407d2B967387"
    },
    "attached": [
        "DiamondLoupeFacet",
        "OwnershipFacet",
        "GOFPFacet"
    ]
}
```

The deployment sets up an [EIP-2535 proxy contract](https://eips.ethereum.org/EIPS/eip-2535). The value
at `.contracts.Diamond` is the address of the Garden of Forking Paths contract.
