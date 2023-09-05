from ReadDocx.ReadDocx import ReadDocx

if __name__ == '__main__':
    path_doc = "SH.docx"
    schedule = ReadDocx(path_doc).schedule_list[0]

    print(schedule.number, schedule.type_week.value.name)
    for i in schedule.matrix:
        print(i.day.value.day)
        for j in i.couple:
            print(j.number, j.couple, j.teacher, j.classroom)