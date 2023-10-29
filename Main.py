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

#Создание заметки
def create_note():
    notes = load_notes()
    title = input("Введите название заметки:")
    body = input("Введите текст заметки:")
    note = {
        "id":len(notes) + 1,
        "title":title,
        "body":body,
        "created_at":get_current_datetime(),
        "updated_at":get_current_datetime(),
    }
    notes.append(note)
    #save_notes
    print("Заметка создана")

#Сохранние заметки
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)
