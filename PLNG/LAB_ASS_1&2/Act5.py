def last_alphabetically(word1, word2, word3):
    return max(word1, word2, word3)


word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
word3 = input("Enter third word: ")

last_word = last_alphabetically(word1, word2, word3)

print("The word that comes last alphabetically is:", last_word)