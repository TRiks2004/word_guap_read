from ReadDocx.ScheduleClass.ScheduleWeekDay import ScheduleWeekDay
from ReadDocx.Enum.TypeWeek import TypeWeek
from ReadDocx.Enum.DayWeek import DayWeek
from ReadDocx.ScheduleClass.Сouple import Сouple


class ScheduleWeekGroup:
    matrix: list[ScheduleWeekDay]

    def __init__(self, number: str, type_week: TypeWeek, table_schedule):
        self.number = number
        self.type_week = type_week
        self.table_schedule = table_schedule

        self.__matrix()

    def get_name_week(self, name: str):
        if name == DayWeek.Monday.value.day:
            return DayWeek.Monday
        elif name == DayWeek.Tuesday.value.day:
            return DayWeek.Tuesday
        elif name == DayWeek.Wednesday.value.day:
            return DayWeek.Wednesday
        elif name == DayWeek.Thursday.value.day:
            return DayWeek.Thursday
        elif name == DayWeek.Friday.value.day:
            return DayWeek.Friday
        elif name == DayWeek.Saturday.value.day:
            return DayWeek.Saturday
        elif name == DayWeek.Sunday.value.day:
            return DayWeek.Sunday
        else:
            raise ValueError("Неизвестный день недели")

    def __get_list_table(self):
        return [[cell.text for cell in colum.cells] for colum in self.table_schedule.columns]

    def __matrix(self):
        schedule = self.__get_list_table()

        schedule_week_group = []
        for day in schedule[2:]:
            name_day = self.get_name_week(day[0])
            couples = []
            for number_couple, couple in enumerate(day[1:], 1):
                if couple != "-" * 7:
                    couples.append(Сouple(number_couple, couple))

            schedule_week_group.append(ScheduleWeekDay(name_day, couples))

        self.matrix = schedule_week_group
