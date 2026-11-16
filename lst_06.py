
stocks = [
    ("TCS", 3500, 4.5),
    ("INFY", 1450, 2.5),
    ("WIPRO", 450, -1.5),
    ("HDFC", 1700, 3.8),
    ("ITC", 420, 1.2)
]

print("1. Change greater than 3%")
print("2. Price less than 500")

choice = int(input("Enter choice: "))

if choice == 1:
    rule = lambda x: x[2] > 3
    message = "Stocks with change above 3%"

elif choice == 2:
    rule = lambda x: x[1] < 500
    message = "Stocks with price below 500"

else:
    rule = None

if rule:
    result = list(filter(rule, stocks))

    print("\n", message)

    prices = list(map(
        lambda x: f"₹{x[1]:.2f}", result
    ))

    for stock, price in zip(result, prices):
        print(stock[0], price, stock[2], "%")
else:
    print("Invalid choice!")
