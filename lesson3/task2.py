from smartphone import Smartphone
catalog = []
phone1 = Smartphone("Apple", "Iphone 15", "+79124515687")
phone2 = Smartphone("Apple", "Iphone 14", "+79125478523")
phone3 = Smartphone("Samsung", "M51", "+79134245785")
phone4 = Smartphone("Xiaomi", "mi 10 pro", "+79145852525")
phone5 = Smartphone("Huawei", "15", "+7932458797")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.phone_number}")