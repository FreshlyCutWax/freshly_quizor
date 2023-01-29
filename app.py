# App
from modes import *

# Textual
from textual.app import App, ComposeResult
from textual.widgets import Header, Static, Button

class QuizorApp(App):

    TITLE = "Freshly Quizor"
    CSS_PATH = "style/app.css"
    BINDINGS = []

    def __init__(self):
        super().__init__()
        self.mode = Mode()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Static("Welcome", id="welcome")
        yield Button("Exit", id="exit", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id == "exit")

if __name__ == "__main__":
    app = QuizorApp()
    app.run()
