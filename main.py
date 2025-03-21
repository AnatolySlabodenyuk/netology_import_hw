from application.db.people import get_employees
from application.salary import calculate_salary

from datetime import date

if __name__ == '__main__':
    calculate_salary(5, 3)
    print('________________________')
    get_employees()
    print('________________________')
    print(date.today())
