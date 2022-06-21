msg_ = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)",
]

msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0

ok = 0
ok2 = 0


def is_one_digit(v):
    if v > -10 and v < 10 and (float(v)).is_integer():
        output = True
    else:
        output = False
    return output

def check(v1,v2,v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def result2():


    global memory, result
    print(msg_0)
    calc = input()
    calc = calc.split()

    if calc[0] == 'M':
        x = memory
    else:
        while True:
            try:
                x = float(calc[0])
                break
            except ValueError:
                print(msg_1)
                print(msg_0)
                calc = input()
    if calc[2] == 'M':
        y = memory
    else:
        while True:
            try:
                y = float(calc[2])
                break
            except ValueError:
                print(msg_1)
                print(msg_0)
                calc = input()

    oper = calc[1]
    if oper == "+" or oper == "-" or oper == "*" or oper == "/":
        check(x,y,oper)
        if oper == "+":
            result = x + y
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif oper == "/" and y != 0:
            result = x / y
        else:
            print(msg_3)
            result2()
    else:
        print(msg_2)
        result2()
    print(result)
    print(msg_4)
    answer = input()
    if answer == 'y':
        if is_one_digit(result):
            msg_index = 10
            while True:
                print(msg_[msg_index])
                answer = input()
                if answer == "y":
                    if msg_index < 12:
                        msg_index = msg_index + 1
                        continue
                    else:
                        memory = result
                        break
                elif answer != "n":
                    continue
                else:
                    break
        else:
            memory = result

    while True:
        print(msg_5)
        answer = input()
        if answer == "y":
            result2()
        elif answer != "n":
            continue
        else:
            quit()

result2()







