#Convert Temperature from Farenheit to Celsius
name = input("What is your name? ").title().strip()
print("\nHi"+ " " + name+"!" + "\nWelcome to Temperature Conversion App!")

tempF = float(input("\nWhat is the temperature in Fahrenheit?"))
tempF = int(tempF)

tempC = (float(tempF - 32)*0.55556)
tempC = round(tempC, 2)
tempK = (float(tempC + 273.15))
tempK = round(tempK, 2)

print("\n"+name +"!"+ "\nYour temperature is " + str(tempC) + " in Celsius, and " + str(tempK) + " in Kelvin!" )
print("\nHave a nice day!")

