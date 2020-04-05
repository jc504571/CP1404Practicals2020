"""
CP1404 Practical
Count the occurrence of words in a string
"""
word_to_count = {}
text = input("Text: ")

words = text.split()
for word in words:
    frequency_of_word = word_to_count.get(word, 0)
    word_to_count[word] = frequency_of_word+ 1

words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))