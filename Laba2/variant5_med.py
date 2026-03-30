import itertools
def task1():
    """
    >>> task1()
    4352
    """
    letters = 'ВИШНЯ'
    glas = 'ИЯ'
    k = 0  
    for i in itertools.product(letters, repeat=6):
        word = ''.join(i)  
        if word.count('В') <= 1 and word[0] != 'Ш' and word[-1] not in glas:
            k += 1
    return k

def task2():
    """
    >>> task2()
    2013
    """
    x = 4**2014 + 2**2015 - 8
    num = ""
    while x != 0:
        num += str(x % 2) 
        x //= 2  
    num = num[::-1]
    return num.count("1")

def task3():
    """
    >>> task3()
    [408146688, 452984832, 516560652, 573308928]
    """
    s = []
    for m in range(0, 30, 2):
        for n in range(1, 20, 2):
            x = 2**m * 3**n
            if 400000000 <= x <= 600000000:
                s.append(x)
    return sorted(s)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    print("\n=== Результаты ===")
    print("task1 =", task1())
    print("task2 =", task2())
    print("task3 =", task3())