#Grocery List App
import datetime

#Create the datetime object and store current date and time
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)


foods = ["Rice", "Beans"]
print("Welcome to the Grocery List App")

#Local time formatting
print("Current Date and Time: " + time.strftime("%c"))

#No time format
print("Current Date and Time: " + month + "/" + day + "\t" + hour + ":" + minute)

print("\nYou currently have " + foods[0] + " and " + foods[1] + " in your list")

#Get User input
food = input("\nWhat food do you want to add to your list? ")
foods.append(food.title())
food = input("What food do you want to add to your list? ")
foods.append(food.title())
food = input("What food do you want to add to your list? ")
foods.append(food.title())

#Print and sort the list
print("\nHere is your grocery list: ")
print(foods)

foods.sort()
print("\nHere is your grocery list sorted: ")
print(foods)

#Simulate Shopping
print("\nSimulating grocery shopping....")

print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy? ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list.....")

print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy? ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list.....")

print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
buy_food = input("What food did you just buy? ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list.....")

#The store is out of supplies
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods)
no_item = foods.pop()
print("\nSorry, the store is out of " + no_item + ".")

#Add new food items to the grocery list
new_food = input("What food would you prefer to buy instead? ").title()
print("\nAdding " + new_food + " to the list.....")
foods.insert(0, new_food)

new_food = input("What food would you prefer to buy instead? ").title()
print("\nAdding " + new_food + " to the list.....")
foods.insert(0, new_food)

new_food = input("What food would you prefer to buy instead? ").title()
print("\nAdding " + new_food + " to the list.....")
foods.insert(0, new_food)

print("\nHere is what remains on your grocery list: ")
print(foods)