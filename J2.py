
#inputs
N = int(input())

bids = []
for x in range(N):
    info = ["", ""]

    name = input()
    bid = int(input())
    info[0] = name
    info[1] = bid

    bids.append(info)

#output
highest_value = 0
winner = ""

for information in bids:

    if information[1] > highest_value:
        highest_value = information[1]
        winner = information[0]

    else:
        continue

print (winner)
        
