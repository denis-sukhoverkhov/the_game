import random
from uuid import uuid4


class Player:
    def __init__(self, name, medals, money):
        id = uuid4()
        name = name
        power = random.randint(1, 1000)
        medals = medals
        money = money


# class Tournament:
#