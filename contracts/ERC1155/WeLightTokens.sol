import "./ERC1155.sol";

contract WeLightTokens is ERC1155 {
    address public governance;
    uint256 public airlineCount;

    modifier onlyGovernance() {
        require(msg.sender == governance, "only governance can call this");

        _;
    }

    constructor(string memory uri,address governance_) public ERC1155(uri) {
        governance = governance_;
        airlineCount = 0;
    }

    function addNewTokens(uint256 initialSupply, uint256 tokenID) external onlyGovernance {
        airlineCount ++;
        _mint(msg.sender, tokenID, initialSupply, "");
    }
}
