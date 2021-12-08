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
    i+=1

ans = lanternfish(exampleLanterns, 80, 0)
ansPuzzle = lanternfish(puzzleLanterns, 80, 0)
print(ans, ansPuzzle)