x = input("Input Number:")
x = int(x)

def counting(x):
    i = 1
    while(i<=x):
        print(i)
        i += 1
    return
counting(x)
counting(5)
# print(i), i is a local variable, not defined in main code, only defined in function
