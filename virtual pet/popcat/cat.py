import os
import time
import tkinter as tk
from PIL import Image, ImageTk
from configparser import ConfigParser

class VirtualPet:
    def __init__(self, root, cat1_path, cat2_path, resolution):
        self.root = root
        self.root.overrideredirect(True)  # Usuń tło tytułu i guziki
        self.root.attributes("-topmost", True)  # Wyświetl okno na wierzchu innych okien

        self.cat1_path = cat1_path
        self.cat2_path = cat2_path

        # Wczytaj obrazy
        self.cat1_image = Image.open(cat1_path)
        self.cat2_image = Image.open(cat2_path)

        # Dopasuj rozmiar obrazka do rozdzielczości okna
        self.resolution = resolution
        width, height = map(int, self.resolution.split('x'))
        self.cat1_image = self.cat1_image.resize((width, height), Image.ANTIALIAS)
        self.cat2_image = self.cat2_image.resize((width, height), Image.ANTIALIAS)

        # Ustawienie początkowych wartości
        self.current_image = self.cat1_image
        self.image_label = tk.Label(root, image=None)
        self.image_label.pack()

        # Ustawienie interwału czasowego
        self.root.after(100, self.update)

        # Ustawienie początkowych współrzędnych
        self.x = 100
        self.y = 100

        # Ustawienie prędkości
        self.speed_x = 3
        self.speed_y = 2

    def update(self):
        # Zmień obraz co pewien czas
        if int(time.time()) % 5 < 2.5:
            self.current_image = self.cat2_image
        else:
            self.current_image = self.cat1_image

        # Zaktualizuj obraz w etykiecie
        imgtk = ImageTk.PhotoImage(self.current_image)
        self.image_label.configure(image=imgtk)
        self.image_label.image = imgtk

        # Przesuń wirtualnego peta
        self.x += self.speed_x
        self.y += self.speed_y

        # Odbij od krawędzi ekranu
        if self.x > self.root.winfo_screenwidth() - self.cat1_image.width:
            self.speed_x = -self.speed_x
            self.x = self.root.winfo_screenwidth() - self.cat1_image.width
        elif self.x < 0:
            self.speed_x = -self.speed_x
            self.x = 0

        if self.y > self.root.winfo_screenheight() - self.cat1_image.height:
            self.speed_y = -self.speed_y
            self.y = self.root.winfo_screenheight() - self.cat1_image.height
        elif self.y < 0:
            self.speed_y = -self.speed_y
            self.y = 0

        # Ustaw współrzędne okna
        self.root.geometry("+{}+{}".format(self.x, self.y))

        # Wywołaj metodę update rekurencyjnie
        self.root.after(100, self.update)

def read_config(filename="conf.txt"):
    config = ConfigParser()
    config.read(filename)
    resolution = config.get("Settings", "resolution", fallback="200x200")
    return resolution

def main():
    # Wczytaj rozdzielczość z pliku konfiguracyjnego
    resolution = read_config()

    root = tk.Tk()
    root.title("Virtual Pet")

    # Ścieżka do foldera z obrazami
    folder_path = "data/"

    # Nazwy plików z obrazami
    cat1_path = os.path.join(folder_path, "cat1.png")
    cat2_path = os.path.join(folder_path, "cat2.png")

    # Utwórz obiekt VirtualPet
    virtual_pet = VirtualPet(root, cat1_path, cat2_path, resolution)

    root.mainloop()

if __name__ == "__main__":
    main()
