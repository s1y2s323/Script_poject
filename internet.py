from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import urllib
import urllib.request



server = "api.visitkorea.or.kr"
regKey='nPSDIXgi3zg%2BhHUuuE6%2Fa3MirmFbhh%2BtwN1N8jRjCrs8dgXn8Wp3b9g190zHZGXqgo8DxqgcgK1fq2AjFXdJbg%3D%3D'
DataList=[]
conn = None

host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
port = "587"


def userURIBuilder(server, **user):
    str = "http://" + server + "/openapi" + "/service" +"/rest"+"/KorService"+"/areaBasedList?"

    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str


def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

#areaCode=1&numOfRows=20&pageNo=1&
def getBookDataFromISBN(sigungu,contentid):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()

    uri = userURIBuilder(server, ServiceKey=regKey,areaCode="1",sigunguCode=sigungu,numOfRows="500",  MobileOS="ETC", MobileApp="AppTesting")
    conn.request("GET", uri)
#http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey="서비스키"
    # &contentTypeid=39&areaCode=1&sigunguCode=4&numOfRows=50&MobileOS=ETC&MobileApp=AppTesting
    req = conn.getresponse()

   # print(req.status)
    if int(req.status) == 200:
        print("Book data downloading complete!")
        return extractBookData(req.read(),contentid)
    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def extractBookData(strXml,contentid):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    print(itemElements)
    for item in itemElements:
        content=item.find("contenttypeid")
       # print(content.text)
        #print(contentid)
       # title = item.find("title")
       # DataList.append(title.text)

        if str(content.text)==contentid:
            id=item.find("contentid")
            title = item.find("title")
            tel = item.find("tel")
            addr1 = item.find("addr1")
            image=item.find("firstimage")

            try:
               DataList.append((id.text, title.text, tel.text, addr1.text, image.text))
            except:
                try:
                    DataList.append((id.text, title.text, " ", addr1.text, image.text))
                except:
                    try:
                        DataList.append((id.text, title.text, tel.text, addr1.text, " "))
                    except:
                        DataList.append((id.text, title.text, " ", addr1.text, " "))

def sendMain():
    global host, port
    html = ""
    title = str(input('Title :'))
    senderAddr = str(input('sender email address :'))
    recipientAddr = str(input('recipient email address :'))
    msgtext = str(input('write message :'))
    passwd = str(input(' input your password of gmail account :'))
    msgtext = str(input('Do you want to include book data (y/n):'))
    if msgtext == 'y':
        keyword = str(input('input keyword to search:'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))

    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse
        import sys

        parts = urlparse(self.path)
        keyword, value = parts.query.split('=', 1)

        if keyword == "title":
            html = MakeHtmlDoc(SearchBookTitle(value))  # keyword에 해당하는 책을 검색해서 HTML로 전환합니다.
            ##헤더 부분을 작성.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))  # 본분( body ) 부분을 출력 합니다.
        else:
            self.send_error(400, ' bad requst : please check the your url')  # 잘 못된 요청라는 에러를 응답한다.


def startWebService():
    try:
        server = HTTPServer(('localhost', 8080), MyHandler)
        print("started http server....")
        server.serve_forever()

    except KeyboardInterrupt:
        print("shutdown web server")
        server.socket.close()  # server 종료합니다.


def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True

