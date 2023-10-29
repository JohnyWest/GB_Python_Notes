import datetime
import json

#Получаем текущие дату/время
def get_current_datetime():
    return datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

#Загрузка заметок через json
def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
        return notes
    except FileNotFoundError:
        return[]
