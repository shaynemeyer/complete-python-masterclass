# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

sampleText = "Python is a very powerful language"

vowels = frozenset('aeiou')

final_set = set(sampleText).difference(vowels)
print(final_set)

final_list = sorted(final_set)
print(final_list)