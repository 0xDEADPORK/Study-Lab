name = input("Enter your IGN: ")

if len(name) > 12 or not name.find(" ") == -1 or name.isalpha() :
    print("Name cannot be more than 12 character!\nNo Spaces!\nNo Digits!")
else:
    print(f"Welcome {name}")
