numbersOfStudents = int(input("Nhập vào số Sinh viên: "))

numbersOfScores = int(input("Nhập vào số môn học: "))
averageOfScores = []
for i in range(0, numbersOfStudents):
    sumNumber = 0
    print("Nhập điểm của sinh vien thứ ", i + 1, " :")
    for i in range(0, numbersOfScores):
        score = float(input())
        sumNumber += score  
    averageOfScore10 = sumNumber / numbersOfScores
    averageOfScores.append(averageOfScore10)
    
for i in range(numbersOfStudents): 
    print("Kết quả của sinh viên thứ ", i + 1, " :")
    print("ĐTB hệ số 10:    ", averageOfScores[i]) 