fib_old=0
fib_mid=1
fib_new=1
for num in range(0,20):
    print(fib_mid)
    fib_mid=fib_old+fib_new
    fib_old=fib_new
    fib_new=fib_mid

