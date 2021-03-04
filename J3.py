
#input
number = 0
instructions = []
numcount = 1

while number != "99999":
    number = input()

    if number == "99999":
        continue

    else:
        split_number = list(number)
        instructions.append(split_number)
        numcount = numcount + 1

#algorithm
directions = []
cords = []

for x in instructions:
    digit1 = int(x[0])
    digit2 = int(x[1])

    total = digit1 + digit2

    if total == 0:
        direction = directions[-1]
        directions.append(direction)
        
    elif total % 2 == 1:
        direction = "left"
        directions.append(direction)
        
    elif total % 2 == 0:
        direction = "right"
        directions.append(direction)

for x in instructions:
    digit3 = x[2]
    digit4 = x[3]
    digit5 = x[4]

    move = digit3 + digit4 + digit5
    cords.append(move)

#output
counter = 0
for y in directions:
    print (y, cords[counter])
    counter = counter + 1
