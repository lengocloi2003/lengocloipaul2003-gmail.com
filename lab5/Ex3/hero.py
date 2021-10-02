from gameunit import *


class Hero(Attacker):
    def __init__(self, name):
        self._health = 100
        self._attack = 50
        self.name = name
        self._experience = 0

    def attack(self, target):
        """
        Атакует соперника, уменьшая его health
        :param target: сопеник
        :return: измененные target._health, self.experience
        """
        target._health -= self._attack
        self._experience += target._attack