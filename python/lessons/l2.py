# STRING, INTEGERS, FLOAT, BOOLEAN

#STRINGS
first_name = "REGISTER"
food = "PIZZA"
email = "fakegmail@email.com"

print(f"WE ARE ABOUT TO {first_name}")
print(f"{food} IS GOOD")
print(f"EMAIL IS {email}")

#INTEGERS
AGE = 26
QUANTITY = 3

print(f"AGE IS {AGE}")
print(f"NUMBER IS {QUANTITY}")

#FLOAT

PRICETAG = 10.99
GPA = 3.2
DISTANCE = 5.5

print(f"The price is {PRICETAG}")
print(f"YOUR GRADE IS {GPA}")
print(f"YOU RAN FOR {DISTANCE} KM")

#BOOLEAN

is_student = True
for_sale = True

print(f"Are you a student? {is_student}")

if is_student:
    print("You are student")

else:
    print("Not a student")

if for_sale:
    print("For sale!")
else:
    print("Not available!")
