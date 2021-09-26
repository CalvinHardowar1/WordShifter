
user = input("Enter a word: ")

string = ""

for c in user:
    add = chr((((ord(c)+13)-65)%26)+65)
    string = string + add
print("Your word in code is: ", string)
