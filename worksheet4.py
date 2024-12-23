def currency_converter(amount, from_currency, to_currency):
    
    conversion_rate = {
    'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
    'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
    'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
    'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }


    if from_currency in conversion_rate and to_currency in conversion_rate[from_currency]:
        rate = conversion_rate[from_currency][to_currency]
        converted_amount = amount * rate
        return round(converted_amount, 2)
    else:
        return 0.0