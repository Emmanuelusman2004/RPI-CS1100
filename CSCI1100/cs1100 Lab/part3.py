import math
base10size = input("Disk size in GB => ")
print(base10size)

base2size = (int(base10size) * (10**9))/2**30

lost_size = int(base10size) - base2size

print(str(base10size) + "GB in base 10 is actually " + str(math.floor(base2size)) + " GB in base 2, " + str(math.ceil(lost_size)) + " GB less than advertised.")

print("Input:  " + ("*" * int(base10size)))
print("Actual: " + ("*" * math.floor(base2size)))