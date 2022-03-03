# dz1
duration = int(input("duration = "))
if duration < 60:
    print(duration, 'сек')
elif 3600 > duration >= 60:
    min = duration // 60
    sec = duration % 60
    print(min, 'мин', sec, 'sec')
elif 86400 > duration >= 3600:
    hour = duration // 3600
    remainder_hour = duration % 3600
    min = remainder_hour // 60
    sec = duration % 60
    print(hour, 'час(а/ов)', min, 'мин', sec, 'сек')
else:
    duration >= 86400
    day = duration // 86400
    remainder_hour = duration % 86400
    hour = remainder_hour // 3600
    remainder = duration % 3600
    min = remainder // 60
    sec = duration % 60
    print(day, 'день', hour, 'час(а/ов)', min, 'мин', sec, 'сек')
