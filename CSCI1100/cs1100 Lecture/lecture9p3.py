new_list = []
i = 1
while i != 0:
    i = int(input("Enter a value (0 to end): "))
    print(i)
    new_list.append(i)
    

new_list.sort()

x = new_list[1]
y = (new_list[len(new_list)-1])
z = sum(new_list) / (len(new_list) - 1)

print("Min: " + str(x))
print("Max: " + str(y))
print("Avg: " + str(round(z,1)))