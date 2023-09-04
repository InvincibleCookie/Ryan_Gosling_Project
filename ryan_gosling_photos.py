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


if __name__ == "__main__":
    show_random_photo()
