sec_in_minute = 60
sec_in_hour = 3600
sec_in_day = 86400

duration = int(input('Укажите количество секунд: '))

if duration < sec_in_minute:
    print('{} сек'.format(duration))

elif sec_in_minute <= duration and sec_in_hour > duration:
    my_minute = duration // sec_in_minute
    my_second = duration % sec_in_minute
    print('{} мин {} сек'.format(my_minute, my_second))

elif duration >= sec_in_hour and duration < sec_in_day:
    my_hour = duration // sec_in_hour
    duration = duration % sec_in_hour
    my_minute = duration // sec_in_minute
    my_second = duration % sec_in_minute
    print('{} час {} мин {} сек'.format(my_hour, my_minute, my_second))

elif duration >= sec_in_day:
    my_day = duration // sec_in_day
    duration = duration % sec_in_day
    my_hour = duration // sec_in_hour
    duration = duration % sec_in_hour
    my_minute = duration // sec_in_minute
    my_second = duration % sec_in_minute
    print('{} дн {} час {} мин {} сек'.format(my_day, my_hour, my_minute, my_second))
