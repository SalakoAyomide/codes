#Develop a miles per hour conversion app

print("Good day! Welcome to the Miles per Hour Conversion App")

#Gather user input
name = input("\nWhat is your name? ").title().strip()
print("\nHello, " + name +"!")

milesTravelled = float(input("Kindly enter the amount of miles spent on your way to school this morning: "))
milesTravelled = int(milesTravelled)

#carry out the conversion
milesPerSec = milesTravelled*0.4474
milesPerSec = round(milesPerSec, 2)

print("\nYour speed in meters per seconds is " + str(milesPerSec) + "!")
