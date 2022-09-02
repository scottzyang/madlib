
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!


# declared variables to take in user input
food = input("Favorite Food: ")
number = input("Numberic Value: ")
snack = input("Favorite Snack (plural): ")
feeling = input("Give a word to describe how you feel: ")
activity = input("Favorite Activity (ending in -ing): ")
verb = input("Give me a verb: ") 
place = input("Name of a place: ")

# combines user input into an f-string and prints the text
print(f"Every monday I love eating {food}, it is by far my favorite meal. \nHowever, when I can't have {food}, I typically eat about {number} {snack} in one sitting. It's delicious, it makes me feel {feeling}. \nAfter consuming {number} {snack}, I typically like {activity}, and this requires me to {verb} a lot. \nAfter {activity} I usually head over to {place} for more {snack} because they are addicting. Man, I love {snack}.")



































# --------------------------------------------------
# Partial solution
























# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")