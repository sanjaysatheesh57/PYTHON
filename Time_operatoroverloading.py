class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):
         new_sec = self.__second + other.__second
         new_min = self.__minute + other.__minute + new_sec 
         new_sec = new_sec % 60
         new_hour = self.__hour + other.__hour + new_min // 60
         new_min = new_min % 60
         return Time(new_hour, new_min, new_sec)
    def show(self):
        print(f"{self.__hour} hr {self.__minute} min {self.__second} sec")
t1 = Time(2, 45, 50)
t2 = Time(3, 20, 30)
t3 = t1 + t2
print("Time 1 =", end=" "); t1.show()
print("Time 2 =", end=" "); t2.show()
print("Sum =", end=" ");    t3.show()
