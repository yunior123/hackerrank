# ex 1
# scheduleStart = [1, 1, 2]
# scheduleEnd = [3, 2, 4]
# result = 2 Explanation: a person can attend to meeting 2 
# that ends at 2 and meeting 3 that starts at 2 and ends at 4. 
# That is the maximum number of meetings one person can attend.
# ex 2
# scheduleStart = [6,1,2,3]
# scheduleEnd = [8,9,4,7]
# result = 2
# once a presentation has started no one can enter or leave the room.
def maxPresentations(scheduleStart, scheduleEnd):
    # Write your code here
    schedule = []
    for i in range(len(scheduleStart)):
        schedule.append([scheduleStart[i], scheduleEnd[i]])
    schedule.sort(key=lambda x: x[1])
    count = 0
    end = 0
    for i in range(len(schedule)):
        if schedule[i][0] >= end:
            count += 1
            end = schedule[i][1]
    return count



            
if __name__ == '__main__':
    start = [1, 1, 2]
    end = [3, 2, 4]
    x = maxPresentations(start, end)
    print(x) # 2
    scheduleStart = [6,1,2,3]
    scheduleEnd = [8,9,4,7]
    x = maxPresentations(scheduleStart, scheduleEnd)
    print(x) # 2


