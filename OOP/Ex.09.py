class Student:
    def __init__(self, name, grade, freq):
        self.nome = name
        self.grade = grade
        self.freq = freq
    def is_approved (self):
        if self.grade >= 6 and self.freq >= 0.75:
            return True
        else:
            return False


    
s1 = Student("tom", 9.3, 0.95)
print(s1)

print (s1.grade)
print(s1.is_approved())
