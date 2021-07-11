
# [(2,3),(3,6),(4,5)]
# [(2,3),(4,5),(3,6)]

def jobSchedule(schedule):
    schedule = sorted(schedule,key=lambda x:x[1])
    result=[]
    visited=[]
    visited.append(schedule[0])
    result.append(schedule[0])

    for i in range(len(schedule)):
        if schedule[i] not in visited:
            if schedule[i][0]>=visited[len(visited)-1][1]:
                result.append(schedule[i])
                visited.append(schedule[i])
    return result
schedule=[(1,2),(3,5),(6,19),(2,100)]
print(jobSchedule(schedule))