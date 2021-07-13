class Person(object):
    total = 0

    def __init__(self, name, age): # 기본생성자=(self)만 있음
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age

# class상속
class Man(Person):
    gender = 'male'

class Korean(Person):
    nationality = 'Korea'

class KoreanMan(Man, Korean):
    pass # 일단 나중에 개발하기 위해서 그냥 넘어가도록 하는 기능


