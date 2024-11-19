from web3 import Web3

# Ethereum network via Infura
infura_url = "https://mainnet.infura.io/v3/a3e5ff12850046cca277cb9c655ee4ea"
web3 = Web3(Web3.HTTPProvider(infura_url))

def check_node_health():
    """
    Check if the node is connected to the Ethereum network.
    """
    try:
        # Attempt to retrieve the current block number
        block_number = web3.eth.block_number  # add own block number
        print("Node is connected to the Ethereum network.")
        print(f"Current Block Number: {block_number}")
    except Exception as e:
        print("Node is not connected.")
        print(f"Error: {e}")

def get_latest_block_info():
    """
    Get details about the latest block on the blockchain.
    """
    latest_block = web3.eth.get_block('latest')
    print(f"Latest Block Number: {latest_block['number']}")
    print(f"Block Hash: {latest_block['hash'].hex()}")
    print(f"Block Timestamp: {latest_block['timestamp']}")
    print(f"Number of Transactions in Block: {len(latest_block['transactions'])}")

def get_block_transactions(block_number):
    """
    Get the transactions from a specific block.
    """
    block = web3.eth.get_block(block_number, full_transactions=True)
    print(f"Transactions in Block {block_number}:")
    for tx in block.transactions:
        print(f"  Transaction Data: {tx}")  # Debugging line
        print(f"  Tx Hash: {tx['hash'].hex()}")
        print(f"  From: {tx['from']}")
        print(f"  To: {tx['to']}")
        try:
            value_in_ether = Web3.fromWei(tx['value'], 'ether')
            print(f"  Value: {value_in_ether} ETH")  # value of ether
        except Exception as e:
            print(f"  Value conversion error: {e}")
        try:
            gas_price_in_gwei = Web3.fromWei(tx['gasPrice'], 'gwei')
            print(f"  Gas Price: {gas_price_in_gwei} Gwei")  # gas price
        except Exception as e:
            print(f"  Gas Price conversion error: {e}")
        print(f"  ----------------------------")


def monitor_transaction_flow():
    """
    Monitor the flow of transactions by checking the latest block periodically.
    """
    latest_block_number = web3.eth.block_number  # block number
    print(f"Monitoring transactions from block {latest_block_number} onwards...")
    
    while True:
        current_block_number = web3.eth.block_number  # block number
        if current_block_number > latest_block_number:
            print(f"New Block Detected: {current_block_number}")
            get_block_transactions(current_block_number)
            latest_block_number = current_block_number

# Main function to run the scanner
def run_blockchain_scanner():
    print("Running Blockchain Network Scanner...")
    
    # Check the health of the Ethereum node
    check_node_health()
    
    # Get information about the latest block
    get_latest_block_info()
    
    # Monitor the flow of transactions in real-time
    monitor_transaction_flow()

# Run the scanner
if __name__ == "__main__":
    run_blockchain_scanner()
