from ryan_gosling_movies import get_movies
from ryan_gosling_photos import show_random_photo, show_specific_photo

def main():
    print("Добро пожаловать в мир Райана Гослинга!")
    print("Выберите, что вы хотели бы увидеть:")
    print("1. Фильмы")
    print("2. Фотографии")
    print("3. Открыть конкретную фотографию")

    choice = input("Введите номер вашего выбора: ")

    if choice == "1":
        get_movies()
    elif choice == "2":
        show_random_photo()
    elif choice == "3":
        photo_name = input("Введите имя файла фотографии: ")
        show_specific_photo(photo_name)
    else:
        print("Неправильный выбор. Пожалуйста, введите 1, 2 или 3.")

if __name__ == "__main__":
    main()