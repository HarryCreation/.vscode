'''sentence = "As far as the laws of mathematics refer to reality they are not certain as far as they are certain they do not refer to reality"
sentence1 ="hello world is world in world hello"
def duplicat(sentence):
    
 words = sentence.split()
 counts = {}
 for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

 print(counts)
 l=[i for i,j in counts.items() if j >1]
 print("#".join(l))
             
duplicat(sentence)'''


list1 =["7and","or","f77or","Fono","Bon","Ghon7"]
list2 =[[x for x in i]for i in list1]
x = max(list1,key=len)
for i in range(0,len(x)):
    for j in range(0,len(list2[i])):
     if list2[i][j].isdigit():
         list1.pop(i)
         
l=[chr(x) for x in range(65,65+26)]
vowel =["A","E","I","O","U"]
'''res=[list1[i] for i in range(0,len(list1)) if list1[i][0] in l and list1[i][0] not in vowel]
print(res)'''
res=""
for i in range(0,len(list1)):
    if list1[i][0] in l and list1[i][0] not in vowel:
        res += " "+list1[i]
print("".join(res))