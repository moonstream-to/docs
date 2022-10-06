---
tags:
  - alpha
  - api
  - data
  - economics
---

# Leaderboards

Moonstream Leaderboards allow you to create player rankings based on both on-chain and off-chain activity.
You can use [Dropper](./dropper.md) to reward your players for attaining a high rank on a leaderboard.

This combination of Leaderboards and Dropper make it easy to improve the health of your game and your
economy by incentivizing players to engage in entertaining and productive activities.

## Example: Crypto Unicorns Summer of Love

In the Summer of 2022, [Crypto Unicorns](https://cryptounicorns.fun) created a leaderboard
tracking the breeding, hatching, and evolution of Unicorn NFTs. The event was a 3-month long event
powered by Moonstream Leaderboards:

![Crypto Unicorns Summer of Love leaderboard](./cu-leaderboard.png)

Each of the listed rewards is a [Terminus](../terminus.md) token, distributed via the [Dropper](./dropper.md)
contract.

The Summer of Love event led to an almost 100% increase in the number of active unicorns in the game.

## Workflow

### Creating and updating a leaderboard

Leaderboards are currently in **closed alpha**. If you would like to use our leaderboards
in your game, message `#moonstream` on [Moonstream Discord](https://discord.gg/w7wrqrAswq).

This is still an alpha feature because it takes some amount of custom work to populate a leaderboard
with data. For each of our customers using leaderboards, the Moonstream team maintains crawlers which
calculate player scores and update through the API.

For example: [The Crypto Unicorns Summer of Love Leaderboard crawler](https://github.com/bugout-dev/autocorns/blob/cf00fb492de254821730a256d238d5a332810db6/season-of-breeding.bash).

One of the items on our roadmap is to make it easy for game developers to build their own crawlers using
our Query API, and to host these crawlers on our infrastructure. At that point, it will make sense to open
Moonstream Leaderboards to the public. In the mean time, we are happy to work with any team that does want leaderboards for their game. It will just take some custom work. If you are interested, reach out and talk
to us on our [Discord](https://discord.gg/w7wrqrAswq).

You can track our progress towards the public beta of Leaderboards on the
[Leaderboard Beta Release milestone on GitHub](https://github.com/bugout-dev/engine/milestone/6).

### Viewing a leaderboard

Integrating a leaderboard into a web frontend or game client is very simple. You can use the Leaderboard
REST API to do this.

Link: [Live Leaderboard API docs](https://engineapi.moonstream.to/leaderboard/docs)

## Implementation

You can view the API implementation of leaderboards in our `engine` repository. The natural entrypoint
is our implementation of the
[`/leaderboard`](https://github.com/bugout-dev/engine/blob/87486652770b11ea146b49a6d3a2934d3384876b/api/engineapi/routes/leaderboard.py)
route.
