n = 100
fact = 1

if n < 0:
  print("Negative numbers do not apply to factorial.")
elif n == 0:
  print("The factorial of 0 is 1.")
else:
  for i in range(1,n + 1):
    fact = fact*i

arr = [int(x) for x in str(fact)]

sum = 0
for z in arr:
  sum += int(z)
print (sum)

