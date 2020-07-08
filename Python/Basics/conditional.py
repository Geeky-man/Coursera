'''
#conditional if
x=int(input("Enter the number"))
if x  < 10:
    print("X is smaller")

if x > 10:
    print("X is bigger")

print("finish")

#for loop
y=5
for i in range(5):
    print(i)
    if i > 2 : #nested if
        print("Y is bigger")
    print("End of for loop",i)
print("All done")

#nested decisions
f=12
if f < 15:
    print("F is smaller")
    if f > 10:
        print("F is bigger")
print("All done")

#if-else(two way decisions)
h=10
if h < 50:
    print("H is smaller")
else:
    print("H is greater")
print("All done")
'''
#multi way decisions
d=int(input("Enter a number"))
if d < 20:
    print('D is smaller')
elif d < 15:
    print('D is medium')
else:
    print ('D is bigger')
print ("All done")
