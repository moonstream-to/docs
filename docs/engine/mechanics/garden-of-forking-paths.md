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

The Garden of Forking Paths (GOFP) is a multiplayer choose your own adventure mechanic.

It draws inspiration from:

1. The huge body of [traditional choose your own adventure literature](https://en.wikipedia.org/wiki/Gamebook).
2. [The Garden of Forking Paths](https://en.wikipedia.org/wiki/The_Garden_of_Forking_Paths), a short
story by [Jorge Luis Borges](https://en.wikipedia.org/wiki/Jorge_Luis_Borges).
3. [Dungeons and Dragons](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons) and other [tabletop roleplaying games](https://en.wikipedia.org/wiki/Tabletop_role-playing_game).

## Philosophy

We care deeply about our game mechanics being *fun* for players. The GOFP allows
game communities to collaboratively create the lore for their game universe.

All the rules dictating what players can do are represented on the smart contract, but we place no restrictions
on game masters for how they determine the canonical path through their adventures. Game masters are free
to use any mechanism they like to resolve paths. From choosing randomly, to choosing based on player votes, to
choosing by fiat. It is not our place to impose any constraints on game masters.

In our experiences playing and running the GOFP, the fun has been in players creating the lore of
their game universe through play.


## Players and game masters

GOFP contracts have two kinds of users:

1. Players
2. Game masters

The GOFP allows players to experience adventures using their NFTs. Game masters
are the ones responsible for creating and running these adventures.

When a GOFP contract is set up, the deployer specifies a [Terminus](../../terminus.md)
badge which defines whether or not an account is a game master. Any account with that badge is treated as
a game master. Any account without that badge is treated as a player.

GOFP contracts do not care if a game master account represents a human, a bot, or
even a smart contract. One of our principles of composability is that this shouldn't matter. All that
matters is that they have a badge signifying their authority to run adventures for players.

## Gameplay

GOFP allows game masters to run adventures for players. Each adventure is represented
by a *session*.

Each session has an associated [EIP-721](https://eips.ethereum.org/EIPS/eip-721) contract. The tokens
from that contract are the characters that the player can use in the adventure. When a player elects to
participate in an adventure with one of their NFTs, that NFT is staked into the GOFP contract.
This means that, ownership of the NFT is transferred to the GOFP contract during the
session.

Whenever they want, players can unstake their NFTs from a GOFP session. NFTs cannot
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

GOFP sessions can be *forgiving* or *unforgiving*. In an unforgiving session, player
tokens which made an incorrect choice in the previous stage may not make a choice in the current stage
(or for any stage in the rest of the session). In a forgiving session, any player token may make a choice
at the current stage but *only* the tokens which chose correctly in the previous stage receive stage
rewards.

## Contract

The GOFP mechanic is implemented by the [`GOFPFacet` smart contract](https://github.com/bugout-dev/engine/blob/main/contracts/mechanics/garden-of-forking-paths/GardenOfForkingPaths.sol).

This contract can be used as a facet on an [EIP-2535 proxy contract](https://eips.ethereum.org/EIPS/eip-2535).
It can also be deployed as a standalone contract. Whether you use a proxy or deploy as a standalone depends
on your use case.

### Modifiers

#### `onlyGameMaster`

The GOFP smart contract defines an `onlyGameMaster` modifier. Smart contract methods
with this modifier can only be invoked by accounts that hold a game master badge.

#### `diamondNonReentrant`

The GOFP can be used to provide method implementations for [EIP-2535 Diamond proxies](https://eips.ethereum.org/EIPS/eip-2535).

The `diamondNonReentrant` modifier is similar to the Open Zeppelin `nonReentrant` modifier but uses a
predefined storage slot to make it suitable for use on Diamond contracts.

The implementation is in [`DiamondReentrancyGuard.sol`](https://github.com/bugout-dev/engine/blob/main/contracts/diamond/security/DiamondReentrancyGuard.sol).

### Methods

GOFP contracts have the following external/public methods:

| Method | Description | returns | method visibility | `onlyGameMaster`? | `diamondNonReentrant`? |
|--------|-------------|---------|-------------------|-------------------|------------------------|
| `init` | Initializes a GOFP contract by setting the Terminus address and pool ID for its game master badge. Only the contract owner can call this method. | None | `external` | No | No |
| `getSession` | Retrieves information about a GOFP game session. | [`Session`](https://github.com/bugout-dev/engine/blob/main/contracts/mechanics/garden-of-forking-paths/GardenOfForkingPaths.sol) | `external view` | No | No |
| `adminTerminusInfo` | Returns the Terminus address and pool ID for the Game Master badge registered on the GOFP contract. | (`address`, `uint256`) | `external view` | No | No |
| `numSessions` | Returns the number of game sessions that have been created on the GOFP contract. | `uint256` | `external view` | No | No |
| `createSession` | Allows game masters to create a new game session. | None | `external` | Yes | No |
| `getStageReward` | Returns the reward for a given stage in a given session. | [`StageReward`](https://github.com/bugout-dev/engine/blob/main/contracts/mechanics/garden-of-forking-paths/GardenOfForkingPaths.sol) | `external view` | No | No |
| `setStageRewards` | Allows game masters to set rewards for any number of stages in a given session. | None | `external` | Yes | No |
| `setSessionActive` | Allows game masters to activate and deactivate game sessions. | None | `external` | Yes | No |
| `getCorrectPathForStage` | For a given stage in a given session, returns the path that has been marked by game masters as the correct path for that stage. | `uint256` | `external view` | No | No |
| `setCorrectPathForStage` | Allows game masters to set the correct path for a specific stage in a specific session. | None | `external` | Yes | No |
| `setSessionChoosingActive`| Allows game masters to allow and disallow NFTs from choosing paths in the current stage of a given session. | None | `external` | Yes | No |
| `setSessionUri`| Allows game masters to associate a URI with a session. This URI can contain JSON metadata. | None | `external` | Yes | No |
| `getStakedTokenInfo` | If a given NFT is staked into any GOFP session, this method allows anyone to see which session it is in and who staked it there. | (`uint256`, `address`) | `external view` | No | No |
| `getSessionTokenStakeGuard`| Allows anyone to see if a given NFT was *ever* staked into a given session. The NFT is specified only by its `tokenId` and is assumed to come from the NFT contract associated with the given session. | `bool` | `external view` | No | No |
| `numTokensStakedIntoSession` | Allows anyone to see how many tokens a given stakers has staked into a given session. | `uint256` | `external view` | No | No |
| `tokenOfStakerInSessionByIndex` | Allows anyone to enumerate over the tokens that a given staker has staked into a given session. The staked tokens are 1-indexed. | `uint256` | `external view` | No | No |
| `getPathChoice` | Allows anyone to see which path (if any) a given NFT chose at a given stage in a given session. | `uint256` | `external view` | No | No |
| `stakeTokensIntoSession` | Allows players to enter their NFTs into a game session via staking. The contract takes ownership of the staked NFTs. This is a batch method - multiple NFTs can be staked at once. | None | `external` | No | Yes |
| `unstakeTokensFromSession` | Allows players to remove their NFTs from a game session. The contract transfers the tokens back to the original staker. This is a batch method - multiple NFTs can be unstaked at once. | None | `external` | No | Yes |
| `getCurrentStage` | Allows anyone to see what the current stage is for a given session. This shows how far a session has progressed. | `uint256` | `external view` | No | No |
| `chooseCurrentStagePaths` | Allows players to choose a path in the current stage of a given session. | None | `external` | No | Yes |



## Usage


You can use the [`enginecli` command-line tool](https://github.com/bugout-dev/engine) to deploy and
interact with GOFP contracts.

### Deploying a GOFP contract

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
at `.contracts.Diamond` is the address of the GOFP contract.

### Game masters

#### Creating a session

Only game masters can create sessions on a GOFP contract. They can do this by invoking
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

Game masters can register rewards for entering stages in a given session using the `setStageRewards` method:

```solidity
function setStageRewards(
    uint256 sessionId,
    uint256[] calldata stages,
    address[] calldata terminusAddresses,
    uint256[] calldata terminusPoolIds,
    uint256[] calldata rewardAmounts
) external onlyGameMaster {};
```

All rewards are assumed to be [Terminus](../../terminus.md) tokens. It is assumed that the Garden of Forking
Paths contract has the ability to mint the reward tokens.

Stage rewards can only be set on inactive sessions. This setting can be changed using `setSessionActive`.

The arguments to `setStageRewards` are:

1. `sessionId` - The ID of the session to set rewards for.
2. `stages` - An array containing the numbers of the stages for which to set rewards. Note that stages are 1-indexed.
3. `terminusAddresses` - An array of addresses to the Terminus contracts from which the rewards for the corresponding stage
are minted. This array must be equal in length to the `stages` array.
4. `terminusPoolIds` - An array of Terminus pool IDs on the corresponding Terminus contracts that represent
the rewards for the corresponding stages. This array must be equal in length to the `stages` and `terminusAddresses`
arrays.
5. `rewardAmounts` - The number of tokens from the corresponding Terminus pools that are minted as rewards for
the corresponding stages. This array must be equal in length to the `stages`, `terminusAddresses`, and `terminusPoolIds`
arrays.

Game masters may use the `enginecli` tool to set stage rewards at their command lines:

```
$ enginecli gofp set-stage-rewards --help

usage: enginecli set-stage-rewards [-h] --network NETWORK [--address ADDRESS] --sender SENDER [--password PASSWORD] [--gas-price GAS_PRICE] [--max-fee-per-gas MAX_FEE_PER_GAS]
                                   [--max-priority-fee-per-gas MAX_PRIORITY_FEE_PER_GAS] [--confirmations CONFIRMATIONS] [--nonce NONCE] [--value VALUE] [--verbose] --session-id SESSION_ID
                                   --stages STAGES [STAGES ...] --terminus-addresses TERMINUS_ADDRESSES [TERMINUS_ADDRESSES ...] --terminus-pool-ids TERMINUS_POOL_IDS [TERMINUS_POOL_IDS ...]
                                   --reward-amounts REWARD_AMOUNTS [REWARD_AMOUNTS ...]

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
  --session-id SESSION_ID
                        Type: uint256
  --stages STAGES [STAGES ...]
                        Type: uint256[]
  --terminus-addresses TERMINUS_ADDRESSES [TERMINUS_ADDRESSES ...]
                        Type: address[]
  --terminus-pool-ids TERMINUS_POOL_IDS [TERMINUS_POOL_IDS ...]
                        Type: uint256[]
  --reward-amounts REWARD_AMOUNTS [REWARD_AMOUNTS ...]
                        Type: uint256[]
```

#### Setting the correct path for a stage

Game masters can set the correct path for the current stage in a given session using the  `setCorrectPathForStage` method:

```solidity
function setCorrectPathForStage(
    uint256 sessionId,
    uint256 stage,
    uint256 path,
    bool setIsChoosingActive
) external onlyGameMaster {};
```

Correct paths can only be set for sessions in which choosing is inactive. This setting can be changed
using `setSessionChoosingActive`.

The arguments to `setCorrectPathForStage` are:

1. `sessionId` - ID for the session in which you want to set the correct path for a stage.
2. `stage` - Number of the stage for which you want to set the correct path.
3. `path` - Path that should be designated as correct for the given stage.
4. `setChoosingActive` - Set to `true` to allow NFTs to choose paths in the *next* stage as soon as this
transaction is successfully completed.

Game masters may use the `enginecli` tool to set stage correct paths for a stage at their command lines:

```
$ enginecli gofp set-correct-path-for-stage --help
usage: enginecli set-correct-path-for-stage [-h] --network NETWORK [--address ADDRESS] --sender SENDER [--password PASSWORD] [--gas-price GAS_PRICE] [--max-fee-per-gas MAX_FEE_PER_GAS]
                                            [--max-priority-fee-per-gas MAX_PRIORITY_FEE_PER_GAS] [--confirmations CONFIRMATIONS] [--nonce NONCE] [--value VALUE] [--verbose] --session-id
                                            SESSION_ID --stage STAGE --path PATH --set-is-choosing-active SET_IS_CHOOSING_ACTIVE

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
  --session-id SESSION_ID
                        Type: uint256
  --stage STAGE         Type: uint256
  --path PATH           Type: uint256
  --set-is-choosing-active SET_IS_CHOOSING_ACTIVE
                        Type: bool
```

### Players

#### Staking

Players can stake their NFTs into a session using the `stakeTokensIntoSession` method:

```solidity
function stakeTokensIntoSession(
    uint256 sessionId,
    uint256[] calldata tokenIds
) external diamondNonReentrant {};
```

Tokens can only be staked into active sessions.

A token that was previously staked into the same session and subsequently unstaked may not be restaked
into the same session.

The arguments to `stakeTokensIntoSession` are:

1. `sessionId` - The ID of the session to stake into.
2. `tokenIds` - An array containing the `tokenId`s of the NFTs that the player would like to stake into the
session. The tokens are assumed to be from the EIP-721 contract that was set as the `playerTokenAddress`
on the session. You can view the session configuration using the `getSession` view method.

Players may use the `enginecli` tool to stake tokens into a session at their command lines:

```
$ enginecli gofp stake-tokens-into-session --help

usage: enginecli stake-tokens-into-session [-h] --network NETWORK [--address ADDRESS] --sender SENDER [--password PASSWORD] [--gas-price GAS_PRICE] [--max-fee-per-gas MAX_FEE_PER_GAS]
                                           [--max-priority-fee-per-gas MAX_PRIORITY_FEE_PER_GAS] [--confirmations CONFIRMATIONS] [--nonce NONCE] [--value VALUE] [--verbose] --session-id
                                           SESSION_ID --token-ids TOKEN_IDS [TOKEN_IDS ...]

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
  --session-id SESSION_ID
                        Type: uint256
  --token-ids TOKEN_IDS [TOKEN_IDS ...]
                        Type: uint256[]
```

#### Unstaking

Players can unstake their NFTs from a session using the `unstakeTokensFromSession` method:

```solidity
function unstakeTokensFromSession(
    uint256 sessionId,
    uint256[] calldata tokenIds
) external diamondNonReentrant {};
```

Tokens can be unstaked from sessions at any time. Tokens can only be unstaked by their original staker.

The arguments to `unstakeTokensFromSession` are:

1. `sessionId` - The ID of the session to unstake from.
2. `tokenIds` - An array containing the `tokenId`s of the NFTs that the player would like to unstake from the
session. The tokens are assumed to be from the EIP-721 contract that was set as the `playerTokenAddress`
on the session. You can view the session configuration using the `getSession` view method.

Players may use the `enginecli` tool to unstake tokens from a session at their command lines:

```
$ enginecli gofp unstake-tokens-from-session --help

usage: enginecli unstake-tokens-from-session [-h] --network NETWORK [--address ADDRESS] --sender SENDER [--password PASSWORD] [--gas-price GAS_PRICE] [--max-fee-per-gas MAX_FEE_PER_GAS]
                                             [--max-priority-fee-per-gas MAX_PRIORITY_FEE_PER_GAS] [--confirmations CONFIRMATIONS] [--nonce NONCE] [--value VALUE] [--verbose] --session-id
                                             SESSION_ID --token-ids TOKEN_IDS [TOKEN_IDS ...]

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
  --session-id SESSION_ID
                        Type: uint256
  --token-ids TOKEN_IDS [TOKEN_IDS ...]
                        Type: uint256[]
```

#### Choosing paths

Players can choose paths for their NFTs in the current stage of a session using the `chooseCurrentStagePaths` method:

```solidity
function chooseCurrentStagePaths(
    uint256 sessionId,
    uint256[] memory tokenIds,
    uint256[] memory paths
) external diamondNonReentrant {};
```

Tokens can only choose paths if choosing is active for the session.

The arguments to `chooseCurrentStagePaths` are:

1. `sessionId` - The ID of the session to choose paths in.
2. `tokenIds` - An array containing the `tokenId`s of the NFTs that the player would like to choose paths
for. The tokens are assumed to be from the EIP-721 contract that was set as the `playerTokenAddress`
on the session. You can view the session configuration using the `getSession` view method.
3. `paths` - An array of path choices per `tokenId` in the `tokenIds` array. This array should have the
same length as the `tokenIds` array. Remember that paths are 1-indexed.

Players may use the `enginecli` tool to choose paths for their NFTs at their command lines:

```
$ enginecli gofp choose-current-stage-paths --help

usage: enginecli choose-current-stage-paths [-h] --network NETWORK [--address ADDRESS] --sender SENDER [--password PASSWORD] [--gas-price GAS_PRICE] [--max-fee-per-gas MAX_FEE_PER_GAS]
                                            [--max-priority-fee-per-gas MAX_PRIORITY_FEE_PER_GAS] [--confirmations CONFIRMATIONS] [--nonce NONCE] [--value VALUE] [--verbose] --session-id
                                            SESSION_ID --token-ids TOKEN_IDS [TOKEN_IDS ...] --paths PATHS [PATHS ...]

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
  --session-id SESSION_ID
                        Type: uint256
  --token-ids TOKEN_IDS [TOKEN_IDS ...]
                        Type: uint256[]
  --paths PATHS [PATHS ...]
                        Type: uint256[]
```

### ABI

```json
[
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "stage",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "path",
        "type": "uint256"
      }
    ],
    "name": "PathChosen",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "stage",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "path",
        "type": "uint256"
      }
    ],
    "name": "PathRegistered",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "bool",
        "name": "isActive",
        "type": "bool"
      }
    ],
    "name": "SessionActivated",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "bool",
        "name": "isChoosingActive",
        "type": "bool"
      }
    ],
    "name": "SessionChoosingActivated",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "playerTokenAddress",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "paymentTokenAddress",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "paymentAmount",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "uri",
        "type": "string"
      },
      {
        "indexed": false,
        "internalType": "bool",
        "name": "active",
        "type": "bool"
      },
      {
        "indexed": false,
        "internalType": "bool",
        "name": "isForgiving",
        "type": "bool"
      }
    ],
    "name": "SessionCreated",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "string",
        "name": "uri",
        "type": "string"
      }
    ],
    "name": "SessionUriChanged",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "stage",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "terminusAddress",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "terminusPoolId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "rewardAmount",
        "type": "uint256"
      }
    ],
    "name": "StageRewardChanged",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "adminTerminusInfo",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "uint256[]",
        "name": "tokenIds",
        "type": "uint256[]"
      },
      {
        "internalType": "uint256[]",
        "name": "paths",
        "type": "uint256[]"
      }
    ],
    "name": "chooseCurrentStagePaths",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "playerTokenAddress",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "paymentTokenAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "paymentAmount",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "isActive",
        "type": "bool"
      },
      {
        "internalType": "string",
        "name": "uri",
        "type": "string"
      },
      {
        "internalType": "uint256[]",
        "name": "stages",
        "type": "uint256[]"
      },
      {
        "internalType": "bool",
        "name": "isForgiving",
        "type": "bool"
      }
    ],
    "name": "createSession",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "stage",
        "type": "uint256"
      }
    ],
    "name": "getCorrectPathForStage",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      }
    ],
    "name": "getCurrentStage",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "stage",
        "type": "uint256"
      }
    ],
    "name": "getPathChoice",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      }
    ],
    "name": "getSession",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "playerTokenAddress",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "paymentTokenAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "paymentAmount",
            "type": "uint256"
          },
          {
            "internalType": "bool",
            "name": "isActive",
            "type": "bool"
          },
          {
            "internalType": "bool",
            "name": "isChoosingActive",
            "type": "bool"
          },
          {
            "internalType": "string",
            "name": "uri",
            "type": "string"
          },
          {
            "internalType": "uint256[]",
            "name": "stages",
            "type": "uint256[]"
          },
          {
            "internalType": "bool",
            "name": "isForgiving",
            "type": "bool"
          }
        ],
        "internalType": "struct Session",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "getSessionTokenStakeGuard",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "stage",
        "type": "uint256"
      }
    ],
    "name": "getStageReward",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "terminusAddress",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "terminusPoolId",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "rewardAmount",
            "type": "uint256"
          }
        ],
        "internalType": "struct StageReward",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "nftAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "name": "getStakedTokenInfo",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "adminTerminusAddress",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "adminTerminusPoolID",
        "type": "uint256"
      }
    ],
    "name": "init",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "numSessions",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "staker",
        "type": "address"
      }
    ],
    "name": "numTokensStakedIntoSession",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "uint256[]",
        "name": "",
        "type": "uint256[]"
      },
      {
        "internalType": "uint256[]",
        "name": "",
        "type": "uint256[]"
      },
      {
        "internalType": "bytes",
        "name": "",
        "type": "bytes"
      }
    ],
    "name": "onERC1155BatchReceived",
    "outputs": [
      {
        "internalType": "bytes4",
        "name": "",
        "type": "bytes4"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "bytes",
        "name": "",
        "type": "bytes"
      }
    ],
    "name": "onERC1155Received",
    "outputs": [
      {
        "internalType": "bytes4",
        "name": "",
        "type": "bytes4"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "bytes",
        "name": "",
        "type": "bytes"
      }
    ],
    "name": "onERC721Received",
    "outputs": [
      {
        "internalType": "bytes4",
        "name": "",
        "type": "bytes4"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "stage",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "path",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "setIsChoosingActive",
        "type": "bool"
      }
    ],
    "name": "setCorrectPathForStage",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "isActive",
        "type": "bool"
      }
    ],
    "name": "setSessionActive",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "bool",
        "name": "isChoosingActive",
        "type": "bool"
      }
    ],
    "name": "setSessionChoosingActive",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "string",
        "name": "uri",
        "type": "string"
      }
    ],
    "name": "setSessionUri",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "uint256[]",
        "name": "stages",
        "type": "uint256[]"
      },
      {
        "internalType": "address[]",
        "name": "terminusAddresses",
        "type": "address[]"
      },
      {
        "internalType": "uint256[]",
        "name": "terminusPoolIds",
        "type": "uint256[]"
      },
      {
        "internalType": "uint256[]",
        "name": "rewardAmounts",
        "type": "uint256[]"
      }
    ],
    "name": "setStageRewards",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "uint256[]",
        "name": "tokenIds",
        "type": "uint256[]"
      }
    ],
    "name": "stakeTokensIntoSession",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes4",
        "name": "interfaceId",
        "type": "bytes4"
      }
    ],
    "name": "supportsInterface",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "staker",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "index",
        "type": "uint256"
      }
    ],
    "name": "tokenOfStakerInSessionByIndex",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "sessionId",
        "type": "uint256"
      },
      {
        "internalType": "uint256[]",
        "name": "tokenIds",
        "type": "uint256[]"
      }
    ],
    "name": "unstakeTokensFromSession",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
```
