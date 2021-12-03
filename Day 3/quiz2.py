f = open("input.txt", "r")

lines = []
length = 12
oxygen = []
scrubber = []

def getDecimalFromBinary(binaryArray):
  total = 0
  reversed = binaryArray[::-1]
  for i in range(len(reversed)):
    if (int(reversed[i]) > 0):
      total += (2 ** i)

  return total

line = f.readline()
while (line):
  lines.append(line.removesuffix('\n'))
  line = f.readline()

oxygen = lines.copy()
scrubber = lines.copy()

position = 0
while (len(oxygen) > 1):
  zeros = 0
  ones = 0
  for line in oxygen:
    if int(line[position]) > 0:
      ones += 1
    else:
      zeros += 1

  print(ones >= zeros)
  oxygen = [line for line in oxygen if int(line[position]) == (1 if ones >= zeros else 0)]
  position += 1
  print(oxygen)

position = 0
while (len(scrubber) > 1):
  zeros = 0
  ones = 0
  for line in scrubber:
    if int(line[position]) > 0:
      ones += 1
    else:
      zeros += 1

  scrubber = [line for line in scrubber if int(line[position]) == (1 if ones < zeros else 0)]
  position += 1

print(list(oxygen[0]))
print(list(scrubber[0]))
print(getDecimalFromBinary(list(oxygen[0])) * getDecimalFromBinary(list(scrubber[0])))