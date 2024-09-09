def calc_media (list):
    sum = 0
    divisor = len(list)
    for i in range(len(list)):
        sum += list[i]
    media = sum / divisor
    return media
