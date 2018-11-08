def a(n):
    if n > 9999:
        print("*.***", end="")
    else:
        print("{}.".format(n//1000), end="")
        print("{}".format((n%1000)//100), end="")
        print("{}".format((n%100)//10), end="")
        print("{}".format((n%10)), end="")
    print(" cm")

a(99999)
a(9999)
a(999)
a(99)
a(9)
a(0)