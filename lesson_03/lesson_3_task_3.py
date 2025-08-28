from Address import Address
from Mailing import Mailing

to_address = Address("24800", "Калуга", "Ленина", "62", "22")
from_address = Address("101000", "Москва", "Пушкина", "29", "13")
cost = 500
track = "123"

mailing = Mailing(to_address, from_address, cost, track)

print(mailing)
