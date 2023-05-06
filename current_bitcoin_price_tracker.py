import requests

# Define the API URL for Bitcoin price in INR
url = "https://api.coindesk.com/v1/bpi/currentprice/INR.json"

# Send an HTTP GET request to the API URL
response = requests.get(url)

# Parse the JSON response to a Python dictionary
data = response.json()

# Extract the current Bitcoin price in INR from the dictionary
price_inr = data["bpi"]["INR"]["rate_float"]

# Print the current Bitcoin price in INR
print("Current Bitcoin price in INR:", price_inr)


