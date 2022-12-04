print("Nhap vao so hoc sinh: "); numberStudents = int(input())
group4 = []
for index in range(0, numberStudents):
    print("Nhap vao so hs dat ", index, " : ")
    gradesOfStudent = []
    for grades in  range (0, 3):
         gradesOfStudent.append(float(input()))
    group4.append(gradesOfStudent)
    
numberStudentsRetakeExams = 0
for gradesOfStudent in group4:
    for grades in gradesOfStudent:
        if grades <= 4:
            numberStudentsRetakeExams += 1
            break
print("So hs can phai lam lai kiem tra: ", numberStudentsRetakeExams)