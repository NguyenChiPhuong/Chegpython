arrayA = [1, 3, 5, 9, 11, 2, 6, 8, 10]
arrayB = [1, 3, 5, 9, 11]

sumA = 0
sumB = 0

for element in arrayA:
    sumA += element
for element in arrayB:
    sumB += element
    
averageA = sumA / len(arrayA)
averageB = sumB / len(arrayB)

print("Average A: ", averageA)
print("Average B: ", averageB)