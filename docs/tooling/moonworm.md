---
tags:
  - tooling
  - python
  - library
  - cli
---

# moonworm

[`moonworm`](https://github.com/bugout-dev/moonworm) is a code generation tool which makes it easy
for anyone to interact with smart contracts on an EVM-based blockchain.

It is inspired by [`abigen`](https://github.com/ethereum/go-ethereum/blob/468d1844c7a32b51eebce6c5f35c44a66b9acf64/cmd/abigen/main.go)
and generates Python bindings to smart contracts when it is provided their ABIs as inputs.

More importantly, `moonworm` also generates fully-featured command-line interfaces to those smart contracts,
which is extremely useful when running live operations against deployed contracts. It is also helpful
in creating bots that interact with deployed contracts.

`moonworm` is capable of generating Python bindings and CLIs which use any of the following libraries
to interact with EVM-based blockchains:

1. [`web3.py`](#generating-web3py-compatible-smart-contract-interfaces)

2. [`brownie`](#generating-brownie-compatible-smart-contract-interfaces)

Finally, `moonworm` also makes it easy to gather information about smart contracts and how people are
using them:

1. [`watch`](#crawling-events-and-method-calls-to-smart-contracts) - generates a crawler for a given contract at runtime

2. [`find_deployment`](#discovering-the-block-at-which-a-smart-contract-was-deployed) - uses a binary search to pin down the exact block at which
a smart contract was deployed


## Installation

Install [`moonworm`](https://pypi.org/project/moonworm/) using:

```
pip install moonworm
```

## Uses

### Generating brownie-compatible smart contract interfaces

::: moonworm.generators.brownie.generate_brownie_interface
    options:
      heading_level: 5
      show_root_heading: true
      show_root_toc_entry: true

#### CLI: `moonworm generate-brownie`

To access this functionality from the `moonworm` command-line interface, use the `moonworm generate-brownie` command:

```
moonworm generate-brownie --help
```


### Generating web3.py-compatible smart contract interfaces

::: moonworm.generators.basic
    options:
      heading_level: 4
      show_root_heading: false
      show_root_toc_entry: false
      members:
        - generate_contract_interface_content
        - generate_contract_cli_content

#### CLI: `moonworm generate`

To access this functionality from the `moonworm` command-line interface, use the `moonworm generate` command:

```
moonworm generate --help
```


### Crawling events and method calls to smart contracts

::: moonworm.watch.watch_contract
    options:
      heading_level: 5
      show_root_heading: true
      show_root_toc_entry: true

#### State providers: Accessing blockchain state

[`watch_contract`][moonworm.watch.watch_contract] uses [`EthereumStateProvider`][moonworm.crawler.ethereum_state_provider.EthereumStateProvider]
objects to crawl blockchain state. Any object inheriting from the `EthereumStateProvider` base class
will suffice.

::: moonworm.crawler.ethereum_state_provider.EthereumStateProvider
    options:
      members: []
      heading_level: 5
      show_root_heading: true
      show_root_full_path: false
      show_bases: false

For example:

::: moonworm.crawler.ethereum_state_provider.Web3StateProvider
    options:
      heading_level: 5
      show_root_heading: true
      show_root_full_path: false

#### CLI: `moonworm watch`

To access this functionality from the `moonworm` command-line interface, use the `moonworm watch` command:

```
moonworm watch --help
```


### Discovering the block at which a smart contract was deployed

::: moonworm.deployment.find_deployment_block
    options:
        heading_level: 5
        show_root_heading: true
        show_root_toc_entry: true

#### CLI: `moonworm find-deployment`

To access this functionality from the `moonworm` command-line interface, use the `moonworm find-deployment` command:

```
moonworm find-deployment --help
```
