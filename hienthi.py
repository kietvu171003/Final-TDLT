while Tong_Thoi_Gian>=0:
    if Tong_Thoi_Gian>=172800:
        hienthi=str(datetime.timedelta(seconds=int(Tong_Thoi_Gian))).split()
        hienthi.remove('days,')
        trung_gian_dem_nguoc=hienthi.pop(1).split(':')
        hienthi.extend(trung_gian_dem_nguoc)
    elif 172800>Tong_Thoi_Gian>=86400:
        hienthi=str(datetime.timedelta(seconds=int(Tong_Thoi_Gian))).split()
        hienthi.remove('day,')
        trung_gian_dem_nguoc=hienthi.pop(1).split(':')
        hienthi.extend(trung_gian_dem_nguoc)
    else:
        hienthi=str(datetime.timedelta(seconds=int(Tong_Thoi_Gian))).split(":")
        hienthi.insert(0,0)
    time.sleep(1)
    print(hienthi)
    Tong_Thoi_Gian-=1