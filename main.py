from application.db.people import get_employees
from application.salary import calculate_salary

from datetime import date

from art import text2art


def ascii_from_text(text):
    ascii_art2 = text2art(text, font='slant')
    print(ascii_art2)


if __name__ == '__main__':
    calculate_salary(5, 3)
    print('________________________')
    get_employees()
    print('________________________')
    print(date.today())
    print('________________________')
    ascii_from_text("Python is great!")
