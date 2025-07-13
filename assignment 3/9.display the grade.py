
per=float(input("enter a persentage:"))

if(per>=80 and per<=100):
    print("destinction")
elif(per>=70 and per<=80):
    print("first class")
elif(per>=60 and per<=70):
    print("higher second  class")
elif(per>=40 and per<=60):
    print("second class")
elif(per<40 and per>=0 ):
    print("fail")
else:
    print("wrong input")