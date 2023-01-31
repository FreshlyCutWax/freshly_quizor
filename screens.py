# textual
from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Static

class DefaultScreen(Screen):

    MESSAGE = "Oopsie, an error must have occurred."

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(self.MESSAGE)
