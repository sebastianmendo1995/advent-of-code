from collections import defaultdict

example = open("example.txt", "r").read()
puzzle = open("puzzle.txt", "r").read()

example = [list(map(int, list(i.strip()))) for i in example.split("\n")]
puzzle = [list(map(int, list(i.strip()))) for i in puzzle.split("\n")]

directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

def smokeBasinPart1 (points):
  stack = [];
  lowPointsXY=[]

  for y in range(len(points)):
    for x in range(len(points[y])):
      cell = points[y][x]
      isLowPoint = True
      for dir in directions:
        new_y = y + dir[0]
        new_x = x + dir[1]
        if 0 <= new_x < len(points[0]) and 0<= new_y < len(points):
          neighbour = points[new_y][new_x]
          if cell >= neighbour:
            isLowPoint = False
            break
      if isLowPoint: 
        stack.append(cell + 1)
        lowPointsXY.append((y, x))
  
  return sum(stack), lowPointsXY

#part 2

def smokeBasinPart2 (points, minimuns):

  def flood(m, visited):
    if m in visited: return

    visited[m] = True

    y, x = m

    for dir in directions:
      new_y = y + dir[0]
      new_x = x + dir[1]
      if 0 <= new_x < len(points[0]) and 0<= new_y < len(points):
        neighbour = points[new_y][new_x]
        if neighbour != 9:
          flood((new_y, new_x), visited)
    
    return visited

  basinSizes = []

  for min in minimuns:
    basinSizes.append(len(flood(min, {})))

  basinSizes.sort()

  print(basinSizes)

  prod = 1

  for size in basinSizes[-3:]:
    prod *= size
  
  return prod

res, minimuns = smokeBasinPart1(example)
res2, minimuns2 = smokeBasinPart1(puzzle)

print(smokeBasinPart2(example, minimuns))
print(smokeBasinPart2(puzzle, minimuns2))