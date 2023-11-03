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
        "updated_at":get_current_datetime()
    }
    notes.append(note)
    save_notes (notes)
    print("Заметка создана")

#Сохранение заметки
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

#ВЫвод всех заметок
def show_notes():
    notes = load_notes()
    if notes:
        for note in notes:
            print("ID:", note["id"])
            print("Заголовок:", note["title"])
            print("Текст:", note["body"])
            print("Дата создания:", note["created_at"])
            print("Дата изменения:", note["updated_at"])
            print("____________________________________")
    else:
        print("Заметок пока нет.")

# Редактирование заметки
def edit_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для редактирования: "))
    found = False
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки:")
            note["title"] = title
            note["body"] = body
            note["updated_at"] = get_current_datetime()
            found = True
            break
        if found:
            save_notes(notes)
            print("Заметка успешно изменена")
        else:
            print("Заметка с таким ID отсутствует")

#Удаление заметки
def delete_note():
    notes = load_notes()
    note_id = int(input("ВВедите ID заметки для удаления: "))
    found = False
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            found = True
            break
        if found:
            save_notes(notes)
            print("Заметка успешно удалена")
        else:
            print("Заметка с таким ID не найдена.")

#Основной метод
def main():
    while True:
        print("1. Создание заметки")
        print("2. Показать все заметки")
        print("3. Сохранение заметки")
        print("4. Редактирование заметки")
        print("5. Удаление заметки")
        print("0. Выйти из приложения")

        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы выбрали создать заметку")
            create_note()
        elif choice == "2":
            print("Вы выбрали показать все заметки")
            show_notes()
        elif choice == "3":
            print("Вы выбрали сохранить заметку")
            save_notes()
        elif choice == "4":
            print("Вы выбрали редактировать заметку")
            edit_note()
        elif choice == "5":
            print("Вы выбрали удалить заметку")
            delete_note()
        elif choice == "0":
            print("Выход из приложения")
            break
        else:
            print("Неверный выбор, попробуйте ещё раз")

if __name__ == "__main__":
    main()