
def plain():
    text = input("Text:")
    return text

def bold():
    text = input("Text:")
    return f"**{text}**"

def italic():
    text = input("Text:")
    return f"*{text}*"

def inline_code():
    text = input("Text:")
    return f"`{text}`"

def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"

def header():
    while True:
        level = int(input("Level:"))
        if level < 1 or level > 6:
            print("The level should be within the range of 1 to 6")
        else:
            break
    text = input("Text:")

    return f"{level * '#' } {text}\n"

def new_line():
    return "\n"

def unordered_list():
    list = ""
    l = ""
    while True:
        row = int(input("Number of rows: "))
        if row > 0:
            for i in range(1,row+1):
                list += "* " + input(f"Row #{i}") + "\n"
            return list
        else:
            print("The number of rows should be greater than zero")
            continue

def ordered_list():
    list = ""
    l = ""
    while True:
        row = int(input("Number of rows: "))
        if row > 0:
            for i in range(1,row+1):
                list += f"{i}. " + input(f"Row #{i}") + "\n"
            return list
        else:
            print("The number of rows should be greater than zero")
            continue
    



functions = {
'plain' : plain,
'bold' : bold,
'italic' : italic,
'inline-code': inline_code,
'link' : link,
'header' : header,
'new-line' : new_line,
'unordered-list' : unordered_list,
'ordered-list' : ordered_list
}

entire_text = ""
command_list = "plain bold italic header link inline-code  new-line unordered-list ordered-list"
while True:
    command = input("Choose a formatter:")
    if command == "!help":
        print("Available formatters: plain bold italic header link inline-code new-line")
        print("Special commands: !help !done")
    elif command == "!done":
        with open("output.md", 'w') as f:
            f.write(entire_text)
            break
    elif command not in command_list:
        print("Unknown formatting type or command")
    elif command in command_list:
            entire_text += functions[command]()
            print(entire_text)


