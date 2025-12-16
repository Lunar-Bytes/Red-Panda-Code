import tkinter as tk
from PIL import Image, ImageTk

# -------------------------
# Generic Entity
# -------------------------
class Entity:
    def __init__(self, name):
        self.name = name
        self.image = None
        self.pos = [400, 300]
        self.speed = 10
        self.controls = {}  # key -> direction

    def sprite(self, path):
        try:
            img = Image.open(path)
            self.image = ImageTk.PhotoImage(img)
            print(f"{self.name} sprite loaded: {path}")
        except Exception as e:
            print(f"Error loading sprite for {self.name}:", e)
            self.image = None

    def move(self, direction, key=None):
        # Bind movement to a key
        if key:
            self.controls[key.lower()] = direction

    def update(self, keys_pressed):
        for key, direction in self.controls.items():
            if key in keys_pressed:
                if direction == "up":
                    self.pos[1] -= self.speed
                elif direction == "down":
                    self.pos[1] += self.speed
                elif direction == "left":
                    self.pos[0] -= self.speed
                elif direction == "right":
                    self.pos[0] += self.speed


# -------------------------
# Game
# -------------------------
class Game:
    def __init__(self):
        self.root = None
        self.canvas = None
        self.width = 800
        self.height = 600
        self.title_text = "Red Panda Game"

        self.entities = {}        # name -> Entity
        self.text_elements = []
        self.keys_pressed = set()

    # 🔥 MAGIC: auto-create entities
    def __getattr__(self, name):
        if name not in self.entities:
            self.entities[name] = Entity(name)
            print(f"Entity created: {name}")
        return self.entities[name]

    def init(self):
        self.root = tk.Tk()
        self.root.title(self.title_text)
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        self.root.bind("<KeyPress>", self._on_key_press)
        self.root.bind("<KeyRelease>", self._on_key_release)

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

    def window_text(self, pos, text):
        self.text_elements.append((pos, str(text)))

    def _on_key_press(self, event):
        self.keys_pressed.add(event.keysym.lower())

    def _on_key_release(self, event):
        self.keys_pressed.discard(event.keysym.lower())

    def render(self):
        if not self.canvas:
            raise RuntimeError("Game not initialized!")

        def update():
            self.canvas.delete("all")

            # Update & draw entities
            for entity in self.entities.values():
                entity.update(self.keys_pressed)
                if entity.image:
                    x, y = entity.pos
                    self.canvas.create_image(x, y, image=entity.image)

            # Draw text
            for pos, text in self.text_elements:
                self.canvas.create_text(
                    10, 10,
                    anchor="nw",
                    text=text,
                    fill="white",
                    font=("Arial", 16)
                )

            self.root.after(16, update)  # ~60 FPS

        update()
        self.root.mainloop()
