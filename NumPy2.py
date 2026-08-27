# ============================================================
# PROJECT: E-COMMERCE SALES ANALYTICS
# TECHNOLOGY: Python + NumPy
# LEVEL: B.Tech Final Year
# ============================================================

import numpy as np


# ============================================================
# 1. CREATE DATASET
# ============================================================
# We create a small e-commerce transaction dataset using
# NumPy arrays. Each index represents one order.
# ============================================================

# Generate order IDs from 1 to 30
order_id = np.arange(1, 31)

# Customer IDs
customer_id = np.array([
    "C101", "C102", "C103", "C104", "C105",
    "C106", "C107", "C108", "C109", "C110",
    "C101", "C102", "C103", "C104", "C105",
    "C106", "C107", "C108", "C109", "C110",
    "C101", "C102", "C103", "C104", "C105",
    "C106", "C107", "C108", "C109", "C110"
])

# Product purchased in each order
product = np.array([
    "Laptop", "Mobile", "Headphones", "Tablet", "Smartwatch",
    "Mobile", "Laptop", "Tablet", "Headphones", "Mobile",
    "Smartwatch", "Laptop", "Mobile", "Tablet", "Headphones",
    "Laptop", "Mobile", "Smartwatch", "Tablet", "Headphones",
    "Laptop", "Mobile", "Tablet", "Smartwatch", "Headphones",
    "Mobile", "Laptop", "Tablet", "Mobile", "Smartwatch"
])

# Product category
category = np.array([
    "Electronics", "Electronics", "Accessories", "Electronics",
    "Wearable", "Electronics", "Electronics", "Electronics",
    "Accessories", "Electronics", "Wearable", "Electronics",
    "Electronics", "Electronics", "Accessories", "Electronics",
    "Electronics", "Wearable", "Electronics", "Accessories",
    "Electronics", "Electronics", "Electronics", "Wearable",
    "Accessories", "Electronics", "Electronics", "Electronics",
    "Electronics", "Wearable"
])

# Customer city
city = np.array([
    "Delhi", "Mumbai", "Lucknow", "Delhi", "Pune",
    "Mumbai", "Delhi", "Lucknow", "Pune", "Mumbai",
    "Delhi", "Pune", "Mumbai", "Delhi", "Lucknow",
    "Pune", "Delhi", "Mumbai", "Lucknow", "Pune",
    "Delhi", "Mumbai", "Lucknow", "Pune", "Delhi",
    "Mumbai", "Delhi", "Lucknow", "Pune", "Mumbai"
])

# Number of products purchased in each order
quantity = np.array([
    1, 2, 3, 1, 2,
    3, 1, 2, 4, 2,
    1, 2, 3, 2, 5,
    1, 4, 2, 1, 3,
    2, 3, 1, 2, 4,
    2, 1, 3, 2, 2
])

# Price of one unit of the product
price = np.array([
    60000, 25000, 2000, 30000, 5000,
    25000, 60000, 30000, 2000, 25000,
    5000, 60000, 25000, 30000, 2000,
    60000, 25000, 5000, 30000, 2000,
    60000, 25000, 30000, 5000, 2000,
    25000, 60000, 30000, 25000, 5000
])

# Discount percentage applied to each order
discount = np.array([
    5, 10, 15, 5, 10,
    20, 5, 10, 15, 10,
    5, 15, 10, 20, 10,
    5, 15, 10, 5, 20,
    10, 5, 15, 10, 20,
    10, 5, 20, 10, 15
])

# Order delivery status
status = np.array([
    "Delivered", "Delivered", "Delivered", "Cancelled", "Delivered",
    "Delivered", "Delivered", "Delivered", "Cancelled", "Delivered",
    "Delivered", "Delivered", "Cancelled", "Delivered", "Delivered",
    "Delivered", "Delivered", "Delivered", "Cancelled", "Delivered",
    "Delivered", "Cancelled", "Delivered", "Delivered", "Delivered",
    "Delivered", "Delivered", "Cancelled", "Delivered", "Delivered"
])

# Payment method used by the customer
payment_method = np.array([
    "UPI", "Card", "Cash", "Card", "UPI",
    "UPI", "Card", "UPI", "Cash", "Card",
    "UPI", "Card", "UPI", "Cash", "Card",
    "UPI", "Card", "UPI", "Card", "Cash",
    "UPI", "Card", "Cash", "UPI", "Card",
    "UPI", "Card", "Cash", "UPI", "Card"
])


# ============================================================
# 2. SALES CALCULATION
# ============================================================
# Gross sales = Quantity × Price
#
# Example:
# Quantity = 2
# Price = ₹25,000
# Gross Sales = 2 × ₹25,000 = ₹50,000
# ============================================================

gross_sales = quantity * price


# Calculate the actual discount amount.
#
# Discount Amount = Gross Sales × Discount Percentage / 100

discount_amount = gross_sales * discount / 100


# Net revenue is the revenue remaining after discount.
#
# Net Revenue = Gross Sales - Discount Amount

net_revenue = gross_sales - discount_amount


# ============================================================
# 3. BASIC BUSINESS ANALYSIS
# ============================================================
# These KPIs provide an overall picture of e-commerce
# business performance.
# ============================================================

# Total number of orders
total_orders = len(order_id)

# Total revenue generated
total_revenue = np.sum(net_revenue)

# Average revenue generated per order
average_order_value = np.mean(net_revenue)

# Highest-value order
highest_order_value = np.max(net_revenue)

# Lowest-value order
lowest_order_value = np.min(net_revenue)

# Total number of products sold
total_units_sold = np.sum(quantity)

# Average number of products per order
average_quantity = np.mean(quantity)


# Display the main KPIs
print("=" * 60)
print("          E-COMMERCE SALES ANALYTICS")
print("=" * 60)

print(f"Total Orders        : {total_orders}")
print(f"Total Revenue       : ₹{total_revenue:,.2f}")
print(f"Average Order Value : ₹{average_order_value:,.2f}")
print(f"Highest Order Value : ₹{highest_order_value:,.2f}")
print(f"Lowest Order Value  : ₹{lowest_order_value:,.2f}")
print(f"Total Units Sold    : {total_units_sold}")
print(f"Average Quantity    : {average_quantity:.2f}")


# ============================================================
# 4. ORDER STATUS ANALYSIS
# ============================================================
# We use Boolean indexing to separate delivered and
# cancelled orders.
# ============================================================

# Create a Boolean array for delivered orders
delivered = status == "Delivered"

# Count True values to get the number of delivered orders
delivered_orders = np.sum(delivered)


# Create a Boolean array for cancelled orders
cancelled = status == "Cancelled"

# Count cancelled orders
cancelled_orders = np.sum(cancelled)


# Calculate cancellation percentage
#
# Cancellation Rate =
# Cancelled Orders / Total Orders × 100

cancellation_rate = (
    cancelled_orders / total_orders
) * 100


print("\n" + "=" * 60)
print("          ORDER STATUS ANALYSIS")
print("=" * 60)

print(f"Delivered Orders : {delivered_orders}")
print(f"Cancelled Orders : {cancelled_orders}")
print(f"Cancellation Rate: {cancellation_rate:.2f}%")


# ============================================================
# 5. PRODUCT ANALYSIS
# ============================================================
# np.unique() gives us all different products.
# Boolean indexing is then used to filter transactions
# belonging to each product.
# ============================================================

unique_products = np.unique(product)

print("\n" + "=" * 60)
print("             PRODUCT ANALYSIS")
print("=" * 60)

for item in unique_products:

    # Select only transactions for the current product
    mask = product == item

    # Calculate total revenue for that product
    product_revenue = np.sum(net_revenue[mask])

    # Calculate total units sold for that product
    product_units = np.sum(quantity[mask])

    print(
        f"{item:<15}"
        f"Revenue: ₹{product_revenue:,.2f} | "
        f"Units: {product_units}"
    )


# ============================================================
# 6. CATEGORY ANALYSIS
# ============================================================
# This section compares the performance of different
# product categories.
# ============================================================

unique_categories = np.unique(category)

print("\n" + "=" * 60)
print("            CATEGORY ANALYSIS")
print("=" * 60)

for cat in unique_categories:

    # Filter transactions for the current category
    mask = category == cat

    # Calculate category revenue
    category_revenue = np.sum(net_revenue[mask])

    # Calculate category units sold
    category_units = np.sum(quantity[mask])

    print(
        f"{cat:<15}"
        f"Revenue: ₹{category_revenue:,.2f} | "
        f"Units: {category_units}"
    )


# ============================================================
# 7. CITY-WISE ANALYSIS
# ============================================================
# We compare sales performance across different cities.
# This helps the company identify its strongest markets.
# ============================================================

unique_cities = np.unique(city)

print("\n" + "=" * 60)
print("             CITY ANALYSIS")
print("=" * 60)

for location in unique_cities:

    # Filter orders belonging to the current city
    mask = city == location

    # Calculate revenue generated by the city
    city_revenue = np.sum(net_revenue[mask])

    # Count number of orders from the city
    city_orders = np.sum(mask)

    print(
        f"{location:<10}"
        f"Revenue: ₹{city_revenue:,.2f} | "
        f"Orders: {city_orders}"
    )


# ============================================================
# 8. CUSTOMER ANALYSIS
# ============================================================
# We calculate the total amount spent by each customer.
# ============================================================

unique_customers = np.unique(customer_id)

# Create an empty NumPy array to store customer revenue
customer_revenue = np.zeros(len(unique_customers))


for i, customer in enumerate(unique_customers):

    # Select all orders belonging to this customer
    mask = customer_id == customer

    # Add the customer's total revenue
    customer_revenue[i] = np.sum(net_revenue[mask])


print("\n" + "=" * 60)
print("            CUSTOMER ANALYSIS")
print("=" * 60)

for i in range(len(unique_customers)):

    print(
        f"{unique_customers[i]} "
        f"-> ₹{customer_revenue[i]:,.2f}"
    )


# ============================================================
# 9. TOP 5 CUSTOMERS
# ============================================================
# np.argsort() sorts the indexes of the customer revenue.
# The last five indexes represent the highest values.
# [::-1] reverses them so highest comes first.
# ============================================================

top_customers = np.argsort(customer_revenue)[-5:][::-1]

print("\n" + "=" * 60)
print("              TOP 5 CUSTOMERS")
print("=" * 60)

for index in top_customers:

    print(
        f"{unique_customers[index]} "
        f"-> ₹{customer_revenue[index]:,.2f}"
    )


# ============================================================
# 10. PAYMENT METHOD ANALYSIS
# ============================================================
# We determine how many customers use each payment method.
# ============================================================

payment_methods = np.unique(payment_method)

print("\n" + "=" * 60)
print("          PAYMENT METHOD ANALYSIS")
print("=" * 60)

for method in payment_methods:

    # Select orders using the current payment method
    mask = payment_method == method

    # Count orders
    order_count = np.sum(mask)

    # Calculate percentage share
    percentage = (
        order_count / total_orders
    ) * 100

    print(
        f"{method:<8}"
        f"Orders: {order_count} | "
        f"Share: {percentage:.2f}%"
    )


# ============================================================
# 11. DISCOUNT ANALYSIS
# ============================================================
# We analyze the discount strategy used by the company.
# ============================================================

average_discount = np.mean(discount)

maximum_discount = np.max(discount)

# Count orders where discount is greater than 15%
high_discount_orders = np.sum(discount > 15)


print("\n" + "=" * 60)
print("             DISCOUNT ANALYSIS")
print("=" * 60)

print(f"Average Discount : {average_discount:.2f}%")
print(f"Maximum Discount : {maximum_discount}%")
print(f"Orders Above 15% : {high_discount_orders}")


# ============================================================
# 12. PROFIT ANALYSIS
# ============================================================
# For this practice dataset, we assume the product cost is
# 80% of the original selling price.
#
# In a real company, actual cost data should be used.
# ============================================================

cost = quantity * price * 0.80

# Profit = Net Revenue - Cost
profit = net_revenue - cost

# Total profit generated
total_profit = np.sum(profit)

# Average profit per order
average_profit = np.mean(profit)

# Overall profit margin
profit_margin = (
    total_profit / total_revenue
) * 100


print("\n" + "=" * 60)
print("             PROFIT ANALYSIS")
print("=" * 60)

print(f"Total Profit   : ₹{total_profit:,.2f}")
print(f"Average Profit : ₹{average_profit:,.2f}")
print(f"Profit Margin  : {profit_margin:.2f}%")


# ============================================================
# 13. TOP 5 ORDERS
# ============================================================
# np.argsort() helps us rank orders according to revenue.
# ============================================================

top_orders = np.argsort(net_revenue)[-5:][::-1]

print("\n" + "=" * 60)
print("               TOP 5 ORDERS")
print("=" * 60)

for index in top_orders:

    print(
        f"Order {order_id[index]} | "
        f"Customer {customer_id[index]} | "
        f"{product[index]} | "
        f"₹{net_revenue[index]:,.2f}"
    )


# ============================================================
# 14. STATISTICAL ANALYSIS
# ============================================================
# Statistical measures help us understand the distribution
# and variation of order revenue.
# ============================================================

mean_revenue = np.mean(net_revenue)

median_revenue = np.median(net_revenue)

revenue_std = np.std(net_revenue)

revenue_variance = np.var(net_revenue)


print("\n" + "=" * 60)
print("           STATISTICAL ANALYSIS")
print("=" * 60)

print(f"Mean Revenue          : ₹{mean_revenue:,.2f}")
print(f"Median Revenue        : ₹{median_revenue:,.2f}")
print(f"Standard Deviation    : ₹{revenue_std:,.2f}")
print(f"Variance              : {revenue_variance:,.2f}")


# ============================================================
# 15. HIGH-VALUE ORDERS
# ============================================================
# We identify orders whose revenue is greater than the
# average order revenue.
# ============================================================

high_value_orders = net_revenue > mean_revenue

print("\n" + "=" * 60)
print("            HIGH-VALUE ORDERS")
print("=" * 60)

print("Orders above average revenue:")

print(order_id[high_value_orders])


# ============================================================
# 16. BUSINESS INSIGHTS
# ============================================================
# Finally, we convert our numerical analysis into
# meaningful business information.
# ============================================================

best_order_index = np.argmax(net_revenue)

print("\n" + "=" * 60)
print("             BUSINESS INSIGHTS")
print("=" * 60)

print(
    f"1. Highest-value order: "
    f"Order {order_id[best_order_index]}"
)

print(
    f"2. Product in highest-value order: "
    f"{product[best_order_index]}"
)

print(
    f"3. Cancellation rate: "
    f"{cancellation_rate:.2f}%"
)

print(
    f"4. Average order value: "
    f"₹{average_order_value:,.2f}"
)

print(
    f"5. Total revenue: "
    f"₹{total_revenue:,.2f}"
)

print(
    f"6. Total units sold: "
    f"{total_units_sold}"
)

print("=" * 60)
