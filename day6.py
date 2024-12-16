graph = []
i = 0
startI = -1
startJ = -1

with open('day6.txt') as f:
  for line in f:
    line = line.replace("\n", "")
    line = list(line)
    graph.append(line)
    if startI == -1 and startJ == -1:
      for j in range(len(line)):
        if line[j] == "^":
          startI = i
          startJ = j
    i += 1

visited = set()
visited.add((startI, startJ))
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = 0
i = startI
j = startJ
while True:
  newI = i + directions[direction][0]
  newJ = j + directions[direction][1]
  if newI < 0 or newI >= len(graph) or newJ < 0 or newJ >= len(graph[newI]):
    print("escaped")
    break
  elif (newI, newJ) in visited:
    print("visited", newI, newJ)
    break
  elif graph[newI][newJ] == "#":
    direction = (direction + 1) % 4
  else:
    visited.add((newI, newJ))
    i = newI
    j = newJ
  
print("Part 1 Solution:", len(visited))

