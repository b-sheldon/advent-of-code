from collections import defaultdict
graph = defaultdict(set)


def isValid(line):
  for i in range(1, len(line)):
    for j in range(i - 1, -1, -1):
      if line[j] in graph[line[i]]:
        return False
  return True

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



