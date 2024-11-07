"""
CP1404 prac 5
Word Occurrences
Estimate: 25 minutes
Actual: 34 minutes
"""

word_count = {}
text = input("text: ")
words = text.split()
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
word_count_list = list(word_count)
word_count_list = sorted(word_count_list)
longest_word_length = 0
for word in word_count_list:
    word_length = len(word)
    if word_length > longest_word_length:
        longest_word_length = word_length
for word in word_count_list:
    print(f"{word:{longest_word_length}}: {word_count[word]}")

