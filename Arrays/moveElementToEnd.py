def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:

        while i < j and array[j] == toMove:
            j -= 1

        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]

        i += 1
    return array

print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))

# I move the right pointer inwards to integer that don't need to move
# moving the left pointer inwards to integer to move