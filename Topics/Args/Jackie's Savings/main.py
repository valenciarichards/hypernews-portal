def final_deposit_amount(*monthly_rates, amount=1000):
    final_amount = amount
    for monthly_rate in monthly_rates:
        interest = final_amount * monthly_rate / 100
        final_amount += interest
    return round(final_amount, 2)
