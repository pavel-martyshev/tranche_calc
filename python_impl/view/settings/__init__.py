import json
import os

from view.settings.settings import AppSettings, FrameSettings

SETTINGS_PATH = os.path.join(os.path.dirname(__file__), "settings.json")

with open(SETTINGS_PATH, "r", encoding="UTF-8") as settings_file:
    settings_rows = json.load(settings_file)

app_settings = AppSettings(**settings_rows["settings"]["app_settings"])
frame_settings = FrameSettings(**settings_rows["settings"]["frame_settings"])
