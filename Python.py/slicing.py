#Q1

string1 = "hello how are you?"
string1 = string1.split()
for x in string1:
    y = x[0].capitalize()
    print(y,end="")

#Q2
print("what your string :")
x = input()
print(x[::-1])

#Q3
my = [1,2,3,4,5]
print(my[3:])

#Q4
my = [1,2,3,4,5]
odd =[]
for x in filter(lambda a: a%2!=0,my):
    odd.append(x)
print(odd)


#Q5

x ="hey how are you doing"
y = x.split()
print(y)

#Q6
name = input("what your name : ")
if len(name) > 12:
    print(name[0:7],"...",name[-2:])

#Q7
x = input()
print(x[3:-2])