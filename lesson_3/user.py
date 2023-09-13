from card import Card

class User:
    def __init__ (self, first_name, last_name, first_and_last_name, name: str) :
        self.first_name = first_name
        self.last_name = last_name
        self.first_and_last_name = first_and_last_name
        self.username = name

    age = 0

    def print_first_name(self):
        print("Ваше имя:", self.first_name)

    def print_last_name(self):
        print("Ваша фамилия:", self.last_name)

    def print_first_and_last_name(self):
        print("Ваше имя и фамилия:", self.first_and_last_name)

    def sayName(self) -> None:
        """Печатает имя пользователя"""
        print("Меня зовут", self.username)

    def seyAge(self) -> None:
        """Печатает возраст пользователя"""
        print(self.age)

    def setAge(self, newAge: int) -> None:
        """Устанавливает возраст пользоваетеля"""
        self.age = newAge

    def addCard(self, card: Card) -> None:
        """Добавляет пользователю карту"""
        self.card = card

    def getCard(self)-> Card:
        """Возвращает пользователю карту"""
        return self.card