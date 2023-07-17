class User:
    def __init__ (self, first_name, last_name, first_and_last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.first_and_last_name = first_and_last_name

    def print_first_name(self):
        print("Ваше имя:", self.first_name)

    def print_last_name(self):
        print("Ваша фамилия:", self.last_name)

    def print_first_and_last_name(self):
        print("Ваше имя и фамилия:", self.first_and_last_name)