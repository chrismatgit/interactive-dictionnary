import json

# load the json data
data = json.load(open('data.json'))

# function to search for the word in the dictionnary
def searching(word):
    return data[word]

# user should put a word in the command line and save it the variable word
word = input("Enter word: ")

# finally printing the meaning if the word was found
print(searching(word))