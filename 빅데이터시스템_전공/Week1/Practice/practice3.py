# Example 1 : Filter
a = filter(lambda x : x < 0, range(-5, 5))
print(list(a))

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(list(filter(lambda x : x in a, b)))

# Example 2 
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x) :
    if x < 18 :
        return False
    else :
        return True

adults = filter(myFunc, ages)
print(list(adults))

# Example 3
alphabets = ['a','b','c','e','i','j','o']

def filterVowels(alphabet) :
    vowels = ['a','e','i','o','u']

    if alphabet in vowels :
        return True
    else :
        return False
result = filter(filterVowels, alphabets)
print(list(result)) 

# Example 4
listOfStr = ['hi', 'this', 'is', 'a' , 'very', 'simple', 'string', 'for', 'us']
filteredList = filter(lambda s : len(s) == 2, listOfStr)
print(list(filteredList))

# Example 5
strObj = 'Hi this is a sample string, a very sample string'

filteredChars = ' '.join(filter(lambda x: x not in ['a','s'], strObj)) #공백 문자열에 새로운 문자들 또는 문자열들을 넣는다
print(filteredChars)