# for operations = [[1,1,1]],the output should be rectangleBoxes(operations) = [true]
# for operations = [[0,1,3],[0,4,2],[1,3,4],[1,3,2]]
# the output should be rectangleBoxes(operations) = [true,false]
# save rectangle that start with 0,and check if after rectangle start with 1 can include it
# 以1开头的长方形能不能包含以0开头的长方形
def rectangleBoxes(operations):
    ans = []
    largest_long_side = -1
    largest_short_side = -1


    for box in operations:
        larger = max(box[1], box[2])
        smaller = min(box[1], box[2])
        if box[0] == 0:
            largest_long_side = max(larger, largest_long_side)
            largest_short_side = max(smaller, largest_short_side)
        else:
            if larger < largest_long_side or smaller < largest_short_side:
                ans.append(False)
            else:
                ans.append(True)
    return ans

    # ans = []
    # long_inside = -1
    # short_inside = -1
    # long_outside = -1
    # short_outside = -1
    # for operation in operations:
    #     # 需要fit in 的是0开头的operation，需要更新边长
    #     # 因为可以反转，我们只需要里面长方形的最长边<外边长方形的最长边就可以了
    #
    #     if operation[0] == 0:
    #         larger = max(operation[1], operation[2])
    #         smaller = min(operation[1], operation[2])
    #         long_inside = max(larger,long_inside)
    #         short_inside = max(smaller,short_inside)
    #
    #     if operation[0]==1:
    #         larger_out = max(operation[1], operation[2])
    #         smaller_out = min(operation[1], operation[2])
    #         long_outside = max(larger_out, long_outside)
    #         short_outside = max(smaller_out, short_outside)
    #
    #     else
    #
    #         if long_inside<long_outside and short_inside<short_outside:
    #             ans.append(True)
    #         else:
    #             ans.append(False)
    # return ans
# operations = [[0,1,3],[0,4,2],[1,3,4],[1,3,2]]
operations = [[1,1,1]]
print(rectangleBoxes(operations))







