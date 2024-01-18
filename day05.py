word = 'letter'
letter_counts = {}
for letter in word:
    letter_counts[letter] = word.count(letter)
print(letter_counts)
