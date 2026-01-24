from address import Address
from mailing import Mailing


mailing = Mailing(
        Address("661225", "Красноярск", "Мира", "70", "90"),
        Address("345000", "Смоленск", "Гагарина", "10", "3"),
        150,
        113558654)

print(mailing)
