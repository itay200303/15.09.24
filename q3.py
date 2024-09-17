# start

# x : int = int(input("enter num: "))
# for i in range(1, 5 + 1):
#     for i in range(1 , i + 1):
#         print(i, end = "")
#     print()
# for i in range(4, 0, -1):
#     for j in range(1, i + 1,):
#         print(j, end="")
#     print()


x : int = int(input("enter num: "))
max_width = 2 * x - 1
for i in range(1, x - 2):
    stars = 2 * i - 1
    spaces = max_width - stars // 2
    print(' ' * spaces + '*' * stars)
print()

# end