from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(300, 160)
        main_window.setMinimumSize(QtCore.QSize(300, 160))
        main_window.setMaximumSize(QtCore.QSize(300, 160))
        self.gridLayoutWidget = QtWidgets.QWidget(parent=main_window)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 282, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dst_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.dst_button.setFont(font)
        self.dst_button.setObjectName("dst_button")
        self.gridLayout.addWidget(self.dst_button, 5, 0, 1, 1)
        self.instruction_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.instruction_button.setFont(font)
        self.instruction_button.setObjectName("instruction_button")
        self.gridLayout.addWidget(self.instruction_button, 3, 0, 1, 1)
        self.blanks_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.blanks_button.setFont(font)
        self.blanks_button.setObjectName("blanks_button")
        self.gridLayout.addWidget(self.blanks_button, 1, 0, 1, 1)
        self.cbd_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.cbd_button.setFont(font)
        self.cbd_button.setObjectName("cbd_button")
        self.gridLayout.addWidget(self.cbd_button, 0, 0, 1, 1)
        self.po_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.po_button.setFont(font)
        self.po_button.setObjectName("po_button")
        self.gridLayout.addWidget(self.po_button, 4, 0, 1, 1)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "ЦБД ГАИ Челябинск"))
        self.dst_button.setText(_translate("main_window", "Парольные фразы dst"))
        self.instruction_button.setText(_translate("main_window", "Инструкции по установке ПОИБ"))
        self.blanks_button.setText(_translate("main_window", "Шаблоны заявок"))
        self.cbd_button.setText(_translate("main_window", "База данных"))
        self.po_button.setText(_translate("main_window", "Загузить программное обеспечение ИСОД МВД"))
