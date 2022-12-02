with open('input.txt') as f:
  data = f.read().splitlines()

data = [line.split("x") for line in data]
result = []

for j in data:
  result.append(2 * int(j[0]) * int(j[1]) + 2 * int(j[1]) * int(j[2]) + 2 * int(j[0]) * int(
      j[2]) + min(int(j[0]) * int(j[1]), int(j[1]) * int(j[2]), int(j[0]) * int(j[2])))

print(f"Total square feet of wrapping paper : {sum(result)}")

result = []

for j in data:
  j = sorted([int(i) for i in j])
  result.append((2 * j[0]) + (2 * j[1]) + (j[0] * j[1] * j[2]))

print(f"Total feet of ribbon : {sum(result)}")
