import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]

    elif word.upper() in data:
        return data[word.upper]

    elif word.title() in data:
        return data[word.title]

    elif len(get_close_matches (word, data.keys())) > 0 :
        print ("do you mean %s instead?" % get_close_matches (word, data.keys()) [0])
        decide = input("enter yes or no")
        if decide == "yes":
             return data [get_close_matches (word, data.keys()) [0]]
        elif decide == "no":
            return ("Try another word; you have entered the wrong word")
        else:
            return ("kindly, enter yes or no")
        
    else:
        print("Try another word; you have entered the wrong word")

word = input("What are you searching for?")
output = translate(word)
print(output)