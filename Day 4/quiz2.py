f = open('input.txt', 'r')
drawNumbers = f.readline().removesuffix('\n').split(',')
print(drawNumbers)

boards = []

boardLines = 5
line = f.readline()
while (line):
  if (len(line) == 1): 
    line = f.readline()
    boards.append([])
  
  numbers = [[x, False] for x in line.removesuffix('\n').split(' ') if len(x) > 0]
  boards[len(boards) - 1].append(numbers)
  line = f.readline()

winnerBoards = []
winnerDraw = list()
def checkBoardWins(drawnNumber):
  # Check rows
  for index, board in enumerate(boards):
    for line in board:
      winningNumbers = [x for x in line if x[1]]
      if (len(winningNumbers) == boardLines):
        if (not index in winnerBoards):
          winnerBoards.append(index)
          winnerDraw.insert(index, drawnNumber)

  # Check columns
  for index, board in enumerate(boards):
    for column in range(boardLines):
      columnNumbers = []
      for line in board:
        columnNumbers.append(line[column])

      columnNumbers = [x for x in columnNumbers if x[1]]
      if (len(columnNumbers) == boardLines):
        if (not index in winnerBoards):
          winnerBoards.append(index)
          winnerDraw.insert(index, drawnNumber)
        

for draw in drawNumbers:
  for board in boards:
    for line in board:
      for numberTuple in line:
        if (numberTuple[0] == draw):
          numberTuple[1] = True
  
  checkBoardWins(draw)
  if (len(winnerBoards) == len(boards)):
    break

unmarked = 0
winner = winnerBoards[len(winnerBoards) - 1]
print(winner)
for line in boards[winner]:
  for numberTuple in line:
      if not numberTuple[1]:
        unmarked += int(numberTuple[0])

print(winnerBoards) 
print(winnerDraw[winner])
print(unmarked * int(winnerDraw[winner]))
