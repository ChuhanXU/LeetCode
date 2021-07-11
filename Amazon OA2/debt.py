# Amazon is working on a new application for recording internal debts across teams.
# This program can be used to create groups that show all records of debts between the group members. Given the group debt records observed for this team (including the borrower name, lender name, and debt amount), who in the group has the smallest negative balance?
#
# Notes: -10 is smaller than -1. If multiple people have the smallest negative balance, return the list in alphabetical order. If nobody has a negative balance, return the list consisting of string "Nobody has a negative balance".
#
# Write an algorithm to find who in the group has the smallest negative balance.
#
# Input:
# The input to the function/method consists of three arguments:
# numRows, an integer representing the number of debt records.
# numCols, an integer representing th enumber of elements in debt records. It is always 3.
# debts, a list of triplet representing debtRecord consisting of a string borrower, a string lender, and an integer amount, representing the debt record.
#
# Output:
# Return a list of strings representing an alphabetically ordered list of members with the smallest negative balance. If no team member has a negative balance then return a list containing the string "Nobody has a negative balance".
#
# Constraints:
# 1 ≤ numRows ≤ 2*10^5
# 1 ≤ amount in debts ≤ 1000
# 1 ≤ length of borrower and lender in debts ≤ 20

# input
# numRows=6
# numCols=3
# debts=[['Alex','Black',2],['Black','Alex',2],['Casey','Alex',5],['Alex','Black',4],['Alex','Casey',4]]

# output
# ['Alex','Black']
class debtRecord:
    borrower = ""
    lender = ""
    amount = 0

    def __init__(self, borrower, lender, amount):
        self.borrower = borrower
        self.lender = lender
        self.amount = amount

def minimumDebtMembers(records):
    hash={}
    for item in records:
        hash[item[0]]=hash.get(item[0],0)-item[2]
        hash[item[1]] = hash.get(item[1], 0) + item[2]
    hashlist = sorted(hash.items(),key=lambda item:item[1])
    minbalance= hashlist[0][1]
    list=[]
    for pair in hashlist:
        if pair[1]==minbalance:
            list.append(pair[0])
    print(hash)
    print(hashlist)
    return sorted(list)


# records = [['Alex','Black',2],['Black','Alex',2],['Casey','Alex',5],['Black','Casey',7],['Alex','Black',4],['Alex','Casey',4]]
records = [['Black','Alex',7],['Black','Alex',3],['Alex','Black',4],['Black','Alex',1],['Alex','Black',7]]
print(minimumDebtMembers(records))



