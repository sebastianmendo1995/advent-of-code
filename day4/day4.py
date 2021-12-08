file = open("bingo.txt", "r").read()

def solve(s):
  s = s.split("\n\n");

  order = [int(i) for i  in s[0].split(",")]

  s=s[1:]

  def makeBoard(arr):
    board = []
    for row in arr:
      r = row.split(" ")
      r = ' '.join(r).split()
      r = [int(i) for i in r]
      board.append(r)
    return(board)

  boards = []

  for i in s:
    i = i.split("\n")
    board = makeBoard(i)
    boards.append(board)

  def winning(cb):
    for i in range(len(cb)):
      cw = True
      for j in cb[i]:
        if j != -1: cw = False
      if cw: return True
    
    for j in range(len(cb[0])):
      cw = True
      for i in range(len(cb)):
        if cb[i][j] != -1:
          cw = False
      if cw: return True

    return False

  def gs(cb):
    res = 0
    for i in cb:
      for j in i:
        if j != -1:
          res += j
    return res


  for num in order:

    nb = []
    lv = -1

    for i in range(len(boards)):
      for j in range(len(boards[i])):
        for k in range(len(boards[i][j])):
          if boards[i][j][k] == num:
            boards[i][j][k] = -1
      if winning(boards[i]):
        lv = gs(boards[i]) * num
      else:
        nb.append(boards[i])

    boards = nb

    if len(boards) == 0: return lv        


print(solve(file))