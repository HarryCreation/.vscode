#Q1

numbers = (2,3,4,5,6,7,8)
x = list(map(lambda a:a*3,numbers))
print(x)

#Q2
list1 = [500,1000,400,40000,999,2,0.5,17]
list1.sort()
print(list1)

#Q3
l1 =[0,1,2,3,5,8,13]
l_evn= filter(lambda x: x%2==0,l1)
l_odd= filter(lambda y : y%2!=0,l1)

print(list(l_evn))    
print(list(l_odd))

#Q4

l1 = [10,20,30,40,50]
i1=[1,2,3,4,5]
x = map(lambda x,y:x**y,l1,i1)
print(list(x))

#Q5
l=[]
for x in range(101,201):
    if "3" in str(x):
        l.append(x)
print(l)

#Q6
firstname=("tony","thor","captain","elon","bill")
lastname =("stark","odin","america","musk","gates")

x =list(zip(firstname,lastname,firstname))
print(x)