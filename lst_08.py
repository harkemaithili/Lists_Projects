
from functools import reduce

branch1 = [10000, 12000, 15000, 8000]
branch2 = [15000, 10000, 12000, 9000]
branch3 = [12000, 14000, 10000, 11000]

branches = {
    "Branch 1": branch1,
    "Branch 2": branch2,
    "Branch 3": branch3
}

# Day-wise total
daily = list(map(
    lambda x: sum(x),
    zip(branch1, branch2, branch3)
))

print("DAY-WISE SALES REPORT")

for day, amount in enumerate(daily, start=1):
    print("Day", day, ":", amount)

# Convert to lakhs
lakhs = list(map(lambda x: x / 100000, daily))

print("\nSales in Lakhs:", lakhs)

# Monthly total
monthly = reduce(lambda a, b: a + b, daily)

print("Monthly Total:", monthly)

# Maximum daily sale
maximum = reduce(lambda a, b: max(a, b), daily)

print("Maximum Daily Sale:", maximum)

# Days below target
below = list(filter(lambda x: x < 30000, daily))

print("Sales Below Target:", below)

# Branch ranking
ranking = sorted(
    branches.items(),
    key=lambda x: sum(x[1]),
    reverse=True
)

print("\nBRANCH RANKING")

for i, branch in enumerate(ranking, start=1):
    print(i, branch[0], sum(branch[1]))
