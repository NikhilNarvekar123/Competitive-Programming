from queue import PriorityQueue

# approach 1 - O(n^2)


meetingTimes = [ [2,15],[36,45],[9,29],[16,23],[4,9] ]

# sort times by starting time - timsort - O(n) - O(nlogn)
meetingTimes.sort(key=lambda elem: elem[0])

# each entry in this array represents a room, where the value of the entry
# is the endtime of the meeting assigned to the room
rooms = [meetingTimes[0][1]]

for i in range(len(meetingTimes) - 1):
    
    if meetingTimes[i][1] <= meetingTimes[i+1][0]:
        rooms[-1] = meetingTimes[i+1][1]
    else:
        roomFound = False
        for j in range(len(rooms)-1):
            if rooms[j] <= meetingTimes[i+1][0]:
                rooms[j] = meetingTimes[i+1][1]
                roomFound = True
                break
        if not roomFound:
            rooms.append(meetingTimes[i+1][1])
    

print('approach1', len(rooms))
print(rooms)
    

# approach 2 - O(nlogn)

meetingTimes = [ [2,15],[36,45],[9,29],[16,23],[4,9] ]
meetingTimes.sort(key=lambda elem: elem[0])

rooms = PriorityQueue()
rooms.put(meetingTimes[0][1])
count = 1

for i in range(1,len(meetingTimes)):
    
    # O(1)
    if meetingTimes[i][0] < rooms.queue[0]:
        count += 1
        
    # O(log n)
    rooms.put(meetingTimes[i][1]) 
    
print('approach2', count)
    





    
