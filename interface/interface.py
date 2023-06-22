import os
import re

import customtkinter as ctk

from tranche.tranche import Tranche

DATE_PATTERN = r'(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])[.](?:0?[1-9]|1[0-2])[.](?:19[0-9][0-9]|20[' \
               r'0-5][0-9])(?!\d)'
FONT = ('Tahoma', 13)
FRAME_FG = '#242424'
PH_TEXT = '#7e7e8f'
PH_TEXT_ERR = '#f24d41'
ENTRY_CONFIGURE = {'placeholder_text_color': PH_TEXT, 'font': FONT, 'width': 150}
ENTRY_CONFIGURE_ERR = {'placeholder_text_color': PH_TEXT_ERR}
ICON_PATH = os.path.abspath(os.path.join('icon.ico'))
ctk.set_appearance_mode('dark')


class EntryFrame(ctk.CTkFrame):
    def __init__(self, master, per_num):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color=FRAME_FG)
        self.dates_str = ''

        self.period = ctk.CTkLabel(self, text=f'Период {per_num}', font=FONT)
        self.period.grid(row=0, column=0, padx=0, pady=(0, 0))

        self.tr_sum = ctk.CTkEntry(self, placeholder_text='Сумма транша', **ENTRY_CONFIGURE)
        self.tr_sum.grid(row=1, column=0, padx=10, pady=(0, 0), sticky='w')

        self.bdate = ctk.CTkEntry(self, placeholder_text='Дата поступления', **ENTRY_CONFIGURE)
        self.bdate.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')

        self.edate = ctk.CTkEntry(self, placeholder_text='Дата возврата', **ENTRY_CONFIGURE)
        self.edate.grid(row=3, column=0, padx=10, pady=(10, 0), sticky='w')

        self.rate = ctk.CTkEntry(self, placeholder_text='Процентная ставка', **ENTRY_CONFIGURE)
        self.rate.grid(row=4, column=0, padx=10, pady=(10, 10), sticky='w')

    def get(self):
        try:
            return int(self.tr_sum.get()), self.bdate.get(), self.edate.get(), int(self.rate.get())
        except ValueError:
            self.check_formats()
            return False

    def clear(self):
        self.tr_sum.delete(0, 'end')
        self.tr_sum.configure(placeholder_text='Сумма транша', **ENTRY_CONFIGURE)

        self.bdate.delete(0, 'end')
        self.bdate.configure(placeholder_text='Дата поступления', **ENTRY_CONFIGURE)

        self.edate.delete(0, 'end')
        self.edate.configure(placeholder_text='Дата возврата', **ENTRY_CONFIGURE)

        self.rate.delete(0, 'end')
        self.rate.configure(placeholder_text='Процентная ставка', **ENTRY_CONFIGURE)

    def check_formats(self):
        if not self.tr_sum.get().isdigit():
            self.tr_sum.delete(0, 'end')
            self.tr_sum.configure(placeholder_text='Некорректные данные', **ENTRY_CONFIGURE_ERR)

        if not re.findall(DATE_PATTERN, self.bdate.get()):
            self.bdate.delete(0, 'end')
            self.bdate.configure(placeholder_text='Некорректный формат', **ENTRY_CONFIGURE_ERR)

        if not re.findall(DATE_PATTERN, self.edate.get()):
            self.edate.delete(0, 'end')
            self.edate.configure(placeholder_text='Некорректный формат', **ENTRY_CONFIGURE_ERR)

        if not self.rate.get().isdigit():
            self.rate.delete(0, 'end')
            self.rate.configure(placeholder_text='Некорректные данные', **ENTRY_CONFIGURE_ERR)

        self.period.focus()


class TrancheCalcApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Tranche')
        self.geometry('365x300')
        self.iconbitmap(ICON_PATH)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.resizable(False, False)
        self.tranche_result = 0
        self.message = 'Сумма возврата на {0}: {1} руб'

        self.switch_var = ctk.StringVar(value='off')
        self.switch = ctk.CTkSwitch(self, text='2 периода', command=self.switch_periods, font=FONT,
                                    variable=self.switch_var, onvalue='on', offvalue='off')
        self.switch.grid(row=0, column=0, pady=(15, 0), sticky='n', columnspan=2)

        self.res_message = ctk.CTkLabel(self, text='')
        self.res_message.grid(row=3, column=0, pady=0, padx=5, sticky='ew', columnspan=2)

        self.p1_entry = EntryFrame(self, per_num=1)
        self.p1_entry.grid(row=1, column=0, padx=(10, 0), pady=(5, 0), sticky='s')

        self.p2_entry = None

        self.calc_button = ctk.CTkButton(self, text='Рассчитать', command=self.tr_calc, font=FONT)
        self.calc_button.grid(row=4, column=0, pady=5, padx=5, sticky='ew', columnspan=2)

    def tr_calc(self):
        try:
            self.tranche_result = Tranche(*self.p1_entry.get()).main()

            if not self.p2_entry:
                date = self.p1_entry.get()[2]
                self.message = self.message.format(date, round(self.tranche_result, 2))
            else:
                date = self.p2_entry.get()[2]
                self.tranche_result = Tranche(*self.p2_entry.get()).main()
                self.message = self.message.format(date, round(self.tranche_result, 2))
                self.p2_entry.clear()
        except TypeError:
            return

        self.res_message.configure(text=self.message, font=FONT)
        self.p1_entry.clear()
        self.switch.focus()

    def switch_periods(self):
        if self.switch_var.get() == 'on':
            self.p2_entry = EntryFrame(self, per_num=2)
            self.p2_entry.grid(row=1, column=1, padx=(0, 10), pady=(5, 0), sticky='s')
        else:
            self.p2_entry.destroy()
            self.p2_entry = None


def main():
    app = TrancheCalcApp()
    app.mainloop()


if __name__ == '__main__':
    main()
