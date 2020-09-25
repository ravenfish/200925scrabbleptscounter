scrabble_scores = {
    "a": 1,
    "b": 2,
    "c": 2,
    "d": 4,
    "e": 1,
    "f": 2,
    "g": 3,
    "h": 2,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}
word = []
letters_list = []
word_score = ""


def scrabble_points(word):
    word = input("Please type 1 word.")
    word = word.strip()
    word_score = 0
    for c in range(0, len(word)):
        letters_list.append(word[c])
        # print(letters_list)
    for c in letters_list:
        i = scrabble_scores.get(c)
        word_score = word_score + i
        # print(i)
    print(word_score)


scrabble_points(word)
