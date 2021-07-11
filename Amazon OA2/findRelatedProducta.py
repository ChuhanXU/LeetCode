
# input
# [["product1","product2","product3"]
# ["product5","product2"]
# ["product6","product7"]
# ["product8","product7"]]
# output:
# ["product1","product2","product3","product5"]

def largest(list):
    hash={}
    visited={}
    for item in list:

