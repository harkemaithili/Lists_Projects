
queue = []
token = 1
consultation_time = 10

while True:
    print("\n1. Register Patient")
    print("2. Emergency Patient")
    print("3. Serve Patient")
    print("4. Cancel Token")
    print("5. Display Queue")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter patient name: ")
        queue.append([token, name])
        print("Token Number:", token)
        token += 1

    elif choice == 2:
        name = input("Enter emergency patient name: ")
        queue.insert(0, [token, name])
        print("Emergency Token:", token)
        token += 1

    elif choice == 3:
        if queue:
            patient = queue.pop(0)
            print("Serving:", patient[1])
        else:
            print("No patients in queue!")

    elif choice == 4:
        t = int(input("Enter token number: "))

        for patient in queue:
            if patient[0] == t:
                queue.remove(patient)
                print("Token cancelled!")
                break
        else:
            print("Token not found!")

    elif choice == 5:
        print("\nCURRENT QUEUE")
        print("Queue Length:", len(queue))

        for position, patient in enumerate(queue, start=1):
            wait = (position - 1) * consultation_time
            print("Token:", patient[0],
                  "Name:", patient[1],
                  "Wait:", wait, "minutes")

    elif choice == 6:
        break

    else:
        print("Invalid choice!")
