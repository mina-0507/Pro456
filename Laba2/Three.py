s=[]
for m in range(0,30,2):
    for n in range(1,20,2):
        x = 2**m * 3**n
        if 400000000<= x <=600000000:
            s.append(x)
print(*sorted(s))