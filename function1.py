def func1():
    print("I am a function")

func1()
print(func1())
print(func1)

def func2(arg1, arg2):
    print(arg1, " ", arg2)

def cube(x):
    return x*x*x


func2(20, 210)
print(func2(20,10))
print(cube(5))

def power(num, x = 1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(2))
print(power(2, 3))
print(power(x = 3, num = 2)) #python allows to call variables with their names. this can be in an unordered form

#function with variable number of argumets
def multi_add(*args):  #the star character means that u can pass a variable number of arguments
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(4, 5, 10, 4))
