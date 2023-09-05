import random
from PIL import Image


def show_random_photo():
    photos = [
        "ken.png",
        "drive.jpg",
        "bladerunner.jpg",
        "la la land.jpg",
        "nice guys.jpg",
    ]

    random_photo = random.choice(photos)
    img = Image.open(random_photo)
    img.show()


def show_specific_photo(photo_name):
    try:
        img = Image.open(photo_name)
        img.show()
    except Exception as e:
        print(f"Произошла ошибка при открытии изображения: {e}")


if __name__ == "__main__":
    show_random_photo()
