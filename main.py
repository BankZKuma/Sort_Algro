#bubble sort
"""num=[int(i) for i in input().split()]
d=len(num)
for i in range(d-1):#5
    for j in range(d-i-1):#
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
print(num)"""

#selection sort
"""num=[int(i) for i in input().split()]
d=len(num)
for i in range(d-1):
    for j in range(i,d):
        if num[i]>num[j]:
            num[i],num[j]=num[j],num[i]
print(num)"""

#insertion sort
"""num=[int(i) for i in input().split()]
d=len(num)
j=int()
for i in range(1,d):
    temp=num[i]
    while temp<num[i-1] and i>0:
        print('|')
        num[i],num[i-1]=num[i-1],num[i]
        i-=1
print(num)"""
