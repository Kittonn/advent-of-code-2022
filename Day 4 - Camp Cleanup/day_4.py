with open("input.txt") as f:
  data = [line.split(",") for line in f.read().splitlines()]


data = [[j.split("-") for j in i] for i in data]
data = [[[int(j[0]), int(j[1])] for j in i] for i in data]


def part_1(data):
  count = 0
  for i in data:
    if i[0][0] >= i[1][0] and i[0][1] <= i[1][1] or i[1][0] >= i[0][0] and i[1][1] <= i[0][1]:
      count += 1
  print(count)


def part_2(data):
  overlap = 0
  for i in data:
    if not(i[0][0] < i[1][0] and i[0][1] < i[1][0] or i[0][0] > i[1][1] and i[0][1] > i[1][1]):
      overlap += 1

  print(overlap)


part_1(data)
part_2(data)
