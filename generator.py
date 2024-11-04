import sys
import random


def generator():
    for line in sys.stdin:
        if 'Hi' == line.rstrip():
            send_hi()
        elif "GetRandom" == line.rstrip():
            send_number()
        elif "Shutdown" == line.rstrip():
            break



def pseudorandom_number():
    return random.randint(-1000, 1000)


def send_hi():
    sys.stdout.write("Hi\n")
    sys.stdout.flush()


def send_number():
    sys.stdout.write(str(f"{pseudorandom_number()}\n"))
    sys.stdout.flush()


generator()