from itertools import combinations

def eliminate_char():
    text=input()
    text2="".join([c for c in text if c.isalpha()])
    return text2

print(eliminate_char())

def replace_word(word1,word2,prop):
    return prop.replace(word1,word2)

print(replace_word("abc","def","abc"))

def func(x,y):
    cuv_x = x.split()
    cuv_y = y.split()
    count = 0
    for c in cuv_x:
        for b in cuv_y:
            if b.startswith(c):
                count+=1
    return count

print(func("tre pre chi","china, e, faf3qe13"))


def palindrome(num):
    num1 = str(num)
    for i in range(1,len(num1)):
        if num1[-i] != num1[i-1]:
            return False
    return True

print(palindrome(121))

def nr_cuvinte(text):
    return len(text.split())

print(nr_cuvinte("Hello World 325315 1514x1"))


#6
def func(list_nr):
    tris = []
    for a,b,c in combinations(list_nr,3):
        if (a+b > c) and (b+c > a) and (c+a > b):
            tris.append([a,b,c])
            print(a,b,c)
            print("\n")
    return len(tris)

print(func([1,2,3,4,5,6,9]))
