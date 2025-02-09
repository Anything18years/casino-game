class Student:
    def __init__(self, first_name: str , last_name: str, student_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number

    def __eq__(self, other):
        if isinstance(other, Student):
            return other.student_number == self.student_number
        return False
    def __repr__(self):
        return f"{self.last_name}, {self.first_name}\t{self.student_number}"
    
class Course:
    def __init__(self, course_name: str):
        self.course_name = course_name
        self._students = []
    def size(self):
        return len(self._students)
    def add(self, student: Student):
        self._students.append(student)

    def size(self):
        return len(self._students)
    def add(self, student: Student):

        self._students.append(student)
    def _find(self, student: Student):
        for i,x in enumerate(self._students):
            if x == student:
                return i 
            return -1
    def contains(self, student: Student):
        return -1 != self._find(student)
    def remove(self, student: Student):
        if not self.contains(student):
            raise ValueError("No such student to remove")
        else:
            self._students.pop(self._find(student))
    def __repr__(self) :
        s = ""
        for student in self._students:
            s += f"{student} \n"
        return s    
my_course = Course("CS101")
my_course.add(Student("Bob", "Smith", 123456789))
my_course.add(Student("Jane", "Doe", 987654321))
my_course.add(Student("Niles", "MacDonald", 192837465))
my_course.add(Student("Jane", "Doe", 987654321))

print(my_course)