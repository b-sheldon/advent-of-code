
safeLevels = 0

def isSafe(arr):
    direction = 1 if int(arr[1]) - int(arr[0]) > 0 else -1
    safe = True
    for i in range(1, len(arr)):
        diff = (int(arr[i]) - int(arr[i - 1])) * direction
        if diff < 1 or diff > 3:
            safe = False
            break
    return safe

with open('day2.txt') as f:
    for line in f:
        arr = line.replace('\n', '').split(' ')
        safe = isSafe(arr)
        if safe:
            safeLevels += 1
        
        # Day 2 Part 2 Solution
        else:
            for i in range(len(arr)):
                safe = isSafe(arr[:i] + arr[i + 1:])
                if safe:
                    safeLevels += 1
                    break
    
print("Safe levels:", safeLevels)
            