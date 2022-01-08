from enroll import Enroll
from professor import Professor

class Course():
    def __init__(self, name, code, max_, min_, professor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.professores = []
        self.enrollments = []

        if isinstance (professor,Professor):
            self.professores.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry,Professor):
                    raise TypeError('Invalid address...')
            self.professores = professor
        else:
            raise TypeError('Invalid address...')

    def add_professor(self,professor):
        if not isinstance(professor,Professor):
            raise TypeError("Invalid professor...")

        self.professores.append(professor)


    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise TypeError("Invalid enrollment")

        if len(self.enrollments) == self.max:
            raise TypeError("Cannot enroll, course is full...")

        self.enrollments.append(enroll)

    
    def is_Cancelled(self):
        return len(self.enrollments) < self.min

