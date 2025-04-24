import customtkinter as ctk
from blinker import Signal

from view.content.texts import APP_TITLE, INCORRECT_FORMAT, INCORRECT_DATA, RESULT_MASSAGE, SWITCH_TEXT, CALCULATE, \
    CLEAR
from view.frame.entry_frame import EntryFrame
from view.settings import app_settings

ctk.set_appearance_mode("dark")


class AppView(ctk.CTk):
    on_calculate_click = Signal()

    def __init__(self):
        super().__init__()

        self.title(APP_TITLE)
        self.geometry(app_settings.geometry)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.resizable(False, False)

        self.__calculate_result = 0

        self.__switch_var = ctk.StringVar(value="off")
        self.__switch = ctk.CTkSwitch(self, text=SWITCH_TEXT, command=self.switch_periods, font=app_settings.font,
                                      variable=self.__switch_var, onvalue="on", offvalue="off")
        self.__switch.grid(row=0, column=0, pady=(15, 0), sticky="n", columnspan=2)

        self.__result_message = ctk.CTkLabel(self, text="")
        self.__result_message.grid(row=3, column=0, pady=0, padx=5, sticky="ew", columnspan=2)

        self.__period_1_frame = EntryFrame(self, period_number=1)
        self.__period_1_frame.grid(row=1, column=0, padx=(10, 0), pady=(5, 0), sticky="s")

        self.__period_2_frame = None

        self.__calc_button = ctk.CTkButton(self, text=CALCULATE, command=self.calculate, font=app_settings.font)
        self.__calc_button.grid(row=4, column=0, pady=5, padx=5, sticky="ew", columnspan=2)

        self.__reset_button = ctk.CTkButton(self, text=CLEAR, command=self.__reset_entry_fields, font=app_settings.font)
        self.__reset_button.grid(row=5, column=0, pady=5, padx=5, sticky="ew", columnspan=2)

    def get_frame_by_period_number(self, period_number: int):
        return self.__period_1_frame if period_number else self.__period_2_frame

    def set_tranche_sum_placeholder_error_text(self, period_number):
        frame: EntryFrame = self.get_frame_by_period_number(period_number)
        frame.set_tranche_sum_placeholder_text(INCORRECT_DATA, True)

    def set_receipt_date_placeholder_error_text(self, period_number):
        frame: EntryFrame = self.get_frame_by_period_number(period_number)
        frame.set_receipt_date_placeholder_text(INCORRECT_FORMAT, True)

    def set_return_date_placeholder_error_text(self, period_number):
        frame: EntryFrame = self.get_frame_by_period_number(period_number)
        frame.set_return_date_placeholder_text(INCORRECT_FORMAT, True)

    def set_interest_rate_placeholder_error_text(self, period_number):
        frame: EntryFrame = self.get_frame_by_period_number(period_number)
        frame.set_interest_rate_placeholder_text(INCORRECT_DATA, True)

    def update_calculate_result(self, calculate_result: float):
        self.__calculate_result += calculate_result

    def calculate(self):
        self.on_calculate_click.send(**self.__period_1_frame.get(), period_number=1)

        if self.__period_2_frame:
            self.on_calculate_click.send(**self.__period_2_frame.get(), period_number=2)

        self.__set_result_message_text(self.__calculate_result)

    def switch_periods(self):
        if self.__switch_var.get() == "on":
            self.__period_2_frame = EntryFrame(self, period_number=2)
            self.__period_2_frame.grid(row=1, column=1, padx=(0, 10), pady=(5, 0), sticky="s")
        else:
            self.__period_2_frame.destroy()
            self.__period_2_frame = None

    def __set_result_message_text(self, summ: float):
        if self.__period_2_frame:
            date: str = self.__period_2_frame.get_return_date()
        else:
            date: str = self.__period_1_frame.get_return_date()

        self.__result_message.configure(text=RESULT_MASSAGE.format(date=date, sum=round(summ, 2)))

    def __reset_entry_fields(self):
        self.__period_1_frame.reset_entry_fields()

        if self.__period_2_frame:
            self.__period_2_frame.reset_entry_fields()
