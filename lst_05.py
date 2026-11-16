
tax_rules = {
    "Food": lambda price: price * 0.05,
    "Clothes": lambda price: price * 0.12,
    "Electronics": lambda price: price * 0.18,
    "Luxury": lambda price: price * 0.28
}

coupons = {
    "SAVE10": lambda amount: amount * 0.10,
    "SAVE20": lambda amount: amount * 0.20,
    "NONE": lambda amount: 0
}

items = []

n = int(input("Enter number of items: "))

for i in range(n):
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    category = input("Enter category: ")

    if category in tax_rules:
        tax = tax_rules[category](price)
        items.append([name, price, tax])
    else:
        print("Invalid category!")

subtotal = sum(item[1] for item in items)
total_tax = sum(item[2] for item in items)

coupon = input("Enter coupon code: ").upper()

discount = coupons.get(
    coupon, lambda amount: 0
)(subtotal)

grand_total = subtotal + total_tax - discount

print("\n----- INVOICE -----")

for item in items:
    print(item[0], "Price:", item[1], "GST:", item[2])

print("Subtotal:", subtotal)
print("Total GST:", total_tax)
print("Discount:", discount)
print("Grand Total:", grand_total)
