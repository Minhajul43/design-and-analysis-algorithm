coins = [25, 10, 5, 1]

amount = int(input("Enter amount: "))
count = 0

for coin in coins:
    d=amount//coin
    count+=d
    amount-=d*coin
    print(f"Number of {coin} is {d}")


print("\nMinimum number of coins =", count)