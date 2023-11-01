---
tags:
  - tooling
---



# NFT Inventory

This implements a fully on-chain inventory system for ERC721 tokens. It allows ERC721 contracts to treat the blockchain as the source of truth about the state of each token.

Administrators can define the inventory slots that an NFT collection (ERC721 contract) admits. They can specify which items (ERC20 tokens, ERC721 tokens, ERC1155 tokens) are equippable in each slot.

NFT owners can equip and unequip valid items from each slot.

Games can use the items equipped in a character's inventory to determine their abilities in-game.

<table>
  <tr>
    <th>Contract name</th>
    <th>Immutable or Upgradable</th>
    <th>Deployment</th>
    <th>CLI</th>
    <th>Solidity interface</th>
    <th>ABI</th>
  </tr>
  <tr>
    <td><a href="./contracts/inventory/InventoryFacet.sol"><pre>InventoryFacet</pre></a></td>
    <td>Upgradable</td>
    <td><pre>web3cli core inventory-gogogo</pre></td>
    <td><pre>web3cli inventory</pre></td>
    <td><pre>n/a</pre></td>
    <td><a href="./abi/InventoryFacet.json"><pre>abi/InventoryFacet.json</pre></a></td>
  </tr>
</table>


[Here](https://blog.moonstream.to/2023/09/06/nft-inventory-vs-tokenbound-accounts/) is a comparison between ERC-6551 (Tokenbound) and NFT Inventory.

💡***Note***: This technology is being developed in collaboration with Game7 DAO and Summon. [Here](https://github.com/mmoeip/inventory) is a GitHub repository with more details.

