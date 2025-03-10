from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_cbd_window(object):
    def setupUi(self, cbd_window):
        cbd_window.setObjectName("cbd_window")
        cbd_window.resize(899, 610)
        cbd_window.setMinimumSize(QtCore.QSize(899, 610))
        cbd_window.setMaximumSize(QtCore.QSize(899, 610))
        self.layoutWidget_3 = QtWidgets.QWidget(parent=cbd_window)
        self.layoutWidget_3.setGeometry(QtCore.QRect(650, 30, 241, 81))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.export_base_button = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_base_button.sizePolicy().hasHeightForWidth())
        self.export_base_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.export_base_button.setFont(font)
        self.export_base_button.setObjectName("export_base_button")
        self.verticalLayout.addWidget(self.export_base_button)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.cbd_table = QtWidgets.QTableWidget(parent=cbd_window)
        self.cbd_table.setGeometry(QtCore.QRect(10, 120, 881, 471))
        self.cbd_table.setObjectName("cbd_table")
        self.cbd_table.setColumnCount(0)
        self.cbd_table.setRowCount(0)
        self.layoutWidget_2 = QtWidgets.QWidget(parent=cbd_window)
        self.layoutWidget_2.setGeometry(QtCore.QRect(11, 31, 291, 81))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.find_base_input = QtWidgets.QLineEdit(parent=self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find_base_input.sizePolicy().hasHeightForWidth())
        self.find_base_input.setSizePolicy(sizePolicy)
        self.find_base_input.setObjectName("find_base_input")
        self.verticalLayout_3.addWidget(self.find_base_input)
        self.find_base_button = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find_base_button.sizePolicy().hasHeightForWidth())
        self.find_base_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.find_base_button.setFont(font)
        self.find_base_button.setObjectName("find_base_button")
        self.verticalLayout_3.addWidget(self.find_base_button)
        self.layoutWidget_4 = QtWidgets.QWidget(parent=cbd_window)
        self.layoutWidget_4.setGeometry(QtCore.QRect(320, 30, 311, 81))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.add_base_button = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_base_button.sizePolicy().hasHeightForWidth())
        self.add_base_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_base_button.setFont(font)
        self.add_base_button.setObjectName("add_base_button")
        self.verticalLayout_2.addWidget(self.add_base_button)
        self.delete_base_button = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_base_button.sizePolicy().hasHeightForWidth())
        self.delete_base_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_base_button.setFont(font)
        self.delete_base_button.setObjectName("delete_base_button")
        self.verticalLayout_2.addWidget(self.delete_base_button)
        self.cbd_status_label = QtWidgets.QLabel(parent=cbd_window)
        self.cbd_status_label.setGeometry(QtCore.QRect(10, 590, 881, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.cbd_status_label.setFont(font)
        self.cbd_status_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.cbd_status_label.setObjectName("cbd_status_label")
        self.layoutWidget = QtWidgets.QWidget(parent=cbd_window)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 1, 881, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ip_base_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ip_base_button.sizePolicy().hasHeightForWidth())
        self.ip_base_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ip_base_button.setFont(font)
        self.ip_base_button.setObjectName("ip_base_button")
        self.horizontalLayout.addWidget(self.ip_base_button)
        self.personal_base_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personal_base_button.sizePolicy().hasHeightForWidth())
        self.personal_base_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.personal_base_button.setFont(font)
        self.personal_base_button.setObjectName("personal_base_button")
        self.horizontalLayout.addWidget(self.personal_base_button)
        self.inventory_base_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inventory_base_button.sizePolicy().hasHeightForWidth())
        self.inventory_base_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inventory_base_button.setFont(font)
        self.inventory_base_button.setObjectName("inventory_base_button")
        self.horizontalLayout.addWidget(self.inventory_base_button)
        self.skzi_base_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skzi_base_button.sizePolicy().hasHeightForWidth())
        self.skzi_base_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.skzi_base_button.setFont(font)
        self.skzi_base_button.setObjectName("skzi_base_button")
        self.horizontalLayout.addWidget(self.skzi_base_button)

        self.retranslateUi(cbd_window)
        QtCore.QMetaObject.connectSlotsByName(cbd_window)

    def retranslateUi(self, cbd_window):
        _translate = QtCore.QCoreApplication.translate
        cbd_window.setWindowTitle(_translate("cbd_window", "ЦБД ГАИ Челябинск"))
        self.label_3.setText(_translate("cbd_window", "Экспорт из базы данных"))
        self.export_base_button.setText(_translate("cbd_window", "Экспорт в XLS"))
        self.label_4.setText(_translate("cbd_window", "Данные сохранены по адресу C:/CBD/"))
        self.label.setText(_translate("cbd_window", "Поиск по базе данных"))
        self.find_base_input.setPlaceholderText(_translate("cbd_window", "Введите данные для поиска"))
        self.find_base_button.setText(_translate("cbd_window", "Найти данные"))
        self.label_2.setText(_translate("cbd_window", "Редактирование базы данных"))
        self.add_base_button.setText(_translate("cbd_window", "Добавить запись"))
        self.delete_base_button.setText(_translate("cbd_window", "Удалить запись"))
        self.cbd_status_label.setText(_translate("cbd_window", "Статус поделючения к базе данных"))
        self.ip_base_button.setText(_translate("cbd_window", "База IP адресов"))
        self.personal_base_button.setText(_translate("cbd_window", "База личного состава"))
        self.inventory_base_button.setText(_translate("cbd_window", "Подотчеты"))
        self.skzi_base_button.setText(_translate("cbd_window", "Электронные подписи"))
