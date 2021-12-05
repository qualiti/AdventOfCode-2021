f = open('input.txt', 'r')
content = f.read()
lines = content.split('\n')

startX, endX, startY, endY = list(), list(), list(), list()

for line in lines:
  data = line.split('->')
  data = [x.strip() for x in data]
  x1, y1 = data[0].split(',')
  x2, y2 = data[1].split(',')
  startX.append(int(x1))
  endX.append(int(x2))
  startY.append(int(y1))
  endY.append(int(y2))

# Find max X and max Y and fill the list with 0
maxX = max(max(startX), max(endX))
maxY = max(max(startY), max(endY))
hits = list()
for y in range(maxY + 1):
  hits.append(list())
  for x in range(maxX + 1):
    hits[y].append(0)

# They all have the same length
for i in range(len(startX)):
  x1, x2, y1, y2 = startX[i], endX[i], startY[i], endY[i]
  if (x1 != x2 and y1 == y2):
    for pos in range(x1, x2, 1 if x1 < x2 else -1):
      hits[y1][pos] += 1
    hits[y1][x2] += 1
  elif (y1 != y2 and x1 == x2):
    for pos in range(y1, y2, 1 if y1 < y2 else -1):
      hits[pos][x1] += 1
    hits[y2][x1] += 1

overlaps = len([totalHits for column in hits for totalHits in column if totalHits > 1])
print(overlaps)