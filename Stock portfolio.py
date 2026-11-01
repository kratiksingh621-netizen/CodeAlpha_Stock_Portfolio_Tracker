# CodeAlpha - Task 2: Stock Portfolio Tracker
# Created by Kratik Singh

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 380,
    "AMZN": 150
}

portfolio = {}
total_value = 0

print("=== Stock Portfolio Tracker ===")
print("Available Stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (e.g., AAPL) or type 'done' to finish: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print(f"{stock} not available. Choose from {list(stock_prices.keys())}")
        continue
    quantity = int(input(f"Enter quantity for {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n--- Your Portfolio ---")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock}: {qty} x ${stock_prices[stock]} = ${value}")

print(f"\nTotal Portfolio Value: ${total_value}")
