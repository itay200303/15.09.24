# start

num: int = int(input("Enter a number: "))
if num % 5 == 0 and num % 3 ==0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Fizz")
else:
    print("Buzz")

# end