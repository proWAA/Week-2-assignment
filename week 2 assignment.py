my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

my_list.extend([50, 60, 70])

my_list.pop()

my_list.sort()

index30 = my_list.index(30)
print("Index of 30:", index30)

print("Final list:", my_list)
