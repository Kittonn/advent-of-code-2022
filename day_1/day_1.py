m = 0
s = 0

with open('input.txt') as f:
  data = f.read().splitlines()

for i in data:
  if i == '':
    if s >= m:
      m = s
    s = 0
  else:
    s += int(i)
    
print(m)
