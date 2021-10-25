

meetingTimes = [ [5, 10], [0, 30], [15, 20] ]

# sort times by starting time - timsort - O(n) - O(nlogn)
meetingTimes.sort(key=lambda elem: elem[0])

isPossible = True

for i in range(len(meetingTimes) - 1):
    
    endTime = meetingTimes[i][1]
    startTime = meetingTimes[i+1][0]
    
    if endTime > startTime:
        isPossible = False
        break
    

print(isPossible)
    

    
