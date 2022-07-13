vowel =["a","e","i","o","u"]
consonanats =["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
print("whats your sentence ?")
x = input()
y = list(x)
count=[]
const=[]
for i in y:
    if i in vowel:
        count.append(i)
    elif i in consonanats:
        const.append(i)

print("The given input is : ", x)
print("There are ",len(count), "Vowel in given input")
print("There are ",len(const), "consonants in given input")