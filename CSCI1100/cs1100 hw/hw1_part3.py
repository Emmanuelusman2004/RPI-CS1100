frame = input("Enter frame character ==> ").strip()
print(frame)


height = input("Height of box ==> ").strip()
print(height)

width = input("Width of box ==> ").strip()
print(width)

print('')
print('')

print('Box:')
print('')

middle_of_box = width + "x" + height

height = int(height)
width = int(width)

box_width = frame + " " *(width - 2) + frame + "\n"

inner_box = int((width - 2 - len(middle_of_box)/2))

width_length = int((height - 3)/2)

print(frame * width)

print(box_width * width_length, end = "")
print(frame + " " * inner_box + middle_of_box + " " * (width - inner_box - len(middle_of_box) - 2) + frame)

print(box_width * width_length, end = "")

print(frame * width)