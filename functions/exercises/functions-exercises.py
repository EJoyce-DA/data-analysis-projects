# Part 1 A -- Make a Line

def make_line(size):
    line = ''
    for i in range(size):
        line += '#'
    return line 

#print(make_line(5))

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square

def make_square(size):
    square = ''
    for i in range(size):
        square += make_line(size)
        if i < size - 1:
            square += '\n'
    return square

#print(make_square(5))




# Part 1 C -- Make a Rectangle

def make_rectangle(width, height):
    rectangle = '' 
    for i in range(height):
        rectangle += make_line(width)
        if i < height - 1:
            rectangle += '\n'
    return rectangle
#print(make_rectangle(5,3))


def make_rectangle(width, height):
    rectangle = ''
    for i in range(height):
        rectangle += make_square(width)
        if i < height - 1:
            rectangle += '\n'
    return rectangle
#print(make_rectangle(5, 3))




# Part 2 A -- Make a Stairs
def make_downward_stairs(height):
    down_stairs = ''
    for i in range(height):
        down_stairs += make_line(i+1)
        if i < height -1:
            down_stairs += '\n'
    return down_stairs
#print(make_downward_stairs(5)) 




# Part 2 B -- Make Space-Line 

def make_space_line(numSpaces, numChars):
    space_line = ''
    for i in range(numSpaces):
        space_line += ' '
    for i in range(numChars):
        space_line += '#'
    for i in range(numSpaces):
        space_line += ' '
    return space_line
#print(make_space_line(3,5))




# Part 2 C -- Make Isosceles Triangle
def make_isoceles_triangle(height):
    iso_triangle = ''
    for i in range(height):
        iso_triangle += make_space_line((height-i-1), (2*i+1))
        if i < height -1:
            iso_triangle += '\n'
    return iso_triangle
#print(make_isoceles_triangle(5))




# Part 3 -- Make a Diamond

def make_diamond(height):
    diamond = ''
    for i in range(height):
        space = ' ' * (height-i-1)
        hash = '#' * (2*i+1)
        diamond += space + hash + '\n'
    for i in range(height-2, -1, -1):
        space = ' ' * (height-i-1)
        hash = '#' * (2*i+1)
        diamond += space + hash + '\n'
    return diamond
print(make_diamond(5))




