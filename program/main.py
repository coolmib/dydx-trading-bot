from func_connections import connect_dydx
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_private import abort_all_positions
from func_public import construct_market_prices


# MAIN FUNCTION
if __name__ == "__main__":
    # Connect to client
    try:
        print("Connecting to client....")
        client = connect_dydx()
    except Exception as e:
        print("Error connecting to client: ", e)
        exit(1)

    # Abort all open positions    
    if ABORT_ALL_POSITIONS:
        try:
            print("Closing all positions...") 
            close_orders = abort_all_positions(client)
        except Exception as e:
            print("Error Closing all Positions: ", e)
            exit(1)

    # Finf Cointegrated Pairs
    if FIND_COINTEGRATED:

        # Construct Market Prices
        try:
            print("Fetching Market Prices, please allow 3 mins...") 
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print("Error Fetching Market Prices: ", e)
            exit(1)