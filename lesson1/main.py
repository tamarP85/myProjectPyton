import datetime

mydict={}
def warpper(func):
    def inner(*args):
        time_begin=datetime.datetime.now()
        func(*args)
        time_finish=datetime.datetime.now()
        return time_finish-time_begin
    return inner
@warpper
def say_name(n):
    for i in range(n):
        print(i)
#

def warpper2(func):
       def wrapper3(n):
           if mydict.keys().__contains__(n):
               return mydict[n]
           else:
              num=func(n)
              mydict[n]=num
              return num
       return wrapper3

@warpper
@warpper2
def fibonachi(n):
    if n==0:
        return 0
    if n<2:
        return 1
    return fibonachi(n-1)+fibonachi(n-2)

print(say_name(100))

print(fibonachi(200))
print(fibonachi(5))
print(fibonachi(200))