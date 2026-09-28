coins = [25, 10, 5, 1]

amount = int(input("Enter amount: "))
count = 0

for coin in coins:
    while amount >= coin:
        amount -= coin
        count += 1
        print(coin, end=" ")

print("\nMinimum number of coins =", count)