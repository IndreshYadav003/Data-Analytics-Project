'''
Business Problem

A company has employee data and wants to understand:

How many employees are there?
What is the average salary?
Which department has more employees?
Which department has the highest salary?
What is the average experience?
How many employees are performing well?
How many employees are leaving?
Does experience relate to salary?
Which employees have high salaries?
What business insights can HR get from the data?

Worlflow
Employee Data
     ↓
Data Preparation
     ↓
Basic Employee Analysis
     ↓
Salary Analysis
     ↓
Department Analysis
     ↓
Experience Analysis
     ↓
Performance Analysis
     ↓
Employee Attrition Analysis
     ↓
Business Insights
'''
# ==========================================================
# PROJECT 5: HR EMPLOYEE ANALYTICS
# Python + NumPy
# ==========================================================

import numpy as np


# ==========================================================
# 1. EMPLOYEE DATA
# ==========================================================
# We create a small sample dataset of 20 employees.

employee_id = np.arange(101, 121)


# Employee age

age = np.array([
    22, 25, 28, 32, 35,
    29, 41, 38, 26, 30,
    45, 27, 33, 36, 24,
    31, 40, 28, 37, 34
])


# Years of experience

experience = np.array([
    1, 2, 4, 8, 10,
    5, 15, 12, 3, 7,
    18, 4, 9, 11, 2,
    6, 14, 3, 13, 10
])


# Annual salary

salary = np.array([
    300000, 350000, 450000, 650000, 750000,
    500000, 1200000, 950000, 400000, 600000,
    1500000, 450000, 700000, 850000, 320000,
    550000, 1100000, 420000, 1000000, 800000
])


# Department

department = np.array([
    "IT", "HR", "Sales", "IT", "Finance",
    "Sales", "IT", "Finance", "HR", "IT",
    "Finance", "Sales", "IT", "Finance", "HR",
    "Sales", "IT", "HR", "Finance", "IT"
])


# Employee performance score
# Score is between 1 and 10.

performance = np.array([
    7, 8, 6, 9, 8,
    7, 9, 8, 6, 8,
    10, 7, 9, 8, 6,
    7, 9, 7, 9, 8
])


# Employee attrition
# Yes = Employee left the company
# No = Employee is still working

attrition = np.array([
    "No", "No", "Yes", "No", "No",
    "Yes", "No", "No", "Yes", "No",
    "No", "Yes", "No", "No", "Yes",
    "Yes", "No", "Yes", "No", "No"
])


# ==========================================================
# 2. BASIC INFORMATION
# ==========================================================

print("=" * 60)
print("             HR EMPLOYEE ANALYTICS")
print("=" * 60)


# Count total employees

total_employees = len(employee_id)

print("\nTotal Employees:", total_employees)


# ==========================================================
# 3. AVERAGE AGE
# ==========================================================

average_age = np.mean(age)

print(
    "Average Employee Age:",
    round(average_age, 2)
)


# ==========================================================
# 4. AVERAGE EXPERIENCE
# ==========================================================

average_experience = np.mean(experience)

print(
    "Average Experience:",
    round(average_experience, 2),
    "years"
)


# ==========================================================
# 5. SALARY ANALYSIS
# ==========================================================

average_salary = np.mean(salary)

highest_salary = np.max(salary)

lowest_salary = np.min(salary)

median_salary = np.median(salary)


print("\n" + "=" * 60)
print("                SALARY ANALYSIS")
print("=" * 60)

print(
    "Average Salary: ₹",
    round(average_salary, 2)
)

print(
    "Highest Salary: ₹",
    highest_salary
)

print(
    "Lowest Salary: ₹",
    lowest_salary
)

print(
    "Median Salary: ₹",
    median_salary
)


# ==========================================================
# 6. HIGHEST PAID EMPLOYEE
# ==========================================================
# np.argmax() gives the position of the highest salary.

highest_salary_index = np.argmax(salary)

print("\nHighest Paid Employee:")

print(
    "Employee ID:",
    employee_id[highest_salary_index]
)

print(
    "Salary: ₹",
    salary[highest_salary_index]
)

print(
    "Department:",
    department[highest_salary_index]
)


# ==========================================================
# 7. LOWEST PAID EMPLOYEE
# ==========================================================

lowest_salary_index = np.argmin(salary)

print("\nLowest Paid Employee:")

print(
    "Employee ID:",
    employee_id[lowest_salary_index]
)

print(
    "Salary: ₹",
    salary[lowest_salary_index]
)


# ==========================================================
# 8. DEPARTMENT ANALYSIS
# ==========================================================
# np.unique() finds all different departments.

departments = np.unique(department)

print("\n" + "=" * 60)
print("              DEPARTMENT ANALYSIS")
print("=" * 60)


for d in departments:

    # Find employees belonging to this department

    department_mask = department == d

    # Count employees

    employee_count = np.sum(department_mask)

    # Calculate average salary

    department_average_salary = np.mean(
        salary[department_mask]
    )

    print(
        "\nDepartment:",
        d
    )

    print(
        "Number of Employees:",
        employee_count
    )

    print(
        "Average Salary: ₹",
        round(
            department_average_salary,
            2
        )
    )


# ==========================================================
# 9. EXPERIENCE ANALYSIS
# ==========================================================
# Find employees with more than 10 years of experience.

experienced = experience > 10

experienced_count = np.sum(experienced)


print("\n" + "=" * 60)
print("             EXPERIENCE ANALYSIS")
print("=" * 60)

print(
    "Employees with >10 years experience:",
    experienced_count
)

print(
    "Employee IDs:",
    employee_id[experienced]
)


# ==========================================================
# 10. FRESHER ANALYSIS
# ==========================================================
# Employees with 3 or fewer years of experience.

freshers = experience <= 3

fresher_count = np.sum(freshers)


print(
    "\nEmployees with <=3 years experience:",
    fresher_count
)

print(
    "Fresher Employee IDs:",
    employee_id[freshers]
)


# ==========================================================
# 11. HIGH PERFORMANCE EMPLOYEES
# ==========================================================
# Performance score >= 8 is considered high performance
# for this practice project.

high_performance = performance >= 8

high_performance_count = np.sum(
    high_performance
)


print("\n" + "=" * 60)
print("           PERFORMANCE ANALYSIS")
print("=" * 60)

print(
    "High Performance Employees:",
    high_performance_count
)

print(
    "Employee IDs:",
    employee_id[high_performance]
)


# ==========================================================
# 12. LOW PERFORMANCE EMPLOYEES
# ==========================================================

low_performance = performance < 7

low_performance_count = np.sum(
    low_performance
)

print(
    "\nLow Performance Employees:",
    low_performance_count
)

print(
    "Employee IDs:",
    employee_id[low_performance]
)


# ==========================================================
# 13. ATTRITION ANALYSIS
# ==========================================================
# Create Boolean arrays for employees who left
# and employees who stayed.

left_company = attrition == "Yes"

stayed_company = attrition == "No"


# Count employees who left

employees_left = np.sum(left_company)

# Count employees who stayed

employees_stayed = np.sum(stayed_company)


# Calculate attrition rate

attrition_rate = (
    employees_left / total_employees
) * 100


print("\n" + "=" * 60)
print("              ATTRITION ANALYSIS")
print("=" * 60)

print(
    "Employees Left:",
    employees_left
)

print(
    "Employees Stayed:",
    employees_stayed
)

print(
    "Attrition Rate:",
    round(attrition_rate, 2),
    "%"
)


# ==========================================================
# 14. SALARY OF HIGH-PERFORMANCE EMPLOYEES
# ==========================================================

high_performance_salary = salary[
    high_performance
]

average_high_performance_salary = np.mean(
    high_performance_salary
)


print(
    "\nAverage Salary of High Performance Employees:",
    round(
        average_high_performance_salary,
        2
    )
)


# ==========================================================
# 15. HIGH SALARY EMPLOYEES
# ==========================================================
# Find employees earning more than ₹800,000.

high_salary = salary > 800000

high_salary_count = np.sum(high_salary)


print("\n" + "=" * 60)
print("              HIGH SALARY EMPLOYEES")
print("=" * 60)

print(
    "Number of High Salary Employees:",
    high_salary_count
)

print(
    "Employee IDs:",
    employee_id[high_salary]
)


# ==========================================================
# 16. EXPERIENCED + HIGH PERFORMANCE
# ==========================================================
# Find employees who have:
#
# More than 10 years experience
# AND
# Performance score >= 8

experienced_high_performance = (
    (experience > 10) &
    (performance >= 8)
)


print("\n" + "=" * 60)
print("       EXPERIENCED HIGH-PERFORMANCE EMPLOYEES")
print("=" * 60)

print(
    "Employee IDs:",
    employee_id[
        experienced_high_performance
    ]
)


# ==========================================================
# 17. EMPLOYEES WITH HIGH SALARY BUT LOW PERFORMANCE
# ==========================================================
# This can help HR identify employees who may need
# performance review.

high_salary_low_performance = (
    (salary > 800000) &
    (performance < 7)
)


print("\n" + "=" * 60)
print("       HIGH SALARY + LOW PERFORMANCE")
print("=" * 60)

print(
    "Employee IDs:",
    employee_id[
        high_salary_low_performance
    ]
)


# ==========================================================
# 18. EMPLOYEES WHO LEFT THE COMPANY
# ==========================================================

print("\n" + "=" * 60)
print("             EMPLOYEES WHO LEFT")
print("=" * 60)

print(
    "Employee IDs:",
    employee_id[left_company]
)


# ==========================================================
# 19. AVERAGE SALARY OF EMPLOYEES WHO LEFT
# ==========================================================

left_salary = salary[left_company]

average_left_salary = np.mean(
    left_salary
)


print(
    "\nAverage Salary of Employees Who Left: ₹",
    round(average_left_salary, 2)
)


# ==========================================================
# 20. AVERAGE EXPERIENCE OF EMPLOYEES WHO LEFT
# ==========================================================

left_experience = experience[left_company]

average_left_experience = np.mean(
    left_experience
)


print(
    "Average Experience of Employees Who Left:",
    round(average_left_experience, 2),
    "years"
)


# ==========================================================
# 21. FINAL BUSINESS INSIGHTS
# ==========================================================

print("\n" + "=" * 60)
print("               BUSINESS INSIGHTS")
print("=" * 60)


print(
    "1. Total employees:",
    total_employees
)

print(
    "2. Average employee age:",
    round(average_age, 2)
)

print(
    "3. Average experience:",
    round(average_experience, 2),
    "years"
)

print(
    "4. Average salary: ₹",
    round(average_salary, 2)
)

print(
    "5. Highest salary: ₹",
    highest_salary
)

print(
    "6. High-performance employees:",
    high_performance_count
)

print(
    "7. Employees who left:",
    employees_left
)

print(
    "8. Employee attrition rate:",
    round(attrition_rate, 2),
    "%"
)

print(
    "9. Employees with more than 10 years experience:",
    experienced_count
)

print(
    "10. High salary employees:",
    high_salary_count
)


print("\n" + "=" * 60)
print("             ANALYSIS COMPLETED")
print("=" * 60)
