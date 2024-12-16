from collections import defaultdict
graph = defaultdict(set)


def isValid(line):
  for i in range(1, len(line)):
    for j in range(i - 1, -1, -1):
      if line[j] in graph[line[i]]:
        return False
  return True

def reorder(line):
  i = 1
  while i < len(line):
    j = i - 1
    while j >= 0:
      if line[j] in graph[line[i]]:
        break
      j -= 1
    if j == -1:
      i += 1
      continue
    temp = line[i]
    for k in range(i, j, -1):
      line[k] = line[k - 1]
    line[j] = temp
    i = 1
  return line[len(line) // 2]

with open('day5.txt') as f:
  for line in f:
    line = line.replace("\n", "")
    line = line.split("|")
    graph[line[0]].add(line[1])

res = 0
with open('day5-2.txt') as f:
  for line in f:
    line = line.replace("\n", "")
    line = line.split(",")
    if isValid(line):
      res += int(line[len(line) // 2])

print("Part 1 Answer:", res)

res2 = 0
with open('day5-2.txt') as f:
  for line in f:
    line = line.replace("\n", "")
    line = line.split(",")
    if not isValid(line):
      res2 += int(reorder(line))

print("Part 2 Answer:", res2)
