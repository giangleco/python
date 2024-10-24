def MAX(check):
    MAX=check[0]
    for i in range(0,len(check)):
        if check[i]>check[0]:
            MAX=check[i]
    return MAX
def MIN(check):
    MIN=check[0]
    for i in range(0,len(check)):
        if check[i]<check[0]:
            MIN=check[i]
    return MIN
def check(check):
    for i in range(0,len(check)):
        for j in range(0,len(check)):
            if check[j] ==MAX(check) and check[i]==MIN(check):
               return j,i
a=[14, 2, 20 ,5, 25,13,30,24,50,0]
print(check(a))