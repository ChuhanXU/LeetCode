
# input
# 3
# TWLO
# CODE
# HTCH
# 5
# +17474824380
# +14157088956
# +919810155555
# +15109926333
# +1415123456

# output
# 8956 TWLO
# 2633 CODE
# 4824 HTCH
# {2:{a,b,c},3:{d,e,f},4:{g,h,i},5:{j,k,l},6:{m,n,o},7:{p,q,r,s},8:{t,u,v},9:{w,x,y,z}}


hash={
  "A": "2","B": "2","C": "2","D": "3","E": "3","F": "3","G": "4","H": "4","I": "4",
  "J": "5","K": "5","L": "5","M": "6","N": "6","O": "6","P": "7","Q": "7","R": "7",
  "S": "7","T": "8","U": "8","V": "8","W": "9","X": "9","Y": "9","Z": "9"
}

text=["+17474824380","+14157088956","+919810155555","+15109926333","+1415123456"]

codeList=["TWLO","CODE","HTCH"]


def findPhoneNumber(text,codeList):
    decodeList=[]
    result = []
    validPhoneNumber=[]
    # if the phoneNumber is valid
    for phoneNumber in text:
        if phoneNumber[0]=="+" and len(phoneNumber)<=16:
            validPhoneNumber.append(phoneNumber)
    # transform code to number code(decodeList)
    for i in range (len(codeList)):
        decode=""
        code = codeList[i]
        for character in code:
            decode+=hash.get(character)
        decodeList.append(decode)
    #   check if the number code match phoneNumber
    for i in range(len(decodeList)):
        decode=decodeList[i]
        for j in range(len(validPhoneNumber)):
            phoneNumber = validPhoneNumber[j]
            if phoneNumber.find(decode) != -1:
                result.append(phoneNumber)
    return sorted(set(result))
print(findPhoneNumber(text,codeList))

