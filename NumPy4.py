'''
Business Problem

Imagine an investment research company wants to analyze the performance of a stock.

The management wants answers to questions such as:

What is the average stock price?
What was the highest and lowest price?
How much did the stock grow?
What is the average daily return?
How volatile is the stock?
What was the best trading day?
What was the worst trading day?
What is the maximum drawdown?
How many positive-return days occurred?
How many negative-return days occurred?
Is the stock generally trending upward or downward?
During which period was the stock most risky?
                 STOCK PRICE DATA
                        ↓
                Data Preparation
                        ↓
              Basic Price Analysis
                        ↓
          ┌─────────────┴─────────────┐
          ↓                           ↓
     Return Analysis             Price Analysis
          ↓                           ↓
    Daily Returns              High / Low / Mean
          ↓                           ↓
     Volatility                 Moving Average
          ↓                           ↓
       Risk Analysis            Trend Analysis
          ↓                           ↓
          └─────────────┬─────────────┘
                        ↓
                 Drawdown Analysis
                        ↓
                 Business Insights
                        ↓
                 Final Report
'''
# ==========================================================
# PROJECT 4: STOCK MARKET ANALYTICS
# Python + NumPy
# ==========================================================

import numpy as np


# ==========================================================
# 1. STOCK PRICE DATA
# ==========================================================
# These are sample stock prices for 20 trading days.

days = np.arange(1, 21)

price = np.array([
    100, 102, 101, 105, 108,
    107, 110, 112, 111, 115,
    118, 120, 119, 122, 125,
    123, 126, 129, 128, 132
])


# ==========================================================
# 2. BASIC INFORMATION
# ==========================================================

print("========================================")
print("       STOCK MARKET ANALYTICS")
print("========================================")

print("Total Trading Days:", len(price))


# ==========================================================
# 3. AVERAGE PRICE
# ==========================================================
# np.mean() calculates the average.

average_price = np.mean(price)

print("\nAverage Stock Price:", average_price)


# ==========================================================
# 4. HIGHEST PRICE
# ==========================================================
# np.max() finds the highest value.

highest_price = np.max(price)

print("Highest Stock Price:", highest_price)


# ==========================================================
# 5. LOWEST PRICE
# ==========================================================
# np.min() finds the lowest value.

lowest_price = np.min(price)

print("Lowest Stock Price:", lowest_price)


# ==========================================================
# 6. STARTING AND ENDING PRICE
# ==========================================================
# [0] gives the first value.
# [-1] gives the last value.

starting_price = price[0]

ending_price = price[-1]

print("\nStarting Price:", starting_price)

print("Ending Price:", ending_price)


# ==========================================================
# 7. TOTAL PRICE CHANGE
# ==========================================================
# Change = Ending Price - Starting Price

price_change = ending_price - starting_price

print("Total Price Change:", price_change)


# ==========================================================
# 8. TOTAL RETURN
# ==========================================================
# Formula:
#
# Return = ((Ending - Starting) / Starting) * 100

total_return = (
    (ending_price - starting_price)
    / starting_price
) * 100

print("Total Return:", round(total_return, 2), "%")


# ==========================================================
# 9. DAILY RETURN
# ==========================================================
# Daily return tells us how much the stock changed
# compared with the previous day.
#
# np.diff() calculates the difference between prices.

daily_change = np.diff(price)

daily_return = (
    daily_change / price[:-1]
) * 100

print("\nDaily Returns:")
print(np.round(daily_return, 2))


# ==========================================================
# 10. AVERAGE DAILY RETURN
# ==========================================================

average_return = np.mean(daily_return)

print(
    "\nAverage Daily Return:",
    round(average_return, 2),
    "%"
)


# ==========================================================
# 11. BEST DAY
# ==========================================================
# np.argmax() finds the position of the highest return.

best_day = np.argmax(daily_return)

print(
    "\nBest Trading Day:",
    days[best_day + 1]
)

print(
    "Best Return:",
    round(daily_return[best_day], 2),
    "%"
)


# ==========================================================
# 12. WORST DAY
# ==========================================================
# np.argmin() finds the position of the lowest return.

worst_day = np.argmin(daily_return)

print(
    "\nWorst Trading Day:",
    days[worst_day + 1]
)

print(
    "Worst Return:",
    round(daily_return[worst_day], 2),
    "%"
)


# ==========================================================
# 13. POSITIVE DAYS
# ==========================================================
# Find days where the stock price increased.

positive_days = daily_return > 0

number_positive_days = np.sum(positive_days)

print(
    "\nPositive Return Days:",
    number_positive_days
)


# ==========================================================
# 14. NEGATIVE DAYS
# ==========================================================
# Find days where the stock price decreased.

negative_days = daily_return < 0

number_negative_days = np.sum(negative_days)

print(
    "Negative Return Days:",
    number_negative_days
)


# ==========================================================
# 15. VOLATILITY
# ==========================================================
# Standard deviation tells us how much daily returns
# vary from their average.

volatility = np.std(daily_return)

print(
    "\nStock Volatility:",
    round(volatility, 2),
    "%"
)


# ==========================================================
# 16. SIMPLE BUSINESS CONCLUSION
# ==========================================================

print("\n========================================")
print("          BUSINESS INSIGHTS")
print("========================================")

print(
    "1. Stock started at:",
    starting_price
)

print(
    "2. Stock ended at:",
    ending_price
)

print(
    "3. Total return:",
    round(total_return, 2),
    "%"
)

print(
    "4. Average price:",
    round(average_price, 2)
)

print(
    "5. Highest price:",
    highest_price
)

print(
    "6. Lowest price:",
    lowest_price
)

print(
    "7. Positive days:",
    number_positive_days
)

print(
    "8. Negative days:",
    number_negative_days
)

print(
    "9. Volatility:",
    round(volatility, 2),
    "%"
)

print("\nAnalysis Completed!")
