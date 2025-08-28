from user import User
from card import Card

Alex = User("Alex")

Alex.sayName()
Alex.setAge(33)
Alex.sayAge()

card = Card("4353 1234 5678 8765", "11/28", "Alex F")

Alex.addCard(card)
Alex.getCard().pay(1000)