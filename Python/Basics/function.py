'''
print("Welcome to function")
def fun():
    print("Hello")
    print("How are you")

print("Time to call function")
fun()

print("Welcome to calculator")
def show():
    print("Your answer is:",c)
    print("Do you want to continue")
a=int(input("Enter the first number"))
b=int(input("Enter the seconmd number"))
c=a+b
show()
c=a*b
show()
print("Function calledc two times")

big=max("Hello world")
print(big)
tiny=min("Hello world")
print(tiny)
#passing parameter
def check(lang):
    if lang == 'a':
        print("Hi")
    elif lang == 'b':
        print("Hello")
    else:
        print("Check input")
print("All done")

check('a')
#return something
def reuse():
    return ("Hello")
print(reuse(),"Onkar")
print(reuse(),"xyz")
'''
#passing multiple parameter
def mul(a,b):
    result=a+b
    return result
print("time to call function")
x=mul(2,5)
print(x)
