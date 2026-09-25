names = input("enter names:")
list = names.split(" ")
tupled = tuple(list)
length = len(tupled)-1
first = tupled[0]
last = tupled[length]

print(f"First is {first}, last is {last}")
