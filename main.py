# Khai báo các thư viện đồ họa, thời gian, chạy luồng và xử lý ảnh
from tkinter import *
import threading
import datetime
import time
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.title('Clock')
root.geometry('405x720')

# Tạo ra biến để nhận ngày tháng năm giờ phút được nhập vào
# Ngay = 0
# Thang = 0
# Nam = 0
# Gio = 0
# Phut = 0

# Tạo ra các list chứa các câu cho từng chủ đề
Bien_random_cho_chu_de = randint(0, 2) # Cái này để random cái câu trong list
List_Cau_Chu_De_1=['Sắp bước sang tuổi mới,\nhãy làm tốt hơn những cái đã làm được ở hiện tại\nvà khắc phục những cái chưa tốt.Bạn nhé!',
                   'Chuẩn bị thêm 1 tuổi mới\nnhưng bạn không hề già đi đâu nhé!\nChỉ là cái đẳng cấp nó bước lên một tầm cao hơn thôi!!!!',
                   'Chúc tôi của một năm sau đủ trưởng thành\nđủ tình yêu để sống hạnh phúc hơn hiện tại.\nHappy birthday to me!']

List_Cau_Chu_De_2=['Tốc độ thành công của bản thân\nnhất định phải nhanh hơn tốc độ già đi của cha mẹ.',
                   'Thái độ bây giờ của bạn sẽ quyết định mười năm sau\nbạn là một nhân vật tầm cỡ hay chỉ là một kẻ thất bại.',
                   'Nếu như không có vận may, thì hãy thử dùng dũng khí.']

List_Cau_Chu_De_3=['Thành công lớn nhất của con người\nlà biến đam mê thành thu nhập.',
                   ' Không có áp lực, không có kim cương.',
                   'Có làm thì mới có ăn,\nkhông làm mà đòi có ăn thì chỉ có ăn may:))']

List_Cau_Chu_De_4=['Những ký ức đã cũ, nhưng khi nhìn lại,\nngười ta vẫn sẽ thấy yêu thương đó hiện hữu.\nNgười ta không thể quên.',
                   'Mọi thứ bạn đã sống\ngóp phần giúp bạn trở thành con người bạn bây giờ.',
                   'Tuổi trẻ dẫu có bồng bột, dẫu mất mát,đắng cay\nvẫn là những tháng ngày đẹp nhất\ntrong chuỗi kỉ niệm đẹp của cuộc đời này.']

List_Cau_Chu_De_5=['Suy nghĩ quá lâu về một việc\nthường dẫn đến không làm việc đó.',
                   'Đừng chờ đợi.\nSẽ không bao giờ có một thời điểm chính xác.',
                   'Sớm muộn thì\n‘không phải bây giờ’\ncũng sẽ biến thành ‘không bao giờ’']

List_chinh = [List_Cau_Chu_De_1, List_Cau_Chu_De_2, List_Cau_Chu_De_3, List_Cau_Chu_De_4, List_Cau_Chu_De_5]

# Tạo giao diện chọn chủ đề
Bg_Chon_Chu_De = ImageTk.PhotoImage(Image.open('Chọn chủ đề.png').resize((405, 720)))
Bg_Chon_Chu_De_Label = Label(image=Bg_Chon_Chu_De)
Bg_Chon_Chu_De_Label.pack()
#Label(image=Bg_Chon_Chu_De).pack()

# Tạo các image cho background nhập và để vô 1 list chứa các biến đó
Bg_Nhap_1 = ImageTk.PhotoImage(Image.open('Nhập/Nhập_1.png').resize((405, 720)))
Bg_Nhap_2 = ImageTk.PhotoImage(Image.open('Nhập/Nhập_2.png').resize((405, 720)))
Bg_Nhap_3 = ImageTk.PhotoImage(Image.open('Nhập/Nhập_3.png').resize((405, 720)))
Bg_Nhap_4 = ImageTk.PhotoImage(Image.open('Nhập/Nhập_4.png').resize((405, 720)))
Bg_Nhap_5 = ImageTk.PhotoImage(Image.open('Nhập/Nhập_5.png').resize((405, 720)))

List_Bg_Nhap = [Bg_Nhap_1, Bg_Nhap_2, Bg_Nhap_3, Bg_Nhap_4, Bg_Nhap_5]

# Tạo hàm hiển thị Entry nhập, và nút bắt đầu để chạy chương trình
def hien_thi_cho_nhap():
    global Entry_Day, Entry_Month, Entry_Year, Entry_Hour, Entry_Minute, Start_Button
    Entry_Day = Entry(root, bg='#ffede0', fg='black', font=('GlacialIndifference-Regular', 14), highlightthickness=0, bd=0)
    Entry_Month = Entry(root, bg='#ffede0', fg='black', font=('GlacialIndifference-Regular', 14), highlightthickness=0, bd=0)
    Entry_Year = Entry(root, bg='#ffede0', fg='black', font=('GlacialIndifference-Regular', 14), highlightthickness=0, bd=0)
    Entry_Hour = Entry(root, bg='#ffede0', fg='black', font=('GlacialIndifference-Regular', 14), highlightthickness=0, bd=0)
    Entry_Minute = Entry(root, bg='#ffede0', fg='black', font=('GlacialIndifference-Regular', 14), highlightthickness=0, bd=0)
    Entry_Day.place(x=30, y=463, width=47, height=46)
    Entry_Month.place(x=105, y=463, width=47, height=46)
    Entry_Year.place(x=179, y=463, width=47, height=46)
    Entry_Hour.place(x=254, y=463, width=47, height=46)
    Entry_Minute.place(x=329, y=463, width=47, height=46)
    Start_Button = Button(image=Start_Button_Image, command=start_button, highlightthickness=0, bd=0)
    Start_Button.place(x=95, y=578)

# Tạo hàm xóa các nút chọn chủ đề và background chọn chủ đề khi được gọi
def forget_giao_dien_chon_chu_de():
    Button_Chu_De_1_Button.place_forget()
    Button_Chu_De_2_Button.place_forget()
    Button_Chu_De_3_Button.place_forget()
    Button_Chu_De_4_Button.place_forget()
    Button_Chu_De_5_Button.place_forget()
    Button_Chu_De_6_Button.place_forget()
    Button_Chu_De_7_Button.place_forget()
    Bg_Chon_Chu_De_Label.pack_forget()

# Tạo các hình ảnh và nút chọn chủ đề đếm ngược, hình ảnh cho nút bắt đầu, quay lại, và làm mới
Start_Button_Image = ImageTk.PhotoImage(Image.open('Button/Start_Button.jpg'))
Return_Button_Image = ImageTk.PhotoImage(Image.open('Button/Return_button.jpg'))
Restart_Button_Image = ImageTk.PhotoImage(Image.open('Button/Restart_Button.jpg'))
Button_Chu_De_1 = ImageTk.PhotoImage(Image.open('Button/Button_1.jpg'))
Button_Chu_De_2 = ImageTk.PhotoImage(Image.open('Button/Button_2.jpg'))
Button_Chu_De_3 = ImageTk.PhotoImage(Image.open('Button/Button_3.jpg'))
Button_Chu_De_4 = ImageTk.PhotoImage(Image.open('Button/Button_4.jpg'))
Button_Chu_De_5 = ImageTk.PhotoImage(Image.open('Button/Button_5.jpg'))
Button_Chu_De_6 = ImageTk.PhotoImage(Image.open('Button/Button_6.jpg'))
Button_Chu_De_7 = ImageTk.PhotoImage(Image.open('Button/Button_7.jpg'))

Button_Chu_De_1_Button = Button(image=Button_Chu_De_1, highlightthickness=0, bd=0, command=lambda: chuyen_giao_dien_nhap_dem_nguoc(1))
Button_Chu_De_2_Button = Button(image=Button_Chu_De_2, highlightthickness=0, bd=0, command=lambda: chuyen_giao_dien_nhap_dem_nguoc(2))
Button_Chu_De_3_Button = Button(image=Button_Chu_De_3, highlightthickness=0, bd=0, command=lambda: chuyen_giao_dien_nhap_dem_nguoc(3))
Button_Chu_De_4_Button = Button(image=Button_Chu_De_4, highlightthickness=0, bd=0, command=lambda: chuyen_giao_dien_nhap_dem_nguoc(4))
Button_Chu_De_5_Button = Button(image=Button_Chu_De_5, highlightthickness=0, bd=0, command=lambda: chuyen_giao_dien_nhap_dem_nguoc(5))

Button_Chu_De_1_Button.place(x=77, y=137)
Button_Chu_De_2_Button.place(x=77, y=185)
Button_Chu_De_3_Button.place(x=77, y=230)
Button_Chu_De_4_Button.place(x=77, y=276)
Button_Chu_De_5_Button.place(x=77, y=322)

# Tạo hàm chuyển qua giao diện nhập thời điểm cần đếm ngược, bao gồm việc xóa giao diện trước đó và hiển thị giao diện mới
def chuyen_giao_dien_nhap_dem_nguoc(x):
    global bien_trung_gian_dem_nguoc, Bg_Nhap_Label, Return_Button  # global bien_trung_gian_dem_nguoc để lát xài cho chuyển qua giao diện hiển thị
    bien_trung_gian_dem_nguoc = x
    forget_giao_dien_chon_chu_de()
    Bg_Nhap_Label = Label(root, image=List_Bg_Nhap[x - 1])
    Bg_Nhap_Label.pack()
    hien_thi_cho_nhap()
    Return_Button = Button(image=Return_Button_Image, highlightthickness=0, bd=0, command= quay_nguoc_ve_giao_dien_chon_chu_de)
    Return_Button.place(x=25, y=42)

# Tạo các image background cho phần hiển thị
Bg_Hien_Thi_1 = ImageTk.PhotoImage(Image.open('Hiển thị/Hiển thị_1.png').resize((405, 720)))
Bg_Hien_Thi_2 = ImageTk.PhotoImage(Image.open('Hiển thị/Hiển thị_2.png').resize((405, 720)))
Bg_Hien_Thi_3 = ImageTk.PhotoImage(Image.open('Hiển thị/Hiển thị_3.png').resize((405, 720)))
Bg_Hien_Thi_4 = ImageTk.PhotoImage(Image.open('Hiển thị/Hiển thị_4.png').resize((405, 720)))
Bg_Hien_Thi_5 = ImageTk.PhotoImage(Image.open('Hiển thị/Hiển thị_5.png').resize((405, 720)))

List_Bg_Hien_Thi_Dem_Nguoc = [Bg_Hien_Thi_1, Bg_Hien_Thi_2, Bg_Hien_Thi_3, Bg_Hien_Thi_4, Bg_Hien_Thi_5]
# Tạo 1 hàm để hiển thị phần đếm ngược
def hien_thi_bg_dem_nguoc(y):
    Bg_Nhap_Label.pack_forget()
    Bg_Hien_Thi_Label = Label(image=List_Bg_Hien_Thi_Dem_Nguoc[y - 1])
    Bg_Hien_Thi_Label.pack()
    Label_Cau_Cho_Tung_Chu_De = Label(root,text=List_chinh[y-1][Bien_random_cho_chu_de], font=('SVN-Be Cool', 10), bg='#ffede0')
    Label_Cau_Cho_Tung_Chu_De.place(x=27, y=608, width=351, height=67)
# Tạo 1 nút bắt đầu để chạy chương trình sau khi nhập
def start_button():
    #global Ngay, Thang, Nam, Gio, Phut, Tong_Thoi_Gian, Time_Begin, Time_End
    global Tong_Thoi_Gian
    # Lấy giá trị được nhập từ Entry
    Ngay = Entry_Day.get()
    Thang = Entry_Month.get()
    Nam = Entry_Year.get()
    Gio = Entry_Hour.get()
    Phut = Entry_Minute.get()

    # Tạo 2 list chứa các thời gian bắt đầu và kết thúc để xử lý
    Begin = datetime.datetime.now()
    Time_Begin = [Begin.day, Begin.month, Begin.year, Begin.hour, Begin.minute, Begin.second]
    Time_End = [Ngay, Thang, Nam, Gio, Phut, 0]

    # Gọi hàm tính toán thời gian rồi đưa 2 list vào để tính
    Tong_Time_Begin, Tong1 = Tinh_Toan(*Time_Begin)
    Tong_Time_End, Tong2 = Tinh_Toan(*Time_End)

    # Xét TH nếu cùng và khác năm để đưa ra tổng thời gian cần tính
    if int(Time_Begin[2]) == int(Time_End[2]):
        Tong_Thoi_Gian = Tong_Time_Begin-Tong_Time_End
    else:
        Tong_Thoi_Gian = Tong2 * 24 * 60 * 60 - Tong_Time_End + Tong_Time_Begin

    # Xóa các Entry khi chạy chương trình
    Entry_Day.place_forget()
    Entry_Month.place_forget()
    Entry_Year.place_forget()
    Entry_Hour.place_forget()
    Entry_Minute.place_forget()
    Start_Button.place_forget()
    Return_Button.place_forget()

    # Gọi hàm hiển thị đếm ngược và truyền biến đã được gán ở hàm chuyển giao diện nhập ở trên
    hien_thi_bg_dem_nguoc(bien_trung_gian_dem_nguoc)
    hien_thi_thoi_gian_dem_nguoc()

# Tạo ra hàm hiển thị label chứa thời gian đếm ngược và 1 luồng để chạy phần xử lý cho cái đếm ngược
def hien_thi_thoi_gian_dem_nguoc():
    global Label_Ngay_Dem_Nguoc, Label_Gio_Dem_Nguoc, Label_Phut_Dem_Nguoc, Label_Giay_Dem_Nguoc
    Label_Ngay_Dem_Nguoc = Label(root, font=('GlacialIndifference-Regular', 15), bg='#ffede0')
    Label_Gio_Dem_Nguoc = Label(root, font=('GlacialIndifference-Regular', 15), bg='#ffede0')
    Label_Phut_Dem_Nguoc = Label(root, font=('GlacialIndifference-Regular', 15), bg='#ffede0')
    Label_Giay_Dem_Nguoc = Label(root, font=('GlacialIndifference-Regular', 15), bg='#ffede0')
    Label_Ngay_Dem_Nguoc.place(x=66, y=462, width=49, height=48)
    Label_Gio_Dem_Nguoc.place(x=140, y=462, width=49, height=48)
    Label_Phut_Dem_Nguoc.place(x=215, y=462, width=49, height=48)
    Label_Giay_Dem_Nguoc.place(x=290, y=462, width=49, height=48)
    Set_thoi_gian_dem_nguoc = threading.Thread(target=Hien_Thi)
    Set_thoi_gian_dem_nguoc.start()

# Tạo nút quay ngược từ giao diện nhập về giao diện chọn chủ để
def quay_nguoc_ve_giao_dien_chon_chu_de():
    Entry_Day.place_forget()
    Entry_Month.place_forget()
    Entry_Year.place_forget()
    Entry_Hour.place_forget()
    Entry_Minute.place_forget()

    Bg_Nhap_Label.pack_forget()
    Return_Button.place_forget()
    Start_Button.place_forget()

    Bg_Chon_Chu_De_Label.pack()
    Button_Chu_De_1_Button.place(x=77, y=137)
    Button_Chu_De_2_Button.place(x=77, y=185)
    Button_Chu_De_3_Button.place(x=77, y=230)
    Button_Chu_De_4_Button.place(x=77, y=276)
    Button_Chu_De_5_Button.place(x=77, y=322)
    Button_Chu_De_6_Button.place(x=77, y=369)
    Button_Chu_De_7_Button.place(x=77, y=415)

# Xử lý output
Dict_Nam = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} # tạo 1 dict các ngày trong tháng

#Time_Begin=[Begin.day, Begin.month, Begin.year, Begin.hour, Begin.minute, Begin.second]
#Time_End=[Ngay, Thang, Nam, Gio, Phut]
# 2 list cho thời điểm bắt đầu và kết thúc

'''Time_Begin = [9, 11, 2021, 23, 25, 31]
Time_End = [Ngay, Thang, Nam, Gio, Phut]'''
#Time_End = [21, 5, 2022, 8, 27, 37]

# Tạo hàm tính toán thời gian
def Tinh_Toan( Day, Month, Year, Hour, Minute, Second):
    Dict_Phu = dict(Dict_Nam)
    if int(Year) % 4 == 0 and int(Year) % 100 != 0:
        Dict_Phu[2] += 1
        Tong_Ngay = 66
    elif int(Year) % 400 == 0:
        Dict_Phu[2] += 1
        Tong_Ngay = 366
    else:
        Tong_Ngay = 365
    Days = Dict_Phu[int(Month)]-int(Day)
    Hours = 24-int(Hour)
    Minutes = 0-int(Minute)
    Seconds = 0-int(Second)
    Sum = Days*24*60*60+Hours*60*60+Minutes*60+Seconds
    for i in range(int(Month)+1, 13):
        Sum += (Dict_Phu[i]*24*60*60)
    return Sum, Tong_Ngay

def Hien_Thi():
    global Tong_Thoi_Gian
    while Tong_Thoi_Gian >= 0:
        if Tong_Thoi_Gian >= 172800:
            hien_thi_dem_nguoc = str(datetime.timedelta(seconds=int(Tong_Thoi_Gian))).split()
            hien_thi_dem_nguoc.remove('days,')
            trung_gian_dem_nguoc = hien_thi_dem_nguoc.pop(1).split(':')
            hien_thi_dem_nguoc.extend(trung_gian_dem_nguoc)
        elif 172800 > Tong_Thoi_Gian >= 86400:
            hien_thi_dem_nguoc = str(datetime.timedelta(seconds=int(Tong_Thoi_Gian))).split()
            hien_thi_dem_nguoc.remove('day,')
            trung_gian_dem_nguoc = hien_thi_dem_nguoc.pop(1).split(':')
            hien_thi_dem_nguoc.extend(trung_gian_dem_nguoc)
        else:
            hien_thi_dem_nguoc = str(datetime.timedelta(seconds=int(Tong_Thoi_Gian))).split(":")
            hien_thi_dem_nguoc.insert(0, 0)
        time.sleep(1)
        Label_Ngay_Dem_Nguoc.config(text=hien_thi_dem_nguoc[0])
        Label_Gio_Dem_Nguoc.config(text=hien_thi_dem_nguoc[1])
        Label_Phut_Dem_Nguoc.config(text=hien_thi_dem_nguoc[2])
        Label_Giay_Dem_Nguoc.config(text=hien_thi_dem_nguoc[3])
        Tong_Thoi_Gian -= 1

# Tạo các nút cho chủ đề đếm lên
Button_Chu_De_6_Button = Button(image=Button_Chu_De_6, highlightthickness=0, bd=0, command=lambda: chuyen_giao_dien_hien_thi_dem_len(6))
Button_Chu_De_7_Button = Button(image=Button_Chu_De_7, highlightthickness=0, bd=0, command=lambda: chuyen_giao_dien_hien_thi_dem_len(7))

Button_Chu_De_6_Button.place(x=77, y=369)
Button_Chu_De_7_Button.place(x=77, y=415)

Bg_Hien_Thi_6 = ImageTk.PhotoImage(Image.open('Hiển thị/Hiển thị_6.png').resize((405, 720)))
Bg_Hien_Thi_7 = ImageTk.PhotoImage(Image.open('Hiển thị/Hiển thị_7.png').resize((405, 720)))

List_Bg_Hien_Thi_Dem_Len = [Bg_Hien_Thi_6, Bg_Hien_Thi_7]

# Tạo hàm chuyển qua giao diện đếm lên
def chuyen_giao_dien_hien_thi_dem_len(y):
    global Bg_Hien_Thi_Dem_Len, Restart_Button
    forget_giao_dien_chon_chu_de()
    Bg_Hien_Thi_Dem_Len = Label(image=List_Bg_Hien_Thi_Dem_Len[y-6])
    Bg_Hien_Thi_Dem_Len.pack()
    Restart_Button = Button(image=Restart_Button_Image, command=lambda: xu_ly_dem_len(0), highlightthickness=0, bd=0)
    Restart_Button.place(x=154, y=571)
    hien_thi_thoi_gian_dem_len()
    xu_ly_dem_len(y)

# Tạo hàm hiển thị label chứa thời gian đếm lên
def hien_thi_thoi_gian_dem_len():
    global Label_Nam_Dem_Len, Label_Ngay_Dem_Len, Label_Gio_Dem_Len, Label_Phut_Dem_Len, Label_Giay_Dem_Len

    Label_Nam_Dem_Len = Label(root, font=('GlacialIndifference-Regular', 15), bg='#ffede0')
    Label_Ngay_Dem_Len = Label(root, font=('GlacialIndifference-Regular', 15), bg='#ffede0')
    Label_Gio_Dem_Len = Label(root, font=('GlacialIndifference-Regular', 15), bg='#ffede0')
    Label_Phut_Dem_Len = Label(root, font=('GlacialIndifference-Regular', 15), bg='#ffede0')
    Label_Giay_Dem_Len = Label(root, font=('GlacialIndifference-Regular', 15), bg='#ffede0')

    Label_Nam_Dem_Len.place(x=30, y=463, width=47, height=46)
    Label_Ngay_Dem_Len.place(x=105, y=463, width=47, height=46)
    Label_Gio_Dem_Len.place(x=179, y=463, width=47, height=46)
    Label_Phut_Dem_Len.place(x=254, y=463, width=47, height=46)
    Label_Giay_Dem_Len.place(x=329, y=463, width=47, height=46)

so_hien_thi = 0

def start():
    global so_hien_thi, bien_de_loop_ham_start
    if so_hien_thi >= 172800:
        hien_thi_dem_len = str(datetime.timedelta(seconds=int(so_hien_thi))).split()
        hien_thi_dem_len.remove('days,')
        trung_gian_dem_len = hien_thi_dem_len.pop(1).split(':')
        hien_thi_dem_len.extend(trung_gian_dem_len)
        trung_gian_dem_len = hien_thi_dem_len.pop(0)
        nam = int(trung_gian_dem_len) // 365
        ngay = int(trung_gian_dem_len) % 365
        hien_thi_dem_len = [str(nam), str(ngay)] + hien_thi_dem_len
    elif 172800 > so_hien_thi >= 86400:
        hien_thi_dem_len = str(datetime.timedelta(seconds=int(so_hien_thi))).split()
        hien_thi_dem_len.remove('day,')
        trung_gian_dem_len = hien_thi_dem_len.pop(1).split(':')
        hien_thi_dem_len.extend(trung_gian_dem_len)
        hien_thi_dem_len.insert(0, 0)
    else:
        hien_thi_dem_len = str(datetime.timedelta(seconds=int(so_hien_thi))).split(":")
        hien_thi_dem_len = [0, 0] + hien_thi_dem_len
    Label_Nam_Dem_Len.config(text=hien_thi_dem_len[0])
    Label_Ngay_Dem_Len.config(text=hien_thi_dem_len[1])
    Label_Gio_Dem_Len.config(text=hien_thi_dem_len[2])
    Label_Phut_Dem_Len.config(text=hien_thi_dem_len[3])
    Label_Giay_Dem_Len.config(text=hien_thi_dem_len[4])
    so_hien_thi += 1
    bien_de_loop_ham_start = root.after(1000, start)
def xu_ly_dem_len(z):
    global so_hien_thi, bien_de_loop_ham_start, bien_trung_gian_dem_len
    '''so_hien_thi = 0
    def start():
        global so_hien_thi, bien__de_loop_ham_start
        if so_hien_thi >= 172800:
            hien_thi_dem_len = str(datetime.timedelta(seconds=int(so_hien_thi))).split()
            hien_thi_dem_len.remove('days,')
            trung_gian_dem_len = hien_thi_dem_len.pop(1).split(':')
            hien_thi_dem_len.extend(trung_gian_dem_len)
            trung_gian_dem_len = hien_thi_dem_len.pop(0)
            nam = int(trung_gian_dem_len)//365
            ngay = int(trung_gian_dem_len) % 365
            hien_thi_dem_len=[str(nam), str(ngay)]+hien_thi_dem_len
        elif 172800 > so_hien_thi >= 86400:
            hien_thi_dem_len = str(datetime.timedelta(seconds=int(so_hien_thi))).split()
            hien_thi_dem_len.remove('day,')
            trung_gian_dem_len = hien_thi_dem_len.pop(1).split(':')
            hien_thi_dem_len.extend(trung_gian_dem_len)
            hien_thi_dem_len.insert(0, 0)
        else:
            hien_thi_dem_len = str(datetime.timedelta(seconds=int(so_hien_thi))).split(":")
            hien_thi_dem_len = [0, 0] + hien_thi_dem_len
        Label_Nam_Dem_Len.config(text=hien_thi_dem_len[0])
        Label_Ngay_Dem_Len.config(text=hien_thi_dem_len[1])
        Label_Gio_Dem_Len.config(text=hien_thi_dem_len[2])
        Label_Phut_Dem_Len.config(text=hien_thi_dem_len[3])
        Label_Giay_Dem_Len.config(text=hien_thi_dem_len[4])
        so_hien_thi += 1
        bien_de_loop_ham_start = root.after(1000, start)'''
    if z == 6 or z == 7:
        start()
        bien_trung_gian_dem_len = z
    else:
        root.after_cancel(bien_de_loop_ham_start)
        so_hien_thi = 0
        cai_dat_lai_gio_dem_len()
def cai_dat_lai_gio_dem_len():
    Bg_Hien_Thi_Dem_Len.pack_forget()
    Label_Nam_Dem_Len.place_forget()
    Label_Ngay_Dem_Len.place_forget()
    Label_Gio_Dem_Len.place_forget()
    Label_Phut_Dem_Len.place_forget()
    Label_Giay_Dem_Len.place_forget()
    Restart_Button.place_forget()
    Bg_Chon_Chu_De_Label.pack()
    Button_Chu_De_1_Button.place(x=77, y=137)
    Button_Chu_De_2_Button.place(x=77, y=185)
    Button_Chu_De_3_Button.place(x=77, y=230)
    Button_Chu_De_4_Button.place(x=77, y=276)
    Button_Chu_De_5_Button.place(x=77, y=322)
    Button_Chu_De_6_Button.place(x=77, y=369)
    Button_Chu_De_7_Button.place(x=77, y=415)


root.mainloop()