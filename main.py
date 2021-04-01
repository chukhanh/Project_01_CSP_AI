from file.path import *
from file.readfile import *
import cryptarithmetic as csp
import re
import math
from z3 import *
import itertools

def sorter(item):
    return item[1]

def divide(list, num):
    segList = len(list)
    total= math.ceil(segList / num)
    items_per_chunk = num
    out = []
    last = 0

    while last < segList:
        out.append(list[last:(last + items_per_chunk)])
        last += items_per_chunk

    return out



def main():

    output= csp.cryptarithmetic(pathInput())
    input = readfile(pathInput())
    outputSolutions = output[0]
    outputTime = str(output[1])
    print(outputSolutions)
    # print(type(outputSolutions))

    # delw = "["
    # dela = "]"
    # replace = ''
    # regex = r"[a-zA-Z0-9]"
    # result = re.sub(delw, replace ,outputSolutions)
    # result = re.sub(dela, replace, result)
    # print(result)
    # res = list(map(list, "".join(str(outputSolutions).split())))
    # print(res)
    # tokenWords = re.findall(r'\b[a-zA-Z0-9]\w*\b', str(res))
    # print(tokenWords)
    # print(type(tokenWords))

    # result = divide(tokenWords, 2)
    # print(result)

    # for lines in result:
    #     arr = { line: Int(line) for line in list(lines) : line[1] = int[line[1]] }
    #     print(arr)

    
    
    # for line in outputSolutions:
        # result = ''.join(sorted(str(line)))
        # print(line)
        # print(result)

    # print(input) SEND + MORE == MONEY
    # print(outputSolutions) [{'SEND': 9567, 'MORE': 1085, 'MONEY': 10652}]
    # print(outputTime) 0.1

    # outputFile = open(pathOutput(), "w")
    # outputFile.writelines("Given a cryptarithmetic problem: " + "\n" + input + "\n")
    # outputFile.writelines("Solution: " + "\n")
    # for line in outputSolutions:
    #     outputFile.writelines(str(line) + "\n")
    # if len(outputSolutions) == 0:
    #     outputFile.writelines("No Solutions" + "\n")
    #     outputFile.writelines("== " + "0 solutions found in " + outputTime + "s ==")
    # else: outputFile.writelines("== " + str(len(outputSolutions)) + " solutions found in " + outputTime + "s ==")
    # for line in outputSolutions:
        # print(line)
        # tokenWords = re.findall(r'\b[a-zA-Z]\w*\b', str(line))
        # print(''.join(sorted(tokenWords)))
        # print(tokenWords)
        # result = ''.join(sorted(tokenWords))
        # print(result)
        # numbers = re.findall(r'\b[0-9]\w*\b', str(line))
        # print(''.join)
        # for word in tokenWords:
        #     for num in tokenWords:
        #         result = tokenWords[num].join(tokenWords[word])
        #         print(result)
        # letters = { i: Int(i) for i in list("".join(tokenWords))}
        # print(letters)

if __name__ == '__main__': main()


