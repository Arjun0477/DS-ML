
a=[]
n=int(input("Enter the array limit"))
for i in range(n):
    a.append(int(input()))
print(a)
for i in range(n): 
     for j in range(i+1,n):
        if(a[i]>a[j]):
         temp=a[i]
         a[i]=a[j]
         a[j]=temp
print(a)

"""""""
Enter the array limit4
1
2
7
5
[1, 2, 7, 5]
[1, 2, 5, 7]

"""""""
