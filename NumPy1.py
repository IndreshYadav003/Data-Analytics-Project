import numpy as np

transaction_id = np.arange(1, 21)
# create data set
product = np.array([
    "Laptop", "Mobile", "Tablet", "Laptop", "Headphones",
    "Mobile", "Tablet", "Laptop", "Headphones", "Mobile",
    "Laptop", "Tablet", "Mobile", "Headphones", "Laptop",
    "Mobile", "Tablet", "Laptop", "Headphones", "Mobile"
])

region = np.array([
    "North", "South", "East", "West", "North",
    "South", "East", "West", "North", "South",
    "East", "West", "North", "South", "East",
    "West", "North", "South", "East", "West"
])

quantity = np.array([
    2, 3, 1, 2, 5,
    4, 2, 1, 6, 3,
    2, 3, 5, 4, 1,
    3, 2, 2, 5, 4
])

price = np.array([
    60000, 25000, 30000, 60000, 2000,
    25000, 30000, 60000, 2000, 25000,
    60000, 30000, 25000, 2000, 60000,
    25000, 30000, 60000, 2000, 25000
])

cost = np.array([
    50000, 20000, 24000, 50000, 1400,
    20000, 24000, 50000, 1400, 20000,
    50000, 24000, 20000, 1400, 50000,
    20000, 24000, 50000, 1400, 20000
])
# Calculations

revenue = quantity * price
total_cost = quantity * cost
profit = revenue - total_cost

print("\n===== RETAIL SALES ANALYTICS =====")

print("Total Revenue:", np.sum(revenue))
print("Total Cost:", np.sum(total_cost))
print("Total Profit:", np.sum(profit))

print("Average Revenue:", np.mean(revenue))
print("Median Revenue:", np.median(revenue))

print("Highest Revenue:", np.max(revenue))
print("Lowest Revenue:", np.min(revenue))

print("Average Profit:", np.mean(profit))
print("Revenue Std:", np.std(revenue))

# Product Analy

print("\n===== PRODUCT ANALYSIS =====")

products = np.unique(product)

for p in products:

    mask = product == p

    print(
        p,
        "| Revenue:", np.sum(revenue[mask]),
        "| Profit:", np.sum(profit[mask]),
        "| Units:", np.sum(quantity[mask])
    )
# Region Analysis

print("\n===== REGION ANALYSIS =====")

regions = np.unique(region)

for r in regions:

    mask = region == r

    print(
        r,
        "| Revenue:", np.sum(revenue[mask]),
        "| Profit:", np.sum(profit[mask])
    )

# Top 5 Transaction
print("\n===== TOP 5 TRANSACTIONS =====")

top5 = np.argsort(revenue)[-5:][::-1]

for i in top5:

    print(
        "ID:", transaction_id[i],
        "| Product:", product[i],
        "| Revenue:", revenue[i],
        "| Profit:", profit[i]
    )

# High Revenue Transactions

print("\n===== ABOVE AVERAGE SALES =====")

average_revenue = np.mean(revenue)

mask = revenue > average_revenue

print(transaction_id[mask])


# Profit Margin


profit_margin = (profit / revenue) * 100

print("\nAverage Profit Margin:",np.mean(profit_margin))
'''
==== RETAIL SALES ANALYTICS =====
Total Revenue: 1430000
Total Cost: 1160000
Total Profit: 270000
Average Revenue: 71500.0
Median Revenue: 75000.0
Highest Revenue: 125000
Lowest Revenue: 8000
Average Profit: 13500.0
Revenue Std: 39788.81752452566

===== PRODUCT ANALYSIS =====
Headphones | Revenue: 40000 | Profit: 12000 | Units: 20
Laptop | Revenue: 600000 | Profit: 100000 | Units: 10
Mobile | Revenue: 550000 | Profit: 110000 | Units: 22
Tablet | Revenue: 240000 | Profit: 48000 | Units: 8

===== REGION ANALYSIS =====
East | Revenue: 280000 | Profit: 51000
North | Revenue: 327000 | Profit: 63600
South | Revenue: 378000 | Profit: 72400
West | Revenue: 445000 | Profit: 83000

===== TOP 5 TRANSACTIONS =====
ID: 13 | Product: Mobile | Revenue: 125000 | Profit: 25000
ID: 18 | Product: Laptop | Revenue: 120000 | Profit: 20000
ID: 11 | Product: Laptop | Revenue: 120000 | Profit: 20000
ID: 4 | Product: Laptop | Revenue: 120000 | Profit: 20000
ID: 1 | Product: Laptop | Revenue: 120000 | Profit: 20000

===== ABOVE AVERAGE SALES =====
[ 1  2  4  6 10 11 12 13 16 18 20]

Average Profit Margin: 21.0

'''
