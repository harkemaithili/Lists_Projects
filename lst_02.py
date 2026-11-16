
cart = []

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Update Quantity")
    print("4. View Cart")
    print("5. Generate Bill")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        cart.append([item, qty, price])
        print("Item added!")

    elif choice == 2:
        item = input("Enter item name: ")

        for product in cart:
            if product[0].lower() == item.lower():
                cart.remove(product)
                print("Item removed!")
                break
        else:
            print("Item not found!")

    elif choice == 3:
        item = input("Enter item name: ")

        for product in cart:
            if product[0].lower() == item.lower():
                product[1] = int(input("Enter new quantity: "))
                print("Quantity updated!")
                break
        else:
            print("Item not found!")

    elif choice == 4:
        print("\nSHOPPING CART")

        for product in cart:
            print(product)

    elif choice == 5:
        subtotal = sum(p[1] * p[2] for p in cart)
        discount = subtotal * 0.10 if subtotal >= 1000 else 0
        total = subtotal - discount

        print("\n----- INVOICE -----")

        for p in cart:
            print(p[0], p[1], "x", p[2],
                  "=", p[1] * p[2])

        print("Subtotal:", subtotal)
        print("Discount:", discount)
        print("Grand Total:", total)

        expensive = sorted(
            cart, key=lambda x: x[2], reverse=True
        )

        print("\nTop 3 Expensive Items:")

        for p in expensive[:3]:
            print(p)

    elif choice == 6:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice!")
