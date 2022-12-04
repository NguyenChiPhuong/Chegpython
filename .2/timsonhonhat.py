arrayA = [1, 3, 5, 9, 11, 2, 6, 8, 10]
arrayB = [1, 3, 5, 9, 11]

minA = arrayA[0]
minB = arrayB[0]

for element in arrayA:
    if element < minA :
        minA = element
for element in arrayB:
    if element < minB :
        minB = element

print("So nho nhat day A la ", minA, " va nho nhat day B la ", minB)