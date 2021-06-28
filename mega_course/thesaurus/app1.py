import json
from difflib import get_close_matches

data = json.load(open('./data.json'))


def get_result_str(l):
    str = ''
    for index, string in enumerate(l):
        str = str + \
            f'{string}\n' if index != (len(l) - 1) else str + f'{string}'

    return str


def translate(w):
    lowercase_w = w.lower()
    uppercase_w = w.upper()
    title_w = w.title()
    if (lowercase_w in data):
        return get_result_str(data[lowercase_w])
    elif (title_w in data):
        return get_result_str(data[title_w])
    elif (uppercase_w in data):
        return get_result_str(data[uppercase_w])
    elif get_close_matches(lowercase_w, data.keys()):
        closest_match = get_close_matches(lowercase_w, data.keys())[0]
        yn = input(
            "Did you mean \"%s\" instead? Enter Y if yes, or N if no: " % closest_match)
        if yn.lower() == 'y':
            return get_result_str(data[closest_match])
        elif yn.lower() == 'n':
            word = input('Enter word: ')
            return translate(word)
        else:
            return "Cannot recognize you choice. Restart the program"
    else:
        return "The word doesn't exist. Please double check it!"


word = input('Enter word: ')
print(translate(word))
