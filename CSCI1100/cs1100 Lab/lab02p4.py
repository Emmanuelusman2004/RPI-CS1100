user_input1 = input("Enter your first name: ") 
user_input2 = input("Enter your last name: ") 

x = len("Hello,")
y = len(user_input1)
z = len(user_input2 + "!")
list1 = [x,y,z]

longest = max(list1)

print("*" *(longest + 6))

print("**" + " " + "Hello," + (" " * (longest - x)) + " **")
print("**" + " " + user_input1 + (" " * (longest - y)) + " **")
print("**" + " " + user_input2 + "!" + (" " * (longest - z)) + " **")

print("*" *(longest + 6))