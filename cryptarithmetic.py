from file import readfile as read
import time
import re
from z3 import *

# For Example: SEND + MORE == MONEY

a:str = "="
b:str = "==" 
def cryptarithmetic(filename, unique=True):
    input = read.readfile(filename)
    input = input.replace(a, b)
    startTime = time.perf_counter()
    solver = Solver()
    tokenWords = re.findall(r'\b[a-zA-Z]\w*\b', input)
    # tokenWords = sorted(tokenWords)

    # print(type(input))
    letters = { i: Int(i) for i in list("".join(tokenWords))}
    # print(letters)
    # print: {'S': S, 'E': E, 'N': N, 'D': D, 'M': M, 'O': O, 'R': R, 'Y': Y}

    words = { j: Int(j) for j in list(tokenWords)}
    # print(words)
    #print: {'SEND': SEND, 'MORE': MORE, 'MONEY': MONEY}

    # convert each of string from letters to numbers
    for l, s in letters.items(): solver.add(0 <= s, s <= 9)

    # Letters must be unique
    if unique and len(letters) <= 10:
        solver.add(Distinct(*letters.values()))

    # Words must be unique
    solver.add(Distinct(*words.values()))

    # Check first word of letter must be not zero
    for w in words.keys():
        solver.add(letters[w[0]] != 0)

    # Conver word to decimal values
    # 10**index = 10^index
    for w, wKey in words.items():
        solver.add(wKey == Sum(*[
            lKey * 10**index 
            for index, lKey in enumerate(reversed([
                letters[l] for l in list(w)
            ]))
        ])) 

    solver.add(eval(input, None, words))

    solutions = []

    # print(input)
    # print(type(input))
    # print : SEND + MORE == MONEY

    # str(solver.check()) == 'sat'
    # it mean: check true
    while str(solver.check()) == 'sat' :
        solutions.append({ str(s): solver.model()[s] for l,s in letters.items() })
        # print(solutions[-1])
        # {'SEND': 9567, 'MORE': 1085, 'MONEY': 10652}
        solver.add(Or(*[ s != solver.model()[s] for l,s in letters.items() ]))

    runTime = round(time.perf_counter() - startTime, 1)
    return solutions, runTime    


