from file.path import *
from file.readfile import *
import cryptarithmetic as csp

def main():
    output= csp.cryptarithmetic(pathInput())
    input = readfile(pathInput())
    outputSolutions = output[0]
    outputTime = str(output[1])

    # print(input) SEND + MORE == MONEY
    # print(outputSolutions) [{'SEND': 9567, 'MORE': 1085, 'MONEY': 10652}]
    # print(outputTime) 0.1

    outputFile = open(pathOutput(), "w")
    outputFile.writelines("Given a cryptarithmetic problem: " + "\n" + input + "\n")
    outputFile.writelines("Solution: " + "\n")
    for line in outputSolutions:
        outputFile.writelines(str(line) + "\n")
    if len(outputSolutions) == 0:
        outputFile.writelines("No Solutions" + "\n")
        outputFile.writelines("== " + "0 solutions found in " + outputTime + "s ==")
    else: outputFile.writelines("== " + str(len(outputSolutions)) + " solutions found in " + outputTime + "s ==")

if __name__ == '__main__': main()


