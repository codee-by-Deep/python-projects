import requests

api_key = "bf0b0c0315d17f0c94d99946"
url = f"https://v6.exchangerate-api.com/v6/bf0b0c0315d17f0c94d99946/latest/USD"

respond = requests.get(url)
data = respond.json()
currency = input("enter the currency: ").upper()
print(data['conversion_rates'][currency])

rates = data["conversion_rates"]
print(rates)