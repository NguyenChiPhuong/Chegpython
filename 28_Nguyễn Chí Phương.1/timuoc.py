n = int(input("Enter n: "))
index = n 
list = []
while index >= 1:
    if n % index == 0:
        list.append(index)
    index -= 1
print (list)