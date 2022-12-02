with open('input.txt') as f:
  data = [int(i) for i in f]


def count_larger(data):
  count = 0
  for i in range(len(data)):
    if data[i] - data[i-1] > 0:
      count += 1
  return count


def part_1(data):
  print(count_larger(data))


def part_2(data):
  result = []
  for i in range(2, len(data)):
    result.append(data[i] + data[i-1] + data[i-2])
  print(count_larger(result))

part_1(data)
part_2(data)