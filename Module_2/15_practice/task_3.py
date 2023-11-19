class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str: str) -> 'Date':
        day, month, year = map(int, date_str.split('-'))
        return cls(day, month, year)

    @staticmethod
    def is_date_valid(date_str: str) -> bool:
        day, month, year = map(int, date_str.split('-'))
        if month in (1, 3, 5, 7, 8, 10, 12) and 1 <= day <= 31:
            return True
        elif month in (4, 6, 9, 11) and 1 <= day <= 30:
            return True
        elif month == 2 and 1 <= day <= 29:
            return True
        return False

    def __str__(self) -> str:
        return f"День: {self.day}\tМесяц: {self.month}\tГод: {self.year}"


date = Date.from_string('10-12-2077')
print(date)
print('10-12-2077', Date.is_date_valid('10-12-2077'))
print('40-12-2077', Date.is_date_valid('40-12-2077'))
