import "./ERC1155.sol";

contract WeLightTokens is ERC1155 {
    address public governance;
    uint256 public tokenCount;
    address[] public addrList;
    
    // Mapping from contract addr to tokenID
    mapping(address => uint256) public erc721TokenID;
    

    modifier onlyGovernance() {
        require(msg.sender == governance, "only governance can call this");

        _;
    }

    constructor(string memory uri,address governance_) public ERC1155(uri) {
        governance = governance_;
        tokenCount = 0;
    }

    function addNewTokens(uint256 initialSupply, address erc721Addr, uint256 tokenID) external onlyGovernance {
        tokenCount ++;
        addrList.push(erc721Addr);
        erc721TokenID[erc721Addr] = tokenID;
        _mint(msg.sender, tokenID, initialSupply, "");
    }
    
    function getAddrList() public view returns (address[] memory){
        return addrList;
    }
    
    function getTokenList() public view returns (uint256[] memory){
        uint256[] memory payload = new uint256[](tokenCount);
        for(uint i=0; i<tokenCount; i++) {
            payload[i] = erc721TokenID[addrList[i]];
        }
        return payload;
    }
}
