num = int(input("Enter a number"))


def table(n):
    # 10 * 1 = 10
    # 10 * 2 = 20
    # 10 * 3 = 30
    # 10 * 4 = 40
    for i in range(1, 11):
        print(str(n) + " * " + str(i) + " = " + str(n * i))


table(num)
