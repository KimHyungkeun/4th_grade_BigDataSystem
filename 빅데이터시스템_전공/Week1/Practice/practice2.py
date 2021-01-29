# Example1
items = [1,2,3,4,5]
squared = []
for i in items :
    squared.append(i**2)
print(squared)

squared2 = list(map(lambda x: x**2, items))
print(squared2)

# Example2
def fahrenheit(T) :
    return ( (float(9)/5) * T + 32)

def celsius(T) :
    return (float(5)/9) * (T-32)

temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures) # Object 그 자체를 return
C = map(celsius, temperatures) # Object 그 자체를 return

# temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures)) # 함수표현
# print(temperatures_in_Fahrenheit)

F = list(map(lambda x : (float(9)/5) * x + 32, temperatures)) # 람다함수로 표현
print(F)

# Example3
chars = ['s', 'k', 'k', 'a', 'v']
def change_upper_case(s) :
    return str(s).upper()

# map_iterator = list(map(change_upper_case, chars))
# print(map_iterator)

map_iterator = list(map(lambda s : str(s).upper() , chars))
print(map_iterator)

# Example4 : Tuple, Set
squared2 = list(map(lambda x: x**2, items)) # 리스트
print(squared2)
squared2 = tuple(map(lambda x: x**2, items)) # 튜플
print(squared2)
squared2 = set(map(lambda x: x**2, items)) #set, 집합
print(squared2)

# Example5 : Multiple list
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1, -4, 5, 9]
D = list(map(lambda x,y : x+y, a, b))
E = list(map(lambda x,y,z : x+y+z, a, b, c))
F = list(map(lambda x,y,z : 2.5*x + 2*y + - z, a, b, c))
print(D)
print(E)
print(F)

print(list(map(pow, [3,2], [5,10])))

# Example6 : list Functions
def multply(x) :
    return (x*x)

def add(x) :
    return (x+x)

funcs = [multply, add]
for i in range(5) :
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Example7 : Dictionary
dict_a = [ {'name' : 'python', 'points' : 10 },{'name' : 'java', 'points' : 8} ]
A = map(lambda x : x['name'], dict_a)
B = map(lambda x : x['points'] * 10, dict_a)
C = map(lambda x : x['name'] == 'python', dict_a)
print(list(A))
print(list(B))
print(list(C))