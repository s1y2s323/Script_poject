from internet import*
from tkinter import*
from tkinter import font
from io import BytesIO
import urllib
import urllib.request
from PIL import Image,ImageTk

import mimetypes
import mysmptlib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart



import tkinter.messagebox


root=Tk()
root.geometry("1000x700+300+200")


SearchListBox=[]
RenderText=None
DetailRenderText=None

SearchIndex=None
SearchIndex2=None
inputDetail=None
send=None
recipicent=None

inputSenderEmail=None
inputRecipientEmail=None

contentID=None


#with urllib.request.urlopen(url) as u:
#    raw_data = u.read()
#im = Image.open(BytesIO(raw_data))
#image = ImageTk.PhotoImage(im)
def initImage(id):

    url=None
    try:
        for i in range(len(DataList)):
            if DataList[i][0] == id:
                url = DataList[i][4]
    except:
        pass

    with urllib.request.urlopen(url) as u:
        raw_data = u.read()

    im = Image.open(BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)

    label=Label(root,image=image,height=200,width=400)
    label.pack()
    label.place(x=450,y=0)
    root.mainloop()

def EmailAction():
    ID = str(inputDetail.get())
    url = Detailurl(ID)
    host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
    port = "587"
    conn = HTTPConnection(server)
    conn.request("GET", url)
    req = conn.getresponse()

    senderAddr = "ghkdtjdbs33@gmail.com"  # 보내는 사람 email 주소.
    recipientAddr = "s1y2s323@naver.com"  # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "Test email in Python 3.0"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    # htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(req.read(), 'html', _charset='UTF-8')
    # htmlFD.close()

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(HtmlPart)

    # 메일을 발송한다.
    s = mysmptlib.MySMTP(host, port)
    # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("ghkdtjdbs33@gmail.com", "1042ghkd")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

def initTopText():
    TempFont=font.Font(root,size=20,weight='bold',family='Consolas')
    MainText=Label(root,font=TempFont,text="[SCRIPT]")
    MainText.pack()
    MainText.place(x=20)

def inputDetail():
    global inputDetail
    TempFont = font.Font(root, size=15, weight='bold', family='Consolas')
    inputDetail = Entry(root, font=TempFont, width=15, borderwidth=12, relief='ridge')
    inputDetail.pack()
    inputDetail.place(x=10,y=110)

def inputSenderEmail():
    global send
    TempFont = font.Font(root, size=13, weight='bold', family='Consolas')
    send = Entry(root, font=TempFont, width=25, borderwidth=10, relief='ridge')
    send.pack()
    send.place(x=450,y=600)

def inputRecipicentEmail():
    global recipicent
    TempFont = font.Font(root, size=13, weight='bold', family='Consolas')
    recipicent = Entry(root, font=TempFont, width=25, borderwidth=10, relief='ridge')
    recipicent.pack()
    recipicent.place(x=450,y=650)

def initSearchlistBox():
    global SearchListBox,TypeListBox
    ListBoxScrollbar=Scrollbar(root)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150,y=50)

    ListBoxScrollbar2 = Scrollbar(root)
    ListBoxScrollbar2.pack()
    ListBoxScrollbar2.place(x=320, y=50)



    TempFont = font.Font(root, size=15, weight='bold', family='Consolas')
    SearchListBox.append(Listbox(root, font=TempFont, activestyle='none', width=10, height=1, borderwidth=12,
                               relief='ridge', yscrollcommand=ListBoxScrollbar.set))
    SearchListBox.append(Listbox(root, font=TempFont, activestyle='none', width=10, height=1, borderwidth=12,
                                 relief='ridge', yscrollcommand=ListBoxScrollbar2.set))
    # SearchListBox[0] = Listbox(root, font=TempFont,activestyle='none',width=10,height=1,borderwidth=12,
    #                        relief='ridge',yscrollcommand=ListBoxScrollbar.set)

    #SearchListBox[1] = Listbox(root, font=TempFont, activestyle='none', width=10, height=1, borderwidth=12,
   #                         relief='ridge', yscrollcommand=ListBoxScrollbar2.set)

    SearchListBox[0].insert(1, "강남구")
    SearchListBox[0].insert(2, "강동구")
    SearchListBox[0].insert(3, "강북구")
    SearchListBox[0].insert(4, "강서구")
    SearchListBox[0].insert(5, "관악구")
    SearchListBox[0].insert(6, "광진구")
    SearchListBox[0].insert(7, "구로구")
    SearchListBox[0].insert(8, "금천구")
    SearchListBox[0].insert(9, "노원구")
    SearchListBox[0].insert(10, "도봉구")
    SearchListBox[0].insert(11, "동대문구")
    SearchListBox[0].insert(12, "동작구")
    SearchListBox[0].insert(13, "마포구")
    SearchListBox[0].insert(14, "서대문구")
    SearchListBox[0].insert(15, "서초구")
    SearchListBox[0].insert(16, "성동구")
    SearchListBox[0].insert(17, "성북구")
    SearchListBox[0].insert(18, "송파구")
    SearchListBox[0].insert(19, "양천구")
    SearchListBox[0].insert(20, "영등포구")
    SearchListBox[0].insert(21, "용산구")
    SearchListBox[0].insert(22, "은평구")
    SearchListBox[0].insert(23, "종로구")
    SearchListBox[0].insert(24, "중구")
    SearchListBox[0].insert(25, "중랑구")

    SearchListBox[0].pack()
    SearchListBox[0].place(x=10,y=50)

    SearchListBox[1].insert(1, "관광지")  # 12
    SearchListBox[1].insert(2, "쇼핑")  # 38
    SearchListBox[1].insert(3, "음식")  # 39
    SearchListBox[1].pack()
    SearchListBox[1].place(x=180, y=50)


def initSearchButton1():
    TempFont=font.Font(root,size=12,weight='bold',family='Consolas')
    SearchButton=Button(root,font=TempFont,text="제목순",command=SearchButtonActionByText)
    SearchButton.pack()
    SearchButton.place(x=20,y=170)

def initSearchButton2():
    TempFont=font.Font(root,size=12,weight='bold',family='Consolas')
    SearchButton=Button(root,font=TempFont,text="인기순",command=SearchButtonActionByLike)
    SearchButton.pack()
    SearchButton.place(x=80,y=170)

def initSearchButton3():
    TempFont=font.Font(root,size=12,weight='bold',family='Consolas')
    SearchButton=Button(root,font=TempFont,text="수정일순",command=SearchButtonActionByRegister)
    SearchButton.pack()
    SearchButton.place(x=140,y=170)

def initSearchButton4():
    TempFont=font.Font(root,size=12,weight='bold',family='Consolas')
    SearchButton=Button(root,font=TempFont,text="등록순",command=SearchButtonActionByModify)
    SearchButton.pack()
    SearchButton.place(x=220,y=170)

def initEmailButton():
    TempFont=font.Font(root,size=12,weight='bold',family='Consolas')
    SearchButton=Button(root,font=TempFont,text="이메일",command=EmailAction)
    SearchButton.pack()
    SearchButton.place(x=720,y=630)


def initSearchDetailButton():
    TempFont=font.Font(root,size=12,weight='bold',family='Consolas')
    SearchButton=Button(root,font=TempFont,text="상세검색",command=SearchDetailButtonAction)
    SearchButton.pack()
    SearchButton.place(x=210,y=120)



def SearchDetailButtonAction():
    global DetailDataList,DetailRenderText
    DetailDataList.clear()
    DetailRenderText.configure(state='normal')
    DetailRenderText.delete(0.0, END)
   # print(inputDetail.get() )

    ID=str(inputDetail.get())
    getDetailDataFromID( ID )

    ShowDetailDataList()
    initImage(ID)
    DetailRenderText.configure(state='disabled')


def SearchButtonAction():
    global SearchListBox,SearchIndex,SearchIndex2,DataList,RenderText
    DataList.clear()
    RenderText.configure(state='normal')
    RenderText.delete(0.0,END)
    #getBookDataFromISBN('1','39')
    try:
        SearchIndex = SearchListBox[0].curselection()[0]+1
    except:
        SearchIndex2 = SearchListBox[1].curselection()[0]

    if SearchIndex2==0:
        SearchIndex2=12
    elif SearchIndex2==1:
        SearchIndex2=38
    elif SearchIndex2==2:
        SearchIndex2=39

    if SearchIndex and SearchIndex2 :
        getBookDataFromISBN(str(SearchIndex), str(SearchIndex2))
        ShowDataList()
      #  initImage()

   # print(str(SearchIndex))
    #print(SearchIndex2)
    RenderText.configure(state='disabled')

def SearchButtonActionByText():
    global SearchListBox,SearchIndex,SearchIndex2,DataList,RenderText
    DataList.clear()
    RenderText.configure(state='normal')
    RenderText.delete(0.0,END)
    #getBookDataFromISBN('1','39')
    try:
        SearchIndex = SearchListBox[0].curselection()[0]+1
    except:
        SearchIndex2 = SearchListBox[1].curselection()[0]

    if SearchIndex2==0:
        SearchIndex2=12
    elif SearchIndex2==1:
        SearchIndex2=38
    elif SearchIndex2==2:
        SearchIndex2=39

    if SearchIndex and SearchIndex2 :
        getDataFromlike(str(SearchIndex), str(SearchIndex2),"A")
        ShowDataList()

    RenderText.configure(state='disabled')

def SearchButtonActionByLike():
    global SearchListBox,SearchIndex,SearchIndex2,DataList,RenderText
    DataList.clear()
    RenderText.configure(state='normal')
    RenderText.delete(0.0,END)
    #getBookDataFromISBN('1','39')
    try:
        SearchIndex = SearchListBox[0].curselection()[0]+1
    except:
        SearchIndex2 = SearchListBox[1].curselection()[0]

    if SearchIndex2==0:
        SearchIndex2=12
    elif SearchIndex2==1:
        SearchIndex2=38
    elif SearchIndex2==2:
        SearchIndex2=39

    if SearchIndex and SearchIndex2 :
        getDataFromlike(str(SearchIndex), str(SearchIndex2),"B")
        ShowDataList()

    RenderText.configure(state='disabled')




def SearchButtonActionByRegister():
    global SearchListBox,SearchIndex,SearchIndex2,DataList,RenderText
    DataList.clear()
    RenderText.configure(state='normal')
    RenderText.delete(0.0,END)
    #getBookDataFromISBN('1','39')
    try:
        SearchIndex = SearchListBox[0].curselection()[0]+1
    except:
        SearchIndex2 = SearchListBox[1].curselection()[0]

    if SearchIndex2==0:
        SearchIndex2=12
    elif SearchIndex2==1:
        SearchIndex2=38
    elif SearchIndex2==2:
        SearchIndex2=39

    if SearchIndex and SearchIndex2 :
        getDataFromlike(str(SearchIndex), str(SearchIndex2),"C")
        ShowDataList()

    RenderText.configure(state='disabled')

def SearchButtonActionByModify():
    global SearchListBox,SearchIndex,SearchIndex2,DataList,RenderText
    DataList.clear()
    RenderText.configure(state='normal')
    RenderText.delete(0.0,END)
    #getBookDataFromISBN('1','39')
    try:
        SearchIndex = SearchListBox[0].curselection()[0]+1
    except:
        SearchIndex2 = SearchListBox[1].curselection()[0]

    if SearchIndex2==0:
        SearchIndex2=12
    elif SearchIndex2==1:
        SearchIndex2=38
    elif SearchIndex2==2:
        SearchIndex2=39

    if SearchIndex and SearchIndex2 :
        getDataFromlike(str(SearchIndex), str(SearchIndex2),"D")
        ShowDataList()

    RenderText.configure(state='disabled')

def ShowDataList():
    for i in range(len(DataList)):
       # RenderText.insert(INSERT,i+1)
        RenderText.insert(INSERT, "ID: ")  #
        RenderText.insert(INSERT, DataList[i][0])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "시설명: ")#
        RenderText.insert(INSERT, DataList[i][1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "전화번호: ")
        RenderText.insert(INSERT, DataList[i][2])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "주소: ")
        RenderText.insert(INSERT, DataList[i][3])
        RenderText.insert(INSERT, "\n\n")

def ShowDetailDataList():
    print("ShowDetail!")
   # print( DetailDataList[0])
    DetailRenderText.insert(INSERT, DetailDataList[0])
    DetailRenderText.insert(INSERT, "\n")


def initRenderText():
    global RenderText

    RenderTextScrollbar=Scrollbar(root)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375,y=200)

    TempFont=font.Font(root,size=10,family='Consolas')
    RenderText=Text(root,width=49,height=27,borderwidth=12,relief='ridge',
                    yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10,y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)

    RenderText.configure(state='disabled')

def initDetailRenderText():
    global DetailRenderText

    RenderTextScrollbar=Scrollbar(root)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=200,y=200)

    TempFont=font.Font(root,size=10,family='Consolas')
    DetailRenderText=Text(root,width=49,height=27,borderwidth=12,relief='ridge',
                    yscrollcommand=RenderTextScrollbar.set)
    DetailRenderText.pack()
    DetailRenderText.place(x=450,y=215)
    RenderTextScrollbar.config(command=DetailRenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)

    DetailRenderText.configure(state='disabled')










initTopText()
initSearchlistBox()
inputDetail()

initSearchButton1()
initSearchButton2()
initSearchButton3()
initSearchButton4()
initEmailButton()

initSearchDetailButton()
inputSenderEmail()
inputRecipicentEmail()



initRenderText()
initDetailRenderText()






root.mainloop()

