import datetime
import emoji
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print(datetime.date.today())
    calculate_salary()
    get_employees()
    print(emoji.emojize(':pensive_face:'))