from address import Address
from mailing import Mailing

to_address = Address("123456", "Novosibirsk", "Lenina", "12", "4")
from_address = Address("654321", "Moscow", "Pushkina", "42", "2")
mailing = Mailing(to_address, from_address, 2000, "AB48754")

print(f"Departure {mailing.track} from {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street},"
      f" {mailing.from_address.house}, {mailing.from_address.apartment}"
      f" in {mailing.to_address.index}, {mailing.to_address.street}, {mailing.to_address.house}, {mailing.to_address.apartment}."
      f" Cost {mailing.cost} RUB.")