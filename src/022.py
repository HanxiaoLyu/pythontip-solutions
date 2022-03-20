st = "00:00:00"
et = "00:00:52"


def seconds(time):
    return int(time[0:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])


print(seconds(et) - seconds(st))
