
#largest number
largest = -1
print("Before",largest)
for sorting in [15,25,1,78,56,9]:
    if sorting > largest:
        largest = sorting
    print("Largest",sorting)
print("After",largest)
#counting
start = 0
print("Before",start)
for thing in [15,25,1,78,56,9]:
    start = start + 1
    print(thing)
print("Count",start)

#summation in loop
new = 0
print("At starting",new)
for thing in [15,25,1,78,56,9]:
    new = new + thing
    print(thing)
print("Addition is",new)

#avg in loop
new = 0
count = 0
print("At starting",new)
for thing in [15,25,1,78,56,9]:
    count = count + 1
    new = new + thing
    print(thing)
print("Avg  is",new/count)

#filtering in loop
print("Before")
for thing in [15,25,1,78,56,9]:
    if thing > 20:
        print("Result",thing)
        
#smallest number
smallest = None
print("Before",smallest)
for sorting in [15,25,1,78,56,9]:
    if smallest is None:
        smallest = sorting
    elif sorting < smallest:
        smallest = sorting
    print("smallest",sorting)
print("After",smallest)
