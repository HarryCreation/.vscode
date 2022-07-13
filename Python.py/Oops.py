

# class Tv:
#     def __init__(self, size, type, price):
        
       
#         self.size = size
#         self.type = type
#         self.price = price
        
    
#     def compare(self,other):
#         if self.size == other.size:
#             return self.size + other.size
#         else:
#             return self.size - other.size
        
#     def Total_cost(self,*agrs):
#         return self.price + agrs.price
        
    
        
# room_1 = Tv(32, "LED", 23000)
# room_2 = Tv(42, "LCD", 40000)
# room_3 = Tv(52, "OLED", 70000)

# print(room_1.Total_cost(room_2))

# print(room_1.compare(room_2))




class car:
    
    Wheels = 4
    
    def __init__(self, company, price):
        self.company = company
        self.price = price
        self.Engine = self.engine()
    
    def show(self):
        # self.engine.show()
        print(self.eng.show())
        
    @classmethod   
    def info(cls):
        return cls.Wheels
    
    
    @staticmethod
    def information():
        return "This class is of Cars"
    
    class engine:
        
        def __init__(self):
            self.name = "Leapor"
            self.rpm = 67
            
        def show(self):
            print(self.name, self.rpm)
            
    eng = engine()
            
        
class ShowRoom(car):
    
    def inf(self):
        print(self.company, self.price)

showroom = ShowRoom("Verno", 90000000000)

# print(showroom.info())

Car_1 = car("Mini Cooper", 600000)
Car_2 = car("Bugati", 900000)
Car_3 = car("Telsa", 800000)

print(Car_1.show())


# Car_1.Wheels =7

# print(Car_1.Wheels , "&"  , Car_2.Wheels)
# print(Car_1.info())
# print(car.info())
# print(car.information())
# print(Car_2.company)


