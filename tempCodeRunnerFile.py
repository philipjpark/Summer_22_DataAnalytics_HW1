def collatz(num):
    collatzSequence = [num]
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
            collatzSequence.append(num)
        elif num % 2 == 1:
            num = (num * 3) + 1
            collatzSequence.append(num)
          
        return collatzSequence
         
    largest = 0
    largestNum = 0
         
    for i in range(1, 1000000):
        if i % 2 != 0:
            if len(collatz(i)) > largest:
                largest = len(collatz(i))
                largestNum = i
              
        print(largestNum, largest)
          