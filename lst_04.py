
students = [
    ["Amit", 8.5, 90],
    ["Rahul", 9.2, 85],
    ["Priya", 9.2, 95],
    ["Sneha", 8.8, 90],
    ["Akash", 7.9, 80]
]

sorting = {
    1: lambda x: (-x[1], -x[2], x[0]),
    2: lambda x: (-x[2], x[0]),
    3: lambda x: x[0]
}

print("1. Rank by CGPA")
print("2. Rank by Attendance")
print("3. Rank by Name")

choice = int(input("Enter choice: "))

if choice in sorting:
    result = sorted(students, key=sorting[choice])

    print("\nSTUDENT RANKING")

    for i, student in enumerate(result, start=1):
        print(i, student)
else:
    print("Invalid choice!")
