#-*encoding:utf-8-*-
#求出1000以内的完数
def myfunc(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
            if n==sum:
                print n
                return True
for i in range(1,1001):
    if myfunc(i):
        print (u"1000以内的完数:{}".format(i))
