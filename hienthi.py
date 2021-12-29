while Tong_Thoi_Gian>=0:
    if Tong_Thoi_Gian>=172800:
        a=str(datetime.timedelta(seconds=int(Tong_Thoi_Gian))).split()
        a.remove('days,')
        b=a.pop(1).split(':')
        a.extend(b)
    elif 172800>Tong_Thoi_Gian>=86400:
        a=str(datetime.timedelta(seconds=int(Tong_Thoi_Gian))).split()
        a.remove('day,')
        b=a.pop(1).split(':')
        a.extend(b)
    else:
        a=str(datetime.timedelta(seconds=int(Tong_Thoi_Gian))).split(":")
        a.insert(0,0)
    time.sleep(1)
    print(a)
    Tong_Thoi_Gian-=1
