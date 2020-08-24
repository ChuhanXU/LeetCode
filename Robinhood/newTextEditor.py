
# your task is to simulate the working process of a text editor which can handle five types of operation
# insert
# delete
# paste
# copy
# undo
# input:operations =
# ["INSERT Da","COPY 0","UNDO","PASTE","PASTE","COPY 2","PASTE",
# "PASTE","DELETE","INSERT aaam"]
# 有问题

# string1 = "he"
# string2 = "llo"
# n = len(string2)
# print(string1+string2)
# print(string2[0:n-1])

def operate(operations):
    text=""
    n = len(operations)
    deleteCharacter = ""
    pasteNumber = 0
    insertNumber=0

    for i in range(n):
        if operations[i][0]=="I":
            insertindex = operations[i].find(" ")+1
            insertNumber=len(operations[i][insertindex::])
            text = text + operations[i][insertindex::]

        elif operations[i][0]=="D":

            m = len(text)
            if m==0:
                break
            deleteCharacter = text[m-1]
            text = text[0:m-1]

        elif operations[i][0]=="C":
            clipboard = ""
            index = operations[i].find(" ")+1
            copyStart = int(operations[i][index])
            clipboard = text[copyStart::]
            pasteNumber = len(clipboard)

        elif operations[i][0]=="P":
            text = text+clipboard

        elif operations[i][0]=="U":
            text = undo(i-1,operations[i-1],operations,text,insertNumber,deleteCharacter,pasteNumber)

    return text
def undo(i,operation,operations,text,insertNumber,deleteCharacter,pasteNumber):
    if operation[0] == "I":
        lengthOfText = len(text)
        text = text[0:lengthOfText - insertNumber]
    elif operation[0] == "D":
        text = text + deleteCharacter

    elif operation[0] == "P":
        lengthOfText = len(text)
        text = text[0:lengthOfText - pasteNumber]
    elif operation[0] == "C":
        text = undo(i-1,operations[i-1],operations,text,insertNumber,deleteCharacter,pasteNumber)

    return text

# operations = ["INSERT Da","COPY 0","UNDO","PASTE","PASTE","COPY 2","PASTE",
#  "PASTE","DELETE","INSERT aaam"]

operations = ["INSERT a","DELETE","DELETE","COPY 0","UNDO","PASTE","UNDO","INSERT b","COPY 0","PASTE",
 "COPY 2","PASTE","UNDO","DELETE","UNDO"]
print(operate(operations))

