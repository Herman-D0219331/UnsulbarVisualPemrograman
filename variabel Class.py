class Student:
    # Class variable
    school_name = 'ABC School '
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# create first object
s1 = Student('Raja', 10)
print(s1.name, s1.roll_no, Student.school_name)
# access class variable
# create second object
s2 = Student('Ratu', 20)
# access class variable
print(s2.name, s2.roll_no, Student.school_name)