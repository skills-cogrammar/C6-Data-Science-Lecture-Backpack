# A mock-banking system that deposits and withdraws funds.
correct_username="zahir"
correct_password="pass123"
balance=0.0
not_logged_in=True

class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds. Withdrawal amount exceeds balance."):
        super().__init__(message)

           
while not_logged_in:
    # Get the username and password
    username=input("Enter username:")
    password=input("Enter password:")

    if username == correct_username and password == correct_password:
        print("Login successful!\n")
        not_logged_in=False
    else:
        print("Incorrect username and password. Please try again!")

while True:
    try:
        print(f"Hi {username}, your current balance is ${balance:,}")
        print('''
            1 - Deposit Funds
            2 - Withdraw Funds
            3 - Exit
        ''')
        
        choice=input("Choose your option:")
        if choice == "1":
            # Ask for input from the user
            amount= float(input("Enter the deposit amount:"))
            # Add to the balance
            balance += amount
            # print new balance
            print(f"Deposit successful. Your new balance is ${balance:,}\n")
        elif choice == "2":
            # Ask for the amount to withdraw
            amount=float(input("Enter the amount to withdraw: "))
            if amount > balance:
                raise InsufficientFundsError
            else:
                balance -= amount # Deduct the amount from the balance
                print(f"Withdrawal successful. Your new balance is ${balance:,}\n")
        elif choice == "3":
            print(f"Cheers {username}, Come again!")
            break
        else:
            print("Invalid choice. Enter option 1/2/3.\n")
    except:
        print("Theres something wrong with your input.")


