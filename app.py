# App
from modes import *

# Textual
from textual.app import App, ComposeResult
from textual.widgets import Header
class QuizorApp(App):

    BINDINGS = []

    def __init__(self):
        super().__init__()
        self.mode = Mode()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()

if __name__ == "__main__":
    app = QuizorApp()
    app.run()
