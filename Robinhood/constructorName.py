
# constructor name
# className = "abbzccc"
# methodName = "babzzcz"
# constructorNames(className,methodName)=true
# swap any two sumbols in one of the strings
# sawp occurrences of any two exiting symbols in one of the strings
# for example how to transform babzzcz to abbzccc
# exchange the first two characters abbzzcz,abbcczc,abbczcc,abbzccc
def constructorName(className,methodName):
    hashOfClassName = {}
    hashOfMethodName = {}
    n = len(className)
    m = len(methodName)

    for i in range(n):
        hashOfClassName[className[i]] = hashOfClassName.get(className[i],0)+1
    for i in range(m):
        hashOfMethodName[methodName[i]] = hashOfMethodName.get(methodName[i],0)+1


    for symbol in hashOfClassName:
        #检查字母是否存在
        if symbol in hashOfMethodName:
            continue
        return False
    # 检查字母数量是否一致

    print(sorted(hashOfMethodName.values()))
    if sorted(hashOfMethodName.values())!=sorted(hashOfClassName.values()):
        return False

    return True

className = "abbzccc"
methodName = "babzzcz"
print(constructorName(className,methodName))

