with open('input.txt') as f:
  data = [int(line) for line in f]


def part_1(data):
  print(sum([i // 3 - 2 for i in data]))


def part_2(data):
  total = 0
  for i in data:
    while i > 0:
      i = i // 3 - 2
      if i > 0:
        total += i
  print(total)


part_1(data)
part_2(data)
