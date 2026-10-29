
def knapsack():
    n = int(input("Enter number of items: "))

    wt = list(map(int, input("Enter weights of items:\n").split()))
    val = list(map(int, input("Enter values of items:\n").split()))

    W = int(input("Enter knapsack capacity: "))

    # Create DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if wt[i - 1] <= w:
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    print("\nMaximum value =", dp[n][W])

    # Find selected items (backtracking)
    w = W
    total_weight = 0

    print("Selected items:")

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            print(
                f"Item {i}: Weight = {wt[i - 1]}, "
                f"Value = {val[i - 1]}"
            )

            total_weight += wt[i - 1]
            w -= wt[i - 1]

    print("Total weight =", total_weight)


knapsack()
