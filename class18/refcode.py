class Student:
    def __init__(self, name):
        self.name="Shyam"
    def joined_institute(self):
        self.joined_institute=True
        print("Joined at the Prostack Academy")
    def attend_classes(self):
        self.attended_classes=True
        print((self.name),"attended the classes.")
    def practice_daily(self):
        self.practiced_daily=True
        print((self.name),"practiced daily.")
    def give_mock_interviews(self):
        self.given_mock_interviews=True
        print((self.name),"gave mock interviews.")
    def check_success(self):
        if self.attended_classes and self.practiced_daily and self.given_mock_interviews:
            print((self.name),"got placed and succeeded!")
        else:
            print((self.name),"did not attend the classes or practice and thus did not get the job. They didn't succeed.")
student = Student("Shyam")
student.joined_institute()
student.attend_classes()
student.practice_daily()
student.give_mock_interviews()
student.check_success()
