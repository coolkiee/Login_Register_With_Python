class User:
    def __init__(self, first_name, last_name, email, password, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.age = age
#templates
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email} {self.password})"

    def __int__(self):
        return self.age