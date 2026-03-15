pin = 1234
balance = 6575
entered_pin = int(input("Enter your PIN: "))
if entered_pin == pin:
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        print ("Withdrawal successful")
        balance2 = balance - amount
        print ("Your remaining balance is ", balance2)
    else: 
        print ("Sorry! You don't have enough money for withdrawal. You have", balance, "pounds")
else:
    print ("Incorrect PIN")
