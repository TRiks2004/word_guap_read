import enum


class Day:
    def __init__(self, number: int, day: str, abbreviation: str) -> None:
        self.number = number
        self.day = day
        self.abbreviation = abbreviation

class DayWeek(enum.Enum):
    Monday = Day(0, "Понедельник", "Пн")
    Tuesday = Day(1, "Вторник", "Вт")
    Wednesday = Day(2, "Среда", "Ср")
    Thursday = Day(3, "Четверг", "Чт")
    Friday = Day(4, "Пятница", "Пт")
    Saturday = Day(5, "Суббота", "Сб")
    Sunday = Day(6, "Воскресенье", "Вс")

    def get_all_value():
        return [i.value for i in DayWeek]