

#Q2
n=int(input())
count=0
for x in range(1,n+1):
    count += x
    if x == n:
        avg=count/n
        print("sum of all natural number is : ",count)
        print("avg of all natural number is : ",avg)
       

#Q3
n = 6
k = n-1
b = -3
for x in range(0,n):
    for j in range(0,k):
        print(" ",end="")
    k = k-1
    b +=2
    for j in range(1,x+1):
        print(b,end=" ")
    print("")
    
        
#Q4
for i in range(10,51):
    if i%2==0:
        print(i,end=" ")
        
#Q5
k= 5-1
for i in range(1,9,2):
    for j in range(1,k):
        print(" ",end=" ")
    k = k-1
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
n = 2-1
for x in range(5,1,-2):
    for y in range(n,0,-1):
        print(" ",end=" ")
    n = n+1
    for y in range(1,x+1):
        print("*",end=" ")
    print("")
h = 7-1
for a in range(1,4):
    for b in range(0,h):
        print(" ",end="")
    h = h-1
    for b in range(1,a+1):
        print("*",end=" ")
    print("")
#Q6

x = list(range(101,201))
d_3=[]
for i in x:
    j = str(i)
    f_value,l_value=j[0],j[2]
    d = int(f_value)+int(l_value)
    if d%3==0:
        d_3.append(i)
print(d_3)

#Q7

n = list(range(1,101))
d_5 = []
for i in n:
    j = str(i)
    h = j[::-1]
    ans=int(h)+i
    if ans%5==0:
        d_5.append(ans)
print(d_5)
        
#Q8
for i in range( 1 , 6 ) :
    for j in range( 0 , i) :
       print( i , end = " ")
    print("")
    
#Q9
list1= [23,16,45,24,27,99]
for i in list1:
    if i%8==0:print(i)
    
#Q10
dict1 = {"name":"value"
         ,"weight":"500"
         ,"color":"brown"}

dict2 ={"name":"value"
         ,"hahh":"500","color":"brown"}
result =[]
for x in zip(dict1.keys(),dict2.keys()):
    if x[0]==x[1]:
         result.append(True)
    else:
        result.append(False)
print(all(result))

#Q11

s = "abcd efgh ijkl mnop"
x = s.upper()
y = x.split()
for i in y:
    print(i)
