# how-to-get-market-cap-from-Coin-Market-Cap-CMC-API

A Python script that retrieves cryptocurrency market capitalization data from the CoinMarketCap Pro API. It uses an environment variable for the API key, includes full debug-level logging, and provides an async-friendly entrypoint.

## Features

* Load `CMC_API_KEY` from a `.env` file
* Fetch USD market capitalization for any symbol via CoinMarketCap Pro API
* Detailed debug logging for HTTP, third-party libraries, and application code
* Async entrypoint for seamless integration in workflows

## Prerequisites

* Python 3.8 or newer
* Internet access
* A CoinMarketCap Pro API key (free tiers available)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/how-to-get-market-cap-from-Coin-Market-Cap-CMC-API.git
   cd how-to-get-market-cap-from-Coin-Market-Cap-CMC-API
   ```

2. **Create and activate a virtual environment (recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

> **requirements.txt** should contain:
>
> ```text
> python-dotenv>=0.19.0
> requests>=2.25.0
> telethon>=1.24.0        # optional, for Telegram integration if extended
> ```

## Configuration

1. Copy the sample environment file and add your API key:

   ```bash
   cp config.env.example config.env
   ```
2. Edit `config.env` and set:

   ```dotenv
   CMC_API_KEY=YOUR_COINMARKETCAP_API_KEY
   ```

## Usage

Import and run the async entrypoint in your Python code:

```python
import asyncio
from marketcap_retriever import marketcap_retrieve_operations

async def main():
    # Provide ticker as "<SYMBOL>_tag", e.g. "BTC_demo"
    await marketcap_retrieve_operations("ETH_demo")

if __name__ == "__main__":
    asyncio.run(main())
```

**Output**

* The script logs the market cap in USD:

  ```
  INFO:__main__:Market cap of ETH from CoinMarketCap: 183456789012.34 USD
  ```

## Configuration Details

* **Logging Level**: set to `DEBUG` by default in `logging.basicConfig(level=logging.DEBUG)`.
* **HTTP Debug**: enabled via `http.client.HTTPConnection.debuglevel = 1`.
* **Library Debug**: `requests`, `urllib3`, and `telethon` log at `DEBUG` level.

## Function Reference

| Function                                | Description                                                      |
| --------------------------------------- | ---------------------------------------------------------------- |
| `get_market_cap_from_cmc(symbol)`       | Synchronously fetches USD market cap for `symbol` from CMC API.  |
| `marketcap_retrieve_operations(ticker)` | Async entrypoint: parses ticker, calls CMC, and logs the result. |

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to your branch: `git push origin feature/my-feature`
5. Open a Pull Request

Please follow PEP 8 guidelines and include tests for new functionality.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
