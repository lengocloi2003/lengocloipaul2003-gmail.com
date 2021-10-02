class Attacker:
    """Общий класс для всех объектов игры"""
    _health = None
    _attack = None

    def attack(self, target):
        """
        Нападение на соперника
        :param target: соперник
        :return: Value
        """
        target._health -= self._attack

    def is_alive(self):
        """
        Проверка health
        :return: Value
        """

        return self._health > 0