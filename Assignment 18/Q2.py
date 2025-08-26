class Distance:
    def __init__(self,km=0,m=0,cm=0):
        self.km=km
        self.m=m
        self.cm=cm
        self._normalize()

    def __del__(self):
        print(f"object with distance {self.km} km {self.m} m {self.cm} cm is destroyed")

    def _normalize(self):
        """convert  cm and m and m to km if overflow"""
        self.m += self.cm // 100
        self.cm = self.cm % 100

        self.km +=self.m //1000
        self.m =self.m % 1000

    def __add__(self,other):
        return Distance(self.km + other . km, self.m + other.m , self.cm + other.cm)
    
    def __sub__(self,other):
        total1=self.km*100000 +self.m*100+self.cm

        total2 =  other.km*100000 + other.m*100 +other.cm
        diff=abs(total1 - total2)

        km=diff // 100000
        diff %=100000
        m=diff // 100
        cm=diff % 100

        return Distance(km,m,cm)
    
    def __str__(self):
        return f"{self.km} km {self.m } m {self.cm} cm"
    
d1=Distance(2,950,80)
d2=Distance(1,200,50)

print("Distance 1:" ,d1)
print("Distance:",d2)

d3 = d1+d2
print("Addition:",d3)

d4=d1-d2
print("subtraction:",d4)

