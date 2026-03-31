import itertools

class WordCounter:
    def __init__(self, alphabet, length):
        self.alphabet = alphabet
        self.length = length
        self.restrictions = []
    
    def add_count_restriction(self, letter, max_count):
        self.restrictions.append(('count', letter, max_count))
    
    def add_first_restriction(self, forbidden_letters):
        self.restrictions.append(('first', forbidden_letters))
    
    def add_last_restriction(self, forbidden_letters):
        self.restrictions.append(('last', forbidden_letters))
    
    def solve(self):
        count = 0
        for combo in itertools.product(self.alphabet, repeat=self.length):
            word = ''.join(combo)
            ok = True
            for r in self.restrictions:
                if r[0] == 'count' and word.count(r[1]) > r[2]:
                    ok = False
                elif r[0] == 'first' and word[0] in r[1]:
                    ok = False
                elif r[0] == 'last' and word[-1] in r[1]:
                    ok = False
            if ok:
                count += 1
        return count


class DigitCounter:
    def __init__(self, number, base=2, digit='1'):
        self.number = number
        self.base = base
        self.digit = str(digit)
    
    def solve(self):
        if self.base == 2:
            rep = bin(self.number)[2:]
        elif self.base == 8:
            rep = oct(self.number)[2:]
        elif self.base == 16:
            rep = hex(self.number)[2:].upper()
        else:
            num = self.number
            if num == 0:
                rep = "0"
            else:
                rep = ""
                while num > 0:
                    rep = str(num % self.base) + rep
                    num //= self.base
        return rep.count(self.digit)


class PowerNumbersFinder:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        self.m_start = 0
        self.m_step = 1
        self.n_start = 0
        self.n_step = 1
    
    def set_m_parity(self, is_even):
        if is_even:
            self.m_start, self.m_step = 0, 2
        else:
            self.m_start, self.m_step = 1, 2
    
    def set_n_parity(self, is_even):
        if is_even:
            self.n_start, self.n_step = 0, 2
        else:
            self.n_start, self.n_step = 1, 2
    
    def solve(self):
        nums = []
        max_m = 0
        while 2 ** max_m <= self.max_val:
            max_m += 1
        max_n = 0
        while 3 ** max_n <= self.max_val:
            max_n += 1
        
        for m in range(self.m_start, max_m, self.m_step):
            for n in range(self.n_start, max_n, self.n_step):
                x = (2 ** m) * (3 ** n)
                if self.min_val <= x <= self.max_val:
                    nums.append(x)
        return sorted(nums)

# ЗАДАЧА 1
counter1 = WordCounter('ВИШНЯ', 6)
counter1.add_count_restriction('В', 1)
counter1.add_first_restriction('Ш')
counter1.add_last_restriction('ИЯ')
print("Задача 1:", counter1.solve())

counter2 = WordCounter('ИВАН', 4)
counter2.add_count_restriction('И', 2)
counter2.add_first_restriction('В')
counter2.add_last_restriction('Н')
print("Задача 1:", counter2.solve())

# ЗАДАЧА 2
counter3 = DigitCounter(4**2014 + 2**2015 - 8, base=2, digit='1')
print("Задача 2:", counter3.solve())

counter4 = DigitCounter(2**20 + 2**2011 - 6, base=8, digit='2')
print("Задача 2:", counter4.solve())

# ЗАДАЧА 3
finder = PowerNumbersFinder(400000000, 600000000)
finder.set_m_parity(True)
finder.set_n_parity(False)
print("Задача 3:", finder.solve())

finder2 = PowerNumbersFinder(4000011, 600000000)
finder2.set_m_parity(True)
finder2.set_n_parity(False)
print("Задача 3:", finder2.solve())