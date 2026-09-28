def knapsack(n, objects, weights, profits, capacity):

    # Calculate profit/weight ratio
    ratio = []

    for i in range(n):
        ratio.append(profits[i] / weights[i])

    # Sort by decreasing ratio
    for i in range(n):
        for j in range(i + 1, n):

            if ratio[i] < ratio[j]:

                ratio[i], ratio[j] = ratio[j], ratio[i]
                weights[i], weights[j] = weights[j], weights[i]
                profits[i], profits[j] = profits[j], profits[i]
                objects[i], objects[j] = objects[j], objects[i]

    # Fractional Knapsack
    x = [0.0] * n
    total_profit = 0.0
    remaining_capacity = capacity

    for i in range(n):

        if weights[i] > remaining_capacity:
            break

        x[i] = 1.0
        total_profit += profits[i]
        remaining_capacity -= weights[i]

    # Take fraction of the next object
    if i < n and remaining_capacity > 0:
        x[i] = remaining_capacity / weights[i]
        total_profit += x[i] * profits[i]

    # Display result
    print("\nResult:")
    print("Object\tWeight\tProfit\tRatio\tTaken")

    for i in range(n):
        print(f"{objects[i]}\t{weights[i]:.2f}\t"
              f"{profits[i]:.2f}\t{ratio[i]:.2f}\t{x[i]:.2f}")

    print(f"\nMaximum profit is: {total_profit:.2f}")


# Main program

n = int(input("Enter the number of objects: "))

if n <= 0 or n > 20:
    print("Invalid number of objects.")
    exit()

objects = []
weights = []
profits = []

print("Enter the weights and profits of each object:")

for i in range(n):
    weight, profit = map(float, input().split())

    objects.append(i + 1)
    weights.append(weight)
    profits.append(profit)

capacity = float(input("Enter the capacity of knapsack: "))

# Call function
knapsack(n, objects, weights, profits, capacity)