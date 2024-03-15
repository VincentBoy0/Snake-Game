import numpy as np
def checkContinue():
    with open('Data/check.txt', 'r') as file:
        data = file.read()
        ok = int(data)
        return ok

def colorHead():
    with open('Data/colorHead.txt', 'r') as file:
        data = file.read()
        color = eval(data)
        return color

def colorBody():
    with open('Data/colorBody.txt', 'r') as file:
        data = file.read()
        color = eval(data)
        return color

def snakeArray():
    with open('Data/snake.txt', 'r') as file:
        lines = file.readlines()
        processed_lines = [line.replace('[', '').replace(']', '') for line in lines]
    return np.loadtxt(processed_lines)

def foodArray():
    with open('Data/fruit.txt', 'r') as file:
        lines = file.readlines()
        processed_lines = [line.replace('[', '').replace(']', '') for line in lines]
    return np.loadtxt(processed_lines)

def snakeDir():
    with open('Data/direction.txt', 'r') as file:
        data = file.read()
        dir = int(data)
        return dir
    
def levelGame():
    with open('Data/level.txt', 'r') as file:
        data = file.read()
        level = int(data)
        return level