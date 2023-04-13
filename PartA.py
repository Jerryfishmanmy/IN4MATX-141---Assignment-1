import sys
import re
import time

# The runtime complexity of this function is O(N), where N is the number of words in the text file. the function
# is iterating through each lines in the text file, which is O(1) each time, ending up being O(N).
def tokenize(TextFilePath) -> list:
    with open(TextFilePath, "r") as f:
        lines = f.read()
    tokens = re.findall(r"\b[a-zA-Z0-9]+\b", lines.lower())
    return tokens


# The runtime complexity of this function is O(N), where N is the number of words in tokens.
# This function iterates through tokens to return the frequency of each word, worst case scenario is that all
# the words in the tokens are unique, and the program has to run through all the items in the list with a time
# of O(1) each, which concludes to O(N).
def computeWordFrequencies(tokens) -> dict:
    frequency = {}
    for word in tokens:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


# The runtime complexity of this function is O(NlogN), since the function sorted() takes O(NlogN).
# In addition, iterating through a dictionary takes O(N), however, the function sorted() dominates most of the
# runtime complexity, we can assume that the runtime complexity for the whole function is O(NLogN).
def printFrequency(frequency):
    sort_by_words = dict(sorted(frequency.items(), key=lambda x:x[0]))
    sort_by_frequency = dict(sorted(sort_by_words.items(), key=lambda x:x[1], reverse=True))
    for word, count in sort_by_frequency.items():
        print(f"{word} -> {count}")

if __name__ == "__main__":
    text = sys.argv[1] #https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
    start_time = time.time()
    token = tokenize(text)
    frequency = computeWordFrequencies(token)
    printFrequency(frequency)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")






