n = 100

fact = 1

if n < 0:
  print("Negative numbers do not apply to factorial.")
elif n == 0:
  print("The factorial of 0 is 1.")
else:
  for i in range(1,n + 1):
    fact = fact*i
  #print("The factorial of",num,"is",factorial)
#print(str(factorial))

arr = [int(x) for x in str(fact)]
#print(str(arr))
#print(arr)

sum = 0
for z in arr:
  sum += int(z)
print (sum)

