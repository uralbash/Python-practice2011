# coding=utf8

from math import sqrt 
filename = "result.txt"
f1 = open(filename, "w") 
a=float(input(u"Enter A: ")) 
b=float(input(u"Enter B: "))
n=int(input(u"Enter N: "))
s = (b-a)/n 

while a<=b: 

    print('%-10.4f ' % (a)), str(sqrt(a)) 

    f1.write('%10.4f ' % (a)), f1.write('%15.8f\n' % (sqrt(a)))

    a=a+s
    
f1.close()
    


