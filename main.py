from ryan_gosling_movies import get_movies
from ryan_gosling_photos import show_random_photo

def main():
    choice = input()
    if choice == "1":
        get_movies()
    elif choice == "2":
        show_random_photo()
    else:
        print("Неправильный выбор")


if __name__ == "__main__":
    main()
