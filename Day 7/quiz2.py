data = [int(x) for x in open('input.txt').read().split(',')]
averagePos = round((sum(data) / len(data)))

best = 32 ** 32
for y in range(averagePos - 1, averagePos + 1):
  total = 0
  for x in data:
    steps = abs(x - y)
    for step in range(steps):
      total += step + 1
  
  if (total < best):
    best = total

print(best)