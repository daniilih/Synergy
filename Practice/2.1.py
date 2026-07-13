from datetime import datetime, date
import calendar

def get_birth_date():
    print("Введите дату вашего рождения")
    day = int(input("День: "))
    month = int(input("Месяц: "))
    year = int(input("Год: "))
    return day, month, year

def is_leap_year(year):
    return calendar.isleap(year)

def get_day_of_week(day, month, year):
    try:
        d = date(year, month, day)
        days_names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        return days_names[d.weekday()]
    except ValueError as e:
        return f"Некорректная дата: {e}"

def calculate_age(day, month, year):
    today = date.today()
    try:
        birthday = date(today.year, month, day)
    except ValueError:
        birthday = date(today.year, 2, 28)

    age = today.year - year
    if today < birthday:
        age -= 1
    return age

DIGITS = {
    '0': [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ],
    '1': [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        "  *  ",
        "  *  ",
        " ****"
    ],
    '2': [
        " *** ",
        "*   *",
        "    *",
        "   * ",
        "  *  ",
        " *   ",
        "*****"
    ],
    '3': [
        " *** ",
        "*   *",
        "    *",
        " *** ",
        "    *",
        "*   *",
        " *** "
    ],
    '4': [
        "   * ",
        "  ** ",
        " * * ",
        "*  * ",
        "**** ",
        "   * ",
        "   * "
    ],
    '5': [
        "*****",
        "*    ",
        "**** ",
        "    *",
        "    *",
        "*   *",
        " *** "
    ],
    '6': [
        " *** ",
        "*    ",
        "*    ",
        "**** ",
        "*   *",
        "*   *",
        " *** "
    ],
    '7': [
        "**** ",
        "   * ",
        "  *  ",
        " *   ",
        " *   ",
        " *   ",
        " *   "
    ],
    '8': [
        " *** ",
        "*   *",
        "*   *",
        " *** ",
        "*   *",
        "*   *",
        " *** "
    ],
    '9': [
        " *** ",
        "*   *",
        "*   *",
        " ****",
        "    *",
        "    *",
        " *** "
    ]
}

def print_star_date(dd, mm, yyyy):
    
    date_str = f"{dd:02d} {mm:02d} {yyyy:04d}"
    
    lines = [[] for _ in range(7)]
    
    for char in date_str:
        if char == ' ':
            for i in range(7):
                lines[i].append("     ") 
        elif char.isdigit():
            digit_lines = DIGITS[char]
            for i in range(7):
                lines[i].append(digit_lines[i])
        else:
            for i in range(7):
                lines[i].append("     ")

    print("\nВаша дата рождения в звездочках:")
    for line in lines:
        print("".join(line))
    print()

def main():
   
    try:
        day, month, year = get_birth_date()
    except ValueError:
        print("Ошибка: Пожалуйста, вводите только числа.")
        return

    leap = is_leap_year(year)
    print(f"Ваш год ({year}) {'является' if leap else 'не является'} високосным.")

    weekday = get_day_of_week(day, month, year)
    if "Некорректная дата" in weekday:
        print ("Некорректная дата")
        return
    print(f"Вы родились в: {weekday}.")

    age = calculate_age(day, month, year)
    print(f"Вам сейчас: {age} лет.")

    print_star_date(day, month, year)

if __name__ == "__main__":
    main()
