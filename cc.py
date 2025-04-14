"""
This program is capable of converting from one currency to another as of today itself.
It uses the free API at exchangerate-api.com to get current exchange rates.
"""

import requests
import json
import sys
from pprint import pprint

# Free API endpoint for currency exchange rates
url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    response = requests.get(url)
    data = response.json()
    fx = data["rates"]
except:
    print("Failed to fetch exchange rates. Please check your internet connection.")
    sys.exit(1)

currencies = [
    "USD : US Dollar,United States Dollar",
    "EUR : Euro,Euro Member Countries",
    "GBP : British Pound,United Kingdom Pound",
    "JPY : Japanese Yen,Japan Yen",
    "CHF : Swiss Franc,Switzerland Franc",
    "CAD : Canadian Dollar,Canada Dollar",
    "AUD : Australian Dollar,Australia Dollar"
]

def validate_input(data):
    if not data:
        return False, "Пустое значение"
    if len(data) != 16:  # Для примера, проверка длины номера карты
        return False, "Неверная длина"
    if not data.isdigit():
        return False, "Ввод должен содержать только цифры"
    return True, "Ввод корректен"


def convert_currency():
    while True:
        query = input(
            "Please specify: amount from_currency to_currency (with spaces)\n"
            "Or type SHOW to list currencies, Q to quit: "
        ).strip().upper()
        
        if query == "Q":
            sys.exit()
        elif query == "SHOW":
            pprint(currencies)
            continue
        
        try:
            parts = query.split()
            if len(parts) != 3:
                raise ValueError("Invalid input format")
                
            qty, from_curr, to_curr = parts
            qty = float(qty)
            
            if from_curr not in fx or to_curr not in fx:
                raise ValueError("Invalid currency code")
                
            # Convert from USD equivalent rates
            amount = round(qty * (fx[to_curr] / fx[from_curr]), 2)
            print(f"\n{qty} {from_curr} = {amount} {to_curr}\n")
            
        except ValueError as e:
            print(f"\nError: {e}. Please try again.\n")
        except Exception as e:
            print(f"\nAn error occurred: {e}. Please try again.\n")

if __name__ == "__main__":
    print("\nCurrency Converter")
    print("------------------\n")
    convert_currency()