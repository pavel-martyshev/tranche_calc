from typing import List

from pydantic import BaseModel, Field


class AppSettings(BaseModel):
    font_: List[str] = Field(alias="font")
    geometry: str

    @property
    def font(self) -> (str, int):
        return self.font_[0], int(self.font_[1])


class EntryFieldSettings(BaseModel):
    placeholder_text_color: str
    placeholder_error_text_color: str
    font_: List[str] = Field(alias="font")
    width: int

    @property
    def font(self) -> (str, int):
        return self.font_[0], int(self.font_[1])

    def dump(self):
        return {
            "font": self.font,
            "placeholder_text_color": self.placeholder_text_color,
            "placeholder_error_text_color": self.placeholder_error_text_color,
            "width": self.width,
        }

class FrameSettings(BaseModel):
    fg_color: str
    entry_fields: EntryFieldSettings
