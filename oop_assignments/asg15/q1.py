class Person:
    def _init_(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and {self.gender}.")

# Example usage:
if __name__ == "_main_":
    person1 = Person("neha", 30, "female")
    person1.introduce()

    person2 = Person("rahul", 25, "male")
    person2.introduce()