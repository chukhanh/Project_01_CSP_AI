import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def pathInput():
    my_file = os.path.join(THIS_FOLDER, 'input.txt')
    return (my_file)

def pathOutput():
    my_file = os.path.join(THIS_FOLDER, 'output.txt')
    return (my_file)  