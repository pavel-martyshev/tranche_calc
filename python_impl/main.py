from model.tranche import Tranche
from presenter.presenter import Presenter
from view.app_view import AppView


def main():
    view = AppView()

    presenter = Presenter(view, Tranche())
    presenter.run()


if __name__ == '__main__':
    main()
