from smartphone import Smartphone

catalog = []
catalog.append(Smartphone("Samsung", "Galaxy A50", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 12", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 9", "+79345678901"))
catalog.append(Smartphone("Huawei", "P40 Pro", "+79456789012"))
catalog.append(Smartphone("Google", "Pixel 5", "+79567890123"))


for phone in catalog:
    print(f"{phone.name_phone} - {phone.model_phone} - {phone.number_phone}")