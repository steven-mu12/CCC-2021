
#input
original_seq = input()
split_seq = list(original_seq)

counter = 0
for x in split_seq:
    if x == "L":
        split_seq[counter] = 3
        counter = counter + 1
    elif x == "S":
        split_seq[counter] = 1
        counter = counter + 1
    elif x == "M":
        split_seq[counter] = 2
        counter = counter + 1

for i in range(len(split_seq)):
    split_seq[i] = int(split_seq[i])

#algorithm
small_positions = []
medium_positions = []
moves = 0
counter = 0
smallpos = 0
medpos = 0

# For large and medium switch
for number in split_seq:
    if number == 3:  
        if medpos > 0:
            del medium_positions[0]
            moves = moves + 1
            medpos = 0

    elif number == 2:
        medpos = counter
        medium_positions.append(medpos)
        counter = counter  + 1

    else:
        counter = counter + 1

counter = 0

# For medium and small switch
for number in split_seq:
    if number == 2:  
        if smallpos > 0:
            del small_positions[0]
            moves = moves + 1
            smallpos = 0

    elif number == 1:
        smallpos = counter
        small_positions.append(smallpos)
        counter = counter  + 1
    
    else:
        counter = counter + 1

counter = 0

# For large and small switch
for number in split_seq:
    if number == 3:  
        if smallpos > 0:
            del small_positions[0]
            moves = moves + 1
            smallpos = 0

    elif number == 1:
        smallpos = counter
        small_positions.append(smallpos)
        counter = counter  + 1

    else:
        counter = counter + 1

counter = 0

#output
print (moves)