def fib(n):
    if n == 1: 
    	y = 1 
    elif n == 0: 
    	y = 0
    else: 
    	y = fib(n-1)+fib(n-2)
    return y

print(fib(6))

