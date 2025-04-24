from datetime import datetime

from blinker import Signal


class Tranche:
    __year_days = 365

    on_calculated = Signal()

    @staticmethod
    def __get_days_amount(start_date: datetime, end_date: datetime) -> int:
        return (end_date - start_date).days

    @classmethod
    def calculate(cls,
                  tranche_sum: float,
                  receipt_date: datetime,
                  return_date: datetime,
                  interest_rate: float):
        result = tranche_sum * (interest_rate / 100) / cls.__year_days * cls.__get_days_amount(receipt_date, return_date)

        cls.on_calculated.send(result)


if __name__ == "__main__":
    def main():
        t_sum = int(input("Введите сумму транша: "))
        date1 = datetime.strptime(input("Введите дату выдачи: "), "%d.%m.%Y")
        date2 = datetime.strptime(input("Введите дату возврата: "), "%d.%m.%Y")
        t_rate = float(input("Введите процентную ставку: "))

        print(Tranche.calculate(t_sum, date1, date2, t_rate))

    main()
