from student import Student
from courseGroup import CourseGroup


student = Student("Антон", "Костенко", 39, "Инженер по тестированию")
classmate1 = Student("Елизавета", "Ковальчук", 27, "Инженер по тестированию")
classmate2 = Student("Людмила", "Чикова", 24, "Инженер по тестированию")
classmate3 = Student("Екатерина", "Акусок", 26, "Инженер по тестированию")


courseGroup = CourseGroup(student, [classmate1, classmate2, classmate3])


print(courseGroup)