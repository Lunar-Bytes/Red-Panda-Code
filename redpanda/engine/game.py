class Game:
    def __init__(self):
        self.title_text = ""
        self.width = 800
        self.height = 600
        self.player_sprite_path = ""
        self.text_elements = []

    def init(self):
        print("Game initialized")

    def title(self, text):
        self.title_text = text
        print(f"Game title: {text}")

    def size(self, size_str):
        # parse size like "w=1660, h=900"
        parts = size_str.replace(" ", "").split(',')
        self.width = int(parts[0].split('=')[1])
        self.height = int(parts[1].split('=')[1])
        print(f"Game size: {self.width}x{self.height}")

    class player:
        sprite_path = ""
        @classmethod
        def sprite(cls, path):
            cls.sprite_path = path
            print(f"Player sprite: {path}")

        @classmethod
        def move(cls, direction, key):
            print(f"Move {direction} with key {key}")

    def window_text(self, pos, text):
        self.text_elements.append((pos, text))
        print(f"Text at {pos}: {text}")

    def render(self):
        print(f"Rendering game: {self.title_text}")
        print(f"Player sprite path: {self.player_sprite_path}")
        for t in self.text_elements:
            print(f"Text at {t[0]}: {t[1]}")
