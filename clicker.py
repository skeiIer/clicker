def factorial(n= 1000000):
        if n == 1:
            yield 1
        if n == 2:
            yield 1
        else:
            yield factorial(n-1) + factorial(n-2)

print(factorial())
for i in factorial():
    print(i)