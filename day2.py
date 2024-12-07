
safeLevels = 0

with open('day2.txt') as f:
    for line in f:
        arr = line.replace('\n', '').split(' ')
        direction = 1 if int(arr[1]) - int(arr[0]) > 0 else -1
        safe = True
        for i in range(1, len(arr)):
            diff = (int(arr[i]) - int(arr[i - 1])) * direction
            if diff < 1 or diff > 3:
                safe = False
                break
        if safe:
            safeLevels += 1
    
print("Safe levels:", safeLevels)
            