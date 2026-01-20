# Create a program that can manage bank accounts like a real system.

def show_menu():
    print("\n----- BANK MANAGEMENT SYSTEM -----")
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Delete Account")
    print("7. Exit")

def load_acc():
    accounts = {}
    try:
        with open("accounts.txt","r")as f:
            for line in f:
                name, acc_no, age, balance = line.strip().split(" | ")
                accounts[acc_no] = {
                    "name":name,
                    "age":age,
                    "balance": float(balance)
                }
    except FileNotFoundError:
        pass
    return accounts

def save_accounts(accounts):
    with open("accounts.txt", "w") as f:
        for acc_no, data in accounts.items():
            f.write(f"{data['name']} | {acc_no} | {data['age']} | {data['balance']}\n")


def create_acc(accounts):
    
    print("\nSet 5 Digits Account Number ")
    acc_no = input("Set 5 digit account no.: ")
    if not acc_no.isdigit() or len(acc_no) != 5:
        print("Account number must be exactly 5 digits")
        return

    if acc_no in accounts:
        print("Account number aleady exist")
        return
        
    name = input("Enter Account Holder name: ")
    age = input("Enter Account Holder age: ")

    while True:
        try:
            init_balance = float(input("Enter initial balance: "))
            if init_balance < 500:
                print("Minimum balance should be 500")
            else:
                break
        except ValueError:
            print("Enter valid amount")
        
    accounts[acc_no] = {'name':name, 'balance':init_balance, 'age':age}
    save_accounts(accounts)
    print("Account created successfully!")
    
    
def view_all_acc(accounts):
    if not accounts:
        print("No Accounts Found")
        return

    print("\nName | Account Number | Age | Balance")
    for acc_no, data in accounts.items():
        print(f"{data['name']} | {acc_no} | {data['age']} | ₹{data['balance']:.2f}")



def search_acc(accounts):
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        data = accounts[acc_no]
        print("\nAccount Found")
        print(f"Name    : {data['name']}")
        print(f"Age     : {data['age']}")
        print(f"Balance : ₹{data['balance']:.2f}")

    else:
        print("Account not found")



def dep_money(accounts):
    acc_no = input("Enter your account number: ")
    if acc_no not in accounts:
        print("Account not found")
        return
    
    while True:
        try: 
            dep_balance = float(input("Enter deposit amount: "))
            if dep_balance <= 0:
                print("Amount must be positive")
            else:
                break
        except ValueError:
            print("Enter valid amount")

    accounts[acc_no]["balance"] += dep_balance
    save_accounts(accounts)
    print("Money deposited successfully!")


def withdraw_money(accounts):
    acc_no = input("Enter your account number: ")
    if acc_no not in accounts:
        print("Account not found")
        return
    
    while True:
        try:
            with_bal = float(input("Enter withdrawal amount: "))
            if with_bal <= 0:
                print("Amount must be positive")
            elif with_bal > accounts[acc_no]["balance"]:
                print("Insufficient balance")
            else:
                break
        except ValueError:
            print("Enter valid amount!")
    
    accounts[acc_no]["balance"] -= with_bal
    save_accounts(accounts)
    print("Money withdrawal successfully!")


def delete_account(accounts):
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        confirm = input("Are you sure? (yes/no): ").lower()
        if confirm == "yes":
            del accounts[acc_no]
            save_accounts(accounts)
            print("Account deleted successfully")
    else:
        print("Account not found")

while True:
    accounts = load_acc()
    show_menu()
    try:
        choice = int(input("Enter a number: "))
        
        if choice == 1:
            create_acc(accounts)
        elif choice == 2:
            view_all_acc(accounts)
        elif choice == 3:
            search_acc(accounts)
        elif choice == 4:
            dep_money(accounts)
        elif choice == 5:
            withdraw_money(accounts)
        elif choice == 6:
            delete_account(accounts)
        elif choice == 7:
            print("Thank you for using our banking system")
            break
        else:
            print("Enter valid number")

    except ValueError:
        print("Invalid input!")

        