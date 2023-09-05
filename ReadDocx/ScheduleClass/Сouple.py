import re


class Сouple:
    couple: str
    teacher: list[str]
    classroom: list[str]

    def __init__(self, number: int, couple: str) -> None:
        self.number = number
        self.not_separation_couple = couple

        self.__separation()

    def __separation(self):
        par_match = re.match(r'(.*) (ауд\.\d*.*$)', self.not_separation_couple)

        if par_match is not None:
            match_res = list(par_match.groups())
            classroom = match_res[1].replace(',', ',ауд.').split(',')
        else:
            match_res = [self.not_separation_couple]
            classroom = ""

        words = [w for w in match_res[0].split(' ') if w != '']

        tech = []
        tech_count = 0

        for i, word in enumerate(words):
            if word.count('.') == 2 and len(word) == 4 and not any(char.isdigit() for char in word):
                tech.append(words[i - 1] + " " + words[i])
                tech_count += 1

        self.couple = ' '.join(words[:tech_count * -2])
        self.teacher = tech
        self.classroom = classroom
