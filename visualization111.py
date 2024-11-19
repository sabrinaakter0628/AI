  # Set a non-GUI backend
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas as pd

# Initialize data
average_price = 600  # Average price of the smartphone
stock_threshold = 10  # Critical stock level
discount_threshold = 0.20  # 20% discount threshold
minimum_order = 10  # Minimum quantity to order
additional_order = 15  # Quantity to order if not critical

# Function to determine order quantity
def decide_order(current_price, stock_level):
    discount_price = average_price * (1 - discount_threshold)
    tobuy = 0

    if stock_level < stock_threshold:  # Critical stock level
        tobuy = minimum_order
    elif current_price < discount_price:  # Price below threshold
        tobuy = additional_order

    return tobuy

# Simulation Data
prices = [600, 550, 500, 580, 490, 620, 560]  # Example prices
stock_levels = [15, 12, 9, 8, 25, 18, 10]  # Example stock levels
orders = []

# Process and log decisions
for price, stock in zip(prices, stock_levels):
    order = decide_order(price, stock)
    orders.append(order)
    print(f"Price: {price}, Stock: {stock}, Order Quantity: {order}")

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(prices, label="Prices", marker='o')
plt.plot(stock_levels, label="Stock Levels", marker='x')
plt.plot(orders, label="Orders", marker='s')
plt.axhline(y=average_price * (1 - discount_threshold), color='red', linestyle='--', label="Discount Threshold")
plt.axhline(y=stock_threshold, color='orange', linestyle='--', label="Stock Threshold")
plt.xlabel("Time Step")
plt.ylabel("Values")
plt.title("Trading Agent Decision Visualization")
plt.legend()
plt.grid()
plt.show()
