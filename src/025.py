t = {"year": "2013", "month": "9", "day": "30", "hour": "16", "minute": "45", "second": "2"}
# 2013-09-30 16:45:02
for i in t.keys():
    if int(t[i]) < 10:
        t[i] = '0' + t[i]
print(f"{t.get('year')}-{t.get('month')}-{t.get('day')} {t.get('hour')}:{t.get('minute')}:{t.get('second')}")
