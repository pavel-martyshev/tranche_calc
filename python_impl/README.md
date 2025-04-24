# Tranche Calculator

📊 Приложение для расчёта процентов по траншам. Реализовано на Python с использованием библиотеки [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).

---

## 🚀 Возможности

- Ввод суммы, даты поступления и возврата транша, процентной ставки
- Расчет возвращенных процентов на конец заданного периода 

---

## 🛠 Установка и запуск (из исходников)

### 1. Клонируй репозиторий и перейди в проект:

```bash
git clone https://github.com/pavel-martyshev/tranche_calc.git
cd tranche_calc/python_impl
```

### 2. Создай и активируй виртуальное окружение (опционально):

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Установи зависимости:

```bash
pip install -r requirements.txt
```

### 4. Запусти приложение:

```bash
python main.py
```

---

## 📦 Сборка `.exe`

Для сборки Windows-приложения без консоли:

```bash
pyinstaller --noconfirm --onedir --windowed --icon=..\logo.ico --add-data "C:\not_work\tranche_calc\python_impl\venv\Lib\site-packages/customtkinter;customtkinter/" main.py && mkdir .\dist\main\view\settings && copy .\view\settings\settings.json .\dist\main\view\settings\settings.json
```

📌 **Что делает эта команда:**

- `--noconfirm` — не спрашивать подтверждений
- `--onedir` — собрать в папку (а не один `.exe`)
- `--windowed` — не открывать консоль при запуске GUI
- `--icon` — установить иконку для приложения
- `--add-data` — добавить в сборку `customtkinter`
- `mkdir + copy` — вручную добавить `settings.json` в нужное место

После сборки файл можно найти по пути:  
📁 `dist\main\main.exe`

---

## 🔧 Настройки

Файл настроек находится в:
```
view/settings/settings.json
```

Можно изменить:
- Цвета
- Размеры полей
- Шрифты интерфейса

---

## 🧑‍💻 Автор

Разработчик: [@pavel-martyshev](https://github.com/pavel-martyshev)  
