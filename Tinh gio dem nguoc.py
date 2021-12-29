#ap dung cong thuc tinh nam nhuan de tim thoi gian dem nguoc
Nam={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
Time_Begin=[9,11,2021,23,25,31] 
Time_End=[9,12,2021,8,27,37]
def Tinh_Toan(Day, Month, Year, Hour, Minute, Second):
    Dict_Phu=dict(Nam)
    if Year%4==0 and Year%100!=0:
        Dict_Phu[2]+=1
        Tong_Ngay=366
    elif Year%400==0:
        Dict_Phu[2]+=1
        Tong_Ngay=366
    else:
        Tong_Ngay=365
    Days=Dict_Phu[int(Month)]-int(Day)
    Hours=24-Hour
    Minutes=0-Minute
    Seconds=0-Second
    Sum=Days*24*60*60+Hours*60*60+Minutes*60+Seconds
    for i in range(int(Month)+1,13):
        Sum+=(Dict_Phu[i]*24*60*60)
    return Sum, Tong_Ngay
Tong_Time_Begin, Tong1 = Tinh_Toan(*Time_Begin)
Tong_Time_End, Tong2 = Tinh_Toan(*Time_End)
Tong_Thoi_Gian=Tong2*24*60*60-Tong_Time_End+Tong_Time_Begin
print(Tong_Thoi_Gian)
#luu y: Tong_Thoi_Gian la thoi gian da doi ra giay
