# lambda 연습

# Examples
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a + b
print(x(5,6))

high_ord_func = lambda x, func : x + func(x)
ans = high_ord_func(2, lambda x : x + 3)
print(ans)

def square(x) :
    return x * x

def add3(x) :
    return x + 3

ans = high_ord_func(2, square)
print(ans)

ans = high_ord_func(2, add3)
print(ans)