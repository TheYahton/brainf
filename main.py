import sys


def interpret(text: str) -> None:
    arr = [0] * 30000
    i = 0
    s = 0
    while s < len(text):
        match text[s]:
            case '+':
                arr[i] += 1
            case '-':
                arr[i] -= 1
            case '>':
                i += 1
            case '<':
                i -= 1
            case '.':
                print(chr(arr[i]), end = '')
            case ',':
                arr[i] = ord(input()[0])
            case '[':
                if arr[i] == 0:
                    j = s
                    count = 0
                    while True:
                        if text[j] == '[':
                            count += 1
                        elif text[j] == ']':
                            count -= 1
                        j += 1

                        if count == 0:
                            s = j
                            break
            case ']':
                if arr[i] != 0:
                    j = s
                    count = 0
                    while True:
                        if text[j] == '[':
                            count += 1
                        elif text[j] == ']':
                            count -= 1
                        j -= 1

                        if count == 0:
                            s = j
                            break
        s += 1

def main():
    prog_name = sys.argv[0]

    if len(sys.argv) != 2:
        print(f"Usage: {prog_name} FILENAME")
        return

    path = sys.argv[1]

    with open(path, "r") as f:
        code = f.read()

    interpret(code)


if __name__== "__main__":
    main()

