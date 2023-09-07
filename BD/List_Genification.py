from ReadDocx.ScheduleClass.ScheduleWeekGroup import ScheduleWeekGroup


class GenificationList:
    group_number_dict: dict

    couples_dict: dict
    classroom_dict: dict
    tech_dict: dict

    schedule_list: list

    def __init__(self, schedule_week: list[ScheduleWeekGroup]) -> None:
        self.schedule_week = schedule_week
        self.set_number_group()
        self.set_day()
        self.set_schedule_list()

    def set_schedule_list(self):
        # group, week_type, week_day, couple_number, lesson, teacher, classroom
        schedule_list = []

        for week in self.schedule_week:
            week_list = [self.group_number_dict.get(week.number), week.type_week.value.number]

            for day in week.matrix:
                day_list = [*week_list, day.day.value.number]

                for couple in day.couple:
                    couple_list = [
                        *day_list, couple.number,
                        self.couples_dict.get(couple.couple),
                        self.tech_dict.get(couple.get_teacher_merge_str()),
                        self.classroom_dict.get(couple.get_classroom_merge_str())
                    ]
                    schedule_list.append(couple_list)

        self.schedule_list = schedule_list

    def set_number_group(self):
        groups = [group.number for group in self.schedule_week]
        self.group_number_dict = self.__list_to_dict(groups)

    def set_day(self):
        days = [day.matrix for day in self.schedule_week]

        classroom = []
        tech = []
        couples = []

        for day in days:
            for week_day in day:
                classroom += week_day.get_classroom_list()
                tech += week_day.get_teacher_list()
                couples += week_day.get_couple_list()

        self.classroom_dict = self.__list_to_dict(classroom)
        self.tech_dict = self.__list_to_dict(tech)
        self.couples_dict = self.__list_to_dict(couples)

    def __list_to_dict(self, list_items: list):
        return {item: i for i, item in enumerate(sorted(set(list_items)))}
