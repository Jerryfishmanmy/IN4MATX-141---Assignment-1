import PartA as a
import sys


# The run time complexity of this program is O(N). The code first creates two sets, store1 and store2,
# containing the unique words in each file. The time complexity of creating these sets is O(n1 + n2),
# where n1 is the number of unique words in file1 and n2 is the number of unique words in file2.
# The code iterates through each word in store1, which takes O(n1) time. For each word, it checks if
# it is in store2, which takes O(1) time on average due to the use of a set. If the word is in store2,
# it adds it to the common_words set. Finally, the code iterates through common_words and prints each word,
# which takes O(N) time, where N is the number of words in common_words. In conclusion, the average runtime
# complexity of this program is O(N).
def inCommon(file1, file2) -> int:
    common_words = set() # creates a set to store unique words
    store1 = set(a.tokenize(file1)) # tokenizes first text file
    store2 = set(a.tokenize(file2)) # tokenizes second text file
    for word in store1:  # loops through all the words in store1
        if word in store2: # if the word from store1 is also in store 2, the word will be added to common_words
            common_words.add(word)
    print("Intersected words:")
    for word in common_words:
        print(word) # loops through the set and print all the words
    return len(common_words) # return the amount of duplicated words between two text files

if __name__ == "__main__":
    text1 = sys.argv[1] #https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
    text2 = sys.argv[2]
    print(f"Total Intersection of two files: {inCommon(text1, text2)}")
