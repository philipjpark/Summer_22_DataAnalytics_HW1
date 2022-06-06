def mostWater(h, leng):
    maxContain = 0
    for x in range(leng):
      for y in range(x + 1, leng):
        maxContain = max(maxContain, (min(h[x], h[y]) * abs(x-y)))
    return maxContain
 
heights = [1,8,6,2,5,4,8,3,7]
length = len(heights)
print(mostWater(heights, length))
