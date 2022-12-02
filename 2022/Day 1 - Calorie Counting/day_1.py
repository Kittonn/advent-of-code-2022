result = []
s = 0
with open('input.txt') as f:
  data = f.read().splitlines()

for i in data:
  if i == '':
    m = s
    result.append(m)
    s = 0
  else:
    s += int(i)


def part_1(data):
  print(max(data))


def part_2(data):
  print(sum(sorted(data, reverse=True)[:3]))


part_1(result)
part_2(result)
