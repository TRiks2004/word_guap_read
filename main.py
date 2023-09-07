from ReadDocx.ReadDocx import ReadDocx

from BD.List_Genification import GenificationList

if __name__ == '__main__':
    path_doc = "SH.docx"
    schedule = ReadDocx(path_doc).schedule_list

    
    r = GenificationList(schedule_week=schedule)


