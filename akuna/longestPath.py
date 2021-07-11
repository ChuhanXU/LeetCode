
# input: CHI:NYC:719       NONE
# input: NYC:LA:2414       3133:CHI:NYC:LA
# input: NYC:SEATTLE:2448  4862:LA:NYC:SEATTLE
# input: NYC:HAWAII:4924   7372:HAWALL:NYC:SEATTLE
dic = {}
class calculator:
    def _init_(self):
        pass
    def longest(self,line):
        s= line.split(":")

        dic[(s[0],s[1])] = s[2]
        if(len(dic)==1):
            return "NONE"
        weight = list(dic.values())
        sorteddic = {}
        for i in range(len(weight)-1):
            for j in range(len(weight)-1-i):
                sorteddic[(i,i+j+1)]=int(weight[i])+int(weight[i+j+1])
        sorteddic = sorted(sorteddic.items(),key=lambda item:item[1],reverse = True)
        for (i,j),w in sorteddic:
            cities = list(dic.keys())
            new = cities[i]+cities[j]
            if len(set(new))==3:
                city2=[x for x in new if new.count(x)==2]
                city1,city3=[x for x in set(new) if x!=city2[0]]
                if city1<city3:
                    return str(w)+":"+str(city1)+":"+str(city2[0]+":"+str(city3))
                return str(w) + ":" + str(city3) + ":" + str(city2[0] + ":" + str(city1))
        return None
solution = calculator()
str1="CHI:NYC:719"
str2="NYC:LA:2414"
str3="NYC:SEATTLE:2448"
str4="NYC:HAWAII:4924"
print(solution.longest(str1))
print(solution.longest(str2))
print(solution.longest(str3))
print(solution.longest(str4))





