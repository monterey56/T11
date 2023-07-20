#ask the user to input a string
#print the string, with every other character being uppercase
#print the string, with every other word being uppercase

def chars(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i].upper()
        else:
            result += string[i]
    print(result)

def words(string):
    words = string.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].upper()
    result = " ".join(words)
    print(result)

string = input("Enter a string: ")
chars(string)
words(string)