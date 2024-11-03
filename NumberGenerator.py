import random
import sys


def programA():
    for line in sys.stdin:
        if 'Hi' == line.rstrip():
            print("Hi")
            programA()
        elif "GetRandom" == line.rstrip():
            print(generator())
            programA()
        elif "Shutdown" == line.rstrip():
            exit()
        else:
            programA()


def generator():
    return random.randint(-100, 100)


def programB():
    programA()
    sys.stdout.write("Hi")


programB()
