
import math

menu = input("Welcome to the Calculator\n[+] ADDITION\n[-] SUBTRACTION\n[*] MULTIPLICATOIN\n[/][DIVISION]\nENTER SIGN: ")

print(f"You have choosen {menu}")      

if menu == "+" or menu == "-" or menu == "/" or menu == "*":
    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))

    if menu == "+":

        print(num1 + num2)

    elif menu == "-":
        print(num1 - num2)

    elif menu == "*":
        print(num1 * num2)

    elif menu == "/":
        if num2 == 0:
            print("Division by Zero Error!")

        else:
            print(num1 / num2)

else:
    print("You are out of bounds!")

