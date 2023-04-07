import PartA as a

def inCommon(file1, file2) -> int:
    common_words = set()
    store1 = a.tokenize(file1)
    store2 = a.tokenize(file2)
    for word in store1:
        if word in store2:
            common_words.add(word)
    for word in common_words:
        print(word)
    return len(common_words)

print(inCommon("text2.txt", "text3.txt"))