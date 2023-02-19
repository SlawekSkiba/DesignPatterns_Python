class Grade:
    def __init__(self):
        self._value = 0
        
    def __get__(self, instance, owner):
        return self._value
    
    def __set__(self, instance, value):
        if not(0<=value<=100):
            raise ValueError('Ocena musi być wartością z zakresu 0-100')
        self._value = value
        
        
class ExamD:
    def __init__(self):
        self._math_grade = Grade()
        self._writing_grade = Grade()

    @property
    def math_grade(self):
        return self._math_grade;
    
    @math_grade.setter
    def math_grade(self, value):
        self._math_grade = value;

    @property
    def writing_grade(self):
        return self._writing_grade;
    
    @writing_grade.setter
    def writing_grade(self, value):
        self._writing_grade = value;