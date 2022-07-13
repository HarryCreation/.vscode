#Q1
l1 = {23,42,65,57,89,45,29}
l2 ={57,45,29,67,73,43,48}
l = l1&l2
for x in l:
    l1.remove(x)
print(l1)


#Q2
roll_number = [47,64,69,37,76,83,95,97]
dict1={"A1":47,"B1":69,"C1":76,"D1":97}
for y in dict1.values():
    for x in roll_number:
        if x == y:print("yes")
    else:
       roll_number.remove(x)
       print(roll_number)

#Q3
list_1=["a","b","c","d","e"]
list_2=["a","c","e"]

if set(list_1).issuperset(set(list_2)):print("All ELEMENT  are there in list_1")
else:print("it doesnt contain all the element")        

#Q4

list1=[6,52,74,62]
list2=[85,17,81,92]
list1.extend(list2)
print(list1)


#Q5
import random
lottery_no1 = []
winning_no1 = [1,7,9,11,13,17,23,26,30,34,38,39,41,43,47]
a= random.randint(1,10)
lottery_no1.append(a)


b= random.randint(11,20)
lottery_no1.append(b)


x= random.randint(21,30)
lottery_no1.append(x)


x= random.randint(31,40)
lottery_no1.append(x)


x= random.randint(41,50)
lottery_no1.append(x)

lottery_no = set(lottery_no1)
winning_no = set(winning_no1)

inter = lottery_no&winning_no

print("Your lottery number is : ",lottery_no1)


if len(inter) == 5:print("you have win the lottery")
elif len(inter) == 4:print("Missed by 1 number")
elif len(inter) == 3:print("Missed by 2 number")
elif len(inter) == 2:print("Better luck next time")
elif len(inter) == 1 or len(inter)==0:print("its not your lucky day")


#Q6
dic1={1:20,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)

print(dic1)


#Q7

print("What Element you want to insert :")
no = int(input())
print("At what Position you want to insert :")
p = int(input())

list1 = [12,67,80,57,30]
list1.insert(p,no)
print(list1)


#Q8

l1 =[5,10,15,20,25]
l2=[30,15,10,40,45]
l3=[50,60,15,75,10]
l4=[95,10,15,101,105]
l5=[205,210,15,35,10]

l12_s = set(l1)&set(l2)
l34_s = set(l3)&set(l4)

l12_34 = l12_s&l34_s
l = l12_34&set(l5)
l = list(l)
o = l[0]+l[1]
print(o)