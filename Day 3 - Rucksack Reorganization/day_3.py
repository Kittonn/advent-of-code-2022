from string import ascii_lowercase, ascii_uppercase

characters = ascii_lowercase + ascii_uppercase

with open("input.txt") as f:
  data = f.read().splitlines()
  
  
def find_sum_index(data):
  data = [characters.index(j) + 1 for i in data for j in i]
  return sum(data)

def part_1(data):
  middle = [len(line) // 2 for line in data]
  data = [[set(line[:middle[i]]), set(line[middle[i]:])]
          for i, line in enumerate(data)]
  data = [i[0].intersection(i[1]) for i in data]
  sum_index = find_sum_index(data)
  print(sum_index)


def part_2(data):
  data = [data[i:i+3] for i in range(0, len(data), 3)]
  data = [[set(i[0]),set(i[1]),set(i[2])] for i in data]
  data = [i[0].intersection(i[1],i[2]) for i in data]
  sum_index = find_sum_index(data)
  print(sum_index)

part_1(data)
part_2(data)
