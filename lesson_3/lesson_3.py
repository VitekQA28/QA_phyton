from user import User
from card import Card

alex = User("Alex")

alex.sayName()
alex.setAge()
alex.seyAge()

card = Card("5456 1231 5646 6413", "11/29", "Alex F")

alex.addCard(card)
alex.getCard().pay(100)