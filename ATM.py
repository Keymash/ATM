balance = 194.68
fee ='%.2f' % 2.50
print("Balance: $" + str(balance))
print("Enter withdrawel amount:\nMust be a multiple of 20 or 50\nWithdrawel Fee: $" + fee)
withdraw = float(input())
if withdraw + float(fee) <= balance:
    if withdraw % 20 == 0 or withdraw % 50 == 0:
        balance -= withdraw + float(fee)
        print("New Balance: $" + str(balance))
    else:
        print("Not a multiple of 20 or 50.\nBalance Unchanged: $" + str(balance))
else:
    print("Insufficient Funds.\nBalance Unchanged: $" + str(balance))
