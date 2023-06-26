# Tranche calc

Расчет начисленных процентов за пользование заемными средствами

## Запуск

Для запуска программы необходимо установить требуемые библиотеки:

```
pip install -r requirements.txt
```

Далее запускаем main.py:

```
python main.py
```

Для того чтобы запускать программу через .exe файл, необходимо выполнить следующее:

```
pip show customtkinter
```

Копируем "Location" и вставляем в следующую команду:

```
pyinstaller --noconfirm --onedir --windowed --icon=logo.ico --add-data "<CustomTkinter Location>/customtkinter;customtkinter/" main.py
```

После чего копируем logo.ico в папку /dist/main и запускаем main.exe
