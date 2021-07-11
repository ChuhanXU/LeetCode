# input: start = "hit"，end = "cog"，dict = ["hot", "dot", "dog", "lot", "log"]
import collections

# O(V+E)
# O(N)

def bfs(start, end, dict):
    dict.append(end)
    queue= collections.deque()

    queue.append(start)

    step =1
    while queue:
        for _ in range(len(queue)):
            currentWord = queue.popleft()
            if currentWord == end:
                return step
            nextwordList = get_nextword(currentWord)
            for word in nextwordList:
                if word in dict:
                    queue.append(word)

        step+=1


def get_nextword(word):
    result = []
    characterList="abcdefghijklmnopqrstuvwxyz"
    # we can use a for loop to iterate change every character in word with 26 different char
    for i in range(len(word)):
        # if word is hit i=0 part1="" part2="it"
        part1=word[:i]
        part2=word[i+1:]
        for character in characterList:
            newWord = part1+character+part2
            result.append(newWord)
    return result


# print(get_nextword("hit"))
start = "hit"
end = "cog"
dict = ["hot", "dot", "dog", "lot", "log"]

print(bfs(start,end,dict))