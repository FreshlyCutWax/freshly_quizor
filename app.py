# App
from screens import *

# Textual
from textual.app import App

class QuizorApp(App):

    TITLE = "Freshly Quizor"
    CSS_PATH = "styles.css"
    SCREENS = {"default": DefaultScreen()}
    BINDINGS = []

    def __init__(self):
        super().__init__()

    def on_mount(self) -> None:
        self.push_screen(self.SCREENS["default"])

if __name__ == "__main__":
    app = QuizorApp()
    app.run()
