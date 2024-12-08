def search(arr, word="XMAS"):
  def searchDirection(i, j, direction, word):
    if word == "":
      return True
    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[i]) or word[0] != arr[i][j]:
      return False
    return searchDirection(i + direction[0], j + direction[1], direction, word[1:])
  
  count = 0
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if arr[i][j] == word[0]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
          if searchDirection(i + direction[0], j + direction[1], direction, word[1:]):
            count += 1
  return count

def searchXMAS(arr):
  count = 0
  for i in range(1,len(arr) - 1):
    for j in range(1, len(arr[i]) - 1):
      if arr[i][j] == "A":
        one = (arr[i-1][j-1] == "M" and arr[i+1][j+1] == "S") or (arr[i-1][j-1] == "S" and arr[i+1][j+1] == "M")
        two = (arr[i-1][j+1] == "M" and arr[i+1][j-1] == "S") or (arr[i-1][j+1] == "S" and arr[i+1][j-1] == "M")
        if one and two:
          count += 1
  return count

arr = []
with open('day4.txt') as f:
  for line in f:
    line.replace("\n", "")
    arr.append(list(line))

print("Part 1 Solution:", search(arr))
print("Part 2 Solution:", searchXMAS(arr))