#Grade Sorter App

name = input("Welcome and what is your name?  ").title().strip()

print("\n" + name + "," + " Welcome to the Grade Sorter App!")


#getting users grade inputs and putting it in a list
grades = []
grade = float(input("\nEnter your first grade (0-100):  "))
grades.append(grade) 
grade = float(input("Enter your second grade (0-100):  "))
grades.append(grade)  
grade = float(input("Enter your third grade (0-100):  "))
grades.append(grade) 
grade = float(input("Enter your fourth grade (0-100):  "))
grades.append(grade) 

print("\nYour grades are " + str(grades))

#Sort the list from highest to lowest

grades.sort(reverse=True)
print("\nYour grades from Highest to lowest are " + str(grades))

#Removing the lowest two grades.
print("\nDon't worry! The lowest grade would be removed!")
removed_grade = grades.pop()
print ("\nYour grade, " + str(removed_grade) + " has been removed!")
removed_grade = grades.pop()
print ("Your grade, " + str(removed_grade) + " has been removed!")

#Print remaining grades
print("\nYour remaining grades are: " + str(grades) + " and your Highest grade is, " + str(grades[0]) + "!")

print("\nNice work!")