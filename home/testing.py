import requests

# Define the API URL and key
url = "https://api.currencyapi.com/v3/latest"
api_key = "cur_live_1Pb7XsPrsYyevJqA5RoiB6yUHX0Q3zrr1ANSSaA3"

# Make the GET request
response = requests.get(url, params={"apikey": api_key})

# Check the response status
if response.status_code == 200:
    data = response.json()  # Parse the response as JSON
    print("Exchange Rates:", data)
else:
    print("Error:", response.status_code, response.text)
