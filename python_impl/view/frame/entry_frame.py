from typing import Dict

import customtkinter as ctk

from view.content.texts import PERIOD_TITLE, TRANCHE_SUM, RECEIPT_DATE, RETURN_DATE, \
    INTEREST_RATE
from view.settings import frame_settings, app_settings


class EntryFrame(ctk.CTkFrame):
    def __init__(self, master, period_number):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color=frame_settings.fg_color)

        self.__period_label = ctk.CTkLabel(
            self,
            text=PERIOD_TITLE.format(period_number=period_number),
            font=app_settings.font
        )
        self.__period_label.grid(row=0, column=0, padx=0, pady=(0, 0))

        self.__base_entry_settings = frame_settings.entry_fields.dump()

        self.__placeholder_error_text_color = self.__base_entry_settings.pop("placeholder_error_text_color")

        self.__tranche_sum = ctk.CTkEntry(self, placeholder_text=TRANCHE_SUM, **self.__base_entry_settings)
        self.__tranche_sum.grid(row=1, column=0, padx=10, pady=(0, 0))

        self.__receipt_date = ctk.CTkEntry(self, placeholder_text=RECEIPT_DATE, **self.__base_entry_settings)
        self.__receipt_date.grid(row=2, column=0, padx=10, pady=(10, 0))

        self.__return_date = ctk.CTkEntry(self, placeholder_text=RETURN_DATE, **self.__base_entry_settings)
        self.__return_date.grid(row=3, column=0, padx=10, pady=(10, 0))

        self.__interest_rate = ctk.CTkEntry(self, placeholder_text=INTEREST_RATE, **self.__base_entry_settings)
        self.__interest_rate.grid(row=4, column=0, padx=10, pady=(10, 10))

    def get(self) -> Dict[str, str]:
        return {
            "tranche_sum": self.__tranche_sum.get(),
            "receipt_date": self.__receipt_date.get(),
            "return_date": self.__return_date.get(),
            "interest_rate": self.__interest_rate.get(),
        }

    def set_period_label_focus(self):
        self.__period_label.focus()

    def __get_placeholder_text_color(self, is_error: bool) -> str:
        return self.__base_entry_settings["text_placeholder_color"] if not is_error else self.__placeholder_error_text_color

    @staticmethod
    def __set_placeholder_text(entry_field: ctk.CTkEntry, text: str, text_color: str):
        entry_field.delete(0, "end")
        entry_field.configure(
            placeholder_text=text,
            placeholder_text_color=text_color
        )

    def set_tranche_sum_placeholder_text(self, text: str, is_error: bool = False):
        self.__set_placeholder_text(self.__tranche_sum, text, self.__get_placeholder_text_color(is_error))

    def set_receipt_date_placeholder_text(self, text: str, is_error: bool = False):
        self.__set_placeholder_text(self.__receipt_date, text, self.__get_placeholder_text_color(is_error))

    def set_return_date_placeholder_text(self, text: str, is_error: bool = False):
        self.__set_placeholder_text(self.__return_date, text, self.__get_placeholder_text_color(is_error))

    def set_interest_rate_placeholder_text(self, text: str, is_error: bool = False):
        self.__set_placeholder_text(self.__interest_rate, text, self.__get_placeholder_text_color(is_error))

    def get_return_date(self) -> str:
        return self.__return_date.get()

    def reset_entry_fields(self):
        self.__tranche_sum.delete(0, "end")
        self.__tranche_sum.configure(placeholder_text=TRANCHE_SUM, **self.__base_entry_settings)

        self.__receipt_date.delete(0, "end")
        self.__receipt_date.configure(placeholder_text=RECEIPT_DATE, **self.__base_entry_settings)

        self.__return_date.delete(0, "end")
        self.__return_date.configure(placeholder_text=RETURN_DATE, **self.__base_entry_settings)

        self.__interest_rate.delete(0, "end")
        self.__interest_rate.configure(placeholder_text=INTEREST_RATE, **self.__base_entry_settings)
