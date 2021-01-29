from functools import reduce
result = reduce(lambda x, y : x * y, [1,2,3,4])
print(result)

result = reduce(lambda x, y : x * y, [1,2,3,4], 100)
print(result)

# Example1
lists = [10,6,7,5,2,1,8,5]
s = reduce(lambda x, y : x if (x > y) else y, lists) # 리스트 내에서 가장 큰 수를 뽑아낸다
print(s)

lists = [10,6,7,105,2,1,8,5]
s = reduce(lambda x, y : x if (x > y) else y, lists, 200) # 리스트 내에서 200보다도 더 큰 수를 뽑아낸다. 
print(s)