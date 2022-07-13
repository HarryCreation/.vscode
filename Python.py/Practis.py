# # user_input,sum = input("Enter the Word :"),0
# # l = [[int(x) for x in str(ord(i))] for i in user_input]
# # for i in range(len(l)):
# #     sum += max(l[i])
# # print("The ascii value of word in which greater number are added :",sum)

# #Bubble Sorting
# l=[]
# for i in range(int(input("enter the number"))):
#     l.append(i)
    

# for i in range(len(l)-1):
#     for j in range(len(l)-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)   

# #Selection Sorting 



# l=[7,9,6,1,2]

# for i in range(1,len(l)):
#     current = l[i]
#     j = i-1
#     while(j>=0 and current<l[j]):
#         l[j+1] = l[j]
#         j=j-1
#     l[j+1]=current
# print(l)   


# dict1 = {"a":12,"b":22,"c":9}
# s =sorted(dict1.items(),key=lambda x:x[1])
# print(s)

# l = [1,2,3,4,9]
# # l.reverse()
# l = list(reversed(l,Boolean = False))
# print(l)

# x=[('Alberto Franco','15/05/2002','32kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
# print(list(map(lambda x:int(x[2][:2]),x)))
# print(list(filter(lambda x:int(x[2][:2])%2==0,x)))

# from typing import ChainMap


# dict_1 = {'John': 15, 'Rick': 10, 'Misa' : 12 }
# dict_2 = {'Bonnie': 18,'Rick': 20,'Matt' : 16 }
# d1 = {'a': 1, 'b': 2} 
# l =ChainMap(d1,dict_1,dict_2)

# print({**dict_1,**dict_2})

x =123
sum=0

for i in range(0,len(str(x))):
    a=x%10
    sum = (sum*10)+a
    x = x//10
print(sum)

l=[2,9,5,1,7]

for i in range(len(l)-1):
    print(i," i")
    for j in range(len(l)-i-1):
        print(j)
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
# print(l)
    