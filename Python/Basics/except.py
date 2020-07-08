
astr="Hello Bob"
try:
    istr=int(astr)
except:
    istr="Error"
print("first",istr)
astr=123
istr=int(astr)
print("Second",istr)

astr="bob"
try:
    print("Hello")
    istr=int(astr)
    print("There")
except:
    istr="Error"
print("All donhe",istr)

x=input("Enter a number")
print(x)
try:
    x1=int(x)
    print("Processing")
except:
    x1="Error"
print(x1)

if x1 == 5:
    print("String matched")

else:
    print("String does not matched")
print("All donme")
#ass 3.2
hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate:")
r=float(rate)
if hrs < 40:
    print(40*r + (h-40)*r*1.5)
else:
    print (h*r)

#ass 3.2 grades
try:
    if score < 1.0:
        print("Out of range")
except:
    score=-1

score = float(input("Enter Score: "))
if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >=  0.6:
    print("D")
elif score < 0.5:
    print("F")
