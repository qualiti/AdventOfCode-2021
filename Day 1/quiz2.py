f = open("input.txt", "r")
lines = []
increases = 0

line = f.readline()
while (line):
  lines.append(int(line))
  line = f.readline()

f.close()

for i in range(1, len(lines) - 2):
  first = lines[i - 1] + lines[i] + lines[i + 1]
  second = lines[i] + lines[i + 1] + lines[i + 2]
  if (second > first):
    increases += 1
  

print(increases)