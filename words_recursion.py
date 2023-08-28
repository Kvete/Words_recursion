from random import randint


def recursion(alphabet, word, length=0):
    if length == len(word):
        print(word)
        return
    for i in range(len(alphabet)):
        word[length] = alphabet[i]
        recursion(alphabet, word, length + 1)


t = randint(1, 7)  # number of letters in word

alphabets = ['a', 'b', 'c', 'd']
words = [0 for j in range(t)]
recursion(alphabets, words)
