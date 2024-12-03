import random

def charReplace(text, pos, char):
    text = text[:pos]+char+text[pos+1:]
    return text

def textChange(text, char):
    for i in range(len(text)):
        text = charReplace(text, i, char)
    return text

file = open("wordlist.txt", "r")

wordList = []
numOfWords = 0

for line in file:
    wordList.append(line)
    numOfWords += 1

lineNum = random.randint(1,250)

text1 = (wordList[lineNum]).strip()

text2 = textChange(text1, "-")

print(f"Text 1: {text1}\nText 2: {text2}")

guess = (input("What letter do you want to guess? ")).lower()

letterNum = 0

for i in range(len(text1)):
    letterNum += 1
    if guess in text1[i]:
        pass

file.close()



