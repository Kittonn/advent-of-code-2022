with open('input.txt') as f:
  data = f.read().splitlines()

data = [int(i) for i in data]


def count_larger(data):
  count = 0
  for i in range(len(data)):
    if data[i] - data[i-1] > 0:
      count += 1
  return count

print(f"Count of measurements larger than previous measurements : {count_larger(data)}")

result = []

for i in range(2,len(data)):
  result.append(data[i] + data[i-1] + data[i-2])
  
print(f"Count of sum measurements larger than previous sum : {count_larger(result)}")