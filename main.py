from file.path import *
from file.readfile import *
import cryptarithmetic as csp
import re
import math
from z3 import *



def main():

    output= csp.cryptarithmetic(pathInput())
    input = readfile(pathInput())
    outputSolutions = output[0]
    outputTime = str(output[1])
    print(outputSolutions)
    # print(type(outputSolutions))




    # print(input) SEND + MORE == MONEY
    # print(outputSolutions) [{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}]
    # print(outputTime) 0.1

    outputFile = open(pathOutput(), "w")
    outputFile.writelines("Given a cryptarithmetic problem: " + "\n" + input + "\n")
    outputFile.writelines("Solution: " + "\n")
    for line in outputSolutions:
        if len(outputSolutions) == 0:
            outputFile.writelines("No Solutions" + "\n")
            outputFile.writelines("== " + "0 solutions found in " + outputTime + "s ==")
        else:
            result = {k: line[k] for k in sorted(line)}
            words = re.findall(r'\b[a-zA-Z]\w*\b', str(result))
            numbers = re.findall(r'\b[0-9]\w*\b', str(result))
            outputWords = "".join(words)
            outputNumbers="".join(numbers)
            outputFile.writelines(outputWords + " = " + outputNumbers + "\n")
    # for line in outputSolutions:
    outputFile.writelines("== " + str(len(outputSolutions)) + " solutions found in " + outputTime + "s ==")
    #     outputFile.writelines(str(line) + "\n")

    # else: outputFile.writelines("== " + str(len(outputSolutions)) + " solutions found in " + outputTime + "s ==")

if __name__ == '__main__': main()


