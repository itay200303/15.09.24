# start
import  random
guessing_counter: int = 1
num1: int = random.randint(1, 100)
number_choice: int = int(input("Choice your number :"))
while number_choice > num1:
    print("Your number is too big...")
    number_choice: int = int(input("Choice your number :"))
    guessing_counter += 1
    if number_choice < num1:
        print("Your number is too small...")
        number_choice: int = int(input("Choice your number :"))
        guessing_counter += 1
else:
    print("BINGO")
    print(f"Your guessing attempts was : {guessing_counter}")

# end


