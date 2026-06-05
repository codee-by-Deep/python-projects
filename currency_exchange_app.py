import requests

def currency_conversion():
    api_key = "bf0b0c0315d17f0c94d99946"
    url = f"https://v6.exchangerate-api.com/v6/bf0b0c0315d17f0c94d99946/latest/USD"

    respond = requests.get(url)
    data = respond.json()

    amount = float(input("Enter the amount: "))
    from_currency = input("Converting currency from (AUD,USD,INR): ").upper()
    to_currency = input("Converting currency to (AUD,USD,INR): ").upper()

    rates = data["conversion_rates"]

    result = round((amount / rates[from_currency] ) * rates[to_currency],2) 

    print(amount, from_currency,"=",result, to_currency)

while True:
    currency_conversion()
    again = input("Do you want to convert currency (y/n): ")
    if again == "n":
        break