data = [int(x) for x in open('input.txt').read().split(',')]

lessFuel = 32 ** 32
for x in data:
  total = 0
  for y in data:
    total += abs(x - y)

  if (total < lessFuel):
    lessFuel = total

print(lessFuel)