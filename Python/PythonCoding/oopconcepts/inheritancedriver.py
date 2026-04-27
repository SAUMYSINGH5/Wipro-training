
from oopconcepts.studentgrade import GradeStudent
from oopconcepts.teacher import Teacher

cc = int(input("College Code: "))
cn = input("College Name: ")
ci = input("City: ")
rno = int(input("Roll No: "))
sn = input("Student Name: ")
m1 = int(input("M1: "))
m2 = int(input("M2: "))
m3 = int(input("M3: "))
eid = int(input("EID: "))
tn = input("Teacher Name: ")
de = input('Department Name: ')
bp = float(input('Bp: '))


project = GradeStudent(cc, cn, ci, rno, sn, m1, m2, m3)

project.welcome_message()
project.display_college_details()

print(
    f'Roll No: {project.rollno}\t'
    f'Name: {project.stuname}\t'
    f'Total: {project.calculate_total()}\t'
    f'Average: {project.calculate_average_total():.2f}'
)

print(f"Result: {project.calculate_result()} \t Grade: {project.calculate_grade()}")

teacher = Teacher(ccode=cc, cname=cn, ccity=ci, eid=eid, tn = tn, de=de, bp=bp)
print(f'Eid: {teacher.empid} \t Name: {teacher.tname} \t Dept: {teacher.dept}')
print(f'Result: {teacher.calculate_salary()}')
























'''
#project = Student(cc, cn, ci, rno, sn, m1, m2, m3)
project = Student.Grade(cc, cn, ci, rno, sn, m1, m2, m3)

project.welcome_message()
project.display_college_details()

print(
    f"Roll No: {project.rollno}\t"
    f"Name: {project.stuname}\t"
    f"Total: {project.calculate_total()}\t"
    f"Average: {project.calculate_average_total():.2f}"
)

project.calculate_grade()
print(f'Result: {project.result} \t Grade: {project.grade}')
'''