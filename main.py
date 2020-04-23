x = int(input("int for x: "))
y = int(input("int for y: "))
z = int(input("int for z 0 or 1: "))
result_string = ((' ' + ('la-' * x)[:-1]) * y).rstrip() + ['!', '.'][z != 1]
print("Everybody sing a song" + result_string)