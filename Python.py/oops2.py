# ''' Constructor in inheriance.
# '''
# class A:
#     def __init__(self):
#         print("its init")
        
#     def fea(self):
#         print("its class A")
        
# class B(A):
    
#     def __init__(self):
#         print("its class be init")
        
#     def fea2(self):
#         print("Its Class B")
#         super().fea()
        
# a1 = B()

# print(a1.fea2())


# '''
# Duck typing

#     “If it looks like a duck and quacks like a duck, it’s a duck”


# '''

  
  
# class Bird:
#     def fly(self):
#         print("fly with wings")
  
# class Airplane:
#     def fly(self):
#         print("fly with fuel")
  
# class Fish:
#     def swim(self):
#         print("fish swim in sea")
  
# # Attributes having same name are
# # considered as duck typing
# for obj in Bird(), Airplane(), Fish():
#     obj.fly()


'''
In this Example i have done operator overloading
'''

class student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        
        if r1 > r2:
            return True
        else:
            return False
        
    def __str__(self):
        return '{} {}'.format(self.m1 , self.m2)
        
        
s1 = student(23, 67)
s2 = student(89, 34)

print(s1 > s2)
print(s1)
