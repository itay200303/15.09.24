# start

sum_temp: int = 0
temp: int = 0
for i in range(1, 5 + 1):
    temp: int = int(input('Enter the temperature :'))
    if temp > 45 or temp < -50:
        print('Try again!')
        break
    sum_temp += temp

else:
    avg: float = sum_temp / 5
    print(f"the avg of the temp is: {avg: .2f}")

# end