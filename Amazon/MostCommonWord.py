
# Input:  paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." and banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.

def MostCommonWord(paragraph,banned):
    hash={}

    ban = set(banned)
    normalize=""
    for c in paragraph:
        if c.isalnum():
            normalize += c.lower()
            continue
        normalize+=" "
    words = normalize.split()
    for word in words:
        if word not in ban:
            hash[word]=hash.get(word,0)+1
    max_count = max(hash.values())
    # 根据value来返回key
    return list(hash.keys())[list(hash.values()).index(max_count)]



paragraph="Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(MostCommonWord(paragraph,banned))

