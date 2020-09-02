#Welcome the user
import math 

#get user input
name = input("Good day and what is your name? ").title().strip()
print("\n " + name + "!" + " Welcome to the Triangle App!")
side_1 = input("Kindly enter the length of the first side of the triangle: ")
side_2 = input("Kindly enter the length of the second side of the triangle: ")

side_1 = float(side_1)
side_2 = float(side_2)

#Calculations
side_3 = math.sqrt(side_1**2 + side_2**2)
side_3 = round(side_3, 2)
area = side_1*side_2*0.5
area = round(area, 2)

print("\n" + name + "!" + "\nThe hypothenuse of your triangle is " + str(side_3) + " and the area is " + str(area) + "!")