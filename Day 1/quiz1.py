f = open("input.txt", "r")
previousLine = None
increases = 0

line = f.readline()
while (line):
  if (previousLine):
    if (int(previousLine) < int(line)):
      print(previousLine + " - " + line)
      increases += 1
  
  previousLine = line
  line = f.readline()

f.close()
print(increases)