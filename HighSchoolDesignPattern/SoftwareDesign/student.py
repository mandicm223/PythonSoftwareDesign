from person import Person
from enroll import Enroll

class Student(Person):
    def __init__(self, first, last, dob, phone, address, internacional=False):
        super().__init__(self, first, last, dob, phone, address)
        self.internacional = internacional
        self.enrolled = []

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise TypeError("Invalid Enroll...")
        
        self.enrolled.append(enroll)

    def is_on_probation(self):
        return False

    def is_part_time(self):
        return len(self.enrolled) <= 3