def Tinh_Toan(Day, Month, Year, Hour, Minute, Second):
    Dict_Phu=dict(Nam)
    if Year%4==0 and Year%100!=0:
        Dict_Phu[2]+=1
        Tong=366
    elif Year%400==0:
        Dict_Phu[2]+=1
        Tong=366
