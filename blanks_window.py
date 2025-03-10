from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_blank_window(object):
    def setupUi(self, blank_window):
        blank_window.setObjectName("blank_window")
        blank_window.resize(509, 69)
        blank_window.setMinimumSize(QtCore.QSize(509, 69))
        blank_window.setMaximumSize(QtCore.QSize(509, 69))
        self.info_label = QtWidgets.QLabel(parent=blank_window)
        self.info_label.setGeometry(QtCore.QRect(10, 40, 401, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setItalic(True)
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=blank_window)
        self.buttonBox.setGeometry(QtCore.QRect(420, 10, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.blanks_combo = QtWidgets.QComboBox(parent=blank_window)
        self.blanks_combo.setGeometry(QtCore.QRect(10, 10, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.blanks_combo.setFont(font)
        self.blanks_combo.setObjectName("blanks_combo")
        self.blanks_combo.addItem("")
        self.blanks_combo.addItem("")
        self.blanks_combo.addItem("")
        self.blanks_combo.addItem("")
        self.blanks_combo.addItem("")

        self.retranslateUi(blank_window)
        QtCore.QMetaObject.connectSlotsByName(blank_window)

    def retranslateUi(self, blank_window):
        _translate = QtCore.QCoreApplication.translate
        blank_window.setWindowTitle(_translate("blank_window", "Шаблоны заявок"))
        self.info_label.setText(
            _translate("blank_window", "Образец заявки будет загружен в рабочую папку по адресу C:\\CBD\\"))
        self.blanks_combo.setItemText(0, _translate("blank_window", "Заявка на создание УЗ пользователей ИСОД МВД РФ"))
        self.blanks_combo.setItemText(1, _translate("blank_window", "Заявка на изменение УЗ пользователей ИСОД МВД РФ"))
        self.blanks_combo.setItemText(2, _translate("blank_window",
                                                    "Заявка на восстановление пароля УЗ пользователей ИСОД МВД РФ"))
        self.blanks_combo.setItemText(3, _translate("blank_window",
                                                    "Заявка и письмо на добавление пользователей ФИС ГИБДД-М"))
        self.blanks_combo.setItemText(4, _translate("blank_window",
                                                    "Заявка и письмо на добавление пользователей АИУС, МИАС"))
