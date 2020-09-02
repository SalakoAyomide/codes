#Football Roaster Program

print("Welcome to the Football Roaster Program")

#Get user input and define the roaster
roaster = []
player = input("Who is your goal keeper? ").title()
roaster.append(player)
player = input("Who is your mid-fielder? ").title()
roaster.append(player)
player = input("Who is your defender? ").title()
roaster.append(player)
player = input("Who is your striker? ").title()
roaster.append(player)
player = input("Who is your utility man? ").title()
roaster.append(player)

#Display roaster
print("\n\tYour starting 5 for the upcoming pre-season")
print("\t\tGoal Keeper is:\t\t" + roaster[0])
print("\t\tMidfielder is:\t\t" + roaster[1])
print("\t\tDefender is:\t\t" + roaster[2])
print("\t\tStriker is:\t\t" + roaster[3])
print("\t\tUtility Man is:\t\t" + roaster[4])

#Remove an injured player
injured_player = roaster.pop(2)
print("\nOh no, " + injured_player + " is injured and is currently unavailable.")

roaster_length = len(roaster)
print("Your roaster only has: " + str(roaster_length) + " players!")

#Add a new player
added_player = input("\nWho will take " + injured_player + "'s spot?").title()
roaster.insert(2, added_player)

#Print the updated list
print("\n\tYour starting 5 for the upcoming pre-season: ")
print("\t\tGoal Keeper is:\t\t" + roaster[0])
print("\t\tMidfielder is:\t\t" + roaster[1])
print("\t\tDefender is:\t\t" + roaster[2])
print("\t\tStriker is:\t\t" + roaster[3])
print("\t\tUtility Man is:\t\t" + roaster[4])

print("\nGoodluck " + roaster[2] + "," + " you will do great!")
roaster_length = len(roaster)

print("\nYour roaster now has " + str(roaster_length) + " players!")