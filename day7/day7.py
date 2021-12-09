example = open("example.txt", "r").read()
puzzle = open("puzzle.txt", "r").read()

example = [int(i) for i in example.split(",")]
puzzle = [int(i) for i in puzzle.split(",")]


def alignCrabs(crabs):
  crabs.sort()
  med = crabs[len(crabs) // 2]
  ans = 0
  for crab in crabs:
    ans += abs(crab - med)

  return ans


print(alignCrabs(example))
print(alignCrabs(puzzle))

# partTwo

def C2(num):
  return num*(num+1)/2


def alignCrabsTwo(crabs):
  best = 1e9

  for med in range(2000):
    score = 0
    for crab in crabs:
      d = abs(crab - med)
      score += C2(d)

    if score < best : best = score

  return best


print(alignCrabsTwo(example))
print(alignCrabsTwo(puzzle))