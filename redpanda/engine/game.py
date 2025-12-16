import tkinter as tk
from PIL import Image, ImageTk  # optional, only for PNG support

class Game:
    def __init__(self):
        self.root = None
        self.canvas = None
        self.width = 800
        self.height = 600
        self.title_text = "Red Panda Game"
        self.player = self.Player()
        self.text_elements = []

    def init(self):
        self.root = tk.Tk()
        self.root.title(self.title_text)
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()
        print("Game initialized")

    def title(self, text):
        self.title_text = text
        if self.root:
            self.root.title(text)
        print(f"Game title: {text}")

    def size(self, size_str):
        parts = size_str.replace(" ", "").split(',')
        self.width = int(parts[0].split('=')[1])
        self.height = int(parts[1].split('=')[1])
        if self.canvas:
            self.canvas.config(width=self.width, height=self.height)
        print(f"Game size: {self.width}x{self.height}")

    class Player:
        def __init__(self):
            self.sprite_path = None
            self.image = None
            self.canvas_item = None
            self.pos = [400, 300]

        def sprite(self, path):
            self.sprite_path = path
            try:
                img = Image.open(path)
                self.image = ImageTk.PhotoImage(img)
            except Exception as e:
                print("Error loading sprite:", e)
                self.image = None
            print(f"Player sprite: {path}")

        def move(self, direction, key=None):
            if direction == "up":
                self.pos[1] -= 10
            elif direction == "down":
                self.pos[1] += 10
            elif direction == "left":
                self.pos[0] -= 10
            elif direction == "right":
                self.pos[0] += 10

    def window_text(self, pos, text):
        self.text_elements.append((pos, str(text)))

    def render(self):
        if not self.canvas:
            raise RuntimeError("Game not initialized!")

        # Draw player if sprite exists
        if self.player.image:
            x, y = self.player.pos
            if self.player.canvas_item:
                self.canvas.coords(self.player.canvas_item, x, y)
            else:
                self.player.canvas_item = self.canvas.create_image(x, y, image=self.player.image)

        # Draw text elements
        for t in self.text_elements:
            # Only support "left, top" for now
            x, y = 10, 10
            self.canvas.create_text(x, y, anchor="nw", text=t[1], fill="white", font=("Arial", 16))

        self.root.mainloop()
