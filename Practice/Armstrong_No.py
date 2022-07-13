


def armstrong(n):
    
    def count_No(n):
        global count
        count = 0
        while n > 0:
            count +=1
            n = n//10
    
    count_No(n)
    
    sum = 0
    temp = n

    while n> 0:
        a = n%10
        sum += a**count
        n = n//10       
    
    if temp == sum:
        return "The {} Armstrong Number.".format(temp)
    else:
        return "The {} is not Armstrong Number.".format(temp)
        
    
    
n = int(input("Enter the number to Check it is Armstrong Number : "))


print(armstrong(n))

