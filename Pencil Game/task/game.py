

import random

# First messages

print("How many pencils would you like to use:")
while True:
    try:
        number = int(input())
        if number <= 0:
            print("The number of pencils should be positive")
            continue
        break
    except ValueError:
        print("The number of pencils should be numeric")
        continue


print("Who will be the first (John, Jack):")
while True:
    name = input()
    if name != "Jack" and name != "John":
        print("Choose between 'John' and 'Jack'")
        continue
    else:
        break
s = "|" * number
print(s)
s = list(s)

# GAME LOOP

while True:
    s = list(s)
    print(f"{name}'s turn:")

    # JOHN MOVES

    if name == 'John':
        while True:
            pencils_taken = input()
            if pencils_taken != '1' and pencils_taken != '2' and pencils_taken != '3':
                print("Possible values: '1', '2' or '3'")
                continue
            elif len(s) < int(pencils_taken):
                print("Too many pencils were taken:")
                continue
            else:
                pencils_taken = int(pencils_taken)
                break

    # BOT MOVES

    elif name == 'Jack':
        # Losing position
        if len(s) % 4 == 1:
            if len(s) > 3:
                pencils_taken = random.choice([1, 2, 3])
            else:
                pencils_taken = 1
        # Winning position
        else:
            if len(s) % 4 == 0:
                pencils_taken = 3
            elif len(s) % 4 == 3:
                pencils_taken = 2
            elif len(s) % 4 == 2:
                pencils_taken = 1
        print(pencils_taken)

    # TAKE PENCILS OUT

    for i in range(0, pencils_taken):
        s[i] = ""
    s = "".join(([str(elem) for elem in s]))
    print(s)

    # CHECK WINNER

    if s == "":
        if name == "Jack":
            print("John won!")
        elif name == "John":
            print("Jack won")
        break

    # CHANGE TURN

    if name == 'Jack':
        name = 'John'
    else:
        name = 'Jack'
