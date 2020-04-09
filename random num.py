import random

def rd():
    '''list random numbers'''

    # n = int(input("Enter how difficult should be numbers: "))
    for _ in range(2):
        n = random.randint(0, 999)
        print(n)

rd()








