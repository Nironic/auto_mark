from vk_messages import MessagesAPI
from vk_messages.utils import get_random
from time import sleep
import datetime
import os
import webbrowser

line = "------------------------------"
def menu():
    print(line)
    print("Инструкция")
    print("Для отметки присудствующих вам потребуется логин и пароль от вашей страницы Вконтакте")
    print("Так же вам спонадобиться id беседы в которой вы отмечаетесь. Чтобы узнать id беседы перейдите в вконтакте в ту беседу и скопируйте последние цыфры url страницы.")
    print("Распределение по парам: \n1 Пара - 8:00\n2 Пара - 9:30\n3 Пара - 12:00\n4 Пара - 13:30")
    print("Если нужно добавить ещё пар то пишите расработчику в вконтакте.")
    print(line)
    print("Открыть страницу разработчика? Y/N  (Y - Да) (N - Нет)")
    com = input("Y/N:")
    if com == "Y":
        webbrowser.open("https://vk.com/n__python", new=0, autoraise=True)
    if com == "N":
        print("Начинаю работу программы..")
        print(line)
    else:
        webbrowser.open("https://vk.com/n__python", new=0, autoraise=True)

menu()
login = input("Логин:")
passw = input("Пароль:")
group = 2000000000 + int(input("id беседы:"))
print(line)
print("Распределение по парам: \n1 Пара - 8:00\n2 Пара - 9:30\n3 Пара - 12:00\n4 Пара - 13:30")
print("Укажите какая будет следующая пара")
para = int(input("Укажите пару (цыфра):"))
print("Очищаю экран..")
os.system("cls")


messages = MessagesAPI(login=login, password=passw)



def send(id, text):
    messages.method('messages.send', user_id=id, message=text, random_id=get_random())

def send_gr(id, text):
    messages.method('messages.send', peer_id=id, message=text, random_id=get_random())

def tsi():
    #TS out
    out = messages.method('messages.getLongPollServer', lp_version = 3, v = "5.103")
    ts = out["ts"]
    return ts


def msg(ts):
    #Server message
    out = messages.method('messages.getLongPollHistory', ts = ts, events_limit = 1000, v = "5.103")
    temp = out["messages"]["items"]
    text = None
    peer_id = None
    for i in temp:
        for _ in i:
            text = i["text"]
            peer_id = i["peer_id"]
    
    return text, peer_id


def times(para):
    if para == 1:
        while True:
            now = datetime.datetime.now()
            print("Жду первой пары (8:00): " + str(now.hour) + ":" + str(now.minute))
            os.system("cls")
            if now.hour == 8:
                if now.minute > 0:
                    break
    if para == 2:
        while True:
            now = datetime.datetime.now()
            print("Жду второй пары (9:30): " + str(now.hour) + ":" + str(now.minute))
            os.system("cls")
            if now.hour == 9:
                if now.minute > 29:
                    break
    if para == 3:
        while True:
            now = datetime.datetime.now()
            print("Жду третьей пары (12:00): " + str(now.hour) + ":" + str(now.minute))
            os.system("cls")
            if now.hour == 12:
                if now.minute > 0:
                    break
    if para == 4:
        while True:
            now = datetime.datetime.now()
            print("Жду четвёртой пары (13:30): " + str(now.hour) + ":" + str(now.minute))
            os.system("cls")
            if now.hour == 13:
                if now.minute > 29:
                    cleari()
                    break


def cleari():
    global para
    para = 1
    times(para)

def main():
    global para
    text = 0
    peer_id = 0
    temp1 = 0
    temp = 0
    times(para)
    print("[START]")
    temp_ts = tsi()
    
    while True:
        text = 0
        peer_id = 0
        text = msg(temp_ts)
        print(text)
        if text[0] == "+" and text[1] == group:
            temp += 1
            if temp == 1:
                temp1 = 1
                send_gr(group, "+")
                temp = 0
            if temp1 == 1:
                para += 1
                break
    main()

main()