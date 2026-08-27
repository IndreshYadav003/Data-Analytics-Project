'''
1. Business Problem

Imagine a telecom company has 30 customers.

Management wants to know:

How many customers left?
What is the churn rate?
Which age group has more churn?
Which plan has the highest churn?
Does monthly bill relate to churn?
Do long-term customers churn less?
Which customers are at higher churn risk?
What is the average monthly bill of churned customers?
Work Flow of codes
Customer Data
      ↓
Data Preparation
      ↓
Churn Analysis
      ↓
Customer Segmentation
      ↓
Statistical Analysis
      ↓
Business Insights

'''
# ============================================================
# CUSTOMER CHURN ANALYTICS USING NUMPY
# B.Tech Final Year Data Analytics Project
# ============================================================

import numpy as np


# ============================================================
# 1. CREATE CUSTOMER DATASET
# ============================================================
# Each index represents one customer.
# We have information about customer age, tenure,
# monthly bill, plan, contract, support calls and churn.
# ============================================================

customer_id = np.arange(101, 131)

age = np.array([
    22, 35, 28, 45, 31,
    52, 24, 39, 41, 29,
    33, 48, 26, 55, 37,
    44, 23, 50, 32, 27,
    36, 42, 25, 47, 30,
    53, 34, 40, 21, 46
])

tenure = np.array([
    5, 24, 12, 48, 18,
    60, 7, 36, 42, 10,
    30, 54, 8, 72, 28,
    45, 6, 66, 20, 9,
    32, 39, 4, 58, 15,
    70, 26, 34, 3, 50
])

monthly_bill = np.array([
    450, 850, 600, 1200, 750,
    1500, 500, 1100, 1300, 550,
    900, 1400, 480, 1600, 950,
    1250, 520, 1550, 700, 580,
    1000, 1150, 430, 1450, 680,
    1700, 880, 1050, 400, 1350
])

plan = np.array([
    "Basic", "Premium", "Standard", "Premium", "Standard",
    "Premium", "Basic", "Premium", "Premium", "Basic",
    "Standard", "Premium", "Basic", "Premium", "Standard",
    "Premium", "Basic", "Premium", "Standard", "Basic",
    "Standard", "Premium", "Basic", "Premium", "Standard",
    "Premium", "Standard", "Premium", "Basic", "Premium"
])

contract = np.array([
    "Monthly", "Yearly", "Monthly", "Yearly", "Monthly",
    "Yearly", "Monthly", "Yearly", "Monthly", "Monthly",
    "Yearly", "Yearly", "Monthly", "Yearly", "Monthly",
    "Yearly", "Monthly", "Yearly", "Monthly", "Monthly",
    "Yearly", "Monthly", "Monthly", "Yearly", "Monthly",
    "Yearly", "Monthly", "Yearly", "Monthly", "Yearly"
])

support_calls = np.array([
    5, 1, 4, 0, 3,
    1, 6, 1, 2, 7,
    2, 0, 5, 1, 3,
    1, 8, 0, 4, 6,
    2, 1, 7, 0, 5,
    1, 3, 0, 6, 1
])

churn = np.array([
    "Yes", "No", "Yes", "No", "Yes",
    "No", "Yes", "No", "No", "Yes",
    "No", "No", "Yes", "No", "Yes",
    "No", "Yes", "No", "Yes", "Yes",
    "No", "No", "Yes", "No", "Yes",
    "No", "Yes", "No", "Yes", "No"
])


# ============================================================
# 2. BASIC DATA INFORMATION
# ============================================================

print("=" * 70)
print("                 CUSTOMER CHURN ANALYTICS")
print("=" * 70)

# Count total customers
total_customers = len(customer_id)

print("\nTotal Customers:", total_customers)

# Display unique plans
print("Available Plans:", np.unique(plan))

# Display unique contract types
print("Contract Types:", np.unique(contract))

# Display churn categories
print("Churn Categories:", np.unique(churn))


# ============================================================
# 3. CHURN ANALYSIS
# ============================================================
# Create a Boolean array.
# True means the customer has churned.
# ============================================================

churned = churn == "Yes"

# Count churned customers
churned_customers = np.sum(churned)

# Create Boolean array for retained customers
retained = churn == "No"

# Count retained customers
retained_customers = np.sum(retained)

# Calculate churn rate
churn_rate = (
    churned_customers / total_customers
) * 100

# Calculate retention rate
retention_rate = (
    retained_customers / total_customers
) * 100


print("\n" + "=" * 70)
print("                    CHURN SUMMARY")
print("=" * 70)

print("Total Customers  :", total_customers)
print("Churned Customers :", churned_customers)
print("Retained Customers:", retained_customers)
print(f"Churn Rate        : {churn_rate:.2f}%")
print(f"Retention Rate    : {retention_rate:.2f}%")


# ============================================================
# 4. CUSTOMER AGE ANALYSIS
# ============================================================

average_age = np.mean(age)
minimum_age = np.min(age)
maximum_age = np.max(age)
median_age = np.median(age)
age_std = np.std(age)

print("\n" + "=" * 70)
print("                    AGE ANALYSIS")
print("=" * 70)

print(f"Average Age      : {average_age:.2f}")
print(f"Median Age       : {median_age:.2f}")
print(f"Minimum Age      : {minimum_age}")
print(f"Maximum Age      : {maximum_age}")
print(f"Age Std Deviation: {age_std:.2f}")


# ============================================================
# 5. MONTHLY BILL ANALYSIS
# ============================================================

average_bill = np.mean(monthly_bill)
median_bill = np.median(monthly_bill)
minimum_bill = np.min(monthly_bill)
maximum_bill = np.max(monthly_bill)
bill_std = np.std(monthly_bill)

print("\n" + "=" * 70)
print("                  MONTHLY BILL ANALYSIS")
print("=" * 70)

print(f"Average Bill       : ₹{average_bill:,.2f}")
print(f"Median Bill        : ₹{median_bill:,.2f}")
print(f"Minimum Bill       : ₹{minimum_bill:,.2f}")
print(f"Maximum Bill       : ₹{maximum_bill:,.2f}")
print(f"Bill Std Deviation : ₹{bill_std:,.2f}")


# ============================================================
# 6. TENURE ANALYSIS
# ============================================================

average_tenure = np.mean(tenure)
median_tenure = np.median(tenure)
minimum_tenure = np.min(tenure)
maximum_tenure = np.max(tenure)

print("\n" + "=" * 70)
print("                   TENURE ANALYSIS")
print("=" * 70)

print(f"Average Tenure : {average_tenure:.2f} months")
print(f"Median Tenure  : {median_tenure:.2f} months")
print(f"Minimum Tenure : {minimum_tenure} months")
print(f"Maximum Tenure : {maximum_tenure} months")


# ============================================================
# 7. CHURNED CUSTOMER BILL ANALYSIS
# ============================================================
# Boolean indexing allows us to select only churned customers.
# ============================================================

churned_bills = monthly_bill[churned]

retained_bills = monthly_bill[retained]

average_churned_bill = np.mean(churned_bills)

average_retained_bill = np.mean(retained_bills)


print("\n" + "=" * 70)
print("             CHURNED VS RETAINED BILL")
print("=" * 70)

print(
    f"Average Churned Customer Bill : "
    f"₹{average_churned_bill:,.2f}"
)

print(
    f"Average Retained Customer Bill: "
    f"₹{average_retained_bill:,.2f}"
)


# ============================================================
# 8. CHURNED VS RETAINED TENURE
# ============================================================

churned_tenure = tenure[churned]

retained_tenure = tenure[retained]

average_churned_tenure = np.mean(churned_tenure)

average_retained_tenure = np.mean(retained_tenure)


print("\n" + "=" * 70)
print("             CHURNED VS RETAINED TENURE")
print("=" * 70)

print(
    f"Average Churned Tenure : "
    f"{average_churned_tenure:.2f} months"
)

print(
    f"Average Retained Tenure: "
    f"{average_retained_tenure:.2f} months"
)


# ============================================================
# 9. CHURN BY PLAN
# ============================================================
# We calculate:
# Total customers in each plan
# Churned customers in each plan
# Churn rate for each plan
# ============================================================

plans = np.unique(plan)

print("\n" + "=" * 70)
print("                     CHURN BY PLAN")
print("=" * 70)

for current_plan in plans:

    # Select customers belonging to the current plan
    plan_mask = plan == current_plan

    # Select customers who both use this plan and churned
    plan_churn_mask = plan_mask & churned

    # Count customers in the plan
    total_plan_customers = np.sum(plan_mask)

    # Count churned customers in the plan
    plan_churned = np.sum(plan_churn_mask)

    # Calculate plan churn rate
    plan_churn_rate = (
        plan_churned /
        total_plan_customers
    ) * 100

    print(
        f"{current_plan:<10}"
        f" Customers: {total_plan_customers:<3}"
        f" Churned: {plan_churned:<3}"
        f" Churn Rate: {plan_churn_rate:.2f}%"
    )


# ============================================================
# 10. CHURN BY CONTRACT TYPE
# ============================================================

contracts = np.unique(contract)

print("\n" + "=" * 70)
print("                  CHURN BY CONTRACT")
print("=" * 70)

for current_contract in contracts:

    # Select customers with current contract type
    contract_mask = contract == current_contract

    # Select customers who churned within this contract
    contract_churn_mask = contract_mask & churned

    # Count customers
    total_contract_customers = np.sum(contract_mask)

    # Count churned customers
    contract_churned = np.sum(contract_churn_mask)

    # Calculate churn rate
    contract_churn_rate = (
        contract_churned /
        total_contract_customers
    ) * 100

    print(
        f"{current_contract:<10}"
        f" Customers: {total_contract_customers:<3}"
        f" Churned: {contract_churned:<3}"
        f" Churn Rate: {contract_churn_rate:.2f}%"
    )


# ============================================================
# 11. SUPPORT CALL ANALYSIS
# ============================================================
# Compare support calls between churned and retained customers.
# ============================================================

churned_calls = support_calls[churned]

retained_calls = support_calls[retained]

average_churned_calls = np.mean(churned_calls)

average_retained_calls = np.mean(retained_calls)


print("\n" + "=" * 70)
print("                 SUPPORT CALL ANALYSIS")
print("=" * 70)

print(
    f"Average Calls - Churned Customers : "
    f"{average_churned_calls:.2f}"
)

print(
    f"Average Calls - Retained Customers: "
    f"{average_retained_calls:.2f}"
)


# ============================================================
# 12. AGE GROUP ANALYSIS
# ============================================================
# We divide customers into three groups:
#
# Under 30
# 30 to 44
# 45 and above
# ============================================================

young_customers = age < 30

middle_age_customers = (
    (age >= 30) &
    (age < 45)
)

senior_customers = age >= 45


# ---------- Under 30 ----------

young_total = np.sum(young_customers)

young_churned = np.sum(
    young_customers & churned
)

young_churn_rate = (
    young_churned / young_total
) * 100


# ---------- Age 30 to 44 ----------

middle_total = np.sum(middle_age_customers)

middle_churned = np.sum(
    middle_age_customers & churned
)

middle_churn_rate = (
    middle_churned / middle_total
) * 100


# ---------- Age 45+ ----------

senior_total = np.sum(senior_customers)

senior_churned = np.sum(
    senior_customers & churned
)

senior_churn_rate = (
    senior_churned / senior_total
) * 100


print("\n" + "=" * 70)
print("                  AGE GROUP CHURN")
print("=" * 70)

print(f"Under 30 : {young_churn_rate:.2f}%")
print(f"30 - 44  : {middle_churn_rate:.2f}%")
print(f"45+      : {senior_churn_rate:.2f}%")


# ============================================================
# 13. HIGH-BILL CUSTOMERS
# ============================================================
# We identify customers whose monthly bill is greater than
# ₹1,000.
# ============================================================

high_bill = monthly_bill > 1000

print("\n" + "=" * 70)
print("                  HIGH-BILL CUSTOMERS")
print("=" * 70)

print(
    "Customer IDs:",
    customer_id[high_bill]
)


# ============================================================
# 14. HIGH SUPPORT-CALL CUSTOMERS
# ============================================================
# Identify customers who contacted support 5 or more times.
# ============================================================

high_support = support_calls >= 5

print("\n" + "=" * 70)
print("             HIGH SUPPORT-CALL CUSTOMERS")
print("=" * 70)

print(
    "Customer IDs:",
    customer_id[high_support]
)


# ============================================================
# 15. HIGH-RISK CUSTOMER ANALYSIS
# ============================================================
# For this practice project, we define a high-risk customer as:
#
# Monthly Bill > ₹1,000
# AND
# Support Calls >= 4
#
# This is a simple business rule, not a machine-learning model.
# ============================================================

high_risk = (
    (monthly_bill > 1000) &
    (support_calls >= 4)
)

high_risk_count = np.sum(high_risk)

print("\n" + "=" * 70)
print("                 HIGH-RISK CUSTOMERS")
print("=" * 70)

print("Number of High-Risk Customers:", high_risk_count)

print(
    "High-Risk Customer IDs:",
    customer_id[high_risk]
)


# ============================================================
# 16. CHURNED HIGH-RISK CUSTOMERS
# ============================================================
# Here we identify customers who are both:
#
# High Risk
# AND
# Already Churned
# ============================================================

high_risk_churned = high_risk & churned

print("\n" + "=" * 70)
print("             HIGH-RISK CHURNED CUSTOMERS")
print("=" * 70)

print(
    "Customer IDs:",
    customer_id[high_risk_churned]
)


# ============================================================
# 17. CUSTOMER WITH HIGHEST MONTHLY BILL
# ============================================================
# np.argmax() returns the index of the maximum value.
# ============================================================

highest_bill_index = np.argmax(monthly_bill)

print("\n" + "=" * 70)
print("             HIGHEST BILL CUSTOMER")
print("=" * 70)

print(
    "Customer ID:",
    customer_id[highest_bill_index]
)

print(
    "Monthly Bill:",
    f"₹{monthly_bill[highest_bill_index]:,.2f}"
)

print(
    "Plan:",
    plan[highest_bill_index]
)

print(
    "Churn:",
    churn[highest_bill_index]
)


# ============================================================
# 18. CUSTOMER WITH LONGEST TENURE
# ============================================================

longest_tenure_index = np.argmax(tenure)

print("\n" + "=" * 70)
print("             LONGEST TENURE CUSTOMER")
print("=" * 70)

print(
    "Customer ID:",
    customer_id[longest_tenure_index]
)

print(
    "Tenure:",
    tenure[longest_tenure_index],
    "months"
)

print(
    "Plan:",
    plan[longest_tenure_index]
)

print(
    "Churn:",
    churn[longest_tenure_index]
)


# ============================================================
# 19. CHURNED CUSTOMER LIST
# ============================================================

print("\n" + "=" * 70)
print("                  CHURNED CUSTOMERS")
print("=" * 70)

print(
    "Customer IDs:",
    customer_id[churned]
)


# ============================================================
# 20. CHURNED CUSTOMER DETAILS
# ============================================================
# Display important information about churned customers.
# ============================================================

print("\n" + "=" * 70)
print("              CHURNED CUSTOMER DETAILS")
print("=" * 70)

print("Customer IDs :", customer_id[churned])
print("Age          :", age[churned])
print("Tenure       :", tenure[churned])
print("Monthly Bill :", monthly_bill[churned])
print("Support Calls:", support_calls[churned])
print("Plan         :", plan[churned])
print("Contract     :", contract[churned])


# ============================================================
# 21. BILL PERCENTILES
# ============================================================
# Percentiles help us understand the distribution of
# customer monthly bills.
# ============================================================

bill_25 = np.percentile(monthly_bill, 25)

bill_50 = np.percentile(monthly_bill, 50)

bill_75 = np.percentile(monthly_bill, 75)

print("\n" + "=" * 70)
print("                  BILL PERCENTILES")
print("=" * 70)

print(f"25th Percentile: ₹{bill_25:,.2f}")
print(f"50th Percentile: ₹{bill_50:,.2f}")
print(f"75th Percentile: ₹{bill_75:,.2f}")


# ============================================================
# 22. REVENUE AT RISK
# ============================================================
# A simple business metric:
#
# Monthly revenue from churned customers.
#
# This estimates how much monthly billing is associated
# with customers who have churned.
# ============================================================

churned_revenue = np.sum(monthly_bill[churned])

print("\n" + "=" * 70)
print("                  REVENUE AT RISK")
print("=" * 70)

print(
    f"Monthly Bill from Churned Customers: "
    f"₹{churned_revenue:,.2f}"
)


# ============================================================
# 23. CHURNED CUSTOMER BILL SHARE
# ============================================================
# Percentage of total monthly billing represented by
# churned customers.
# ============================================================

total_monthly_bill = np.sum(monthly_bill)

churned_bill_share = (
    churned_revenue /
    total_monthly_bill
) * 100

print(
    f"Churned Customer Bill Share: "
    f"{churned_bill_share:.2f}%"
)


# ============================================================
# 24. FINAL BUSINESS INSIGHTS
# ============================================================
# Convert numerical results into understandable
# business observations.
# ============================================================

print("\n" + "=" * 70)
print("                  BUSINESS INSIGHTS")
print("=" * 70)

print(
    f"1. Overall churn rate is {churn_rate:.2f}%."
)

print(
    f"2. Average monthly bill is "
    f"₹{average_bill:,.2f}."
)

print(
    f"3. Churned customers have an average bill of "
    f"₹{average_churned_bill:,.2f}."
)

print(
    f"4. Retained customers have an average bill of "
    f"₹{average_retained_bill:,.2f}."
)

print(
    f"5. Average tenure of churned customers is "
    f"{average_churned_tenure:.2f} months."
)

print(
    f"6. Average tenure of retained customers is "
    f"{average_retained_tenure:.2f} months."
)

print(
    f"7. {high_risk_count} customers satisfy the "
    f"high-risk rule."
)

print(
    f"8. Churned customers represent "
    f"{churned_bill_share:.2f}% of total monthly billing."
)

print("\nAnalysis Completed Successfully!")

print("=" * 70)
