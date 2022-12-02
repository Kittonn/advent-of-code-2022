with open('input.txt') as f:
  data = f.read()


def part_1(data):
  print(data.count('(') - data.count(')'))


def part_2(data):
  floor = 0
  position = 0
  for i in data:
    position += 1
    if i == '(':
      floor += 1
    if i == ')':
      floor -= 1
    if floor <= -1:
      print(position)
      break


part_1(data)
part_2(data)
