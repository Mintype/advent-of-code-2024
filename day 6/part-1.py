raw_map = open("map.txt", "r")

guard_location = tuple()
guard_rotation = 0
    
map = []

for line in open("map.txt", "r"):
    map.append(list(line))

def whats_here(location):
    # print("checking location", location)
    line_number1 = 0
    for line in open("map.txt", "r"):
        if line_number1 == location[0]:
            return line[location[1]]
        line_number1 += 1

def move():
    global guard_location
    global guard_rotation
    if guard_rotation == 0:
        if whats_here((guard_location[0] - 1, guard_location[1])) == "#":
            guard_rotation = 90
        else:
            map[guard_location[0]][guard_location[1]] = "X"
            guard_location = (guard_location[0] - 1, guard_location[1])
    elif guard_rotation == 90:
        if whats_here((guard_location[0], guard_location[1] + 1)) == "#":
            guard_rotation = 180
        else:
            map[guard_location[0]][guard_location[1]] = "X"
            guard_location = (guard_location[0], guard_location[1] + 1)
    elif guard_rotation == 180:
        if whats_here((guard_location[0] + 1, guard_location[1])) == "#":
            guard_rotation = 270
        else:
            map[guard_location[0]][guard_location[1]] = "X"
            guard_location = (guard_location[0] + 1, guard_location[1])
    elif guard_rotation == 270:
        if whats_here((guard_location[0], guard_location[1] - 1)) == "#":
            guard_rotation = 0
        else:
            map[guard_location[0]][guard_location[1]] = "X"
            guard_location = (guard_location[0], guard_location[1] - 1)
    print("Moved to", guard_location)
    
    # # update map
    map[guard_location[0]][guard_location[1]] = "^"
    
    # print out map
    # for line in map:
    #     print(line)
    # print('\n')

line_number = 0
for line in raw_map:
    if "^" in line:
        guard_location = (line_number, line.index("^"))
        break
    line_number += 1
    
# print("Starting position:", guard_location)

# make it MOVE
try:
    while True:
        move()
        if guard_location[0] < 0 or guard_location[1] < 0:
            raise IndexError('list index out of range')
except IndexError:
    print("Out of bounds")
    
    number_of_x = 0
    for line in map:
        number_of_x += line.count("X")
    print("Number of X:", number_of_x)
    pass