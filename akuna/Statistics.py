# input C0FFEE1C:CHI:NYC:714
# 714:C0FFEE1C:CHI
from collections import Counter

hash={}
hash_account={}
def statistics(line):

    lineList = line.split(":")
    hash[(lineList[1],lineList[2])]= int(lineList[3])
    hash_account[lineList[0]]=hash_account.get(lineList[0],0)+int(lineList[3])
    if len(hash)==1:
        if lineList[1]<lineList[2]:
            return str(lineList[3])+":"+str(lineList[0])+":"+str(lineList[1])
        else:
            return str(lineList[3])+":"+str(lineList[0])+":"+str(lineList[2])
    distance = list(hash.values())
    totalDistance = sum(distance)
    cities=[]
    for item in list(hash.keys()):
        cities += item
    city_num={}
    for city in cities:
        city_num[city]=city_num.get(city,0)+1
    maxcount = max(city_num.values())
    maxcountList=[]
    for city in city_num:
        if city_num[city]==maxcount:
            maxcountList.append(city)
    busiestCity = sorted(maxcountList)[0]
    sortedHash = sorted(hash_account.items(), key=lambda item: item[1], reverse=True)
    accountList=[]
    for item in sortedHash:
        accountList.append(item[0])
    if hash_account[accountList[0]]==hash_account[accountList[1]]:
        if int(accountList[1],16)<int(accountList[0],16):
            longest_account = accountList[1]
    longest_account = accountList[0]
    return str(totalDistance)+":"+str(longest_account)+":"+str(busiestCity)
line1="C0FFEE1C:CHI:NYC:714"
line2="0FF1CE18:LA:SEATTLE:961"
line3="C0FFEE1C:NYC:LA:2448"
print(statistics(line1))
print(statistics(line2))
print(statistics(line3))