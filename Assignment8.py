def createDictionary(number):
    fib_old=0
    fib_mid=1
    fib_new=1
    list=[]
    for num in range(0,number):
        print(fib_mid)
        list.append(fib_mid)
        fib_mid=fib_old+fib_new
        fib_old=fib_new
        fib_new=fib_mid
    return list
no=input("Enter how many fibonacci numbers are required")
List=createDictionary(no)
print List

