# Assignment 1

class Employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def full_name(self):
        return self.first + " " + self.last

    def compute_bonus(self, bonus_rate):
        bonus = self.salary * bonus_rate
        return bonus


# Instantiate object
emp1 = Employee("John", "Smith", 50000)

# Display employee info
print("Employee Name:", emp1.full_name())
print("Salary:", emp1.salary)

# Compute and display bonus
bonus_rate = 0.10
bonus_amount = emp1.compute_bonus(bonus_rate)

print("Bonus Rate:", bonus_rate)
print("Bonus Amount:", bonus_amount)