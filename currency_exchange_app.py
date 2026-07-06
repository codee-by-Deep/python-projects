import requests

def currency_conversion():
    api_key = "your_api_key_here"  # placeholder
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

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