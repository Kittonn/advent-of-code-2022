with open('input.txt') as f:
  data = [int(line) for line in f]

def part_1(data):
  result = [i*j if i + j == 2020 else 0 for i in data for j in data]
  print(max(result))

def part_2(data):
  result = [i*j*k if i + j + k ==
          2020 else 0 for i in data for j in data for k in data]
  print(max(result))
  
part_1(data)
part_2(data)
