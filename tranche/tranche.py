from datetime import datetime


class Tranche:
    def __init__(self, tr_sum: int, bdate: str, edate: str, rate: int):
        self.tr_sum = tr_sum
        self.bdate = datetime(*[int(elem) for elem in bdate.strip().split('.')[::-1]])
        self.edate = datetime(*[int(elem) for elem in edate.strip().split('.')[::-1]])
        self.rate = rate / 100
        self.year_days = 365
        self.days = self.days_amount()

    def __str__(self) -> str:
        return f'{self.main()}'

    def days_amount(self) -> int:
        return (self.edate - self.bdate).days

    def main(self) -> float:
        result = self.tr_sum * self.rate / self.year_days * self.days
        return round(result, 2)


def main():
    t_sum = int(input('Введите сумму транша: '))
    date1 = input('Введите дату выдачи: ')
    date2 = input('Введите дату возврата: ')
    t_rate = int(input('Введите процентную ставку: '))

    print(Tranche(t_sum, date1, date2, t_rate))


if __name__ == '__main__':
    main()
