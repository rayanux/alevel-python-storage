database = [1,2,3,4,5,6,7,8,9,10]
copy = database
found = False
start = 0
length = len(database)
midpoint = length//2
number = int(input("enter a number you'd like to find: "))

while found == False:
  if number not in database:
    print("number not found in list")
    break
  elif number > database[midpoint]:
    database = database[midpoint:length]
    midpoint = len(database)//2
    print(database)
  elif number < database[midpoint]:
    database = database[start:midpoint]
    midpoint = len(database)//2
    print(database)
  elif number == database[midpoint]:
    position = copy.index(number)
    print(f"{number} was found in position {position}")
    break
    
