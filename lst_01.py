
# College Attendance Tracker

students = ["Amit", "Rahul", "Priya", "Sneha", "Akash"]

attendance = []

lectures = int(input("Enter number of lectures: "))

# Mark attendance
for i in range(lectures):
    print("\nLecture", i + 1)
    lecture = []

    for student in students:
        status = input("Enter attendance for " + student + " (P/A): ").upper()

        while status not in ["P", "A"]:
            print("Invalid input! Enter P or A.")
            status = input("Enter attendance for " + student + ": ").upper()

        lecture.append(status)

    attendance.append(lecture)

# Calculate attendance percentage
report = []

for i in range(len(students)):
    present = 0

    for lecture in attendance:
        if lecture[i] == "P":
            present += 1

    percentage = (present / lectures) * 100
    report.append([students[i], present, percentage])

# Display attendance sheet
print("\n------ ATTENDANCE SHEET ------")
print("Name\tPresent\tPercentage")

for record in report:
    print(record[0], "\t", record[1], "\t", record[2], "%")

# Find defaulters below 75%
defaulters = []

for record in report:
    if record[2] < 75:
        defaulters.append(record)

# Sort defaulters by percentage
defaulters.sort(key=lambda x: x[2])

print("\n------ DEFAULTER LIST ------")

for record in defaulters:
    print(record[0], "-", record[2], "%")

if len(defaulters) == 0:
    print("No defaulters found.")

# Save report in text file
with open("attendance_report.txt", "w") as file:
    file.write("COLLEGE ATTENDANCE REPORT\n")
    file.write("-------------------------\n")

    for record in report:
        file.write(
            f"{record[0]} - Present: {record[1]}, "
            f"Percentage: {record[2]:.2f}%\n"
        )

    file.write("\nDEFAULTER LIST (Below 75%)\n")

    for record in defaulters:
        file.write(f"{record[0]} - {record[2]:.2f}%\n")

print("\nReport saved successfully!")
