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
    
print(max(result))
