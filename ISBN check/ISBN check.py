from isbnlib import *
#from isbntools.app import *


file = open("ISBN check\\ISBNnumbers.txt","r")
#file = open("ISBNnumbers.txt","r")


numbers = file.read().splitlines()


file.close()

for i in range(1, len(numbers)):
    lineCurrent = numbers[i]
    

    if is_isbn10(numbers[i]) or is_isbn13(numbers[i]):
        continue
    if is_isbn10(numbers[i-1]) or is_isbn13(numbers[i-1]):
        print(meta(numbers[i-1]))
    print(lineCurrent)
    if is_isbn10(numbers[i+1]) or is_isbn13(numbers[i+1]):
        print(meta(numbers[i+1]))
