sentence = input("Enter a sentence: ")

words=sentence.split()
word_count = len(words)
print("the split words are:", words)  # Show the split words
print(f"The number of words in the sentence is: {word_count}")