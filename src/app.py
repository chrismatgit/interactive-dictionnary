import json
# import the difflib for checking word similarity
from difflib import get_close_matches

# load the json data
data = json.load(open('data.json'))

# function to search for the word in the dictionnary
def searching(word):
    # putting the user input to the lower case
    word = word.lower()
    # checking if the word exist
    if word in data: 
        return data[word]
    # checking for the word similarity and return a message
    elif len(get_close_matches(word, data.keys())) > 0 :
        return 'Did you mean %s instead please?' % get_close_matches(word, data.keys())[0]
    else:
        return 'The world entered does not exist. Please double check it'

# user should put a word in the command line and save it the variable word
word = input("Enter word: ")

# finally printing the meaning if the word was found
print(searching(word))