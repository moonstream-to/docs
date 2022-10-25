---
tags:
  - library
  - mechanics
  - EIP-20
  - EIP-721
  - EIP-1155
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
2. [The Garden of Forking Paths](https://en.wikipedia.org/wiki/The_Garden_of_Forking_Paths), a short
story by [Jorge Luis Borges](https://en.wikipedia.org/wiki/Jorge_Luis_Borges).
3. [Dungeons and Dragons](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons) and other [tabletop roleplaying games](https://en.wikipedia.org/wiki/Tabletop_role-playing_game).

## Philosophy

We care deeply about our game mechanics being *fun* for players. The Garden of Forking Paths allows
game communities to collaboratively create the lore for their game universe.

All the rules dictating what players can do are represented on the smart contract, but we place no restrictions
on game masters for how they determine the canonical path through their adventures. Game masters are free
to use any mechanism they like to resolve paths. From choosing randomly, to choosing based on player votes, to
choosing by fiat. It is not our place to impose any constraints on game masters.

In our experiences playing and running the Garden of Forking Paths, the fun has been in players creating the lore of
their game universe through play.


## Roles: Players and game masters

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

## Gameplay

Garden of Forking Paths allows game masters to run adventures for players. Each adventure is represented
by a *session*.

Each session has an associated [EIP-721](https://eips.ethereum.org/EIPS/eip-721) contract. The tokens
from that contract are the characters that the player can use in the adventure. When a player elects to
participate in an adventure with one of their NFTs, that NFT is staked into the Garden of Forking Paths contract.
This means that, ownership of the NFT is transferred to the Garden of Forking Paths contract during the
session.

Whenever they want, players can unstake their NFTs from a Garden of Forking Paths session. NFTs cannot
participate in sessions that they were previously unstaked from.

Game masters can ask players to pay to send their NFTs into a session. Payments are specified as an [EIP-20](https://eips.ethereum.org/EIPS/eip-20)
contract address and a payment amount. The amount is charged per-NFT. If no EIP-20 token is specified,
players can send their NFTs into a session free of charge.

Each session consists of a series of *stages*. Each stage presents each player token a number of *paths* to choose from.
The number of paths can vary from stage to stage.

Stages represent decision points in story. The paths represent the decisions that the characters can
make at that decision point.

Session progress sequentially through their stages as follows:

1. Players choose a path in the current stage with each of their NFTs.
2. Game masters freeze the ability for players to choose a path.
3. Game masters set the correct choice for the current stage.
4. This progresses play to the next stage.
5. Game masters unfreeze the ability for players to choose a path.

This process is repeated for each stage in the session until the session ends.

Game masters may also associate a [Terminus](../../terminus.md) reward with each stage. If a stage has
an associated reward, that token is minted to the staker of every NFT which makes choice at that stage
after making the correct choice at the previous stage.

Garden of Forking Paths sessions can be *forgiving* or *unforgiving*. In an unforgiving session, player
tokens which made an incorrect choice in the previous stage may not make a choice in the current stage
(or for any stage in the rest of the session). In a forgiving session, any player token may make a choice
at the current stage but *only* the tokens which chose correctly in the previous stage receive stage
rewards.

## Contract

The Garden of Forking Paths mechanic is implemented by the [`GOFPFacet` smart contract](https://github.com/bugout-dev/engine/blob/main/contracts/mechanics/garden-of-forking-paths/GardenOfForkingPaths.sol).

This contract can be used as a facet on an [EIP-2535 proxy contract](https://eips.ethereum.org/EIPS/eip-2535).
It can also be deployed as a standalone contract. Whether you use a proxy or deploy as a standalone depends
on your use case.

### Modifiers

#### `onlyGameMaster`

The Garden of Forking Paths smart contract defines an `onlyGameMaster` modifier. Smart contract methods
with this modifier can only be invoked by accounts that hold a game master badge.

#### `diamondNonReentrant`

The Garden of Forking Paths can be used to provide method implementations for [EIP-2535 Diamond proxies](https://eips.ethereum.org/EIPS/eip-2535).

The `diamondNonReentrant` modifier is similar to the Open Zeppelin `nonReentrant` modifier but uses a
predefined storage slot to make it suitable for use on Diamond contracts.

The implementation is in [`DiamondReentrancyGuard.sol`](https://github.com/bugout-dev/engine/blob/main/contracts/diamond/security/DiamondReentrancyGuard.sol).

### Methods

Garden of Forking Paths contracts have the following external/public methods:

| Method | Description | returns | method visibility | `onlyGameMaster`? | `diamondNonReentrant`? |
|--------|-------------|---------|-------------------|-------------------|------------------------|
| `init` | Initializes a Garden of Forking Paths contract by setting the Terminus address and pool ID for its game master badge. Only the contract owner can call this method. | None | `external` | No | No |
| `getSession` | Retrieves information about a Garden of Forking Paths game session. | [`Session`](https://github.com/bugout-dev/engine/blob/main/contracts/mechanics/garden-of-forking-paths/GardenOfForkingPaths.sol) | `external view` | No | No |
| `adminTerminusInfo` | Returns the Terminus address and pool ID for the Game Master badge registered on the Garden of Forking Paths contract. | (`address`, `uint256`) | `external view` | No | No |
| `numSessions` | Returns the number of game sessions that have been created on the Garden of Forking Paths contract. | `uint256` | `external view` | No | No |
| `createSession` | Allows game masters to create a new game session. | None | `external` | Yes | No |
| `getStageReward` | Returns the reward for a given stage in a given session. | [`StageReward`](https://github.com/bugout-dev/engine/blob/main/contracts/mechanics/garden-of-forking-paths/GardenOfForkingPaths.sol) | `external view` | No | No |
| `setStageRewards` | Allows game masters to set rewards for any number of stages in a given session. | None | `external` | Yes | No |
| `setSessionActive` | Allows game masters to activate and deactivate game sessions. | None | `external` | Yes | No |
| `getCorrectPathForStage` | For a given stage in a given session, returns the path that has been marked by game masters as the correct path for that stage. | `uint256` | `external view` | No | No |
| `setCorrectPathForStage` | Allows game masters to set the correct path for a specific stage in a specific session. | None | `external` | Yes | No |
| `setSessionChoosingActive`| Allows game masters to allow and disallow NFTs from choosing paths in the current stage of a given session. | None | `external` | Yes | No |
| `setSessionUri`| Allows game masters to associate a URI with a session. This URI can contain JSON metadata. | None | `external` | Yes | No |
| `getStakedTokenInfo` | If a given NFT is staked into any Garden of Forking Paths session, this method allows anyone to see which session it is in and who staked it there. | (`uint256`, `address`) | `external view` | No | No |
| `getSessionTokenStakeGuard`| Allows anyone to see if a given NFT was *ever* staked into a given session. The NFT is specified only by its `tokenId` and is assumed to come from the NFT contract associated with the given session. | `bool` | `external view` | No | No |
| `numTokensStakedIntoSession` | Allows anyone to see how many tokens a given stakers has staked into a given session. | `uint256` | `external view` | No | No |
| `tokenOfStakerInSessionByIndex` | Allows anyone to enumerate over the tokens that a given staker has staked into a given session. The staked tokens are 1-indexed. | `uint256` | `external view` | No | No |
| `getPathChoice` | Allows anyone to see which path (if any) a given NFT chose at a given stage in a given session. | `uint256` | `external view` | No | No |
| `stakeTokensIntoSession` | Allows players to enter their NFTs into a game session via staking. The contract takes ownership of the staked NFTs. This is a batch method - multiple NFTs can be staked at once. | None | `external` | No | Yes |
| `unstakeTokensFromSession` | Allows players to remove their NFTs from a game session. The contract transfers the tokens back to the original staker. This is a batch method - multiple NFTs can be unstaked at once. | None | `external` | No | Yes |
| `getCurrentStage` | Allows anyone to see what the current stage is for a given session. This shows how far a session has progressed. | `uint256` | `external view` | No | No |
| `chooseCurrentStagePaths` | Allows players to choose a path in the current stage of a given session. | None | `external` | No | Yes |



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

### Game masters

#### Creating a session

Only game masters can create sessions on a Garden of Forking Paths contract. They can do this by invoking
the `createSesssion` method, which has the following signature:

```solidity
function createSession(
    address playerTokenAddress,
    address paymentTokenAddress,
    uint256 paymentAmount,
    bool isActive,
    string memory uri,
    uint256[] memory stages,
    bool isForgiving
) external onlyGameMaster {};
```

The arguments to this method are:

1. `playerTokenAddress` - Address of the EIP-721 contract whose NFTs can participate in the session as characters.
2. `paymentTokenAddress` - Address of the EIP-20 contract to require as payment for staking NFTs into the session.
This should be set to the zero address (`0x0000000000000000000000000000000000000000`) for free-to-play sessions.
3. `paymentTokenAmount` - If the `paymentTokenAddress` is not the zero address, this should be the *number* of payment
tokens that will be charged to stake each NFT into the session. Should be `0` for free-to-play sessions.
4. `isActive` - Should be `true` for sessions that are active as soon as they are created. If set to `false`, game masters will have to explicitly
activate the session (using `setSessionActive`) before players can start participating.
5. `uri` - Metadata URI for the session.
6. `stages` - An array specifying the number of paths in each stage of the session. For example, `[2, 5, 7]` specifies
a session with 3 stages, with 2 paths in stage 1, 5 paths in stage 2, and 7 paths in stage 3.
7. `isForgiving` - Set to `true` to create a forgiving session, and `false` to create an unforgiving session.

Game masters may use the `enginecli` tool to create sessions at their command lines:

```
$ enginecli gofp create-session --help

usage: enginecli create-session [-h] --network NETWORK [--address ADDRESS] --sender SENDER [--password PASSWORD] [--gas-price GAS_PRICE] [--max-fee-per-gas MAX_FEE_PER_GAS]
                                [--max-priority-fee-per-gas MAX_PRIORITY_FEE_PER_GAS] [--confirmations CONFIRMATIONS] [--nonce NONCE] [--value VALUE] [--verbose] --player-token-address
                                PLAYER_TOKEN_ADDRESS --payment-token-address PAYMENT_TOKEN_ADDRESS --payment-amount PAYMENT_AMOUNT --is-active IS_ACTIVE --uri URI --stages STAGES [STAGES ...]
                                --is-forgiving IS_FORGIVING

optional arguments:
  -h, --help            show this help message and exit
  --network NETWORK     Name of brownie network to connect to
  --address ADDRESS     Address of deployed contract to connect to
  --sender SENDER       Path to keystore file for transaction sender
  --password PASSWORD   Password to keystore file (if you do not provide it, you will be prompted for it)
  --gas-price GAS_PRICE
                        Gas price at which to submit transaction
  --max-fee-per-gas MAX_FEE_PER_GAS
                        Max fee per gas for EIP1559 transactions
  --max-priority-fee-per-gas MAX_PRIORITY_FEE_PER_GAS
                        Max priority fee per gas for EIP1559 transactions
  --confirmations CONFIRMATIONS
                        Number of confirmations to await before considering a transaction completed
  --nonce NONCE         Nonce for the transaction (optional)
  --value VALUE         Value of the transaction in wei(optional)
  --verbose             Print verbose output
  --player-token-address PLAYER_TOKEN_ADDRESS
                        Type: address
  --payment-token-address PAYMENT_TOKEN_ADDRESS
                        Type: address
  --payment-amount PAYMENT_AMOUNT
                        Type: uint256
  --is-active IS_ACTIVE
                        Type: bool
  --uri URI             Type: string
  --stages STAGES [STAGES ...]
                        Type: uint256[]
  --is-forgiving IS_FORGIVING
                        Type: bool
```

#### Setting stage rewards

#### Setting the right path for a stage

### Players

#### Staking and unstaking

#### Choosing paths
