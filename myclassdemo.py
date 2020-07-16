# name mangling

class Department:
    pass


class Employee:
    id = 10
    version = 20

    # private method
    def __demo(self):
        print("demo")

    @staticmethod
    def stat_demo():
        print("stat_demo")

    def __init__(self, username, password):
        print("constructor")
        self.username = username
        self.password = password
        d = Department()
        self.department = d;

    def __del__(self):
        print("destructor")

    def collect(self):
        print("Emp Collect")
        self.__demo()

    def __str__(self):
        print("__str__")
        return "Employee"

emp = Employee("X", "x");
emp.collect()
