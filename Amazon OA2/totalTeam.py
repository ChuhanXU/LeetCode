
# input
# num = 6
# skills = [12,4,6,13,5,10]
# minAssociates = 3
# minLevel = 4
# maxLevel = 10
# 在 4-10中间找大于3个的组合数量
# output = 5

def numberOfTeam(num,skills,minAssociates,minLevel,maxLevel):
    skills = sorted(skills)
    skillsLevel = skills[skills.index(minLevel):skills.index(maxLevel)+1]
    if len(skillsLevel)==0:
        return
    result = []
    l = len(skillsLevel)
    for i in range(minAssociates,l+1):
        dfs(skillsLevel,0,[],result,i)
    return len(result)
def dfs(nums,index,current,result,length):
    if len(current)>=length:
        result.append(current[:])
        return
    for i in range(index,len(nums)):
        current.append(nums[i])
        dfs(nums,i+1,current,result,length)
        current.pop()
skills = [12,4,6,13,5,10]
#
# print(numberOfTeam(6,skills,3,4,10))
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return (n*factorial(n-1))
#
#
# def numberOfTeam(num,skills,minAssociates,minLevel,maxLevel):
#     skills = sorted(skills)
#     skillsLevel = skills[skills.index(minLevel):skills.index(maxLevel)+1]
#     ans=0
#     if len(skillsLevel)==0:
#         return
#     l=len(skillsLevel)
#     for i in range(minAssociates,l+1):
#         ans+=factorial(l)/(factorial(l-i)*factorial(i))
#     return int(ans)
skills = [12,4,6,13,5,10]
print(numberOfTeam(6,skills,3,4,10))


