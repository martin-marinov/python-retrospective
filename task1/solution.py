HOROSCOPE = {((3, 21), (4, 20)): 'Овен',
             ((4, 21), (5, 20)): 'Телец',
             ((5, 21), (6, 20)): 'Близнаци',
             ((6, 21), (7, 21)): 'Рак',
             ((7, 22), (8, 22)): 'Лъв',
             ((8, 23), (9, 22)): 'Дева',
             ((9, 23), (10, 22)): 'Везни',
             ((10, 23), (11, 21)): 'Скорпион',
             ((11, 22), (12, 21)): 'Стрелец',
             ((1, 1), (1, 19)): 'Козирог',
             ((12, 22), (12, 31)): 'Козирог',
             ((1, 20), (2, 18)): 'Водолей',
             ((2, 19), (3, 20)): 'Риби'}


def what_is_my_sign(day, month):
    birth_date = (month, day)

    for (start_date, end_date), sign in HOROSCOPE.items():
        if birth_date >= start_date and birth_date <= end_date:
            return sign
