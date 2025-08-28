from smartphone import Smartphone

catalog = [
    Smartphone("Huawei", "Mate 50 Pro", "+79641400764"),
    Smartphone("Huawei", "Pura 80 Pro", "+79621722002"),
    Smartphone("IPhone", "16 Pro Max", "+79109129253"),
    Smartphone("Honor", "Magic6 Pro", "+79109158508"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79066442048")
]

for smartphone in catalog:
    print(f"{smartphone.brand_telephone} - {smartphone.model_telephone}. \
{smartphone.number_telephone}")
