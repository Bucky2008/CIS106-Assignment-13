# Assignment 2

class Student:

    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):

        if self.district_code == "I":
            tuition = self.enrolled_credits * 250
        else:
            tuition = self.enrolled_credits * 500

        return tuition


# Instantiate object
student1 = Student("Karol", "Wszelaki", "I", 12)

# Display student information
print("Student Name:", student1.first_name, student1.last_name)
print("District Code:", student1.district_code)
print("Enrolled Credits:", student1.enrolled_credits)

# Compute and display tuition
tuition_owed = student1.compute_tuition()

print("Tuition Owed: $", tuition_owed)