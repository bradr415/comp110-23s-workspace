"""Exercise 2 - Chardle"""

__author__ = "730576359"

word = input("enter a 5-character word: ")

if int(len(word)) != 5:
    print("error: word must contain 5 letters")
    exit()

character =  input("enter a single character: ")

if int(len(character)) != 1:
    print("error: character must be a single character")
    exit()

counter = int(0)

print("searching for " + str(character) + " in " + str(word))

if word[0] == str(character):
    print(str(character) + " found at index 0")
    counter = counter + 1

if word[1] == str(character):
    print(str(character) + " found at index 1")
    counter = counter + 1

if word[2] == str(character):
    print(str(character) + " found at index 2")
    counter = counter + 1


if word[3] == str(character):
    print(str(character) + " found at index 3")
    counter = counter + 1


if word[4] == str(character):
    print(str(character) + " found at index 4")
    counter = counter + 1


if counter == int(0):
    print("no instances of " + (character) + " found in "+ (word))
else:
    counter != int(1)
    print(str(counter) + " instances of " + (character) + " found in " + (word))
    counter == int(1)
    print(str(counter) + " instance of " + (character) + " found in " + (word))

