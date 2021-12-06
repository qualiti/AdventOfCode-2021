f = open('input.txt', 'r')
data = [int(x) for x in f.read().split(',')]
print(data)

for day in range(80):
  currentData = data.copy()
  for i, fish in enumerate(currentData):
    fish -= 1
    if fish < 0:
      fish = 6
      data.append(8)
    data[i] = fish

print(len(data))