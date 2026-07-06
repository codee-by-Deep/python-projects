def add_expense():
    # Add expense
    name = input("Name of the expense: ")
    amount = input("Enter the amount: ")
    with open('expenses.txt','a') as f:
        f.write(f"{name},{amount}\n")

    print("Expense saved")    

def view_expense():
    # Read expense
    with open("expenses.txt","r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split(",")
        print(f"Expense: {parts[0]} Amount: {parts[1]}")
    
def show_total():
    total = 0
    with open("expenses.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            part = line.strip().split(",")
            total = total + float(part[1])
        print("The total expenses: ",total)    

def menu():
     while True:
            print("\n---Expense Tracker---")
            print("1. Add Expense")
            print("2. View all Expenses")
            print("3. Show Total Expenses")
            print("4. Exit")    

            choice = input("choose from this options: ")

            if choice == "1":
                add_expense()
            elif choice == "2":
                view_expense()
            elif choice == "3":
                show_total()
            elif choice == "4":
                print("Goodbye")
                break    
            else:
                print("Invalid choice, try again")

menu()
