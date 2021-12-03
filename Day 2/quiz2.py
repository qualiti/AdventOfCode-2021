f = open("input.txt", "r")

horizontal = 0
depth = 0
aim = 0

line = f.readline()
while (line):
  split = line.split(" ")
  direction = split[0]
  amount = split[1].removesuffix("\n")

  if (direction == "forward"):
    horizontal += int(amount)
    depth += aim * int(amount)
  elif (direction == "up"):
    aim -= int(amount)
  elif (direction == "down"):
    aim += int(amount)

  line = f.readline()

print(horizontal * depth)