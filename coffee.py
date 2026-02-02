amount_due = 75

while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("insert Coin:  "))
    if coin in [50, 20, 20, 5]:
        amount_due -= coin
        print ("Changed owned:", abs(amount_due))