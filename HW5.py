class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    email = property(get_email, set_email) # чтобы не прописывать геттеры и сеттеры

p = Person('Ivan', 35, 'ivan@mail.com')
print(p.get_email())
print(p.name)
print(p.email, p.__dict__)
p.set_email('ivanov@mail.com')
print(p.get_email()) # bez property
print(p.email) # c property
print(p.email, p.__dict__)