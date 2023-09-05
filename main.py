from ryan_gosling_movies import get_movies
from ryan_gosling_photos import show_random_photo, show_specific_photo

def main():
    choice = input()
    if choice == "1":
        get_movies()
    elif choice == "2":
        show_random_photo()
    elif choice == "3":
        photo_name = input("Введите имя файла фотографии: ")
        show_specific_photo(photo_name)
    else:
        print("Неправильный выбор")


if __name__ == "__main__":
    main()
