# What are all of the words containing UU?
print("Question: 1")
with open("sowpods.txt") as f: #Learn this way of importing the words with the help of Chris and Stephen
    words = [] # Made an empty list I can use to import the words to
    key = "UU" # Key is what I am looking for
    for line in f: # Go through every word
        line = line.strip("\n") # This removes the seperate lines and turns all the words into a long list
        if line.find(key) != -1: # -1 mean find() could not find the word. Adding the != is like having two negatives in math, which they are converting it to a positive.This means if the .find() can find the "key"..
            words.append(line) #.. than append the word to the end of the empty list.
print(words)
print("\n")

# What are all of the words containing an X and a Y and a Z?
print("Question: 2")
keys = "XYZ"
def hasLetters(word): # Creating a function
    for key in keys: # that goes through the letters in keys
        if key not in word: # if the word does not have all letters
            return False# Do not store it
    return True # If it does, sotre it.

with open("sowpods.txt") as f:
    words = []
    for line in f:
        line = line.strip("\n")
        if hasLetters(line): # Run function
            words.append(line) # append it to empty list
print(words) # Print out list of words that have all letters in keys.


# What are all of the words containing a Q but not a U?
print("Question: 3")
with open("sowpods.txt") as f:
    words = []
    key = "Q"
    lock = "U" # added an extra var that is opposite to key
    for line in f:
        line = line.strip("\n")
        if line.find(key) != -1:
            if lock not in line: # making sure lock is not found
                words.append(line)
print(words)

# What are all of the words that contain the word CAT and are exactly 5 letters long?
print("Question: 4")
with open("sowpods.txt") as f:
    words = []
    key = "CAT"
    for line in f:
        line = line.strip("\n")
        if line.find(key) != -1:
            if 5 == len(line): # Looking for words with a length of 5
                words.append(line)
print(words)

# def longestLength(words):
#     finalList = []

#     for word in words:
#         finalList.append((len(word), word))

#     finalList.sort()

#     print("The word with the longest length is:", finalList[-1][1],
#           " and length is ", len(finalList[-1][1]))

# with open("sowpods.txt") as f:
#     words = []
#     key = "CAT"
#     # lock = 5==len(line)
#     longestLength(f)

# I used this function to find out what is the longest word in the list. I found out it is "ZYGOPHYLLACEOUS"


# What are all of the words that have no E or A and are at least 15 letters long?
print("Question: 5")
with open("sowpods.txt") as f:
    words = []
    for line in f:
        line = line.strip("\n")
        key = ["E","A"]
        noKey = True # A function needs to have a True boolien in order to work
        for letter in line:
            if letter in key:
                noKey = False # If the word has a letter that it is in key, I dont want it to store it
        if noKey == True: # I am looking for the words with out the key
            if 15 <= len(line): # ensuring the words are 15 or greater
                words.append(line)
print(words)

# What are all of the words that have a B and an X and are less than 5 letters long?
print("Question: 6")
keys = "XB"
def hasLetters(word): # Creating function
    for key in keys: # goes through the letters
        if key not in word: # if the word does not have the letters, do not store it
            return False
    return True # if it has the letters store it in the function

with open("sowpods.txt") as f:
    words = []
    for line in f:
        line = line.strip("\n")
        if 5 > len(line): # making sure word is less than 5 letters
            if hasLetters(line): # running function
                words.append(line)
print(words)

# What are all of the words that start and end with a Y?
print("Question: 7")
with open("sowpods.txt") as f:
    words = []
    for line in f:
        line = line.strip("\n")
        if (line[-1] == line[0]): # making sure first and last letters are the same using indexes
            if line[0] == "Y": # just need to make sure the first letter is what I am looking for
                words.append(line)
print(words)

# What are all of the words with no vowel and not even a Y?
print("Question: 8")
keys = "AEIOUY"
def hasNoKeys(word): # making a function
    for key in keys:
        if key in word: # that is not saving the words with key letters
            return False
    return True # but saving the words without them

with open("sowpods.txt") as f:
    words = []
    for line in f:
        line = line.strip("\n")
        if hasNoKeys(line): # running function
            words.append(line)
print(words)

# What are all of the words that have all 5 vowels, in any order?
print("Question: 9")
keys = "AEIOU"
def hasVowels(word): # making function that
    for key in keys:
        if key not in word: # is saving words with vowels
            return False
    return True

with open("sowpods.txt") as f:
    words = []
    for line in f:
        line = line.strip("\n")
        if hasVowels(line): # run function to save words with all vowels
            words.append(line)
print(words)

# What are all of the words that have all 5 vowels, in alphabetical order?
print("Question: 10")
keys = "AEIOU"
def hasVowels(word): # making function that
    for key in keys:
        if key not in word: # is saving words with vowels
            return False
    return True

def vowelsInOrder(word): # making function that
    n = len(word)
    c = chr(64) # part of the ACSII, start at the beginning of the alphabet
    for i in range(0, n): # goes down the 'range' of the word ("0" is the first letter, "n" is the last letter of the word)
        if (word[i] == 'A' or word[i] == 'E' or word[i] == 'I' or word[i] == 'O' or word[i] == 'U' ):
            if word[i] < c: # if the vowel is smaller than the previous vowel
                return False
            else:
                c = word[i] # save it
    return True


with open("sowpods.txt") as f:
    words = []
    for line in f:
        line = line.strip("\n")
        if hasVowels(line): # run function to save words with all vowels
            if vowelsInOrder(line): # run function to only save words with vowels in alphabetical order.
                words.append(line)
print(words)



print("Setting up storage to use during a for loop, including counters and arrays")

# How many words contain the substring "TYPE”?
print("Question: 11")

with open("sowpods.txt") as f:
    words = []
    key = "TYPE"
    for line in f:
        line = line.strip("\n")
        if line.find(key) != -1:
            words.append(line)
print(len(words))

# Create and print an array containing all of the words that end in "GHTLY"
print("Question: 12")

empty=[]
def lastFour(word):
    if word[-5:] == "GHTLY": # This function only sees the last 5 letters of each word and I ask it to match it with 'GHTLY' in order to return
        return word

with open("sowpods.txt") as f:
    words = []
    key = "TYPE"
    for line in f:
        line = line.strip("\n")
        if lastFour(line):
            words.append(line)
print(words)

# # What is the shortest word that contains all 5 vowels?
# print("Question: 13")
# keys = "AEIOU"
# def hasVowels(word): # making function that
#     for key in keys:
#         if key not in word: # is saving words with vowels
#             return False
#     return True

# def findShortest(lst):
#     length = len(lst)
#     short = len(lst[0])
#     for x in range(1, length):
#         if len(lst[x]) < short:
#             ret = x
#             short = lst[x]


#     return x # return the index of the shortest sentence in the list

# with open("sowpods.txt") as f:
#     words = []
#     for line in f:
#         line = line.strip("\n")
#         if hasVowels(line):
#             if findShortest(line):
#                 words.append(line)
