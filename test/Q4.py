list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l=[]

for x,y in zip(list1,list2):
         s = x+y
         l.append(s)
print(l,end="")