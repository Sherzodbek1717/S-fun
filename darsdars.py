class  User:
    def __init__(self, name, lastname, age, ):
        self.name = name
        self.lastname = lastname
        self.age = age


    def __str__(self):
        return f"User: {self.name} {self.lastname}"

    def get_user_info(self):
        print(f"user: {self.name} {self.lastname}")



user1 = User('Abror', 'Abrorov', 45)
print(user1.age)
user1.get_user_info()


class Employee(User):

        def __init__(self, name, lastname, age, salary, experience ):
            super().__init__(name, lastname, age)
            self.salary = salary
            self.experience = experience

        def get_user_info(self):
            print(f"user: {self.name} {self.lastname} lavozimi: {self.experience}")

        def get_employee_info(self):
            print(f"{self.name}, oylig: {self.salary}, lavozimi: {self.experience}")

# user1 = User("Toxir", "Toxirov", 45)
# employee1 = Employee("Toxir", "Toxirov", 45, 1000, "Junior")
#
# user1.get_user_info()
# employee1.get_user_info()
# employee1.get_employee_info()


class  User:
    def __init__(self, name, lastname, age, ):
        self.name = name
        self.lastname = lastname
        self.age = age


    def __str__(self):
        return f"User: {self.name} {self.lastname}"

    def get_user_info(self):
        print(f"user: {self.name} {self.lastname}")



user1 = User('Abror', 'Abrorov', 45)
print(user1.age)
user1.get_user_info()


class Employee:

        def __init__(self, salary, experience ):

            self.salary = salary
            self.experience = experience

        def get_user_info(self):
            print(f"user: {self.name} {self.lastname} lavozimi: {self.experience}")

        def get_employee_info(self):
            print(f"{self.name}, oylig: {self.salary}, lavozimi: {self.experience}")


class Owner(User, Employee):
    def __init__(self, name, lastname, age, salary, experience, rules):
        User.__init__(self, name, lastname, age)
        Employee.__init__(self, salary, experience)
        self.rules = rules

    def get_owner_info(self):
        print(f"Owner: {self.name} rules: {self.rules}")

owner1 = Owner("Toxir", "Toxirov", 45, 5000, "Team Led", "strict")
owner1.get_owner_info()
owner1.get_user_info()
owner1.get_employee_info()