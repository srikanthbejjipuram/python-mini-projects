
# take the user input

ATM_PIN = int(input("Enter the ATM PIN: "))

BALANCE = 5000

# check the ATM PIN (7799)

if ATM_PIN != 7799:
    print("ATM PIN is incorrect")
else:

    # Show the Options

    print("1. Change PIN\n2. View Balance\n3. Withdraw Amount\n4. Deposit Amount")
    
    choice = int(input("Enter the choice: "))
    

    # for change pin

    if choice == 1:

        NEW_PIN = int(input("Enter New PIN: "))
        CONFIRM_NEW_PIN = int(input("Re-Enter New PIN: "))

    # check new pin

        if NEW_PIN == CONFIRM_NEW_PIN:
            print("ATM PIN is updated")
        else:
            print("Not Matched")
    
    # check the balance

    if choice == 2:
        print("Balance:",BALANCE)

    # withdraw amount

    if choice == 3:
        REQUIRED_AMOUNT = int(input("Amount: "))
        
        if REQUIRED_AMOUNT > BALANCE:
            print("Insufficient Balance in your Account")
        elif REQUIRED_AMOUNT <= 0:
            print("Minimum Balance Should be 100 Rupees")
        else:
            print("Withdrawal Successfull")

    # deposit amount

    if choice == 4:
        DEPOSIT_AMOUNT = int(input("Enter the amount to be deposit: "))
        MIN_DEPOSIT = 100

        if DEPOSIT_AMOUNT >= MIN_DEPOSIT:
            print("Successfully Deposited in your Account")
        else:
            print("Minimum Deposit Amount should be 100")


















