from datetime import datetime


class Tranche:
    def __init__(self, tr_sum: int, bdate: str, edate: str, rate: str):
        self._tr_sum = tr_sum
        self._bdate = datetime(*[int(elem) for elem in bdate.strip().split('.')[::-1]])
        self._edate = datetime(*[int(elem) for elem in edate.strip().split('.')[::-1]])
        self._rate = float(rate.replace(',', '.')) / 100 if ',' in str(rate) else float(rate) / 100
        self._year_days = 365
        self._days = self.days_amount()

    def __str__(self) -> str:
        return f'{self.main()}'

    def days_amount(self) -> int:
        return (self._edate - self._bdate).days

    def main(self) -> float:
        result = self._tr_sum * self._rate / self._year_days * self._days
        return round(result, 2)


def main():
    t_sum = int(input('Введите сумму транша: '))
    date1 = input('Введите дату выдачи: ')
    date2 = input('Введите дату возврата: ')
    t_rate = input('Введите процентную ставку: ')

    print(Tranche(t_sum, date1, date2, t_rate))


if __name__ == '__main__':
    main()
