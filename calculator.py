def calculator():
    val_1 = float(input("Enter your first value: ")) # input for operation
    operator = input("Enter operator (+,-,*,/): ")
    val_2 = float(input("Enter your second value: "))

#conditional statements 
    if operator == "+":
        print("the value is:",val_1 + val_2)
    elif operator == "-":
        print("the value is:",val_1 - val_2)
    elif operator == "*":
        print("the value is:",val_1 * val_2)
    elif operator == "/":
        if val_2 == 0:
            print("invalid!!")
        else:    
            print("the value is:",val_1 / val_2)
    else:
        print("invalid input!!")    



while True:
    calculator()
    again = input("calculate again?:(y/n): ")
    if again == "n":
        break
