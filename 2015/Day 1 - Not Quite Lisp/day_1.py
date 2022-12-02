with open('input.txt') as f:
  data = f.read()

print(
    f"Floor do the instructions take Santa : {data.count('(') - data.count(')')}")

floor = 0
position = 0
for i in data:
  position += 1
  if i == '(':
    floor += 1
  if i == ')':
    floor -= 1
  if floor <= -1:
    print(f"Position of the character that causes Santa to first enter the basement : {position}")
    break
