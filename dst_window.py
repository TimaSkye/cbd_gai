from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dst_window(object):
    def setupUi(self, dst_window):
        dst_window.setObjectName("dst_window")
        dst_window.resize(220, 230)
        dst_window.setMinimumSize(QtCore.QSize(220, 230))
        dst_window.setMaximumSize(QtCore.QSize(220, 230))
        self.layoutWidget = QtWidgets.QWidget(parent=dst_window)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dst_find_input = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.dst_find_input.setText("")
        self.dst_find_input.setObjectName("dst_find_input")
        self.verticalLayout.addWidget(self.dst_find_input)
        self.dst_find_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.dst_find_button.setObjectName("dst_find_button")
        self.verticalLayout.addWidget(self.dst_find_button)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.dst_pass_browser = QtWidgets.QTextBrowser(parent=self.layoutWidget)
        self.dst_pass_browser.setObjectName("dst_pass_browser")
        self.verticalLayout.addWidget(self.dst_pass_browser)

        self.retranslateUi(dst_window)
        QtCore.QMetaObject.connectSlotsByName(dst_window)

    def retranslateUi(self, dst_window):
        _translate = QtCore.QCoreApplication.translate
        dst_window.setWindowTitle(_translate("dst_window", "Пароли dst"))
        self.dst_find_input.setPlaceholderText(_translate("dst_window", "Введите наименование dst-файла"))
        self.dst_find_button.setText(_translate("dst_window", "Найти"))
        self.label.setText(_translate("dst_window", "Парольная фраза"))
