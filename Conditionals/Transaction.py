balance = 1000

customer = input("Deposit or Withdrawal: ")

if customer == "deposit":
    take_in = int(input("Enter amount: "))
    deposit_final = balance + take_in
    print ("Final statement:" , deposit_final)
elif balance <= 0:
    print("you cannot have a negative balance")
elif customer == "withdrawal":
    take_out = int(input("Enter amount: "))
    withdrawal_final = balance - take_out
    if withdrawal_final < 0:
        print("you cannot have a negative balance, try again")
    else:
        print ("Final statement: " , withdrawal_final)
else:
    print ("Invalid transation.")