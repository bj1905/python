import time

start = time.time()
print("hello")

x = int(input("Number:"))
x0 = x // 1000
x1 = (x-x0*1000) // 100
x2 = (x-x1*100-x0*1000) // 10
x3 = (x-x2*10-x1*100-x0*1000) // 1
print(x0+x1+x2+x3)

end = time.time()
print(end - start)
