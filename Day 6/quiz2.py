f = open('input.txt', 'r')
data = [int(x) for x in f.read().split(',')]
print(data)

days = 256
multiplyByDay = [0 for _ in range(days)]
for x in data:
  multiplyByDay[x] += 1

for day in range(days):
  todayFishes = multiplyByDay[day]
  if (todayFishes > 0):
    if (day + 7 < days):
      multiplyByDay[day + 7] += todayFishes

    if (day + 9 < days):
      multiplyByDay[day + 9] += todayFishes

print(sum(multiplyByDay) + len(data))