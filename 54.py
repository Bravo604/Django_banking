from random import randint


def acc_numb():
    numbers = []
    for i in range(16):
        numbers.append(randint(0, 10))
    return "".join(map(str, numbers))
