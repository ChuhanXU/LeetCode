
# input LOC:CHI:41.836944:-87.684722
# output CHI
# input LOC:NYC:40.7127:-74.0059
# output NYC
# TRIP:C0FFEE1C:CHI:NYC
# output:C0FFEE1C:CHI:NYC:714
from math import acos, sin, radians, cos
import re
global city_loc
city_loc = {}
RADIUS_MILES = 3963
class Destination:
    def _init_(self):
        pass
    def travelDistance(self,line):
        s=line.split(":")
        if s[0]=='LOC':
            city=s[1]
            city_loc[city]={float(s[2]),float(s[3])}
            return s[1]
        else:
            start = s[2]
            end = s[3]
            lat1,lon1=city_loc[start]
            lat2,lon2=city_loc[end]
        distance = RADIUS_MILES*acos(sin(radians(lat1))*sin(radians(lat2))+cos(radians(lat1))*cos(radians(lat2))*cos(abs(radians(lon1)-radians(lon2))))
        return str(s[1])+":"+str(start)+":"+str(end)+":"+str(int(distance))

str1 = "LOC:CHI:41.836944:-87.684722"
str2 = "LOC:NYC:40.7127:-74.0059"
str3 = "TRIP:C0FFEE1C:CHI:NYC"
solution = Destination()
print(solution.travelDistance(str1))
print(solution.travelDistance(str2))
print(solution.travelDistance(str3))



