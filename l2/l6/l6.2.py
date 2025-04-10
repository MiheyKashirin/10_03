seconds=int(input('Введите число:'))
if 0<seconds<8640000:
    days,other_seconds=divmod(seconds,86400)
    hours,other_seconds=divmod(other_seconds,3600)
    minutes, other_seconds=divmod(other_seconds,60)
    if days % 10 == 1 and days % 100 != 11:
        days_str = f'{days} день'
    elif days % 10 in [2, 3, 4] and not (12 <= days % 100 <= 14):
        days_str = f'{days} дні'
    else:
        days_str = f'{days} днів'
    time=f'{days_str},{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(other_seconds).zfill(2)}'
    print(time)
else:
    print('Eror enter<8640000')