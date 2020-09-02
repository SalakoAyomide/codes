#Script a letter counter app

print("Welcome to the letter counter app")

name = input("\nWhat is your name? ").title().strip()
print("Hello, " + name + "!")
print("I will count the number of times a specific letter occurs in a message.")
message = input("\nPlease enter a message: ")
letter = input("\nWhat letter would you like me to count? ")

message = message.lower()
letter = letter.lower()

letter_count = message.count(letter)
print(name + "," + " " + "your message has" + " " + str(letter_count) + " " + letter + "'s in it.")
print("Have a nice day! \nWould you need me to run any other message?")
response = input("Yes or No? ")

if response == "Yes":
    print (message)
else:
    print ("Have a nice day!")