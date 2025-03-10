from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_error_dialog(object):
    def setupUi(self, error_dialog):
        error_dialog.setObjectName("error_dialog")
        error_dialog.resize(140, 191)
        error_dialog.setMinimumSize(QtCore.QSize(140, 191))
        error_dialog.setMaximumSize(QtCore.QSize(140, 191))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        error_dialog.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(parent=error_dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 121, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.error_text = QtWidgets.QTextBrowser(parent=self.layoutWidget)
        self.error_text.setObjectName("error_text")
        self.verticalLayout.addWidget(self.error_text)
        self.error_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.error_button.setFont(font)
        self.error_button.setObjectName("error_button")
        self.verticalLayout.addWidget(self.error_button)

        self.retranslateUi(error_dialog)
        QtCore.QMetaObject.connectSlotsByName(error_dialog)

    def retranslateUi(self, error_dialog):
        _translate = QtCore.QCoreApplication.translate
        error_dialog.setWindowTitle(_translate("error_dialog", "Ошибка!"))
        self.label.setText(_translate("error_dialog", "ОШИБКА!"))
        self.error_button.setText(_translate("error_dialog", "Ok"))
