from ryan_gosling_movies import get_movies


def main():
    choice = input()
    if choice == "1":
        get_movies()
    else:
        print("Неправильный выбор")


if __name__ == "__main__":
    main()
