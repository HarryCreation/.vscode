

n = int(input("enter the number : "))
reverse = 0
while n>0:
    '''
    suppose number is 153 , and doing n%10 we get the last number like 3.
     
    '''
    a = n%10
    
    '''
    suppose reverse = 3 
    reverse = 3*10 = 30
    reverse = 30 + 5
    reverse = 35
    
    '''
    
    reverse = reverse * 10 + a
    
    '''
    now we have to remove last number from 153 , for 153//10 = 15
    
    '''
    n = n//10

    