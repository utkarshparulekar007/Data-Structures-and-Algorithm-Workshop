num = 123456
a = num % 10000 #3
num = num // 10000 #12
b = num % 10000 #2
c = num // 10000 #1
rev = a*1000+b*100+c*10+d*1
print(rev)