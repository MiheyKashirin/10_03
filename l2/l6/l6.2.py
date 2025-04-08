seconds=int(input('Enter your number:'))
if 0<seconds<8640000:
    days,other_seconds=divmod(seconds,86400)
    hours,other_seconds=divmod(other_seconds,3600)
    minutes, other_seconds=divmod(other_seconds,60)
    if days==1:
        days_str=f'{days}day'
    else:
        days_str=f'{days}days'
    time=f'{days_str},{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(other_seconds).zfill(2)}'
    print(time)
else:
    print('Eror enter<8640000')