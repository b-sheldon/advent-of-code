from curses.ascii import isdigit

def findValidMultiply(line):
    result = 0
    i = 0
    while i < len(line):
        if line[i:i+4] == "mul(":
            j = i + 4
            valid = True
            num1 = None
            num2 = None
            temp = ""
            while valid and j < len(line):
                if line[j] == "," and not num1:
                    num1 = int(temp)
                    temp = ""
                elif line[j] == ")" and num1 and not num2:
                    num2 = int(temp)
                    temp = ""
                    break
                elif isdigit(line[j]):
                    temp += line[j]
                else:
                    valid = False
                    break
                j += 1
            if valid:
                result += num1 * num2
        i += 1
    return result


def findValidMultiplyDoDont(line, enable=True):
    result = 0
    i = 0
    while i < len(line):
        if line[i:i+4] == "do()":
            enable = True
        elif line[i:i+7] == "don't()":
            enable = False

        if line[i:i+4] == "mul(" and enable:
            j = i + 4
            valid = True
            num1 = None
            num2 = None
            temp = ""
            while valid and j < len(line):
                if line[j] == "," and not num1:
                    num1 = int(temp)
                    temp = ""
                elif line[j] == ")" and num1 and not num2:
                    num2 = int(temp)
                    temp = ""
                    break
                elif isdigit(line[j]):
                    temp += line[j]
                else:
                    valid = False
                    break
                j += 1
            if valid:
                result += num1 * num2
        i += 1
    return result, enable


result = 0
result2 = 0
with open('day3.txt') as f:
    enable = True
    for line in f:
        result += findValidMultiply(line)
        res2, enable = findValidMultiplyDoDont(line, enable)
        result2 += res2


print("Part 1 Solution:", result)
print("Part 2 Solution:", result2)