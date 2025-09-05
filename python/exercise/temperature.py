unit = input("Is this temperature in Celcius or Fahrent? [C] or [F]: ")


if unit == "C":
    temp = float(input("Enter the temperature: "))
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"The temperature in Fahrenheit is: {temp} Fahrenheit")

elif unit == "F":
    temp = float(input("Enter the temperature: "))
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"The temperature in Celcius is: {temp} Celcius")
    pass
else:
    print(f"{unit}: Unit Invalid!")
