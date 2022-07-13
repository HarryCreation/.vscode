# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
    
    
# print(fibo(9))


# a=int(input("Enter the terms : "))
# f=0                                         
# s=1                                        
# if a<=0:
#     print("The requested series is",f)
# else:
#     print(f,s,end=" ")
#     for x in range(2,a):
#         next=f+s                           
#         print(next,end=" ")
#         f,s=s,next





# def fib(n):
#     a,b = 0,1
#     if a < n:
#         yield a
#         a,b = b,a+b
        
# x = fib(5)

# print(x.__next__)
        
# for i in x:
#     print(i)
    
    
def fib(limit):
      
    # Initialize first two Fibonacci Numbers 
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
  
# # Create a generator object
x = fib(int(input("Enter the Limit : ")))
  
# # Iterating over the generator object using next
# print(x.__next__()) # In Python 3, __next__()
# print(x.__next__())

for i in x:
    print(i)
    

