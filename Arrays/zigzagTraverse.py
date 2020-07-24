def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    row, col = 0, 0
    goingDown = True
    result = []
    # Write your code here.


    while not outOfBound(row, col, height, width):
        result.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if col == 0:
                    row += 1
                else:
                    col += 1
            else:
                row += 1
                col -= 1
        else:
            if col == width or row == 0:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                col += 1
                row -= 1
    return result


def outOfBound(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width


print(zigzagTraverse([[1, 3], [2, 4], [5, 7], [6, 8], [9, 10]]))