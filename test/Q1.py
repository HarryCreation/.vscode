l=[]
for i in range(1,51):
    for j in range(2,int(i/2)+1):
        if i%j==0:
            l.append(i)

h = set(l)
print("This is composite number form 1 to 50 :")
print(h)

print("From above composite number set, of which number you want factoral :")
x = int(input())       
g =[]
for j in range(1,51):
        if x%j==0:
            g.append(j)
print("The Factors of",x,"are : ",g)
        
