


a = ("Tom",19,80)
b =("John",20,90)
c =("Jony",17,91)
d = ("Jony",17,93)
e =("Json",21,85)
x = zip(a,b,c,d,e)

li = list(x)
print(li)
name=[]
name.append(li[0])
name.sort()

age=[]
age.append(li[1])
age.sort()

score=[]
score.append(li[2])
score.sort()
print(score)



