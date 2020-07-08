smallest = None
print("Before",smallest)
num = int(input("Enter a number"))
for sorting in range(100):
    if smallest is None:
        smallest = sorting
    elif sorting < smallest:
        smallest = sorting
    print("smallest",sorting)
print("After",smallest)
