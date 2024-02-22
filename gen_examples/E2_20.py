n=100
fib=[1,1]
for i in range(2,n+1):
    print(i)
    fib.append(fib[i-1]+fib[i-2])
print(fib)