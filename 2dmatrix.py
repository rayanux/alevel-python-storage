value = input("enter a valid sequence: ")
list = value.split("/")

for i in range(len(list)):
    list[i] = list[i].split("/")
    
print(list)
