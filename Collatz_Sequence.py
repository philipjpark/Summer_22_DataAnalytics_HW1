def collatz(num):
    increment = 1
    while num > 1:
        if num % 2 == 0:
            num = num/2
        else: 
           num = (3 * num) + 1
        increment += 1
    return increment

def check():
  store = 0
  i = 1
  while i < 1000000:
    s = collatz(i)
    if s > store:
        store = s
        longestChain = i
    i += 1
  return longestChain

print("Please wait as the program processes...")
print(check())