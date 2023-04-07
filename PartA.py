
import re

def tokenize(TextFilePath) -> list:
    with open(TextFilePath, "r") as f:
        lines = f.read()
    tokens = re.findall(r"\b\w+\b", lines.lower())
    return sorted(tokens)

def computeWordFrequencies(tokens) -> dict:
    frequency = {}
    for word in tokens:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def printFrequency(frequency):
    sorting = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
    frequency_dict = {word: count for word, count in sorting}
    for word, count in frequency_dict.items():
        print(f"{word} -> {count}")


token = tokenize("test1.txt")
frequency = computeWordFrequencies(token)
printFrequency(frequency)
