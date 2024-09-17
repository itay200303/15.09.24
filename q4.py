# start

num: int = int(input("enter a number :"))
counter: int = 0
while num % 7 == 0:
    num: int = int(input("enter a number: "))
    counter += 1
if num % 11 == 0:
   print("Number divisible by 11 detected. Exiting...")
else:
    print(f"Number not divisible by 7. Exiting...")

if num % 11 != 0:
        print(f"Total numbers divisible by 7: {counter}")

# end