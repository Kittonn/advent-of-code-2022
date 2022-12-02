with open('input.txt') as f:
  data = f.read().splitlines()

score = [0, 0]

default = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
           'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

default_score = {'X': 1, 'Y': 2, 'Z': 3}

data = [data[i].split(" ") for i in range(len(data))]


def get_score(oppenent, player):
  oppenent = default[oppenent]
  player = default[player]
  if oppenent == player:
    return 3
  elif (oppenent, player) in (('paper', 'scissors'), ('rock', 'paper'), ('scissors', 'rock')):
    return 6
  return 0


for i in data:
  score[0] += default_score[i[1]]
  score[0] += get_score(i[0], i[1])
  score[1] += default_score[i[1]] * 3 - 3
  for j in ('X', 'Y', 'Z'):
    if default_score[i[1]] * 3 - 3 == get_score(i[0], j):
      score[1] += default_score[j]


print(f"Part 1 score : {score[0]}")
print(f"Part 2 score : {score[1]}")
