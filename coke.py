def main():
    amount_due=50
    coins=[25, 10, 5]

    while amount_due > 0:
        print("Amount Due:",amount_due)
        coin = int(input("Insert Coin: "))

        if coin in coins:
            amount_due -= coin
    
    print("Change Owed:",abs(amount_due))
        

main()
