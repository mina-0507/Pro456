x = 4**2014 + 2**2015 - 8
num = ""
while x != 0:
    num += str(x % 2) 
    x //= 2  
num = num[::-1]
count_ones = num.count("1")
print(count_ones)