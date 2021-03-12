def function1 ():
    print("alin")
    print("sergiu")

print("this is out")
function1()
function1()

def function2 (Felicia):
    return 2*Felicia

a = function2 (3)
print(a)

b = function2 (5)
print (b)

def function3 (x, y):
    return x-y
c = function3 (10, 5)
print (c)

def function4 (x):
    print(x)
    print("this is still here")
    return 3*x

e = function4(4)
print (e)

name1 = "Felicia"
height1 = 1.69
weight1 = 63

name2 = "Sergiu"
height2 = 1.78
weight2 = 110

def bmi_calculator(name, height, weight):
    bmi = weight / (height**2)
    print ("bmi:")
    print (bmi)
    if bmi < 25:
       return name + "is not overrated"
    else:
       return name + "is overrated"
result1 = bmi_calculator(name1, height1, weight1)
result2 = bmi_calculator(name2, height2, weight2)

print (result1)
print (result2)