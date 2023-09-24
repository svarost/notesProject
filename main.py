import json
import os

# Функция для создания новой заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": get_timestamp()
    }
    notes.append(note)
    save_notes()
    print("Заметка успешно создана!")

# Функция для вывода списка всех заметок
def list_notes():
    if not notes:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"{note['id']}: {note['title']} ({note['timestamp']})")

# Функция для просмотра конкретной заметки
def view_note(note_id):
    note = find_note_by_id(note_id)
    if note:
        print(f"Заголовок: {note['title']}")
        print(f"Заметка: {note['body']}")
        print(f"Дата/время создания: {note['timestamp']}")
    else:
        print("Заметка не найдена.")

# Функция для редактирования существующей заметки
def edit_note(note_id):
    note = find_note_by_id(note_id)
    if note:
        new_title = input("Введите новый заголовок (оставьте пустым, чтобы не изменять): ")
        new_body = input("Введите новый текст (оставьте пустым, чтобы не изменять): ")
        if new_title:
            note['title'] = new_title
        if new_body:
            note['body'] = new_body
        note['timestamp'] = get_timestamp()
        save_notes()
        print("Заметка успешно отредактирована!")
    else:
        print("Заметка не найдена.")

# Функция для удаления заметки
def delete_note(note_id):
    note = find_note_by_id(note_id)
    if note:
        notes.remove(note)
        save_notes()
        print("Заметка успешно удалена!")
    else:
        print("Заметка не найдена.")

# Функция для поиска заметки по ID
def find_note_by_id(note_id):
    for note in notes:
        if note['id'] == note_id:
            return note
    return None

# Функция для сохранения заметок в файл JSON
def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

# Функция для получения текущей даты и времени
def get_timestamp():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Основная функция приложения
def main():
    global notes
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
    else:
        notes = []

    while True:
        print("\nВыберите действие:")
        print("1. Создать новую заметку")
        print("2. Просмотреть список заметок")
        print("3. Просмотреть заметку по ID")
        print("4. Редактировать заметку по ID")
        print("5. Удалить заметку по ID")
        print("6. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == '1':
            create_note()
        elif choice == '2':
            list_notes()
        elif choice == '3':
            note_id = int(input("Введите ID заметки: "))
            view_note(note_id)
        elif choice == '4':
            note_id = int(input("Введите ID заметки для редактирования: "))
            edit_note(note_id)
        elif choice == '5':
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == '6':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()