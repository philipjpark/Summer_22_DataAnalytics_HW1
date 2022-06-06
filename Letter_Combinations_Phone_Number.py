digits = "23"

telephone = {
  "2": "abc",
  "3": "def",
  "4": "ghi",
  "5": "jkl",
  "6": "mno",
  "7": "pqrs",
  "8": "tuv",
  "9": "wxyz",
  }

arr = [""]

if len(digits) == 0:
    print([])

elif len(digits) >= 4:
     print("The input is too long!") 

else: 
  for digit in digits:
    temp = []
    for x in arr:
      for y in telephone[digit]:
        temp.append(x+y)
        arr = temp
  print(arr)



