from collections import defaultdict

list1 = []
list2 = []

with open('day1.txt') as f:
    for line in f:
        arr = line.replace('\n', '').split(' ')
        list1.append(int(arr[0]))
        list2.append(int(arr[3]))

list1.sort()
list2.sort()

distance = 0
for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])

print("Distance:", distance)

list2Frequency = defaultdict(int)
for i in range(len(list2)):
    list2Frequency[list2[i]] += 1

similarity = 0
for i in range(len(list1)):
    similarity += list1[i] * list2Frequency[list1[i]]
print("Similarity:", similarity)