
# input text = "Hello,this is CodeSignal"
# letters = ['e','i','h','l','o','s']
# output 2
def brokenKeyboard(text,letters):
    letterSet = set(letters)
    result = 0
    words = text.split()
    for word in words:
        for w in word:
            if not w.isalpha():
                continue
            if w.lower() not in letterSet:
                result-=1
                break
        result+=1
    return result
text = "Hello, this is CodeSignal"
letters = ['e','i','h','l','o','s']
print(brokenKeyboard(text,letters))