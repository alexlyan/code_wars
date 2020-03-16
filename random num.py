import random


def rd():
    """list random numbers """

    lst = []
    # n = int(input("Enter how diffuclt should be numbers: "))
    for _ in range(2):
        n = random.randint(0, 999999999)
        lst.append(n)
    print(lst)


rd()








