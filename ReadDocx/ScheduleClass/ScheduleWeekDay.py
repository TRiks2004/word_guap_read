from typing import List

from ReadDocx.Enum.DayWeek import DayWeek
from ReadDocx.ScheduleClass.Сouple import Сouple


class ScheduleWeekDay:
    def __init__(self, day: DayWeek, couple: list[Сouple]):
        self.day = day
        self.couple = couple

    def get_classroom_list(self) -> list[str]:
        return [
            couple.get_classroom_merge_str() for couple in self.couple]

    def get_teacher_list(self) -> list[list[str]]:
        return [couple.get_teacher_merge_str() for couple in self.couple]

    def get_couple_list(self) -> list[str]:
        return [couple.couple for couple in self.couple]
