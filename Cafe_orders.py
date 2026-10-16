"""
Debugging Exercise 2: Cafe Orders
Each order is stored as text in the form "item,price".
This program is supposed to:
  1. Add up the total cost of all orders.
  2. Find the most expensive item.
Run it and check the results by hand. Is everything correct?
"""

orders = [
    "coffee,4.50",
    "sandwich,12.75",
    "muffin,3.25",
    "salad,9.95",
    "smoothie,7.00" ]
total = 0
most_expensive_item, highest_price = orders[0].split(",")

for order in orders:
    item, price = order.split(",")
    total += float(price)
    if float(price) > float(highest_price):
        highest_price = price
        most_expensive_item = item
print("Number of orders:", len(orders))
print("Total cost: $" + format(total, ".2f"))
print("Most expensive item:", most_expensive_item, "($" + highest_price + ")")
