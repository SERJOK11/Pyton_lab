import doctest

from typing import Union


class Hero:
    def __init__(
        self,
        health_point: Union[int, float],
        experience_point: int,
        stamina: Union[int, float],
    ):
        """
        Создание и подготовка к работе объекта "Герой"

        :param health_point: Очки здоровья
        :param experience_point: Очки опыта
        :param stamina: Значение выносливости

        :raise TypeError: Если типы аргументов не соответствуют аннотации, то вызываем ошибку
        :raise ValueError: Если health_point < 0, experience_point < 0 или stamina < 0, то вызываем ошибку

        Пример:
        >>> hero = Hero(100, 0, 100)
        """
        if not isinstance(health_point, (int, float)):
            raise TypeError(
                "Количество здоровья должно быть целым или вещественным числом"
            )
        if health_point < 0:
            raise ValueError("Количество здоровья не может быть отрицательным")
        self.health_point = health_point

        if not isinstance(experience_point, int):
            raise TypeError("Количество опыта должно быть целым числом")
        if experience_point < 0:
            raise ValueError("Количество опыта не может быть отрицательным")
        self.experience_point = experience_point

        if not isinstance(stamina, (int, float)):
            raise TypeError("Выносливость должна быть целым или вещественным числом")
        if stamina < 0:
            raise ValueError("Выносливость не может быть отрицательной")
        self.stamina = stamina

    def run(self, difficulty_factor: float) -> None:
        """
        Метод, отвечающий за возможность бега.
        При беге учитывается выносливость и поверхность, по которой бежит герой

        :param difficulty_factor: Коэффициэнт сложности местноти
        :return: None

        :raise TypeError: Если тип аргумента не вещественное число, то вызываем ошибку
        :raise ValueError: Если коэффициент сложности местности неположительный, то вызываем ошибку

        Пример:
        >>> hero = Hero(100, 0, 100)
        >>> hero.run(1.6)
        """
        if not isinstance(difficulty_factor, float):
            raise TypeError(
                "Коэффицент сложности местности должен быть вещественным числом"
            )
        if difficulty_factor <= 0:
            raise ValueError(
                "Коэффицент сложности местности должен быть неотрицательным"
            )
        ...

    def attack(self, damage: float) -> float:
        """
        Метод, расчитывающий значение урона. Учитываются выносливость и характеристики оружия

        :param damage: Урон из характеристик оружия
        :return: Урон с учетом характеристик героя

        :raise TypeError: Если тип аргумента не вещественное число, то вызываем ошибку
        :raise ValueError: Если значение урона отрицательное, то вызываем ошибку

        Пример:
        >>> hero = Hero(100, 0, 100)
        >>> sword = Weapon(1, 20.0, 1.5)
        >>> final_damage = hero.attack(sword.damage)
        """
        if not isinstance(damage, float):
            raise TypeError("Количество урона должно быть вещественным числом")
        if damage < 0.0:
            raise ValueError("Количество урона не может быть отрицательным")
        ...

    def poisoning(self, poison_power: float) -> None:
        """
        Метод, вызывающий отравление у героя.

        :param poison_power: Коэффициент отравления
        :return: None

        :raise TypeError: Если тип аргумента не вещественное число, то вызываем ошибку
        :raise ValueError: Если коэффициент силы яда неположительный, то вызываем ошибку

        Пример:
        >>> hero = Hero(100, 0, 100)
        >>> hero.poisoning(2.3)
        """
        if not isinstance(poison_power, float):
            raise TypeError("Коэффициент силы яда должен быть вещественным числом")
        if poison_power <= 0:
            raise ValueError("Коэффициент силы яда должен быть неотрицательным")
        ...


class Weapon:
    def __init__(self, rarity: int, damage: float, weight: float):
        """
        Создание и подготовка к работе объекта "Оружие"

        :param rarity: Редкость в промежутке [0, 5]
        :param damage: Урон оружия
        :param weight: Вес оружия

        :raise TypeError: Если типы аргументов не соответствуют аннотации, то вызываем ошибку
        :raise ValueError: Если rarity < 0 or rarity > 5, damage < 0.0 или weight <= 0.0, то вызываем ошибку

        Пример:
        >>> sword = Weapon(1, 20.0, 1.5)
        """
        if not isinstance(rarity, int):
            raise TypeError("Редкость оружия должна описываться целым числом")
        if not (0 <= rarity <= 5):
            raise ValueError(
                "Редкость оружия должна описываться числом в промежутке [0, 5]"
            )
        self.rarity = rarity

        if not isinstance(damage, float):
            raise TypeError("Количество урона должно быть вещественным числом")
        if damage < 0.0:
            raise ValueError("Количество урона не может быть отрицательным")
        self.damage = damage

        if not isinstance(weight, float):
            raise TypeError("Вес оружия должен быть вещественным числом")
        if weight <= 0.0:
            raise ValueError("Вес оружия должен быть неотрицательным")
        self.weight = weight

    def show(self) -> None:
        """
        Показывает оружие в руках.

        :return: None

        Пример:
        >>> sword = Weapon(1, 20.0, 1.5)
        >>> sword.show()
        """
        ...

    def hide(self) -> None:
        """
        Убирает оружие из рук.

        :return: None

        Пример:
        >>> sword = Weapon(1, 20.0, 1.5)
        >>> sword.hide()
        """
        ...


class Food:
    def __init__(self, weight: float, freshness: bool, time_to_spoil: float):
        """
        Создание и подготовка к работе объекта "Еда"

        :param weight: Вес еды
        :param freshness: Свежесть еды
        :param time_to_spoil: Время до порчи еды в часах

        :raise TypeError: Если типы аргументов не соответствуют аннотации, то вызываем ошибку
        :raise ValueError: Если weight <= 0.0 или time_to_spoil <= 0.0, то вызываем ошибку

        Пример:
        >>> apple = Food(0.2, True, 72.0)
        """
        if not isinstance(weight, float):
            raise TypeError("Вес еды должен быть вещественным числом")
        if weight <= 0.0:
            raise ValueError("Вес еды должен быть неотрицательным")
        self.weight = weight

        if not isinstance(freshness, bool):
            raise TypeError("Показатель свежести может быть только true или false")
        self.freshness = freshness

        if not isinstance(time_to_spoil, float):
            raise TypeError("Время до порчи еды должно быть вещественным числом")
        if time_to_spoil <= 0.0:
            raise ValueError("Время до порчи еды должно быть неотрицательным")

    def health_recovery(self) -> float:
        """
        Метод, возвращающий количество восстановленного здоровья

        :return: Восстановленное здоровье

        Пример:
        >>> apple = Food(0.2, True, 72.0)
        >>> increase_health = apple.health_recovery()
        """
        ...

    def spoiling(self):
        """
        Превращает свежую еду в испорченую по истечению срока годности

        :return: None

        Пример:
        >>> apple = Food(0.2, True, 72.0)
        >>> apple.spoiling()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
