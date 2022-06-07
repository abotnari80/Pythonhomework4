from tracemalloc import start


def fibo(n):
    if n>=0:
       idx = range(n+1)
       x = [0,1]
       for k in idx[2:]:
           x.append(x[k-1] + x[k-2]) 
       return x[n]
    else:
       n=-(n-1)
       idx = range(n+1)
       x = [1,0]
       for k in idx[2:]:
           x.append(x[k-2] - x[k-1]) 
       x.reverse()
    return x[0]

value = int(input('Введите число '))
startVlaue = 0 - value

for i in range(startVlaue,value + 1):
   print(fibo(i), end=' ')