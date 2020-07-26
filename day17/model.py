class Teacher(object):
    def __init__(self, name, password):
        import tools
        self.name = name
        self.password = tools.encrypt_password(password)


class Student(object):
    def __init__(self, id, name, age, gender, tel):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.tel = tel
