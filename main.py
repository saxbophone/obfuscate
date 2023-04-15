import random
import sys


def obfuscate_interpreter(code):
    data = []
    pointer = 0
    output = ""
    length = len(code)
    while pointer < length:
        char = code[pointer]
        if char == 'z':
            data.append(random.randint(32, 126))
        elif char == 'V':
            output += chr(data.pop())
        elif char == '7':
            data.append(ord(input("Enter a character: ")))
        elif char == '^':
            data[-1] += 1
        elif char == '%':
            data[-1] -= 1
        elif char == 't':
            data[-2], data[-1] = data[-1], data[-2] 
        elif char == 'F':
            data.pop()
        elif char == '>':
            pointer += data.pop()
        elif char == '[':
            if data[-1] == 0:
                depth = 0
                while True:
                    pointer += 1
                    if code[pointer] == '[':
                        depth += 1
                    elif code[pointer] == ']':
                        if depth == 0:
                            break
                        else:
                            depth -= 1
        elif char == 'q':
            data[-1] = (data[-1] % 128) * 2
        elif char == '@':
            data[-1] = (data[-1] // 2) % 128
        elif char == 'M':
            data[-1] = (data[-1] + data.pop()) % 256
        elif char == '/':
            data.append(data.pop() // data.pop())
        elif char == '!':
            data.append(int(not data.pop()))
        elif char == 'x':
            data.append(data.pop() ^ data.pop())
        elif char == 'D':
            data.pop()
        elif char == 'c':
            data[-1] = ord(chr(data[-1]).lower())
        elif char == 'K':
            data[-1] = ord(chr(data[-1]).upper())
        elif char == '#':
            data.append(len(data))
        elif char == '*':
            data.append(data.pop() * data.pop())
        elif char == '+':
            data.append(data.pop() + data.pop())
        elif char == 's':
            data.append(abs(data.pop()))
        elif char == '<':
            pointer -= data.pop()
        elif char == '0':
            data.append(0)
        elif char == '~':
            data[-1] = -data[-1]
        elif char == '{':
            data.append(1)
        elif char == 'a':
            data[-1] = ord(chr(data[-1]).swapcase())
        elif char == '2':
            data.append(2)
        elif char == 'L':
            data.append(len(str(data.pop())))
        elif char == '_':
            data.append(data.pop() // 10)
        elif char == '&':
            data.append(data.pop() % 10)
        elif char == 'e':
            data[-1] = data[-1] in [69, 101]
        elif char == '"':
            data.append(ord(input("Enter a character: ")[0]))
        elif char == 'H':
            output += str(data.pop())
        elif char == 'l':
            data[-1] = data[-1] & 255
        elif char == '$':
            data.append(data.pop() * 10)
        elif char == ')':
            data[-1] = data[-1] % 2
        elif char == ":":
            a = data.pop()
            data.append(int(a-48))
        elif char == "|":
            output += str(data.pop())
        pointer += 1
    print(output)
    

if len(sys.argv) == 1 or sys.argv[1] == "--shell":
    while True:
        inp = input(">>> ")
        if inp == "quit":
            break
        try:
            obfuscate_interpreter(inp)
        except:
            print("An error occured")
elif len(sys.argv) == 2:
    try:
        with open(sys.argv[1]) as f:
            program = f.read()
            try:
                obfuscate_interpreter(program)
            except:
                print("Error occured when running")
    except:
        print("File not found")
