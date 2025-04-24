from datetime import datetime

from model.tranche import Tranche
from view.app_view import AppView


class Presenter:
    def __init__(self, view: AppView, model: Tranche):
        self.__view = view
        self.__model = model

        self.__view.on_calculate_click.connect(self.__get_entry_values)
        self.__model.on_calculated.connect(self.__get_calculated_interest)

    @staticmethod
    def __validate_date(date: str, date_format: str = "%d.%m.%Y") -> datetime:
        try:
            return datetime.strptime(date, date_format)
        except ValueError:
            raise

    @staticmethod
    def __validate_number(value: str) -> float:
        try:
            return float(value.replace(",", "."))
        except ValueError:
            raise

    def __get_entry_values(self, *_, **kwargs):
        try:
            tranche_sum = self.__validate_number(kwargs["tranche_sum"])
        except ValueError:
            tranche_sum = None
            self.__view.set_tranche_sum_placeholder_error_text(kwargs["period_number"])

        try:
            receipt_date = self.__validate_date(kwargs["receipt_date"])
        except ValueError:
            receipt_date = None
            self.__view.set_receipt_date_placeholder_error_text(kwargs["period_number"])

        try:
            return_date = self.__validate_date(kwargs["return_date"])
        except ValueError:
            return_date = None
            self.__view.set_return_date_placeholder_error_text(kwargs["period_number"])

        try:
            interest_rate = self.__validate_number(kwargs["interest_rate"])
        except ValueError:
            interest_rate = None
            self.__view.set_interest_rate_placeholder_error_text(kwargs["period_number"])

        if tranche_sum and receipt_date and return_date and interest_rate:
            self.__model.calculate(tranche_sum, receipt_date, return_date, interest_rate)

    def __get_calculated_interest(self, calculated_interest: float):
        self.__view.update_calculate_result(calculated_interest)

    def run(self):
        self.__view.mainloop()
