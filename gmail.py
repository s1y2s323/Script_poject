# -*- coding: cp949 -*-
import mimetypes
import mysmptlib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

server = "api.visitkorea.or.kr"
url="http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=nPSDIXgi3zg%2BhHUuuE6%2Fa3MirmFbhh%2BtwN1N8jRjCrs8dgXn8Wp3b9g190zHZGXqgo8DxqgcgK1fq2AjFXdJbg%3D%3D&areaCode=35&MobileOS=ETC&MobileApp=AppTesting"
#url="logo.html"
conn = HTTPConnection(server)
conn.request("GET", url)
req = conn.getresponse()

#global value
host = "smtp.gmail.com" # Gmail STMP ���� �ּ�.
port = "587"
htmlFileName = url

senderAddr = "ghkdtjdbs33@gmail.com"     # ������ ��� email �ּ�.
recipientAddr = "s1y2s323@naver.com"   # �޴� ��� email �ּ�.

msg = MIMEBase("multipart", "alternative")
msg['Subject'] = "Test email in Python 3.0"
msg['From'] = senderAddr
msg['To'] = recipientAddr

# MIME ������ �����մϴ�.
#htmlFD = open(htmlFileName, 'rb')
HtmlPart = MIMEText(req.read(),'html', _charset = 'UTF-8' )
#htmlFD.close()

# ������� mime�� MIMEBase�� ÷�� ��Ų��.
msg.attach(HtmlPart)

# ������ �߼��Ѵ�.
s = mysmptlib.MySMTP(host,port)
#s.set_debuglevel(1)        # ������� �ʿ��� ��� �ּ��� Ǭ��.
s.ehlo()
s.starttls()
s.ehlo()
s.login("ghkdtjdbs33@gmail.com","1042ghkd")
s.sendmail(senderAddr , [recipientAddr], msg.as_string())
s.close()

