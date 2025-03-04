import os
import logging
import http.client
import re
import time
from decimal import Decimal as D
from datetime import datetime
from decimal import ROUND_DOWN  # Import rounding mode
from dotenv import load_dotenv
import requests
import asyncio

# ----- Enable Full Debugging -----
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Increase debugging for third-party libraries
logging.getLogger("telethon").setLevel(logging.DEBUG)
logging.getLogger("requests").setLevel(logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.DEBUG)
http.client.HTTPConnection.debuglevel = 1
# ---------------------------------

# Load environment variables
load_dotenv('config.env')

# Log loaded environment variables (be cautious with sensitive info)
logger.debug(f"CMC_API_KEY is set: {bool(os.getenv('CMC_API_KEY'))}")

# CoinMarketCap API key
CMC_API_KEY = os.getenv('CMC_API_KEY')

# Function to get market cap from CoinMarketCap
def get_market_cap_from_cmc(symbol):
    logger.debug(f"Fetching market cap from CoinMarketCap for symbol: {symbol}")
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': CMC_API_KEY,
    }
    parameters = {'symbol': symbol, 'convert': 'USD'}
    try:
        response = requests.get(url, headers=headers, params=parameters)
        logger.debug(f"CoinMarketCap response status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            market_cap = data['data'][symbol]['quote']['USD']['market_cap']
            logger.debug(f"Market cap from CMC for {symbol}: {market_cap}")
            return market_cap
        else:
            logger.error(f"Error fetching market cap from CoinMarketCap: {response.text}")
            return None
    except Exception as e:
        logger.error(f"Exception fetching market cap from CoinMarketCap for {symbol}: {e}")
        return None


# Function to perform "market cap show" operations
async def marketcap_retrieve_operations(ticker):
    logger.debug(f"Entering marketcap_retrieve_operations with ticker: {ticker}")
    base_currency = ticker.split("_")[0]
    logger.debug(f"Base currency extracted: {base_currency}")

    # Get market cap from CoinMarketCap
    market_cap_cmc = get_market_cap_from_cmc(base_currency)
    if market_cap_cmc is not None:
        logger.info(f"Market cap of {base_currency} from CoinMarketCap: {market_cap_cmc} USD")
    else:
        logger.error(f"Failed to retrieve market cap from CoinMarketCap for {base_currency}")

