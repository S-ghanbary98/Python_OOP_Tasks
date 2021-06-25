
class User:
    def __init__(self, age, drivers_license = True):
        self.age = age
        self.drivers_license = drivers_license


    def vote_check(self):
        if self.age >= 16:
            return "Yes you are able to vote!"
        return "No you are too young you have " + str(18 - self.age) + " years left"

    def drive_check(self):
        if self.drivers_license == True and self.age >= 18:
            return "You are able to drive!"
        elif self.drivers_license == True and self.age < 18:
            return "You are not yet old enough to drive"
        elif self.drivers_license == False and self.age >= 18:
            return " You need a license to drive"
        else:
            return "You are not old enough nor do you have a license. YOU CANNOT DRIVE"

    def drink_check(self):
        if self.age >= 18:
            return "You can drink any beverage you want !!"
        else:
            return "You are not legally allowed to drink but your aunties have your back!!"

    def school_check(self):
        if self.age < 18:
            return "Your TOO young go back to school"
        else:
            return "Time for a real job!!!"


while True:
    age = input("How old are you?")
    if age == "exit":
        break

    license = input("Do you have a drivers licence? (yes/no)")
    if license == "exit":
        break

    if int(age.isdigit()) and int(age) > 0 and license.lower() == 'yes' or license.lower() == 'no':
        user = User(int(age), license)
        print(user.drive_check())
        print(user.school_check())
        print(user.vote_check())
        print(user.drink_check())
        break
    print("Please enter valid age/license information")







