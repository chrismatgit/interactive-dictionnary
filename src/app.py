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
        # prompting the user to comfirm similarity check
        yes_no = input('Did you mean %s instead please? Enter Y if yes, or N if no: ' % get_close_matches(word, data.keys())[0])
        if yes_no == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yes_no == 'N':
            return 'The world entered does not exist. Please double check it'
        else:
            return 'Sorry! We did not understand your entry...'
    else:
        return 'The world entered does not exist. Please double check it'

# user should put a word in the command line and save it the variable word
word = input("Enter word: ")

# finally printing the meaning if the word was found
print(searching(word))