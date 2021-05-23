num=int(input("Enter the no of elements:"))
lst=[]
if num>=0:
    for i in range(num+1):
        str1=input("Enter the value")
        lst.append(str1)
    def Sorting(lst):
        lst2 = sorted(lst, key=len)
        return lst2
    print(Sorting(lst))
    print(lst[0])
else:
    print('Invalid Input')