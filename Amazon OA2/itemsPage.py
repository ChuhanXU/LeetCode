
# input
# numOfItems =3
# items=[["item1",10,15],["item2",3,4],["item3",17,8]]
# sortParameter=1
# sortOrder=0 ascending
# itemPerPage =2
# PageNumber =1
# output
# ["item3"]
def pageNumberItems(numOfItems,items,sortParameter,sortOrder,itemPerPage,PageNumber):
    hash={}
    page = len(items) // itemPerPage + 1
    for i in range(page):
        hash[i]=[]
    if sortOrder == 0:
        items=sorted(items,key=lambda element:element[sortParameter],reverse=False)

    i=0
    for item in items:
        hash[i].append(item)
        if len(hash[i])==itemPerPage:
            i+=1
    result = []
    for item in hash[PageNumber]:
        result.append(item[0])
    return result


items=[["item1",10,15],["item2",3,4],["item3",17,8]]
print(pageNumberItems(3,items,1,0,2,1))