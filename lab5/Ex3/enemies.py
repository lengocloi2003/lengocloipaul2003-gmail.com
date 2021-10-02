from gameunit import *
from random import randint, choice
import math
class Enemy(Attacker):
    """Предковый класс всех enemy"""
    pass

def generate_random_enemy():
    RandomEnemyType = choice(enemies)
    enemy = RandomEnemyType
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list





class Dragon(Enemy):
    """Предковый класс всех dragon"""
    def __init__(self):
        self.__answer = 0

    def set_answer(self, answer):
        """Генерирует правильный ответ"""
        self.__answer = answer

    def check_answer(self, answer):
        """
        Проверяет ответ игрока
        :param answer: ответ игрока
        :return: Value
        """
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'
        __quest = 0

    def question(self):
        x = randint(1,1)
        __quest = "Угадай число от 1 до 5"
        self.set_answer(str(x))
        return __quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'
        __quest = 0
    def prime_number(self,x):
        if x < 2:
            return 'No'
        elif x == 2:
            return 'Yes'
        for i in range(2,int(math.sqrt(x))+1):
            if x % i ==0:
                return 'No'
        return 'Yes'

    def question(self):
        x = randint(1, 100)
        __quest = ' {} является простым числом ? '.format(x)
        self.set_answer(self.prime_number(x))
        return __quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'
        __quest = 0

    def factorize_number(self,x):
        a=[]
        divisor = 2
        while x > 1:
            if x % divisor == 0:
                a.append(divisor)
                x //= divisor
            else:
                divisor += 1
        return ','.join(map(str,a))


    def question(self):
        x = randint(1, 100)
        __quest = 'разложить {} на множители и перечислить их через запятую'.format(x)
        self.set_answer(self.factorize_number(x))
        return __quest


green_dragon = GreenDragon()
red_dragon = RedDragon()
black_dragon = BlackDragon()
enemies = [green_dragon, red_dragon, black_dragon]