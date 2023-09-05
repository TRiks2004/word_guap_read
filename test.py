
import re

def separation(par: str) -> list[str, str, str]:
    par_match = re.match(r'(.*) (ауд\.\d*.*$)', par)

    match_res = list(par_match.groups())
    classroom = match_res[1].replace(',', ',ауд.').split(',')
   
    words = [w for w in match_res[0].split(' ') if w != '']

    tech = []
    tech_count = 0

    for i, word in enumerate(words):
        if word.count('.') == 2 and len(word) == 4 and not any(char.isdigit() for char in word):

            tech.append(words[i-1] + " " + words[i])
            tech_count += 1

    return [' '.join(words[:tech_count * -2]), tech, classroom]


test_str = "Иностранный язык в профессиональной деятельности Бороухина В.М. Хайретдинова Л.М. ауд.608,309"

e = division_lesson(test_str)

print(e)