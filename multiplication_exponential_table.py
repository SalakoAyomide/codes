#Multiplication/Exponental Table Program

print("Welcome to the next challenge lab; what is your name?")

#Get user inputs
name = input("\nMy name is: ").title().strip()
print("\nHello " + name + "!" + "This is the Multiplication/Exponential table program")
num = (input("\nKindly enter the number you would like to work with: "))
num = float(num)

message = ("Hey " + name + "," + " Mathematics is really cool!")

#Multiplication table program
print("\nThe Multiplication table for " + str(num) + " is: ")
print("\n1.0 * " + str(num) + " = " + str(1*num)) 
print("2.0 * " + str(num) + " = " + str(2*num)) 
print("3.0 * " + str(num) + " = " + str(3*num)) 
print("4.0 * " + str(num) + " = " + str(4*num)) 
print("5.0 * " + str(num) + " = " + str(5*num)) 
print("6.0 * " + str(num) + " = " + str(6*num)) 
print("7.0 * " + str(num) + " = " + str(7*num)) 
print("8.0 * " + str(num) + " = " + str(8*num)) 
print("9.0 * " + str(num) + " = " + str(9*num)) 
print("10.0* " + str(num) + " = " +str(10*num)) 

#Exponential table program
print("\nThe Exponential table for " + str(num) + " is: ")
print("\n" + str(num) + "** " + "1.0" + " = " + str(num**1))
print( str(num) + "** " + "2.0" + " = " + str(num**2))
print(str(num) + "** " + "3.0" + " = " + str(num**3))
print(str(num) + "** " + "4.0" + " = " + str(num**4))
print(str(num) + "** " + "5.0" + " = " + str(num**5))
print(str(num) + "** " + "6.0" + " = " + str(num**6))
print(str(num) + "** " + "7.0" + " = " + str(num**7))
print(str(num) + "** " + "8.0" + " = " + str(num**8))
print(str(num) + "** " + "9.0" + " = " + str(num**9))
print(str(num) + "** " + "10.0" + "= " + str(num**10))

print(message)
print("\t" + message.title())
print("\t\t" + message.lower())
print("\t\t\t" + message.upper())

