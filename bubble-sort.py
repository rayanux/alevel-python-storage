list = [35,25,15,2]
length = len(list)-1
start = 0

for x in range(length):
  for i in range(start, length):
    if list[i] > list[i+1]:
      previous = list[i]
      after = list[i+1]
      list[i] = after
      list[i+1] = previous
      print(list)
