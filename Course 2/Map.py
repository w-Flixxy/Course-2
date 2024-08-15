class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]

studentresults = []
for student in students:
#    if student.score >= 0.7:
#        studentresults.append(f"{student.name} passed")
#    else:
#        studentresults.append(f"{student.name} Failed")


    studentresults.append(f"{student.name} passed") if student.score >= 0.7 else studentresults.append(f"{student.name} Failed")

map_results = list(map(lambda student: f"{student.name} passed" if student.score >= 0.7 else f"{student.name} Failed", students))
numbers = [1,2,3,4,5]
times_2 = list(map(lambda number: number * 2, numbers))
print(times_2)

print(studentresults)
print(map_results)
    
