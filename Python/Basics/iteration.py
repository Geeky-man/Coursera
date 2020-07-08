'''
#while loop
n = 5
while n > 2:
    print(n)
    n=n-1
print(n)
#end of while loop
print("New loop")
#for loop
i = 5
for i in range(10):
    print(i)
    i = i - 1
print(i)
s
#break and continue statement
while True:
    line = input(' > ')
    if line[0]=='#':
        continue
    if line == 'done':
        break
    print(line)
print("All done ")

#break statement
while True:
    line = input(' > ')
    if line == 'done':
        break
        print(line)
    print("All done ")

#continue statement
while True:
    line = input(' > ')
    if line     == 'onkar':
        continue
    print(line)
print("All done ")
'''
#definite loop
for i in range(5):
    print(i)
print("All done")
