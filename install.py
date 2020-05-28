import os

line = "---------------"

try:
    from vk_messages import MessagesAPI
    from vk_messages.utils import get_random
except:
    print(line)
    print("Установка vk_messages")
    print(line)
    os.system("pip install vk_messages")


print("OK")