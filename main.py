from model.models import Models
from presenter import Presenter
from view.views import App

if __name__ == "__main__":
    model = Models()
    view = App()
    app = Presenter(model, view)
    app.run()