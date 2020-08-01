# 扫描线的思想，将(0,10)换成(0,1)(10,-1),分别记录meeting room 和 ongoing meeting
def minMeetingRooms(intervals):
    points = []
    for interval in intervals:
        points.append((interval[0], 1))
        points.append((interval[1], -1))

    meeting_rooms = 0
    ongoing_meetings = 0
    for _, delta in sorted(points):
        ongoing_meetings += delta
        meeting_rooms = max(meeting_rooms, ongoing_meetings)

    return meeting_rooms
print(minMeetingRooms([(0,30),(5,10),(15,20)]))