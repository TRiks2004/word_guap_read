import enum


class Day:
    def __init__(self, number: int, day: str, abbreviation: str) -> None:
        self.number = number
        self.day = day
        self.abbreviation = abbreviation


class DayWeek(enum.Enum):
    Monday = Day(1, "Понедельник", "Пн")
    Tuesday = Day(2, "Вторник", "Вт")
    Wednesday = Day(3, "Среда", "Ср")
    Thursday = Day(4, "Четверг", "Чт")
    Friday = Day(5, "Пятница", "Пт")
    Saturday = Day(6, "Суббота", "Сб")
    Sunday = Day(7, "Воскресенье", "Вс")

    def get_all_value():
        return [i.value for i in DayWeek]
