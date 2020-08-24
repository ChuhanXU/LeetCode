
# a valid IPv4 address is an IP in the form "x1.x2.x3.x4"
# where 0<=xi<=255 and xi cannot contain leading zeros
# for example,"192.168.1.1" and "192.168.1.0" are valid IPv4
# but"192.168.01.1" and "192.168.1.00" and "192.168@1.1" are invalid IPv4 adresses.

IP = input()
# s="192.168.01.1"
# n=s.count(".")
# print(n)
# print(s.split("."))


def isIPv4(IP):
    if IP.count(".")==3:
        IPArray = IP.split(".")
        for part in IPArray:
            if 0<=int(part)<=255:
                if part == str(int(part)):
                    continue
                return False
        return True

# IP = "192.168.01.1"
print(isIPv4(IP))


