from ReadDocx.Enum.DayWeek import DayWeek
from ReadDocx.ScheduleClass.Сouple import Сouple


class ScheduleWeekDay():
    def __init__(self, day: DayWeek, couple: list[Сouple]):
        self.day = day
        self.couple = couple
