
from functools import reduce

employees = [
    ["Amit", 30000, "ABCDE1234F"],
    ["Rahul", 40000, "FGHIJ5678K"],
    ["Priya", 25000, "KLMNO1234P"],
    ["Sneha", 50000, "PQRST5678A"]
]

gross = list(map(
    lambda e: e[1] + e[1] * 0.20 + e[1] * 0.10,
    employees
))

bonus = list(filter(
    lambda e: e[1] >= 30000, employees
))

net = list(map(
    lambda salary: salary - salary * 0.05,
    gross
))

total = reduce(lambda a, b: a + b, net)

print("----- PAYROLL REGISTER -----")

for emp, salary in zip(employees, net):
    print(emp[0], "Net Salary:", salary)

print("\nBonus Eligible Employees:")

for emp in bonus:
    print(emp[0])

print("Total Salary Outflow:", total)

print("Any salary above 50000:",
      any(s > 50000 for s in gross))

print("All PAN numbers valid:",
      all(len(e[2]) == 10 for e in employees))
