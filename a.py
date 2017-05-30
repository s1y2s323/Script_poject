from internet import*
from tkinter import*
from tkinter import font
from io import BytesIO
import urllib
import urllib.request
from PIL import Image,ImageTk

import tkinter.messagebox


root=Tk()

root.geometry("1000x800+750+200")


SearchListBox=[]
RenderText=None
SearchIndex=None
SearchIndex2=None


#with urllib.request.urlopen(url) as u:
#    raw_data = u.read()
#im = Image.open(BytesIO(raw_data))
#image = ImageTk.PhotoImage(im)
def initImage():
    url = DataList[0][4]
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))

    image = ImageTk.PhotoImage(im)

    label=Label(root,image=image,height=400,width=400)
    label.pack()
    label.place(x=400,y=20)
    root.mainloop()


def initTopText():
    TempFont=font.Font(root,size=20,weight='bold',family='Consolas')
    MainText=Label(root,font=TempFont,text="[SCRIPT]")
    MainText.pack()
    MainText.place(x=20)

def initSearchlistBox():
    global SearchListBox,TypeListBox
    ListBoxScrollbar=Scrollbar(root)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150,y=50)

    ListBoxScrollbar2 = Scrollbar(root)
    ListBoxScrollbar2.pack()
    ListBoxScrollbar2.place(x=350, y=50)



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
    SearchListBox[1].place(x=200, y=50)


def initSearchButton():
    TempFont=font.Font(root,size=12,weight='bold',family='Consolas')
    SearchButton=Button(root,font=TempFont,text="검색",command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330,y=50)

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
    initImage()
    print(str(SearchIndex))
    print(SearchIndex2)
    RenderText.configure(state='disabled')

def ShowDataList():
    for i in range(len(DataList)):
        RenderText.insert(INSERT,i+1)
        RenderText.insert(INSERT, "시설명: ")#
        RenderText.insert(INSERT, DataList[i][1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "전화번호: ")
        RenderText.insert(INSERT, DataList[i][2])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "ID: ")
        RenderText.insert(INSERT, DataList[i][3])
        RenderText.insert(INSERT, "\n\n")





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










initTopText()
initSearchlistBox()

initSearchButton()
initRenderText()




root.mainloop()

