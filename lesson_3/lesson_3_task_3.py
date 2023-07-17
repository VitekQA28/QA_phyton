from address import Address
from mailing import Mailing

mailing = Mailing(
    to_address = Address("424000", "Йошкар-Ола", "Строителей", "37", "60"), 
    from_address = Address("420087", "Казань", "Гвардейская", "67", "2"), 
    cost = 1000, 
    track = '1sdf123') 
    #Распечатайте в консоль отправление в формате: 
    # Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, 
    # <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей..
print(f"Отправление {mailing.track} из {mailing.from_address.index}, \
{mailing.from_address.city}, {mailing.from_address.street}, \
{mailing.from_address.house} - {mailing.from_address.apartment} в \
{mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, \
{mailing.to_address.house} - {mailing.to_address.apartment}. \
Стоимость {mailing.cost} рублей.")