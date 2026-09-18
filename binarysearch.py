database = [1,2,3,4,5,6,7,8,9,10]
copy = database
length = len(database)
start = 0
midpoint = length//2
found = False

number = int(input("enter a number: "))

while found == False:
    if len(database) == 0:
        print("not found")
        break

    if number > database[midpoint]:
        print("discard left")
        database = database[midpoint:length]
        midpoint = len(database)//2
        print(database)
        print(midpoint)

    elif number < database[midpoint]:
        print("discard right")
        database = database[start:midpoint]
        midpoint = len(database)//2
        print(database)
        print(midpoint)

    elif number == database[midpoint]:
        position = copy.index(number)
        print(f"{number} was found in position {position}")
        found = True
        
