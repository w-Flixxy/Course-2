from functools import reduce
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return f'{self.name}: {self.score}'


students=[Student("Joe", 0.97), Student("Jim", 0.62), Student("Jane", 0.12), Student("Jamal", 0.53), Student("Kat", 0.32), Student("Bob",1)]

score_total = 0
for student in students:
    score_total += student.score

reducetotal=(reduce(lambda total, student:student.score+total ,students, 0))

print(round(score_total/len(students), 2))

print(round(reducetotal/len(students), 2))