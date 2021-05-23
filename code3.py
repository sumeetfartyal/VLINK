x = int(input("Enter any number"))
if x > 9:
    lst=[]
    for i in range(1, x + 1):
        if x % i == 0:
            if i % 2 == 0:
                lst.append(i)
            else:
                continue
    if lst :
        lst.sort(reverse=True)
        print(lst)
        mul=1
        for di in lst:
            mul=mul*di
        print(mul)
    else:print("Please input a different number.")
else:print("Invalid number")