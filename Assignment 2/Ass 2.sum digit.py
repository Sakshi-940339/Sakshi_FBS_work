# sum of digit in 3 digit no
num =int(input("Enter of digit"))
 
a= num %10
num=num//10
c=num % 10
d= num //10
sum=a+c+d
print("The sum of 3 didgit is=",sum)