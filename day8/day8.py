from collections import defaultdict
import itertools

example = open("example.txt", "r").read()
puzzle = open("puzzle.txt", "r").read()

example = [i for i in example.split("\n")]
puzzle = [i for i in puzzle.split("\n")]

# In the output values, how many times do digits 1, 4, 7, or 8 appear?

def sumUniqueDigits (arr) :
  ans = 0
  for line in arr:
    [before, after] = line.split("|")
    before = before.split()
    after = after.split()
    new_list = defaultdict(list)
    
    for signal in before:
      new_list[len(signal)].append(signal)

    for signal in after:
      if len(new_list[len(signal)]) == 1:
        ans +=1
  
  return ans

print(sumUniqueDigits(example), sumUniqueDigits(puzzle))

# Part 2

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

digits = {
  0: "abcefg",
  1: "cf",
  2: "acdeg",
  3: "acdfg",
  4: "bcdf",
  5: "abdfg",
  6: "abdefg",
  7: "acf",
  8: "abcdefg",
  9: "abcdfg",
}

def find_perm_slow(before):
    for perm in itertools.permutations(list(range(8))):
        ok = True
        D = {}
        for i in range(8):
            D[chr(ord('a')+i)] = chr(ord('a')+perm[i])
        for w in before:
            w_perm = ''
            for c in w:
                w_perm += D[c]
            w_perm = ''.join(sorted(w_perm))

            if w_perm not in digits.values():
                ok = False
        if ok:
            return D

def sumOutputValues (arr):
  ans2 = 0

  for line in arr:
    [before, after] = line.split("|")
    before = before.split()
    after = after.split()
    
    D = find_perm_slow(before)
    ret = ''
    for w in after:
        w_perm = ''
        for c in w:
            w_perm += D[c]
        w_perm = ''.join(sorted(w_perm))
        d = [k for k,v in digits.items() if v==w_perm]
        assert len(d) == 1

        ret += str(d[0])
    ans2 += int(ret)
  
  return ans2


print(sumOutputValues(example), sumOutputValues(puzzle))