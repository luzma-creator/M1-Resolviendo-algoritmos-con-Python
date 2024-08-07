import requests
def usd_to_cny(amount, api_key):
    """
    Convert USD to CNY using ExchangeRate-API.

    Parameters:
    amount (float): The amount in USD to be converted.
    api_key (str): Your API key for ExchangeRate-API.

    Returns:
    float: The equivalent amount in CNY.
    """
   #url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"#
    url = f"https://v6.exchangerate-api.com/v6/6ba9a69ce7c53bc2d2f9c716/latest/USD"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data['conversion_rates']['CNY']
        return amount * rate
    else:
        print("Error fetching exchange rate data")
        return None


# Example usage
api_key = "Gibran17"
usd_amount = 100
cny_amount = usd_to_cny(usd_amount, api_key)

if cny_amount is not None:
    print(f"{usd_amount} USD is equivalent to {cny_amount} CNY")
else:
    print("Conversion failed")