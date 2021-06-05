// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.8.0;

import "./ERC20.sol";

contract ERC20Creator is ERC20 {
    address public governance;
    

    modifier onlyGovernance() {
        require(msg.sender == governance, "only governance can call this");
        _;
    }

    constructor(string memory name_, string memory symbol_, uint8 decimals_, address governance_) public ERC20(name_, symbol_, decimals_) {
        governance = governance_;
    }
    
    function mint(uint256 amount) external onlyGovernance {
          _mint(msg.sender, amount);
    }
}