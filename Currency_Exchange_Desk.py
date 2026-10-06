# TASK 9 — Currency Exchange Desk

exchange_rate = 150

usd_amount = float(input("Enter USD amount: "))

etb_amount = usd_amount * exchange_rate

print("\n==============================")
print("       CURRENCY EXCHANGE")
print("==============================")

print(f"\nUSD Amount: {usd_amount:.2f} USD")
print(f"\nExchange Rate: 1 USD = {exchange_rate} ETB")
print(f"\nETB Amount: {etb_amount:,.2f} ETB")

print("==============================")