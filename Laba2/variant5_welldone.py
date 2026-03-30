import itertools

class Task1:
    def __init__(self, letters, glas, repeat, max_v):
        self.letters = letters
        self.glas = glas
        self.repeat = repeat
        self.max_v = max_v
    
    def solve(self):
        k = 0
        for i in itertools.product(self.letters, repeat=self.repeat):
            word = ''.join(i)
            if word.count('В') <= self.max_v and word[0] != 'Ш' and word[-1] not in self.glas:
                k += 1
        return k

class Task2:
    def solve(self):
        x = 4**2014 + 2**2015 - 8
        return bin(x).count('1')

class Task3:
    def solve(self):
        s = []
        for m in range(0, 30, 2):
            for n in range(1, 20, 2):
                x = 2**m * 3**n
                if 400000000 <= x <= 600000000:
                    s.append(x)
        return sorted(s)


print(Task1('ВИШНЯ', 'ИЯ', 6, 1).solve())
print(Task2().solve())
print(Task3().solve())