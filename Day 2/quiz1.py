f = open("input.txt", "r")

horizontal = 0
depth = 0

line = f.readline()
while (line):
  split = line.split(" ")
  direction = split[0]
  amount = split[1].removesuffix("\n")

  if (direction == "forward"):
    horizontal += int(amount)
  elif (direction == "up"):
    depth -= int(amount)
  elif (direction == "down"):
    depth += int(amount)

  line = f.readline()

print(horizontal * depth)