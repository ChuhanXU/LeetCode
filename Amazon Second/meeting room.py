
# meeting room
intervals = [(0,30),(5,10),(15,20)]

# 1.i.start<j.start
# I need to maintain a maxend
# if i.end<maxend return False
# sort nlog(n)

def meeting(intervals):
    maxEnd = 0
    sortedMeeting = sorted(intervals,key=lambda x:x[0])
    for interval in sortedMeeting:
        if interval[0]<maxEnd:
            return False

        maxEnd=max(maxEnd,interval[1])
    return True


intervals = [(0,30),(5,10),(15,20)]
print(meeting(intervals))