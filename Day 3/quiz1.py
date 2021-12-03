f = open("input.txt", "r")

lines = []
length = 12
gammaRate = []
epsilonRate = []

def getDecimalFromBinary(binaryArray):
  total = 0
  reversed = binaryArray[::-1]
  for i in range(len(reversed)):
    if (reversed[i] > 0):
      total += (2 ** i)

  return total

line = f.readline()
while (line):
  lines.append(line.removesuffix('\n'))
  line = f.readline()

for e in range(length):
  zeros = 0
  ones = 0
  for line in lines:
    if int(line[e]) > 0:
      ones += 1
    else:
      zeros += 1
  
  gammaRate.append(0 if zeros > ones else 1)
  epsilonRate.append(1 if zeros > ones else 0)

print(gammaRate)
print(epsilonRate)

print(getDecimalFromBinary(gammaRate)) # 1869
print(getDecimalFromBinary(epsilonRate)) # 2226
print(getDecimalFromBinary(gammaRate) * getDecimalFromBinary(epsilonRate)) # 4160394