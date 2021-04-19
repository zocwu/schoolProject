import vk_api
from random import getrandbits
from vk_api.longpoll import VkLongPoll, VkEventType
import re
import threading
import sys
import os
from PyQt5 import QtWidgets, uic
import sqlite3

# variables
token = open("token.txt", "r").read()
vk = vk_api.VkApi(token=token)
try:
    longpoll = VkLongPoll(vk)
except vk_api.ApiError as e:
    if e.code == 5:
        print("Недействительный api-ключ. Ознакомьтесь с инструкцией.")
        sys.exit()

directory = os.path.dirname(__file__)
patterns = {

    'start': r'!s',
    'test': r'!test',
    'searchNum': r'\d+',
    'delete': r'!d',

}
vk = vk_api.VkApi(token=token)
try:
    longpoll = VkLongPoll(vk)
except vk_api.ApiError as e:
    if e.code == 15:
        print("Сообществу запрещено работать с сообщениями. Ознакомьтесь с инструкцией.")
        sys.exit()

smiles = {
    "/smile/": "&#128522;",
    "/rage/": "&#128545;",
}


# end


# convert text to smile
def give_smile(t):
    for smile in smiles.keys():
        t = t.replace(smile, smiles[smile])
    return t


# send message to vk id
def msg(user_id, message):
    r = getrandbits(64)
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': r})


# main loop vk bot
def main_loop():
    # db
    db = sqlite3.connect("data/user.db")
    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS ids(
                            Id TEXT PRIMARY KEY
                            )""")
    db.commit()

    # end db

    # get ids from data/user.db
    def get_ids():
        arrayIds = []
        for userId in sql.execute(f"SELECT Id FROM ids"):
            arrayIds.append(userId)
        return arrayIds

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                if re.search(patterns['start'], event.text):
                    uid = event.user_id
                    sql.execute(f"SELECT Id FROM ids WHERE Id = '{uid}'")
                    if sql.fetchone() is None:
                        sql.execute(f"INSERT INTO ids VALUES(?)", (str(uid),))
                        db.commit()
                        msg(uid, "You were added.")
                        print(uid, "were added.")

                    else:
                        msg(uid, "You were always added.")

                if re.search(patterns['delete'], event.text):
                    uid = event.user_id
                    sql.execute(f"SELECT Id FROM ids WHERE Id = '{uid}'")
                    if sql.fetchone() is None:
                        msg(uid, "You are not added.")
                    else:
                        sql.execute(f"DELETE FROM ids WHERE Id = '{uid}'")
                        db.commit()
                        print(uid, "were deleted.")
                        msg(uid, "You were deleted.")


# start Get Ids function
mainThread = threading.Thread(target=main_loop)
mainThread.start()

# gui
app = QtWidgets.QApplication([])
win = uic.loadUi("ui/mainForm.ui")
win.show()


# send button
def sendB():
    # db
    db = sqlite3.connect("data/user.db")
    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS ids(
                                Id INT PRIMARY KEY
                                )""")
    db.commit()

    # end db

    # get ids from data/user.db
    def get_ids():
        arrayIds = []
        for userId in sql.execute(f"SELECT Id FROM ids"):
            arrayIds.append(userId)
        return arrayIds

    caption = "Message is done."
    text = win.textEdit.toPlainText()
    text = give_smile(text)
    if len(get_ids()) == 0:
        caption = "No ids."
    else:
        caption = "Message is done."
    for id in get_ids():
        msg(id, text)
    win.captionLabel.setText(caption)
    win.textEdit.setText("")


# bind send button
win.sendButton.clicked.connect(sendB)

# exit when click crosshair at gui
sys.exit(app.exec())
