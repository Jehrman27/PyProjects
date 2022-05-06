"""
Igpay Atinlay Converter

This program takes in a phrase from the user and converts it to Pig Latin
using the standard rules from Wikipedia:
-For words that begin with consonant sounds, all letters before the initial
    vowel are placed at the end of the word sequence. Then, "ay" is added.
-When words begin with consonant clusters, the whole sound is added to the end.
-For words that begin with vowel sounds, 'yay' is appended to the end, 
    with no modifications to the beginning onset.
"""
import re


def str_cluster(word):
    """Returns the position of the end of the starting consonant cluster."""
    position = 0
    vowels = 'aeiuo'
    for letter in word:
        if letter in vowels:
            return position
        else:
            position += 1


print('Igpay Atinlay Converter')
print('This program will convert English phrases into Pig Latin.')

user_input = input('Please enter the phrase you want to convert: ')

# Parse user input by words and punctuation.
input_split = re.findall(r"[\w']+|[\w'\w]+|[.,!?]",user_input)

# Convert words to pig latin, while leaving punctuation in place.
igpayed = ''
for item in input_split:
    if re.search(r"[.,!?]",item):
        igpayed += (item + " ")
        continue
    else:
        pos = str_cluster(item)
        if pos == 0:
            igpayed += (item + "yay ")
        else:
            x = item[pos:]
            x += item[:pos]
            igpayed += (x + "ay ")
            
print(igpayed)
