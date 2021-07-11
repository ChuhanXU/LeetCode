# Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord.
# If there are more than three products with a common prefix return the three lexicographically minimums products.
#
# Return list of lists of the suggested products after each character of searchWord is typed.

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
import bisect


def suggestedProducts(A, word):
    A.sort()
    res = []
    prefix = ''
    i=0
    for c in word:
        prefix += c
        i = bisect.bisect_left(A, prefix, i)
        print (i)
        res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
    return res


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
print(suggestedProducts(products, searchWord))
