example = open("example.txt", "r").read()
puzzle = open("puzzle.txt", "r").read()

exampleLanterns = [int(i) for i  in example.split(",")]
puzzleLanterns = [int(i) for i  in puzzle.split(",")]

def lanternfish (lanterns, days):

  amountLanterns = [0,0,0,0,0,0,0,0,0]

  for i in lanterns:
    amountLanterns[i] += 1

  i = 0

  while i < days:
    firstElement = amountLanterns[:1]
    del amountLanterns[0]
    amountLanterns[6] += firstElement[0]
    amountLanterns.append(firstElement[0])
    i+=1

  return sum(amountLanterns)

ans = lanternfish(exampleLanterns, 256)
ansPuzzle = lanternfish(puzzleLanterns, 256)
print(ans, ansPuzzle)