from course import Course
from student import Student

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")
coding = Course("Python I")
engineering = Course("Mechanical Engineering")

test_student = Student("Jill", "Sample")
test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)

test_student2 = Student("Bill", "Sample")
test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)

silly_cat = Student("Sudo", "Cat")
silly_cat.add_course(math)
silly_cat.add_course(coding)
silly_cat.add_course(science)
silly_cat.add_course(engineering)

roster = []
roster.append(test_student)
roster.append(test_student2)
roster.append(silly_cat)


for student in roster:
    print(student)