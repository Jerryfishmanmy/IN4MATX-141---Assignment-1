import PartA as a
import time
import sys


def inCommon(file1, file2) -> int:
    common_words = set()
    store1 = set(a.tokenize(file1))
    store2 = set(a.tokenize(file2))
    for word in store1:
        if word in store2:
            common_words.add(word)
    for word in common_words:
        print(word)
    return len(common_words)

if __name__ == "__main__":
    text1 = sys.argv[1] #https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
    text2 = sys.argv[2]
    start_time = time.time()
    print(inCommon(text1, text2))
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
