import time

start = time.time()
print("hello")

x = int(input("Number:"))
sum_of_digits = 0
for digit in str(x):

  sum_of_digits += int(digit)

print(sum_of_digits)

end = time.time()
print(end - start)
