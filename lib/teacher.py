#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]):
        
        super().__init__(first_name, last_name)
        self.knowledge = knowledge


    pass
    def teach(self, years_of_experience):
        self.years = years_of_experience
        print(f"Hello, my name is {self.first_name} {self.last_name}. I have {self.years} in :")
        
        return self.knowledge[random.randint(0, len(self.knowledge))]
    
teacher1 = Teacher("Brendah", 'Kiragu')
print(teacher1.teach('2 years of experience'))

        