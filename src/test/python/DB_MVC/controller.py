from model import Model
from view import View

# Controller
class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        ...