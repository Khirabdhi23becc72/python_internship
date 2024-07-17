class Person:
    def __init__(self, name, age, gender):
        # Initialize attributes
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        # Print a statement introducing the person
        print(f"Hello, my name is {self.name}. I am {self.age} years old and {self.gender}.")

# Example usage:
if __name__ == "__main__":
    person1 = Person("Neha", 30, "female")
    person1.introduce()

    person2 = Person("Rahul", 25, "male")
    person2.introduce()
