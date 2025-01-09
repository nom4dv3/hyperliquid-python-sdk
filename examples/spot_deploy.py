from hyperliquid.utils import constants
from hyperliquid.utils.signing import (
    sign_l1_action,
    get_timestamp_ms,
)
import example_utils

TOKEN_ID = 177
IS_MAINNET = True

def main():
    
    _, _, exchange = example_utils.setup(constants.MAINNET_API_URL if IS_MAINNET else constants.TESTNET_API_URL, skip_ws=True)

    # pick a noce
    nonce = get_timestamp_ms()
    
    # action json
    action = {
        "type": "spotDeploy",
        "userGenesis":{
            "token": TOKEN_ID,
            # note: address should use lowercase, uppercase would cause signature error.
            "userAndWei": [["0x553e545d85e2afb67c8b5223f51fe97e7dde8b74","3299999300000000"]],
            "existingTokenAndWei": []
        }
    }

    # sign
    signature = sign_l1_action(exchange.wallet, action, None, nonce, IS_MAINNET)

    # post
    response = exchange._post_action(action, signature, nonce)

    print(response)

if __name__ == "__main__":
    main()