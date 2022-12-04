def input_initial_data():
    numberStudent = int(input('Hay nhap so sinh vien:'))
    numberSubject = int(input('Hay nhap so hoc phan'))
    
#inputgradedata
def input_grade_data(numberStudent,numberSubject):
    studentsGrades=[]
    for student in range(numberStudent):
        print("Hãy nhập vào điểm cho sinh viên thứ :", student+1)
        tempGrades = []
        for grade in range(numberSubject)
            tempGrade = int(input(f'Hãy nhập điểm thứ {grade+1}:'))
            tempGrades.append(tempGrade)
    studentsGrades.append(tempGrades)
averageStudentGrade = []
for student in range(numberStudent):
    tempSumGrade = 0
    for grade in range(numberSubject) :
        tempSumGrades += studentsGrades[student][grade]
    averageStudentGrade.append(tempSumGrade/numberSubject)
    
for student in range(numberStudent):
    print(f"Điểm của sinh viên thứ {student+1}:{studentsGrades[student]}, Điểm TB :{averageStudentGrade[student]}")        