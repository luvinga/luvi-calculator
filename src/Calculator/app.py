import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, RIGHT

class Luvi(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title="Luvi Calculator")

        # Load icon here
        self.my_icon = toga.Icon("icons/icon1.png")  # make sure this path exists

        # Display area
        self.result = toga.Label(
            "0",
            style=Pack(
                padding=10,
                font_size=28,
                text_align=RIGHT,
                color="black",  
                background_color="#f0f0f0",
                width=260,
                height=50,
            ),
        )

        # Buttons layout
        buttons = [
            ["C", "⌫", "/", "*"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", ""],
        ]

        button_box = toga.Box(style=Pack(direction=COLUMN, padding=5))

        for row in buttons:
            row_box = toga.Box(style=Pack(direction=ROW, alignment=CENTER))
            for b in row:
                if b == "":
                    btn = toga.Box(style=Pack(width=60, height=50))
                else:
                    btn = toga.Button(
                        b,
                        on_press=self.on_press,
                        style=Pack(
                            padding=5,
                            width=60,
                            height=50,
                            font_size=16,
                            background_color=self.get_button_color(b),
                            color="white" if b not in ("C", ".", "⌫") else "black",
                        ),
                    )
                row_box.add(btn)
            button_box.add(row_box)

        main_box = toga.Box(
            style=Pack(direction=COLUMN, alignment=CENTER, padding=20)
        )
        main_box.add(self.result)
        main_box.add(button_box)

        self.main_window.content = main_box
        self.main_window.show()

        self.current = ""

    def get_button_color(self, text):
        """Set colors for special buttons."""
        if text == "C":
            return "#ffb3b3"  # red
        elif text == "⌫":
            return "#ffd480"  # orange
        elif text in ("=", "+", "-", "*", "/"):
            return "#80b3ff"  # blue
        else:
            return "#a6a6a6"  # gray

    def on_press(self, widget):
        text = widget.text

        if text == "C":
            self.current = ""
        elif text == "⌫":
            self.current = self.current[:-1]
        elif text == "=":
            try:
                self.current = str(eval(self.current))
            except Exception:
                self.current = "Error"
        else:
            if self.current == "0" or self.current == "Error":
                self.current = ""
            self.current += text

        self.result.text = self.current if self.current else "0"

def main():
    return Luvi()
