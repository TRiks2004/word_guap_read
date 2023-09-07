import enum

class Week:
    def __init__(self, number: str, name: str) -> None:
        self.number = number
        self.name = name

class TypeWeek(enum.Enum):
    Numerator = Week(1, "Числитель")
    Denominator = Week(0, "Знаменатель")
    Error = Week(-1, "Error") 