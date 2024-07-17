from abc import ABC, abstractmethod

# Abstract class Employee
class Employee(ABC):
    def _init_(self):
        super()._init_()

    @abstractmethod
    def calculate_salary(self):
        pass

# Subclass Manager
class Manager(Employee):
    def _init_(self, base_salary, bonus):
        super()._init_()
        self.base_salary = base_salary
        self.bonus = bonus
    
    def calculate_salary(self):
        return self.base_salary + self.bonus

# Subclass Developer
class Developer(Employee):
    def _init_(self, base_salary, project_count, bonus_per_project):
        super()._init_()
        self.base_salary = base_salary
        self.project_count = project_count
        self.bonus_per_project = bonus_per_project
    
    def calculate_salary(self):
        return self.base_salary + self.project_count * self.bonus_per_project

# Subclass Intern
class Intern(Employee):
    def _init_(self, stipend):
        super()._init_()
        self.stipend = stipend
    
    def calculate_salary(self):
        return self.stipend

# Example usage:
if __name__ == "_main_":
    # Creating instances of each subclass
    manager = Manager(base_salary=60000, bonus=10000)
    developer = Developer(base_salary=50000, project_count=5, bonus_per_project=2000)
    intern = Intern(stipend=1500)

    # Calculating and printing their salaries
    print(f"Manager's salary: ${manager.calculate_salary()}")
    print(f"Developer's salary: ${developer.calculate_salary()}")
    print(f"Intern's salary: ${intern.calculate_salary()}")