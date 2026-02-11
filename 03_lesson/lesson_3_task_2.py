from smartphone import Smartphone


catalog = [
    Smartphone("Sumsung", "S52", "+79036541235"),
    Smartphone("Iphone", "17", "+79237412563"),
    Smartphone("Motorolla", "M52", "+79087895142"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79131111111"),
    Smartphone("Meizu", "A12", "+79281284565")
]

for Smartphone_1 in catalog:
    print(f"{Smartphone_1.brand} "
          f"- {Smartphone_1.model} . "
          f"{Smartphone_1.subscriber_number}")
