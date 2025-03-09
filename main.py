import os
import shutil
import sqlite3
import sys
import webbrowser

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QDialog

from blanks_window import Ui_blank_window
from cbd_window import Ui_cbd_window
from dst_window import Ui_dst_window
from error_window import Ui_error_dialog
from login_window import Ui_login_window
from main_window import Ui_main_window

# Глобальные переменные.
OUTPUT_FOLDER = 'C:\\CBD'  # Папка в которую сохраняются все данные из программы.
SRC_FOLDER = os.path.join(os.getcwd(), "src")  # Рабочая папка программы.
CREATOR_URL = 'https://t.me/tima_skye'  # Ссылка на telegram разработчика.


class ErrorWindow(QDialog):
    """Диалоговое окно ошибки."""

    def __init__(self):
        super().__init__()
        # Инициализация UI окна ошибки.
        self.ui = Ui_error_dialog()
        self.ui.setupUi(self)
        # Подключение кнопок.
        self.ui.error_button.clicked.connect(self.close)


class MainAppWindow(QMainWindow):
    """Главное окно программы."""

    def __init__(self):
        super().__init__()
        # Инициализация UI главного рабочего окна.
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        # Подключение UI вспомогательных окон.
        self.cbd_window = CbdAppWindow()
        self.blanks_window = BlanksAppWindow()
        self.dst_window = DstAppWindow()
        # Подключение кнопок.
        self.ui.cbd_button.clicked.connect(self.open_cbd)
        self.ui.blanks_button.clicked.connect(self.open_blanks)
        self.ui.dst_button.clicked.connect(self.open_dst)

    def open_cbd(self):
        """Функция открытия окна ЦБД."""
        self.cbd_window.show()

    def open_blanks(self):
        """Функция отрытия окна с шаблонами."""
        self.blanks_window.show()

    def open_dst(self):
        """Функция открытия окна с паролями dst-файлов."""
        self.dst_window.show()


class LoginAppWindow(QDialog):
    """Окно логина в приложение."""

    def __init__(self):
        super().__init__()
        # Инициализация UI окна логина.
        self.ui = Ui_login_window()
        self.ui.setupUi(self)
        # Подключение UI вспомогательных окон.
        self.error_window = ErrorWindow()
        self.main_window = MainAppWindow()
        # Подключение кнопок.
        self.ui.login_button.clicked.connect(self.auth)
        self.ui.contact_button.clicked.connect(self.telegram_contact)

    def telegram_contact(self):
        """Открывает ссылку на телеграм разработчика программы."""
        webbrowser.open(CREATOR_URL)

    def auth(self):
        """Функция авторизации.
        Необходимо пересмотреть безопасность авторизации."""
        login = self.ui.login_input.text()
        password = self.ui.pass_input.text()
        if login == 'admin' and password == 'admin':
            self.hide()
            self.main_window.show()
        else:
            self.error_window.show()
            self.error_window.ui.error_text.setText(
                'Неверная пара логин/пароль. Введите корректные данные или обратитесь к разработчику.')


class CbdAppWindow(QMainWindow):
    """Окно ЦБД."""

    def __init__(self):
        super().__init__()
        # Инициализация UI окна ЦБД.
        self.ui = Ui_cbd_window()
        self.ui.setupUi(self)


class BlanksAppWindow(QMainWindow):
    """Окно шаблонов заявок."""

    def __init__(self):
        super().__init__()
        # Инициализация UI окна шаблонов заявок.
        self.ui = Ui_blank_window()
        self.ui.setupUi(self)
        # Подключение UI вспомогательных окон.
        self.error_window = ErrorWindow()
        # Подключение кнопок.
        self.ui.buttonBox.accepted.connect(self.save_blank)
        self.ui.buttonBox.rejected.connect(self.close)

    def save_blank(self):
        """Функция сохранения шаблона заявки в рабочую папку."""
        selected_blank = self.ui.blanks_combo.currentIndex()
        try:
            os.makedirs(OUTPUT_FOLDER, exist_ok=True)
            match selected_blank:
                case 0:
                    src_file = os.path.join(SRC_FOLDER, 'Заявка на создание учетных записей пользователей.xls')
                    output_file = os.path.join(OUTPUT_FOLDER, 'Заявка на создание учетных записей пользователей.xls')
                    shutil.copy(src_file, output_file)
                case 1:
                    src_file = os.path.join(SRC_FOLDER, 'Заявка на изменение учетных записей пользователей.xls')
                    output_file = os.path.join(OUTPUT_FOLDER, 'Заявка на изменение учетных записей пользователей.xls')
                    shutil.copy(src_file, output_file)
                case 2:
                    src_file = os.path.join(SRC_FOLDER, 'Заявка на восстановление пароля.xls')
                    output_file = os.path.join(OUTPUT_FOLDER, 'Заявка на восстановление пароля.xls')
                    shutil.copy(src_file, output_file)
                case 3:
                    src_file_blank = os.path.join(SRC_FOLDER, 'На добавление позиций в ФИС.xls')
                    src_file_letter = os.path.join(SRC_FOLDER, 'Сопровод ФИС новый.docx')
                    output_file_blank = os.path.join(OUTPUT_FOLDER, 'На добавление позиций в ФИС.xls')
                    output_file_letter = os.path.join(OUTPUT_FOLDER, 'Сопровод ФИС новый.docx')
                    shutil.copy(src_file_blank, output_file_blank)
                    shutil.copy(src_file_letter, output_file_letter)
                case 4:
                    src_file_blank = os.path.join(SRC_FOLDER, 'Заявка АИУС МИАС.xls')
                    src_file_letter = os.path.join(SRC_FOLDER, 'Сопровод АИУС новый.docx')
                    output_file_blank = os.path.join(OUTPUT_FOLDER, 'Заявка АИУС МИАС.xls')
                    output_file_letter = os.path.join(OUTPUT_FOLDER, 'Сопровод АИУС новый.docx')
                    shutil.copy(src_file_blank, output_file_blank)
                    shutil.copy(src_file_letter, output_file_letter)
        except Exception as e:
            self.error_window.show()
            self.error_window.ui.error_text.setText('Произошла ошибка! Пожалуйста свяжитесь с разработчиком.')


class DstAppWindow(QMainWindow):
    """Окно паролей dst-файлов."""

    def __init__(self):
        super().__init__()
        # Инициализация UI окна паролей dst-файлов.
        self.ui = Ui_dst_window()
        self.ui.setupUi(self)
        # Подключение к БД.
        self.create_connection()
        # Подключение кнопок.
        self.ui.dst_find_button.clicked.connect(self.search_dst)

    def create_connection(self):
        """Функция подключения к БД."""
        self.conn = sqlite3.connect('db.sqlite3')
        self.cursor = self.conn.cursor()

    def search_dst(self):
        """Функция поиска данных из ДБ с выводом."""
        search_text = self.ui.dst_find_input.text().strip().upper()
        if not search_text:
            self.ui.dst_pass_browser.setText('Введите имя dst-файла!')
            return
        try:
            # Ищем частичное совпадение с помощью LIKE
            self.cursor.execute(
                "SELECT name, password FROM dst WHERE name LIKE ?",
                (f'%{search_text}%',)
            )
            results = self.cursor.fetchall()
            if not results:
                self.ui.dst_pass_browser.setText('Совпадений не найдено')
                return
            result_str = "Найдены записи:\n\n"
            for name, password in results:
                result_str += f"Имя: {name}\nПароль: {password}\n\n"
            self.ui.dst_pass_browser.setText(result_str.strip())
        except sqlite3.Error as e:
            self.ui.dst_pass_browser.setText(f'Ошибка базы данных: {str(e)}')

    # def closeEvent(self, event):
    #     """Функция закрытия подключения к БД."""
    #     self.conn.close()
    #     event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginAppWindow()
    login_window.show()
    sys.exit(app.exec())
