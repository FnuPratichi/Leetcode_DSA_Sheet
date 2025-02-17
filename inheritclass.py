# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female
# class.

class Person:
    def getGender(self):
        return 'Unknown'
class Male:
    def getGender(self):
        return 'Male'
class Female:
    def getGender(self):
        return 'Female'


person_obj = Person()
male_obj = Male()
female_obj = Female()
print(person_obj.getGender())
print(male_obj.getGender())
print(female_obj.getGender())

