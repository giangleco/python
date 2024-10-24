for i in range(1,101):
    tong=0
    for j in range(1,i//2+1):
        if i%j==0:
            tong+=j
        if tong==i:
            print(i, end=" ")
        