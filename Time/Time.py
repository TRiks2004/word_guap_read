
class TimeСouple:
    def __init__(self, number: int, couple_start: str, couple_end: str) -> None:
        self.number = number
        self.couple_start = couple_start
        self.couple_end = couple_end


class СoupleNumberTime():
    One = TimeСouple(1, "09:20", "10:55")
    Two = TimeСouple(2, "11:05", "12:40")
    Three = TimeСouple(3, "13:20", "14:55")
    Four = TimeСouple(4, "15:05", "16:40")


    def get_teme(number):
        """
        Returns the corresponding time value for the given number.

        Parameters:
            number (int): The number for which to retrieve the corresponding time value.

        Returns:
            СoupleNumberTime: The time value corresponding to the given number.
        """
        if number == 1:
            return СoupleNumberTime.One
        elif number == 2:
            return СoupleNumberTime.Two
        elif number == 3:
            return СoupleNumberTime.Three
        elif number == 4:
            return СoupleNumberTime.Four