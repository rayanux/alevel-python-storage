list = [22,34,23,534,12312,3]
length = len(list)-1
start = 0

for x in range(length):
  for i in range(start, length):
    if list[i] > list[i+1]:
      after = list[i]
      previous = list[i+1]
      list[i] = previous
      list[i+1] = after
      print(list)
