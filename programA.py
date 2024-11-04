import sys
import random


def programA():
    for line in sys.stdin:
        if 'Hi' == line.rstrip():
            sys.stdout.write("Hi\n")
            sys.stdout.flush()
        elif "GetRandom" == line.rstrip():
            sys.stdout.write(str(f"{generator()}\n"))
            sys.stdout.flush()
        elif "Shutdown" == line.rstrip():
            break



def generator():
    return random.randint(-1000, 1000)

programA()