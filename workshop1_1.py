s = int(input("Enter a start number"))
e = int(input("Enter a end number"))

if s > e:
    print("Start number should be less than end number")
else:
    for i in range(s, e + 1):
        print(i)

    n = s
    while n < e + 1:
        print(n)
        n += 1
