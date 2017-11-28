for num in range(1,50):
    if(num%15==0):
        print("FizzBuzz")
        continue
    elif(num%5==0):
        print("Buzz")
        continue
    elif(num%3==0):
        print("Fizz")
        continue
    print(num)