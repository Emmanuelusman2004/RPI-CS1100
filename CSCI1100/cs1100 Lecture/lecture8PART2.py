values = [ 14, 10, 8, 19, 7, 13 ]

x = int(input("Enter a value: "))
print(x)
values.append(x)

y = int(input("Enter another value: "))
print(y)
values.insert(2,y)

print(values[3], end = " " )
print(values[-1])

print("Difference: " + str(max(values) - min(values)))

avg = sum(values)/len(values)
print("Average: " + format(avg, ".1f"))

values.sort()
median = ((values[3] + values[4])/2)
print("Median: " + str(median))