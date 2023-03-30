from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
 
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 










@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                sendString = ""
                phz=0
                ppole=0
                pkw=0
                php=0
                prpm=0
                IE1=0.0
                IE2=0.0
                IE3=0.0
                IE4=0.0
                text1=event.message.text.lower()
                print(text1)
                #重置區
                if "重置" in event.message.text or "馬達效率轉換" in event.message.text:
                    sendString = "請輸入\n\n頻率(Hz):\n級數(pole):\n功率(Kw):\n馬力(Hp):\n轉速(rpm):"
                
                #判斷區
#HZ
                if "50hz" in text1:
                    phz = 50
                
                if "60hz" in text1:
                    phz = 60
                    


#級數
                if "2pole" in text1:
                    ppole = 2

                if "4pole" in text1:
                    ppole = 4

                if "6pole" in text1:
                    ppole = 6



#功率
                

                if "1.1kw" in text1:
                    pkw = 1.1

                if "1.5kw" in text1:
                    pkw = 1.5

                if "2.2kw" in text1:
                    pkw = 2.2

                if "3kw" in text1:
                    pkw = 3.0

                if "3.7kw" in text1:
                    pkw = 3.7

                if "4kw" in text1:
                    pkw = 4.0

                if "5.5kw" in text1:
                    pkw = 5.5

                if "7.5kw" in text1:
                    pkw = 7.5

                if "11kw" in text1:
                    pkw = 11.0

                if "15kw" in text1:
                    pkw = 15.0

                if "18.5kw" in text1:
                    pkw = 18.5

                if "22kw" in text1:
                    pkw = 22.0

                if "30kw" in text1:
                    pkw = 30.0

                if "37kw" in text1:
                    pkw = 37.0

                if "45kw" in text1:
                    pkw = 45.0

                if "55kw" in text1:
                    pkw = 55.0

                if "75kw" in text1:
                    pkw = 75.0

                if "90kw" in text1:
                    pkw = 90.0

                if "110kw" in text1:
                    pkw = 110.0

                if "132kw" in text1:
                    pkw = 132.0

                if "150kw" in text1:
                    pkw = 150.0

                if "160kw" in text1:
                    pkw = 160.0

                if "185kw" in text1:
                    pkw = 185.0

                if "200kw" in text1:
                    pkw = 200.0

                if "220kw" in text1:
                    pkw = 220.0

                if "250kw" in text1:
                    pkw = 250.0

                if "300kw" in text1:
                    pkw = 300.0

                if "330kw" in text1:
                    pkw = 330.0

                if "375kw" in text1:
                    pkw = 375.0

                if "0.75kw" in text1:
                    pkw = 0.75




#馬力
                if "1hp" in text1:
                    php = 1

                if "1.5hp" in text1:
                    php = 1.5

                if "2hp" in text1:
                    php = 2

                if "3hp" in text1:
                    php = 3

                if "5hp" in text1:
                    php = 5

                if "7.5hp" in text1:
                    php = 7.5

                if "10hp" in text1:
                    php = 10

                if "15hp" in text1:
                    php = 15

                if "20hp" in text1:
                    php = 20

                if "25hp" in text1:
                    php = 25

                if "30hp" in text1:
                    php = 30

                if "40hp" in text1:
                    php = 40

                if "50hp" in text1:
                    php = 50

                if "60hp" in text1:
                    php = 60

                if "75hp" in text1:
                    php = 75

                if "100hp" in text1:
                    php = 100

                if "125hp" in text1:
                    php = 125

                if "150hp" in text1:
                    php = 150

                if "200hp" in text1:
                    php = 200

                if "250hp" in text1:
                    php = 250

                if "300hp" in text1:
                    php = 300

                if "350hp" in text1:
                    php = 350

                if "400hp" in text1:
                    php = 400

                if "450hp" in text1:
                    php = 450

                if "500hp" in text1:
                    php = 500
                    


#同步轉速
                if "3000rpm" in text1:
                    prpm = 3000

                if "1500rpm" in text1:
                    prpm = 1500

                if "1000rpm" in text1:
                    prpm = 1000

                if "3600rpm" in text1:
                    prpm = 3600

                if "1800rpm" in text1:
                    prpm = 1800

                if "1200rpm" in text1:
                    prpm = 1200



                print(phz)
                print(pkw)
                print(prpm)



#是否有缺值
                if phz==0:
                    reply1=0
                if ppole==0 and prpm==0:
                    reply2=0
                if pkw==0 and php==0:
                    reply3=0
                
                if phz>0:
                    reply1=1
                if ppole>0 or prpm>0:
                    reply2=1
                if pkw>0 or php>0:
                    reply3=1 
                
                if reply1==0 and reply2==0 and reply3==0:
                    sendString="缺少條件如下:\n\n頻率(Hz)、\n級數(pole)或轉速(rpm)、\n功率(Kw)或馬力(Hp)"

                if reply1==1 and reply2==0 and reply3==0:
                    sendString="缺少條件如下:\n\n級數(pole)或轉速(rpm)、\n功率(Kw)或馬力(Hp)"

                if reply1==0 and reply2==1 and reply3==0:
                    sendString="缺少條件如下:\n\n頻率(Hz)、\n功率(Kw)或馬力(Hp)"

                if reply1==1 and reply2==1 and reply3==0:
                    sendString="缺少條件如下:\n\n功率(Kw)或馬力(Hp)"

                if reply1==0 and reply2==0 and reply3==1:
                    sendString="缺少條件如下:\n\n頻率(Hz)、\n級數(pole)或轉速(rpm)"

                if reply1==1 and reply2==0 and reply3==1:
                    sendString="缺少條件如下:\n\n級數(pole)或轉速(rpm)"

                if reply1==0 and reply2==1 and reply3==1:
                    sendString="缺少條件如下:\n\n頻率(Hz)"


#有值
                if reply1==1 and reply2==1 and reply3==1:
                    
                    
                    if phz==50:
                        if pkw==0.75 or php==1:
                            pkw=0.75
                            if ppole==2 or prpm==3000:
                                IE1=72.1
                                IE2=77.4
                                IE3=80.7
                                IE4=83.5
                            if ppole==4 or prpm==1500:
                                IE1=72.1
                                IE2=79.6
                                IE3=82.5
                                IE4=85.7
                            if ppole==6 or prpm==1000:
                                IE1=70.0
                                IE2=75.9
                                IE3=78.9
                                IE4=82.7

                        if pkw==1.1 or php==1.5:
                            pkw=1.1
                            if ppole==2 or prpm==3000:
                                IE1=75.0
                                IE2=79.6
                                IE3=82.7
                                IE4=85.2
                            if ppole==4 or prpm==1500:
                                IE1=75.0
                                IE2=81.4
                                IE3=84.1
                                IE4=87.2
                            if ppole==6 or prpm==1000:
                                IE1=72.9
                                IE2=78.1
                                IE3=81.0
                                IE4=84.5

                        if pkw==1.5 or php==2:
                            pkw=1.5
                            if ppole==2 or prpm==3000:
                                IE1=77.2
                                IE2=81.3
                                IE3=84.2
                                IE4=86.5
                            if ppole==4 or prpm==1500:
                                IE1=77.2
                                IE2=82.8
                                IE3=85.3
                                IE4=88.2
                            if ppole==6 or prpm==1000:
                                IE1=75.2
                                IE2=79.8
                                IE3=82.5
                                IE4=85.9

                        if pkw==2.2 or php==3:
                            pkw=2.2
                            if ppole==2 or prpm==3000:
                                IE1=79.7
                                IE2=73.2
                                IE3=85.9
                                IE4=88.0
                            if ppole==4 or prpm==1500:
                                IE1=79.7
                                IE2=84.3
                                IE3=86.7
                                IE4=89.5
                            if ppole==6 or prpm==1000:
                                IE1=77.7
                                IE2=81.8
                                IE3=84.3
                                IE4=87.4

                        if pkw==3.0:
                            pkw=3.0
                            if ppole==2 or prpm==3000:
                                IE1=81.5
                                IE2=84.6
                                IE3=87.1
                                IE4=89.1
                            if ppole==4 or prpm==1500:
                                IE1=81.5
                                IE2=85.5
                                IE3=87.7
                                IE4=90.4
                            if ppole==6 or prpm==1000:
                                IE1=79.7
                                IE2=83.3
                                IE3=85.6
                                IE4=88.6

                        if pkw==3.7 or php==5:
                            pkw=3.7
                            if ppole==2 or prpm==3000:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==4 or prpm==1500:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==6 or prpm==1000:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0

                        if pkw==4.0:
                            pkw=4.0
                            if ppole==2 or prpm==3000:
                                IE1=83.1
                                IE2=85.8
                                IE3=88.1
                                IE4=90.0
                            if ppole==4 or prpm==1500:
                                IE1=83.1
                                IE2=86.6
                                IE3=88.6
                                IE4=91.1
                            if ppole==6 or prpm==1000:
                                IE1=81.4
                                IE2=84.6
                                IE3=86.8
                                IE4=89.5

                        if pkw==5.5 or php==7.5:
                            pkw=5.5
                            if ppole==2 or prpm==3000:
                                IE1=84.7
                                IE2=87.0
                                IE3=89.2
                                IE4=90.9
                            if ppole==4 or prpm==1500:
                                IE1=84.7
                                IE2=87.7
                                IE3=89.6
                                IE4=91.9
                            if ppole==6 or prpm==1000:
                                IE1=83.1
                                IE2=86.0
                                IE3=88.0
                                IE4=90.5

                        if pkw==7.5 or php==10:
                            pkw=7.5
                            if ppole==2 or prpm==3000:
                                IE1=86.0
                                IE2=88.1
                                IE3=90.1
                                IE4=91.7
                            if ppole==4 or prpm==1500:
                                IE1=86.0
                                IE2=88.7
                                IE3=90.4
                                IE4=92.6
                            if ppole==6 or prpm==1000:
                                IE1=84.7
                                IE2=87.2
                                IE3=89.1
                                IE4=91.3

                        if pkw==11.0 or php==15:
                            pkw=11.0
                            if ppole==2 or prpm==3000:
                                IE1=87.6
                                IE2=89.4
                                IE3=91.2
                                IE4=92.6
                            if ppole==4 or prpm==1500:
                                IE1=87.6
                                IE2=89.8
                                IE3=91.4
                                IE4=93.3
                            if ppole==6 or prpm==1000:
                                IE1=86.4
                                IE2=88.7
                                IE3=90.3
                                IE4=92.3

                        if pkw==15.0 or php==20:
                            pkw=15.0
                            if ppole==2 or prpm==3000:
                                IE1=88.7
                                IE2=90.3
                                IE3=91.9
                                IE4=93.3
                            if ppole==4 or prpm==1500:
                                IE1=88.7
                                IE2=90.6
                                IE3=92.1
                                IE4=93.9
                            if ppole==6 or prpm==1000:
                                IE1=87.7
                                IE2=89.7
                                IE3=91.2
                                IE4=92.9

                        if pkw==18.5 or php==25:
                            pkw=18.5
                            if ppole==2 or prpm==3000:
                                IE1=89.3
                                IE2=90.9
                                IE3=92.4
                                IE4=93.7
                            if ppole==4 or prpm==1500:
                                IE1=89.3
                                IE2=91.2
                                IE3=92.6
                                IE4=94.2
                            if ppole==6 or prpm==1000:
                                IE1=88.6
                                IE2=90.4
                                IE3=91.7
                                IE4=93.4

                        if pkw==22.0 or php==30:
                            pkw=22.0
                            if ppole==2 or prpm==3000:
                                IE1=89.9
                                IE2=91.3
                                IE3=92.7
                                IE4=94.0
                            if ppole==4 or prpm==1500:
                                IE1=89.9
                                IE2=91.6
                                IE3=93.0
                                IE4=94.5
                            if ppole==6 or prpm==1000:
                                IE1=89.2
                                IE2=90.9
                                IE3=92.2
                                IE4=93.7

                        if pkw==30.0 or php==40:
                            pkw=30.0
                            if ppole==2 or prpm==3000:
                                IE1=90.7
                                IE2=92.0
                                IE3=93.3
                                IE4=94.5
                            if ppole==4 or prpm==1500:
                                IE1=90.7
                                IE2=92.3
                                IE3=93.6
                                IE4=94.9
                            if ppole==6 or prpm==1000:
                                IE1=90.2
                                IE2=91.7
                                IE3=92.9
                                IE4=94.2

                        if pkw==37.0 or php==50:
                            pkw=37.0
                            if ppole==2 or prpm==3000:
                                IE1=91.2
                                IE2=92.5
                                IE3=93.7
                                IE4=94.8
                            if ppole==4 or prpm==1500:
                                IE1=91.2
                                IE2=92.7
                                IE3=93.9
                                IE4=95.2
                            if ppole==6 or prpm==1000:
                                IE1=90.8
                                IE2=92.2
                                IE3=93.3
                                IE4=94.5

                        if pkw==45.0 or php==60:
                            pkw=45.0
                            if ppole==2 or prpm==3000:
                                IE1=91.7
                                IE2=92.9
                                IE3=94.0
                                IE4=95.0
                            if ppole==4 or prpm==1500:
                                IE1=91.7
                                IE2=93.1
                                IE3=94.2
                                IE4=95.4
                            if ppole==6 or prpm==1000:
                                IE1=91.4
                                IE2=92.7
                                IE3=93.7
                                IE4=94.8

                        if pkw==55.0 or php==75:
                            pkw=55.0
                            if ppole==2 or prpm==3000:
                                IE1=92.1
                                IE2=93.2
                                IE3=94.3
                                IE4=95.3
                            if ppole==4 or prpm==1500:
                                IE1=92.1
                                IE2=93.5
                                IE3=94.6
                                IE4=95.7
                            if ppole==6 or prpm==1000:
                                IE1=91.9
                                IE2=93.1
                                IE3=94.1
                                IE4=95.1

                        if pkw==75.0 or php==100:
                            pkw=75.0
                            if ppole==2 or prpm==3000:
                                IE1=92.7
                                IE2=93.8
                                IE3=94.7
                                IE4=95.6
                            if ppole==4 or prpm==1500:
                                IE1=92.7
                                IE2=94.0
                                IE3=95.0
                                IE4=96.0
                            if ppole==6 or prpm==1000:
                                IE1=92.6
                                IE2=93.7
                                IE3=94.6
                                IE4=95.4

                        if pkw==90.0 or php==125:
                            pkw=90.0
                            if ppole==2 or prpm==3000:
                                IE1=93.0
                                IE2=94.1
                                IE3=95.0
                                IE4=95.8
                            if ppole==4 or prpm==1500:
                                IE1=93.0
                                IE2=94.2
                                IE3=95.2
                                IE4=96.1
                            if ppole==6 or prpm==1000:
                                IE1=92.9
                                IE2=94.0
                                IE3=94.9
                                IE4=95.6

                        if pkw==110.0 or php==150:
                            pkw=110.0
                            if ppole==2 or prpm==3000:
                                IE1=93.3
                                IE2=94.3
                                IE3=95.2
                                IE4=96.0
                            if ppole==4 or prpm==1500:
                                IE1=93.3
                                IE2=94.5
                                IE3=95.4
                                IE4=96.3
                            if ppole==6 or prpm==1000:
                                IE1=93.3
                                IE2=94.3
                                IE3=95.1
                                IE4=95.8

                        if pkw==132.0:
                            pkw=132.0
                            if ppole==2 or prpm==3000:
                                IE1=93.5
                                IE2=94.6
                                IE3=95.4
                                IE4=96.2
                            if ppole==4 or prpm==1500:
                                IE1=93.5
                                IE2=94.7
                                IE3=95.6
                                IE4=96.4
                            if ppole==6 or prpm==1000:
                                IE1=93.5
                                IE2=94.6
                                IE3=95.4
                                IE4=96.0

                        if pkw==150.0 or php==200:
                            pkw=150.0
                            if ppole==2 or prpm==3000:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==4 or prpm==1500:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==6 or prpm==1000:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0

                        if pkw==160.0:
                            pkw=160.0
                            if ppole==2 or prpm==3000:
                                IE1=93.8
                                IE2=94.8
                                IE3=95.6
                                IE4=96.3
                            if ppole==4 or prpm==1500:
                                IE1=93.8
                                IE2=94.9
                                IE3=95.8
                                IE4=96.6
                            if ppole==6 or prpm==1000:
                                IE1=93.8
                                IE2=94.8
                                IE3=95.6
                                IE4=96.2

                        if pkw==185.0 or php==250:
                            pkw=185.0
                            if ppole==2 or prpm==3000:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==4 or prpm==1500:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==6 or prpm==1000:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0

                        if pkw==200.0:
                            pkw=200.0
                            if ppole==2 or prpm==3000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5
                            if ppole==4 or prpm==1500:
                                IE1=94.0
                                IE2=95.1
                                IE3=96.0
                                IE4=96.7
                            if ppole==6 or prpm==1000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.3

                        if pkw==220.0 or php==300:
                            pkw=220.0
                            if ppole==2 or prpm==3000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5
                            if ppole==4 or prpm==1500:
                                IE1=94.0
                                IE2=95.1
                                IE3=96.0
                                IE4=96.7
                            if ppole==6 or prpm==1000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.3

                        if pkw==250.0 or php==350:
                            pkw=250.0
                            if ppole==2 or prpm==3000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5
                            if ppole==4 or prpm==1500:
                                IE1=94.0
                                IE2=95.1
                                IE3=96.0
                                IE4=96.7
                            if ppole==6 or prpm==1000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5

                        if pkw==300.0 or php==400:
                            pkw=300.0
                            if ppole==2 or prpm==3000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5
                            if ppole==4 or prpm==1500:
                                IE1=94.0
                                IE2=95.1
                                IE3=96.0
                                IE4=96.7
                            if ppole==6 or prpm==1000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.6

                        if pkw==330.0 or php==450:
                            pkw=220.0
                            if ppole==2 or prpm==3000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5
                            if ppole==4 or prpm==1500:
                                IE1=94.0
                                IE2=95.1
                                IE3=96.0
                                IE4=96.7
                            if ppole==6 or prpm==1000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.6

                        if pkw==375.0 or php==500:
                            pkw=375.0
                            if ppole==2 or prpm==3000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5
                            if ppole==4 or prpm==1500:
                                IE1=94.0
                                IE2=95.1
                                IE3=96.0
                                IE4=96.7
                            if ppole==6 or prpm==1000:
                                IE1=94.0
                                IE2=95.0
                                IE3=95.8
                                IE4=96.6



#60HZ
                    if phz==60:
                        if pkw==0.75 or php==1:
                            pkw=0.75
                            if ppole==2 or prpm==3600:
                                IE1=74.0
                                IE2=75.5
                                IE3=77.0
                                IE4=82.5
                            if ppole==4 or prpm==1800:
                                IE1=78.0
                                IE2=82.5
                                IE3=85.5
                                IE4=85.5
                            if ppole==6 or prpm==1200:
                                IE1=73.0
                                IE2=80.0
                                IE3=82.5
                                IE4=84.0

                        if pkw==1.1 or php==1.5:
                            pkw=1.1
                            if ppole==2 or prpm==30600:
                                IE1=78.5
                                IE2=82.5
                                IE3=84.0
                                IE4=85.5
                            if ppole==4 or prpm==1800:
                                IE1=79.0
                                IE2=84.0
                                IE3=86.5
                                IE4=87.5
                            if ppole==6 or prpm==1200:
                                IE1=75.0
                                IE2=85.5
                                IE3=87.5
                                IE4=88.5

                        if pkw==1.5 or php==2:
                            pkw=1.5
                            if ppole==2 or prpm==3600:
                                IE1=81.0
                                IE2=84.0
                                IE3=85.5
                                IE4=86.5
                            if ppole==4 or prpm==1800:
                                IE1=81.5
                                IE2=84.0
                                IE3=86.5
                                IE4=88.5
                            if ppole==6 or prpm==1200:
                                IE1=77.0
                                IE2=86.5
                                IE3=88.5
                                IE4=89.5

                        if pkw==2.2 or php==3:
                            pkw=2.2
                            if ppole==2 or prpm==3600:
                                IE1=81.5
                                IE2=85.5
                                IE3=86.5
                                IE4=88.5
                            if ppole==4 or prpm==1800:
                                IE1=83.0
                                IE2=87.5
                                IE3=89.5
                                IE4=91.0
                            if ppole==6 or prpm==1200:
                                IE1=78.5
                                IE2=87.5
                                IE3=89.5
                                IE4=90.2

                        if pkw==3.0:
                            pkw=3.0
                            if ppole==2 or prpm==3600:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==4 or prpm==1800:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==6 or prpm==1200:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0

                        if pkw==3.7 or php==5:
                            pkw=3.7
                            if ppole==2 or prpm==3600:
                                IE1=84.5
                                IE2=87.5
                                IE3=88.5
                                IE4=89.5
                            if ppole==4 or prpm==1800:
                                IE1=85.0
                                IE2=87.5
                                IE3=89.5
                                IE4=91.0
                            if ppole==6 or prpm==1200:
                                IE1=83.5
                                IE2=87.5
                                IE3=89.5
                                IE4=90.2

                        if pkw==4.0:
                            pkw=4.0
                            if ppole==2 or prpm==3600:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==4 or prpm==1800:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==6 or prpm==1200:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0

                        if pkw==5.5 or php==7.5:
                            pkw=5.5
                            if ppole==2 or prpm==3600:
                                IE1=86.0
                                IE2=88.5
                                IE3=89.5
                                IE4=90.2
                            if ppole==4 or prpm==1800:
                                IE1=87.0
                                IE2=89.5
                                IE3=91.7
                                IE4=92.4
                            if ppole==6 or prpm==1200:
                                IE1=85.0
                                IE2=89.5
                                IE3=91.0
                                IE4=91.7

                        if pkw==7.5 or php==10:
                            pkw=7.5
                            if ppole==2 or prpm==3600:
                                IE1=87.5
                                IE2=89.5
                                IE3=90.2
                                IE4=91.7
                            if ppole==4 or prpm==1800:
                                IE1=87.5
                                IE2=89.5
                                IE3=91.7
                                IE4=92.4
                            if ppole==6 or prpm==1200:
                                IE1=86.0
                                IE2=89.5
                                IE3=91.0
                                IE4=92.4

                        if pkw==11.0 or php==15:
                            pkw=11.0
                            if ppole==2 or prpm==3600:
                                IE1=87.5
                                IE2=90.2
                                IE3=91.0
                                IE4=92.4
                            if ppole==4 or prpm==1800:
                                IE1=88.5
                                IE2=91.0
                                IE3=92.4
                                IE4=93.6
                            if ppole==6 or prpm==1200:
                                IE1=89.0
                                IE2=90.2
                                IE3=91.7
                                IE4=93.0

                        if pkw==15.0 or php==20:
                            pkw=15.0
                            if ppole==2 or prpm==3600:
                                IE1=88.5
                                IE2=90.2
                                IE3=91.0
                                IE4=92.4
                            if ppole==4 or prpm==1800:
                                IE1=89.5
                                IE2=91.0
                                IE3=93.0
                                IE4=94.1
                            if ppole==6 or prpm==1200:
                                IE1=89.5
                                IE2=90.2
                                IE3=91.7
                                IE4=93.0

                        if pkw==18.5 or php==25:
                            pkw=18.5
                            if ppole==2 or prpm==3600:
                                IE1=89.5
                                IE2=91.0
                                IE3=91.7
                                IE4=93.0
                            if ppole==4 or prpm==1800:
                                IE1=90.5
                                IE2=92.4
                                IE3=93.6
                                IE4=94.5
                            if ppole==6 or prpm==1200:
                                IE1=90.2
                                IE2=91.7
                                IE3=93.0
                                IE4=94.1

                        if pkw==22.0 or php==30:
                            pkw=22.0
                            if ppole==2 or prpm==3600:
                                IE1=89.5
                                IE2=91.0
                                IE3=91.7
                                IE4=93.0
                            if ppole==4 or prpm==1800:
                                IE1=91.0
                                IE2=92.4
                                IE3=93.6
                                IE4=94.5
                            if ppole==6 or prpm==1200:
                                IE1=91.0
                                IE2=91.7
                                IE3=93.0
                                IE4=94.1

                        if pkw==30.0 or php==40:
                            pkw=30.0
                            if ppole==2 or prpm==3600:
                                IE1=90.2
                                IE2=91.7
                                IE3=92.4
                                IE4=93.6
                            if ppole==4 or prpm==1800:
                                IE1=91.7
                                IE2=93.0
                                IE3=94.1
                                IE4=95.0
                            if ppole==6 or prpm==1200:
                                IE1=91.7
                                IE2=93.0
                                IE3=94.1
                                IE4=95.0

                        if pkw==37.0 or php==50:
                            pkw=37.0
                            if ppole==2 or prpm==3600:
                                IE1=91.5
                                IE2=92.4
                                IE3=93.0
                                IE4=94.1
                            if ppole==4 or prpm==1800:
                                IE1=92.4
                                IE2=93.0
                                IE3=94.5
                                IE4=95.4
                            if ppole==6 or prpm==1200:
                                IE1=91.7
                                IE2=93.0
                                IE3=94.1
                                IE4=95.0

                        if pkw==45.0 or php==60:
                            pkw=45.0
                            if ppole==2 or prpm==3600:
                                IE1=91.7
                                IE2=93.0
                                IE3=93.6
                                IE4=94.5
                            if ppole==4 or prpm==1800:
                                IE1=93.0
                                IE2=93.6
                                IE3=95.0
                                IE4=95.4
                            if ppole==6 or prpm==1200:
                                IE1=91.7
                                IE2=93.6
                                IE3=94.5
                                IE4=95.4

                        if pkw==55.0 or php==75:
                            pkw=55.0
                            if ppole==2 or prpm==6000:
                                IE1=92.4
                                IE2=93.0
                                IE3=93.6
                                IE4=94.5
                            if ppole==4 or prpm==1800:
                                IE1=93.0
                                IE2=94.1
                                IE3=95.4
                                IE4=95.8
                            if ppole==6 or prpm==1200:
                                IE1=92.1
                                IE2=93.6
                                IE3=94.5
                                IE4=95.4

                        if pkw==75.0 or php==100:
                            pkw=75.0
                            if ppole==2 or prpm==3600:
                                IE1=93.0
                                IE2=93.6
                                IE3=94.1
                                IE4=95.0
                            if ppole==4 or prpm==1800:
                                IE1=93.2
                                IE2=94.5
                                IE3=95.4
                                IE4=96.2
                            if ppole==6 or prpm==1200:
                                IE1=93.0
                                IE2=94.1
                                IE3=95.0
                                IE4=95.8

                        if pkw==90.0 or php==125:
                            pkw=90.0
                            if ppole==2 or prpm==3600:
                                IE1=93.0
                                IE2=94.5
                                IE3=95.0
                                IE4=95.4
                            if ppole==4 or prpm==1800:
                                IE1=93.2
                                IE2=94.5
                                IE3=95.4
                                IE4=96.2
                            if ppole==6 or prpm==1200:
                                IE1=93.0
                                IE2=94.1
                                IE3=95.0
                                IE4=95.8

                        if pkw==110.0 or php==150:
                            pkw=110.0
                            if ppole==2 or prpm==3600:
                                IE1=93.0
                                IE2=94.5
                                IE3=95.0
                                IE4=95.4
                            if ppole==4 or prpm==1800:
                                IE1=93.5
                                IE2=95.0
                                IE3=95.8
                                IE4=96.2
                            if ppole==6 or prpm==1200:
                                IE1=94.1
                                IE2=95.0
                                IE3=95.8
                                IE4=96.2

                        if pkw==132.0:
                            pkw=132.0
                            if ppole==2 or prpm==3600:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==4 or prpm==1800:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==6 or prpm==1200:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0

                        if pkw==150.0 or php==200:
                            pkw=150.0
                            if ppole==2 or prpm==3600:
                                IE1=94.1
                                IE2=95.0
                                IE3=95.4
                                IE4=95.8
                            if ppole==4 or prpm==1800:
                                IE1=94.5
                                IE2=95.0
                                IE3=96.2
                                IE4=96.5
                            if ppole==6 or prpm==1200:
                                IE1=94.1
                                IE2=95.0
                                IE3=95.8
                                IE4=96.2

                        if pkw==160.0:
                            pkw=160.0
                            if ppole==2 or prpm==3600:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==4 or prpm==1800:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==6 or prpm==1200:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0

                        if pkw==185.0 or php==250:
                            pkw=185.0
                            if ppole==2 or prpm==3600:
                                IE1=94.1
                                IE2=95.4
                                IE3=95.8
                                IE4=96.2
                            if ppole==4 or prpm==1800:
                                IE1=94.5
                                IE2=95.4
                                IE3=96.2
                                IE4=96.5
                            if ppole==6 or prpm==1200:
                                IE1=94.1
                                IE2=95.0
                                IE3=95.8
                                IE4=96.2

                        if pkw==200.0:
                            pkw=200.0
                            if ppole==2 or prpm==3600:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==4 or prpm==1800:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0
                            if ppole==6 or prpm==1200:
                                IE1=0.0
                                IE2=0.0
                                IE3=0.0
                                IE4=0.0

                        if pkw==220.0 or php==300:
                            pkw=220.0
                            if ppole==2 or prpm==3600:
                                IE1=94.1
                                IE2=95.4
                                IE3=95.8
                                IE4=96.2
                            if ppole==4 or prpm==1800:
                                IE1=94.5
                                IE2=95.4
                                IE3=96.2
                                IE4=96.8
                            if ppole==6 or prpm==1200:
                                IE1=94.1
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5

                        if pkw==250.0 or php==350:
                            pkw=250.0
                            if ppole==2 or prpm==3600:
                                IE1=94.1
                                IE2=95.4
                                IE3=95.8
                                IE4=96.2
                            if ppole==4 or prpm==1800:
                                IE1=94.5
                                IE2=95.4
                                IE3=96.2
                                IE4=96.8
                            if ppole==6 or prpm==1200:
                                IE1=94.1
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5

                        if pkw==300.0 or php==400:
                            pkw=300.0
                            if ppole==2 or prpm==3600:
                                IE1=94.1
                                IE2=95.4
                                IE3=95.8
                                IE4=96.2
                            if ppole==4 or prpm==1800:
                                IE1=94.5
                                IE2=95.4
                                IE3=96.2
                                IE4=96.8
                            if ppole==6 or prpm==1200:
                                IE1=94.1
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5

                        if pkw==330.0 or php==450:
                            pkw=220.0
                            if ppole==2 or prpm==3600:
                                IE1=94.1
                                IE2=95.4
                                IE3=95.8
                                IE4=96.2
                            if ppole==4 or prpm==1800:
                                IE1=94.5
                                IE2=95.4
                                IE3=96.2
                                IE4=96.8
                            if ppole==6 or prpm==1200:
                                IE1=94.1
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5

                        if pkw==375.0 or php==500:
                            pkw=375.0
                            if ppole==2 or prpm==3600:
                                IE1=94.1
                                IE2=95.4
                                IE3=95.8
                                IE4=96.2
                            if ppole==4 or prpm==1800:
                                IE1=94.5
                                IE2=95.4
                                IE3=96.2
                                IE4=96.8
                            if ppole==6 or prpm==1200:
                                IE1=94.1
                                IE2=95.0
                                IE3=95.8
                                IE4=96.5





                    IE11=pkw*4380*3*IE1/100
                    IE12=pkw*4380*3*IE2/100
                    IE13=pkw*4380*3*IE3/100
                    IE14=pkw*4380*3*IE4/100
                    sendString='此馬達額定效率為:\n\nIE1:'+str(IE1)+'%\nIE2:'+str(IE2)+'%\nIE3:'+str(IE3)+'%\nIE4:'+str(IE4)+'%\n\n以馬達全載狀態每年365天，每天12小時，共4380小時，每度3元做電費計算:\n\nIE1:'+str(IE11)+'元\nIE2:'+str(IE12)+'元\nIE3:'+str(IE13)+'元\nIE4:'+str(IE14)+'元'





                
#都不是
                if sendString=='':
                    sendString = event.message.text 











                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(text=sendString)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
