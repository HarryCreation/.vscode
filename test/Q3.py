x = list(range(100,201))

even =[]
odd=[]
for y in x:
    a = y%1000//100
    b = y%100//10
    c=y%10
    if( a+b+c)%2==0:
        even.append(y)
    else:odd.append(y)
print("The sum of digits is even : ",even)
print("      ")
print("The sum of digits is odd : ",odd)

