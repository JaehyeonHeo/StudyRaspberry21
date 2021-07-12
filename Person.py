class Person(object):
    total = 0

    def __init__(self, name, age): # 기본생성자=(self)만 있음
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age

    
