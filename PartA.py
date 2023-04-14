import sys
import re

# The runtime complexity of this function is O(N), where N is the number of words in the text file.
# The function reads through each line in the file one at a time, so the loop runs in O(N) time where N
# is the number of lines in the file. For each line, the re.findall() function is called to find all the
# words and tokenize them. Since the function is called once for each line, the overall runtime complexity
# of the function is O(n), where n is the total number of words in the file.
def tokenize(TextFilePath) -> list:
    tokens = [] # creates a list to store the tokenized words
    with open(TextFilePath, "r") as f:
        for line in f: # reads through all the lines in the text file one line at a time
            extended_tokens = re.findall(r"\b[a-zA-Z0-9]+\b", line.lower()) # finds all the words and tokenizes them
            tokens.extend(extended_tokens) # combines both lists together to get one list
    if len(tokens) == 0:
        print(f"{TextFilePath} is empty")
    return tokens # returns a list with all tokens


# The runtime complexity of this function is O(N), where N is the number of words in tokens.
# This function iterates through tokens to return the frequency of each word, worst case scenario is that all
# the words in the tokens are unique, and the program has to run through all the items in the list with a time
# of O(1) each, which concludes to O(N).
def computeWordFrequencies(tokens) -> dict:
    frequency = {} # creates a dictionary to store and return
    for word in tokens: # loop through all the words in the list
        if word in frequency: # if the word exists in the dictionary frequency, the frequency of the word increments itself by 1
            frequency[word] += 1
        else: # if the word doesn't exist in the dictionary frequency, the word is added as a key, and set with a value 1
            frequency[word] = 1
    return frequency # returns the completed dictionary


# The runtime complexity of this function is O(NlogN), since the function sorted() takes O(NlogN).
# In addition, iterating through a dictionary takes O(N), however, the function sorted() dominates most of the
# runtime complexity, we can assume that the runtime complexity for the whole function is O(NLogN).
def printFrequency(frequency):
    sort_by_words = dict(sorted(frequency.items(), key=lambda x:x[0]))  # sorts the dictionary in alphabetical order
    sort_by_frequency = dict(sorted(sort_by_words.items(), key=lambda x:x[1], reverse=True)) # sorts the dictionary by the words' frequency
    for word, count in sort_by_frequency.items(): # prints the word in order after sorting
        print(f"{word} -> {count}")

if __name__ == "__main__":
    text = sys.argv[1] #https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
    try:
        print("Word Frequencies:")
        token = tokenize(text)
        frequency = computeWordFrequencies(token)
        printFrequency(frequency)
    except FileNotFoundError:
        print("File doesn't exist") # print if file typed in doesn't exist


