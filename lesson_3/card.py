

class Card:
    number = "0000 0000 0000 0000"
    date = "00/00"
    fio = "unknown"
    def __init__(self, number: str, date: str, fio: str) -> None:
        self.number = number
        self.date = date
        self.fio = fio

    def pay(self, amount: int):
        print("с карты", self.number, "списали", amount)