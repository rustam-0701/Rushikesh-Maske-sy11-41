# Fractional Knapsack Problem
# Using Greedy Method

def fractional_knapsack(profits, weights, capacity):
    n = len(profits)

    # Calculate profit/weight ratio
    items = []

    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append((profits[i], weights[i], ratio))

    # Sort items by ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    total_profit = 0.0
    remaining_capacity = capacity

    print("\nItems selected:")

    for profit, weight, ratio in items:

        if remaining_capacity <= 0:
            break

        # Take the complete item if it fits
        if weight <= remaining_capacity:
            total_profit += profit
            remaining_capacity -= weight

            print("Profit =", profit,
                  "Weight =", weight,
                  "Fraction Taken = 1.00")

        # Otherwise take the required fraction
        else:
            fraction = remaining_capacity / weight
            total_profit += profit * fraction

            print("Profit =", profit,
                  "Weight =", weight,
                  "Fraction Taken =", round(fraction, 2))

            remaining_capacity = 0

    return total_profit


# Input
profits = [25, 24, 15]
weights = [18, 15, 10]
capacity = 20

# Calculate maximum profit
maximum_profit = fractional_knapsack(profits, weights, capacity)

# Display result
print("\nMaximum Profit =", maximum_profit)