#Different types of lists

print("Welcome to the List Summary Program")

#List definitions
num_strings = ['45', '190', '101', '96']
num_ints = [32, 89, 100, 65]
num_floats = [4.32, 1.43, 55,76, 0.45]
num_lists = [[1,2,3], [4,5,6], [7,8,9]]

#Summary of each lists
print("\n\t\tSUMMARY TABLE")

print("\nThe variable num_strings is a " + str(type(num_strings)))
print("The elements contained are: " + str(num_strings))
print("The elements: " + str(num_strings) + " are " + str(type(num_strings[0])))


print("\nThe variable num_ints is a " + str(type(num_ints)))
print("The elements contained are: " + str(num_ints))
print("The elements: " + str(num_ints) + " are " + str(type(num_ints[0])))

print("\nThe variable num_ints is a " + str(type(num_floats)))
print("The elements contained are: " + str(num_floats))
print("The elements: " + str(num_floats) + " are " + str(type(num_floats[0])))

print("\nThe variable num_ints is a " + str(type(num_lists)))
print("The elements contained are: " + str(num_lists))
print("The elements: " + str(num_lists) + " are " + str(type(num_lists[0])))

#Sorting the lists
num_strings.sort()
num_ints.sort()
num_floats.sort()
num_lists.sort()

print("\nNow sorting all lists are requested..........")
print("\nSorted num_strings: " + str(num_strings))
print("Sorted num_ints: " + str(num_ints))
print("Sorted num_floats: " + str(num_floats))
print("Sorted num_lists: " + str(num_lists))

print("\nStrings are sorted Alphabetically while Integers are sorted Numerically!!!")