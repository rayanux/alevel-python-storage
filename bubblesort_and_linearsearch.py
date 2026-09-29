list = [24,2,1121,23,42,534,5,12,3,534,212]
length = len(list)-1

for x in range(length):
  for i in range(0, length):
    if list[i] > list[i+1]:
      previous = list[i]
      after = list[i+1]
      list[i] = after
      list[i+1] = previous

number = int(input("enter a number: "))
for i in range(0, length):
  if list[i] == number:
    position = list.index(number)
    print(f"{number} was found in position {position}")
  else:
    pass
