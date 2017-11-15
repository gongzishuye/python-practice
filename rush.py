import requests
import threading

main_url='http://www.ziroom.com/z/vr/307568.html'   #target url
#main_url='http://www.ziroom.com/z/vr/60818127.html'  #test url

def send_text_msg():
    print("sending text message...")

def listending():
    UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36"

    headers = {"User-Agent": UA,
              "Referer": "http://www.v2ex.com/signin"}

    resp = requests.get(main_url, headers = headers)
    if resp.text.find("btn view viewGray") > -1:
        print("-------------stilling scanning------------------")
    else:
        send_text_msg()

    global timer
    timer = threading.Timer(1.0, listending, [])
    timer.start()

if __name__ == '__main__':
    timer = threading.Timer(1.0, listending, [])
    timer.start()