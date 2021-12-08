my_file = open("coordinates.txt", "r")
content = my_file.read()
coordinates = content.split("\n")
my_file.close();

totalLines = len(coordinates)

matrix = [ [ 0 for i in range(1000) ] for j in range(1000) ]

def getPointsInline(line):
  p1, p2 = line
  x1, y1 = p1
  x2, y2 = p2

  dy = y2 - y1
  dx = x2 - x1

  dy = dy / abs(dy) if dy != 0 else 0
  dx = dx / abs(dx) if dx != 0 else 0

  curr_point = (int(x1), int(y1))

  points = [curr_point]

  while curr_point != p2:
    x, y = curr_point
    new_point = (int(x + dx), int(y + dy))
    points.append(new_point)
    curr_point = new_point

  return points


count = 0

for line in coordinates:
  [p1,p2] = line.split("->")
  [x1,y1] = p1.split(",")
  [x2,y2] = p2.split(",")
  x1= int(x1)
  y1= int(y1)
  x2= int(x2)
  y2= int(y2)

  points = getPointsInline([(x1,y1),(x2,y2)])

  for point in points:
    x,y = point
    matrix[x][y] += 1
    if(matrix[x][y] == 2): count += 1


print(count)
      