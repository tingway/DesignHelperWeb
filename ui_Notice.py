# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_NoticeFDUwvi.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Notice(object):
    def setupUi(self, Notice):
        if not Notice.objectName():
            Notice.setObjectName(u"Notice")
        Notice.resize(925, 791)
        self.label_4 = QLabel(Notice)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(530, 84, 51, 16))
        self.calendarWidget = QCalendarWidget(Notice)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(30, 20, 261, 161))
        self.tableWidget = QTableWidget(Notice)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(390, 190, 511, 151))
        self.tableWidget.verticalHeader().setVisible(True)
        self.layoutWidget = QWidget(Notice)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(380, 30, 135, 106))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_survey = QLineEdit(self.layoutWidget)
        self.lineEdit_survey.setObjectName(u"lineEdit_survey")

        self.verticalLayout_4.addWidget(self.lineEdit_survey)

        self.lineEdit_start = QLineEdit(self.layoutWidget)
        self.lineEdit_start.setObjectName(u"lineEdit_start")

        self.verticalLayout_4.addWidget(self.lineEdit_start)

        self.lineEdit_submit = QLineEdit(self.layoutWidget)
        self.lineEdit_submit.setObjectName(u"lineEdit_submit")

        self.verticalLayout_4.addWidget(self.lineEdit_submit)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_expect = QLineEdit(self.layoutWidget)
        self.lineEdit_expect.setObjectName(u"lineEdit_expect")

        self.horizontalLayout_5.addWidget(self.lineEdit_expect)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.comboBox = QComboBox(Notice)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(590, 30, 69, 21))
        self.layoutWidget_2 = QWidget(Notice)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(300, 30, 76, 101))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.radioButton_survey = QRadioButton(self.layoutWidget_2)
        self.radioButton_survey.setObjectName(u"radioButton_survey")

        self.verticalLayout_5.addWidget(self.radioButton_survey)

        self.radioButton_start = QRadioButton(self.layoutWidget_2)
        self.radioButton_start.setObjectName(u"radioButton_start")

        self.verticalLayout_5.addWidget(self.radioButton_start)

        self.radioButton_submit = QRadioButton(self.layoutWidget_2)
        self.radioButton_submit.setObjectName(u"radioButton_submit")

        self.verticalLayout_5.addWidget(self.radioButton_submit)

        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.label)

        self.tableWidget_3 = QTableWidget(Notice)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(300, 350, 601, 291))
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.label_6 = QLabel(Notice)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(310, 150, 48, 16))
        self.layoutWidget_3 = QWidget(Notice)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(760, 90, 131, 23))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_noticeNo = QLineEdit(self.layoutWidget_3)
        self.lineEdit_noticeNo.setObjectName(u"lineEdit_noticeNo")

        self.horizontalLayout_4.addWidget(self.lineEdit_noticeNo)

        self.label_7 = QLabel(self.layoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.layoutWidget_4 = QWidget(Notice)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(590, 87, 152, 50))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_4 = QRadioButton(self.layoutWidget_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setCheckable(True)
        self.radioButton_4.setChecked(False)

        self.horizontalLayout_2.addWidget(self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.layoutWidget_4)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_2.addWidget(self.radioButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_5 = QRadioButton(self.layoutWidget_4)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.layoutWidget_4)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_3.addWidget(self.radioButton_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.layoutWidget_5 = QWidget(Notice)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(590, 57, 126, 21))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.layoutWidget_5)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.layoutWidget_5)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.label_3 = QLabel(Notice)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(530, 57, 51, 16))
        self.tabWidget = QTabWidget(Notice)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 190, 261, 501))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget_6 = QWidget(self.tab)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(11, 0, 234, 461))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_structureType0 = QLabel(self.layoutWidget_6)
        self.label_structureType0.setObjectName(u"label_structureType0")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_structureType0.sizePolicy().hasHeightForWidth())
        self.label_structureType0.setSizePolicy(sizePolicy1)
        self.label_structureType0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_34.addWidget(self.label_structureType0)

        self.comboBox_structureType0 = QComboBox(self.layoutWidget_6)
        self.comboBox_structureType0.addItem("")
        self.comboBox_structureType0.addItem("")
        self.comboBox_structureType0.addItem("")
        self.comboBox_structureType0.addItem("")
        self.comboBox_structureType0.setObjectName(u"comboBox_structureType0")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_structureType0.sizePolicy().hasHeightForWidth())
        self.comboBox_structureType0.setSizePolicy(sizePolicy2)
        self.comboBox_structureType0.setMaximumSize(QSize(136, 16777215))

        self.horizontalLayout_34.addWidget(self.comboBox_structureType0)

        self.label_57 = QLabel(self.layoutWidget_6)
        self.label_57.setObjectName(u"label_57")
        sizePolicy2.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy2)
        self.label_57.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_34.addWidget(self.label_57)


        self.verticalLayout_2.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_caseType0 = QLabel(self.layoutWidget_6)
        self.label_caseType0.setObjectName(u"label_caseType0")
        sizePolicy1.setHeightForWidth(self.label_caseType0.sizePolicy().hasHeightForWidth())
        self.label_caseType0.setSizePolicy(sizePolicy1)
        self.label_caseType0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_35.addWidget(self.label_caseType0)

        self.label_caseType0_2 = QLabel(self.layoutWidget_6)
        self.label_caseType0_2.setObjectName(u"label_caseType0_2")
        sizePolicy2.setHeightForWidth(self.label_caseType0_2.sizePolicy().hasHeightForWidth())
        self.label_caseType0_2.setSizePolicy(sizePolicy2)
        self.label_caseType0_2.setMaximumSize(QSize(136, 16777215))

        self.horizontalLayout_35.addWidget(self.label_caseType0_2)

        self.label_56 = QLabel(self.layoutWidget_6)
        self.label_56.setObjectName(u"label_56")
        sizePolicy2.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy2)
        self.label_56.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_35.addWidget(self.label_56)


        self.verticalLayout_2.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.checkBox_multipleNO = QCheckBox(self.layoutWidget_6)
        self.checkBox_multipleNO.setObjectName(u"checkBox_multipleNO")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.checkBox_multipleNO.sizePolicy().hasHeightForWidth())
        self.checkBox_multipleNO.setSizePolicy(sizePolicy3)
        self.checkBox_multipleNO.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_36.addWidget(self.checkBox_multipleNO)

        self.lineEdit_multipleNO = QLineEdit(self.layoutWidget_6)
        self.lineEdit_multipleNO.setObjectName(u"lineEdit_multipleNO")
        self.lineEdit_multipleNO.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.lineEdit_multipleNO.sizePolicy().hasHeightForWidth())
        self.lineEdit_multipleNO.setSizePolicy(sizePolicy2)
        self.lineEdit_multipleNO.setMaximumSize(QSize(136, 16777215))

        self.horizontalLayout_36.addWidget(self.lineEdit_multipleNO)

        self.label_55 = QLabel(self.layoutWidget_6)
        self.label_55.setObjectName(u"label_55")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy4)

        self.horizontalLayout_36.addWidget(self.label_55)


        self.verticalLayout_2.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_workType0 = QLabel(self.layoutWidget_6)
        self.label_workType0.setObjectName(u"label_workType0")
        sizePolicy1.setHeightForWidth(self.label_workType0.sizePolicy().hasHeightForWidth())
        self.label_workType0.setSizePolicy(sizePolicy1)
        self.label_workType0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_37.addWidget(self.label_workType0)

        self.comboBox_workType0 = QComboBox(self.layoutWidget_6)
        self.comboBox_workType0.addItem("")
        self.comboBox_workType0.addItem("")
        self.comboBox_workType0.setObjectName(u"comboBox_workType0")
        sizePolicy2.setHeightForWidth(self.comboBox_workType0.sizePolicy().hasHeightForWidth())
        self.comboBox_workType0.setSizePolicy(sizePolicy2)
        self.comboBox_workType0.setMaximumSize(QSize(136, 16777215))

        self.horizontalLayout_37.addWidget(self.comboBox_workType0)

        self.label_58 = QLabel(self.layoutWidget_6)
        self.label_58.setObjectName(u"label_58")
        sizePolicy2.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy2)
        self.label_58.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_37.addWidget(self.label_58)


        self.verticalLayout_2.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_oldType0 = QLabel(self.layoutWidget_6)
        self.label_oldType0.setObjectName(u"label_oldType0")
        sizePolicy1.setHeightForWidth(self.label_oldType0.sizePolicy().hasHeightForWidth())
        self.label_oldType0.setSizePolicy(sizePolicy1)
        self.label_oldType0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_38.addWidget(self.label_oldType0)

        self.comboBox_oldType0 = QComboBox(self.layoutWidget_6)
        self.comboBox_oldType0.addItem("")
        self.comboBox_oldType0.addItem("")
        self.comboBox_oldType0.addItem("")
        self.comboBox_oldType0.setObjectName(u"comboBox_oldType0")
        sizePolicy4.setHeightForWidth(self.comboBox_oldType0.sizePolicy().hasHeightForWidth())
        self.comboBox_oldType0.setSizePolicy(sizePolicy4)

        self.horizontalLayout_38.addWidget(self.comboBox_oldType0)

        self.label_59 = QLabel(self.layoutWidget_6)
        self.label_59.setObjectName(u"label_59")
        sizePolicy2.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy2)
        self.label_59.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_38.addWidget(self.label_59)


        self.verticalLayout_2.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_outerFrame0 = QLabel(self.layoutWidget_6)
        self.label_outerFrame0.setObjectName(u"label_outerFrame0")
        sizePolicy1.setHeightForWidth(self.label_outerFrame0.sizePolicy().hasHeightForWidth())
        self.label_outerFrame0.setSizePolicy(sizePolicy1)
        self.label_outerFrame0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_39.addWidget(self.label_outerFrame0)

        self.comboBox_outerFrame = QComboBox(self.layoutWidget_6)
        self.comboBox_outerFrame.addItem("")
        self.comboBox_outerFrame.addItem("")
        self.comboBox_outerFrame.setObjectName(u"comboBox_outerFrame")
        sizePolicy4.setHeightForWidth(self.comboBox_outerFrame.sizePolicy().hasHeightForWidth())
        self.comboBox_outerFrame.setSizePolicy(sizePolicy4)

        self.horizontalLayout_39.addWidget(self.comboBox_outerFrame)

        self.label_60 = QLabel(self.layoutWidget_6)
        self.label_60.setObjectName(u"label_60")
        sizePolicy2.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy2)
        self.label_60.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_39.addWidget(self.label_60)


        self.verticalLayout_2.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_length0 = QLabel(self.layoutWidget_6)
        self.label_length0.setObjectName(u"label_length0")
        sizePolicy1.setHeightForWidth(self.label_length0.sizePolicy().hasHeightForWidth())
        self.label_length0.setSizePolicy(sizePolicy1)
        self.label_length0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_40.addWidget(self.label_length0)

        self.lineEdit_length0 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_length0.setObjectName(u"lineEdit_length0")
        sizePolicy4.setHeightForWidth(self.lineEdit_length0.sizePolicy().hasHeightForWidth())
        self.lineEdit_length0.setSizePolicy(sizePolicy4)
        self.lineEdit_length0.setMaximumSize(QSize(136, 16777215))

        self.horizontalLayout_40.addWidget(self.lineEdit_length0)

        self.label_49 = QLabel(self.layoutWidget_6)
        self.label_49.setObjectName(u"label_49")
        sizePolicy4.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy4)
        self.label_49.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_40.addWidget(self.label_49)


        self.verticalLayout_2.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_depthName0 = QLabel(self.layoutWidget_6)
        self.label_depthName0.setObjectName(u"label_depthName0")
        sizePolicy1.setHeightForWidth(self.label_depthName0.sizePolicy().hasHeightForWidth())
        self.label_depthName0.setSizePolicy(sizePolicy1)
        self.label_depthName0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_43.addWidget(self.label_depthName0)

        self.lineEdit_Depth0 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_Depth0.setObjectName(u"lineEdit_Depth0")
        sizePolicy2.setHeightForWidth(self.lineEdit_Depth0.sizePolicy().hasHeightForWidth())
        self.lineEdit_Depth0.setSizePolicy(sizePolicy2)
        self.lineEdit_Depth0.setMaximumSize(QSize(133, 16777215))

        self.horizontalLayout_43.addWidget(self.lineEdit_Depth0)

        self.label_45 = QLabel(self.layoutWidget_6)
        self.label_45.setObjectName(u"label_45")
        sizePolicy2.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy2)
        self.label_45.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_43.addWidget(self.label_45)


        self.verticalLayout_2.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_WidthName0 = QLabel(self.layoutWidget_6)
        self.label_WidthName0.setObjectName(u"label_WidthName0")
        sizePolicy1.setHeightForWidth(self.label_WidthName0.sizePolicy().hasHeightForWidth())
        self.label_WidthName0.setSizePolicy(sizePolicy1)
        self.label_WidthName0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_42.addWidget(self.label_WidthName0)

        self.lineEdit_Width0 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_Width0.setObjectName(u"lineEdit_Width0")
        sizePolicy2.setHeightForWidth(self.lineEdit_Width0.sizePolicy().hasHeightForWidth())
        self.lineEdit_Width0.setSizePolicy(sizePolicy2)
        self.lineEdit_Width0.setMaximumSize(QSize(133, 16777215))

        self.horizontalLayout_42.addWidget(self.lineEdit_Width0)

        self.label_44 = QLabel(self.layoutWidget_6)
        self.label_44.setObjectName(u"label_44")
        sizePolicy2.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy2)
        self.label_44.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_42.addWidget(self.label_44)


        self.verticalLayout_2.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_WallThick0 = QLabel(self.layoutWidget_6)
        self.label_WallThick0.setObjectName(u"label_WallThick0")
        sizePolicy1.setHeightForWidth(self.label_WallThick0.sizePolicy().hasHeightForWidth())
        self.label_WallThick0.setSizePolicy(sizePolicy1)
        self.label_WallThick0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_41.addWidget(self.label_WallThick0)

        self.lineEdit_WallThick0 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_WallThick0.setObjectName(u"lineEdit_WallThick0")
        sizePolicy2.setHeightForWidth(self.lineEdit_WallThick0.sizePolicy().hasHeightForWidth())
        self.lineEdit_WallThick0.setSizePolicy(sizePolicy2)
        self.lineEdit_WallThick0.setMaximumSize(QSize(133, 16777215))

        self.horizontalLayout_41.addWidget(self.lineEdit_WallThick0)

        self.label_43 = QLabel(self.layoutWidget_6)
        self.label_43.setObjectName(u"label_43")
        sizePolicy2.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy2)
        self.label_43.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_41.addWidget(self.label_43)


        self.verticalLayout_2.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.checkBox_depthRange = QCheckBox(self.layoutWidget_6)
        self.checkBox_depthRange.setObjectName(u"checkBox_depthRange")
        sizePolicy3.setHeightForWidth(self.checkBox_depthRange.sizePolicy().hasHeightForWidth())
        self.checkBox_depthRange.setSizePolicy(sizePolicy3)
        self.checkBox_depthRange.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_44.addWidget(self.checkBox_depthRange)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_depthRange1 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_depthRange1.setObjectName(u"lineEdit_depthRange1")
        self.lineEdit_depthRange1.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.lineEdit_depthRange1.sizePolicy().hasHeightForWidth())
        self.lineEdit_depthRange1.setSizePolicy(sizePolicy3)
        self.lineEdit_depthRange1.setMaximumSize(QSize(29, 21))
        self.lineEdit_depthRange1.setBaseSize(QSize(29, 21))

        self.horizontalLayout_6.addWidget(self.lineEdit_depthRange1)

        self.label_53 = QLabel(self.layoutWidget_6)
        self.label_53.setObjectName(u"label_53")
        sizePolicy3.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy3)
        self.label_53.setMaximumSize(QSize(9, 21))

        self.horizontalLayout_6.addWidget(self.label_53)

        self.lineEdit_depthRange2 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_depthRange2.setObjectName(u"lineEdit_depthRange2")
        self.lineEdit_depthRange2.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.lineEdit_depthRange2.sizePolicy().hasHeightForWidth())
        self.lineEdit_depthRange2.setSizePolicy(sizePolicy3)
        self.lineEdit_depthRange2.setMaximumSize(QSize(29, 21))

        self.horizontalLayout_6.addWidget(self.lineEdit_depthRange2)


        self.horizontalLayout_44.addLayout(self.horizontalLayout_6)

        self.label_54 = QLabel(self.layoutWidget_6)
        self.label_54.setObjectName(u"label_54")
        sizePolicy2.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy2)
        self.label_54.setMaximumSize(QSize(43, 16777215))

        self.horizontalLayout_44.addWidget(self.label_54)


        self.verticalLayout_2.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_oldDepth0 = QLabel(self.layoutWidget_6)
        self.label_oldDepth0.setObjectName(u"label_oldDepth0")
        self.label_oldDepth0.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.label_oldDepth0.sizePolicy().hasHeightForWidth())
        self.label_oldDepth0.setSizePolicy(sizePolicy1)
        self.label_oldDepth0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_46.addWidget(self.label_oldDepth0)

        self.lineEdit_oldDepth0 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_oldDepth0.setObjectName(u"lineEdit_oldDepth0")
        self.lineEdit_oldDepth0.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.lineEdit_oldDepth0.sizePolicy().hasHeightForWidth())
        self.lineEdit_oldDepth0.setSizePolicy(sizePolicy2)
        self.lineEdit_oldDepth0.setMaximumSize(QSize(133, 16777215))

        self.horizontalLayout_46.addWidget(self.lineEdit_oldDepth0)

        self.label_47 = QLabel(self.layoutWidget_6)
        self.label_47.setObjectName(u"label_47")
        sizePolicy2.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy2)
        self.label_47.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_46.addWidget(self.label_47)


        self.verticalLayout_2.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_oldWidth0 = QLabel(self.layoutWidget_6)
        self.label_oldWidth0.setObjectName(u"label_oldWidth0")
        self.label_oldWidth0.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.label_oldWidth0.sizePolicy().hasHeightForWidth())
        self.label_oldWidth0.setSizePolicy(sizePolicy1)
        self.label_oldWidth0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_45.addWidget(self.label_oldWidth0)

        self.lineEdit_oldWidth0 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_oldWidth0.setObjectName(u"lineEdit_oldWidth0")
        self.lineEdit_oldWidth0.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.lineEdit_oldWidth0.sizePolicy().hasHeightForWidth())
        self.lineEdit_oldWidth0.setSizePolicy(sizePolicy2)
        self.lineEdit_oldWidth0.setMaximumSize(QSize(133, 16777215))

        self.horizontalLayout_45.addWidget(self.lineEdit_oldWidth0)

        self.label_46 = QLabel(self.layoutWidget_6)
        self.label_46.setObjectName(u"label_46")
        sizePolicy2.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy2)
        self.label_46.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_45.addWidget(self.label_46)


        self.verticalLayout_2.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_oldWallThick0 = QLabel(self.layoutWidget_6)
        self.label_oldWallThick0.setObjectName(u"label_oldWallThick0")
        self.label_oldWallThick0.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.label_oldWallThick0.sizePolicy().hasHeightForWidth())
        self.label_oldWallThick0.setSizePolicy(sizePolicy1)
        self.label_oldWallThick0.setMaximumSize(QSize(71, 16777215))

        self.horizontalLayout_47.addWidget(self.label_oldWallThick0)

        self.lineEdit_oldWallThick0 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_oldWallThick0.setObjectName(u"lineEdit_oldWallThick0")
        self.lineEdit_oldWallThick0.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.lineEdit_oldWallThick0.sizePolicy().hasHeightForWidth())
        self.lineEdit_oldWallThick0.setSizePolicy(sizePolicy2)
        self.lineEdit_oldWallThick0.setMaximumSize(QSize(133, 16777215))

        self.horizontalLayout_47.addWidget(self.lineEdit_oldWallThick0)

        self.label_48 = QLabel(self.layoutWidget_6)
        self.label_48.setObjectName(u"label_48")
        sizePolicy2.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy2)
        self.label_48.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_47.addWidget(self.label_48)


        self.verticalLayout_2.addLayout(self.horizontalLayout_47)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_50 = QLabel(self.tab_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(230, 230, 21, 41))
        self.label_66 = QLabel(self.tab_2)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(230, 280, 21, 41))
        self.layoutWidget1 = QWidget(self.tab_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(12, 2, 211, 451))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_structureType1 = QLabel(self.layoutWidget1)
        self.label_structureType1.setObjectName(u"label_structureType1")

        self.horizontalLayout_25.addWidget(self.label_structureType1)

        self.comboBox_structureType1 = QComboBox(self.layoutWidget1)
        self.comboBox_structureType1.addItem("")
        self.comboBox_structureType1.addItem("")
        self.comboBox_structureType1.addItem("")
        self.comboBox_structureType1.setObjectName(u"comboBox_structureType1")
        sizePolicy4.setHeightForWidth(self.comboBox_structureType1.sizePolicy().hasHeightForWidth())
        self.comboBox_structureType1.setSizePolicy(sizePolicy4)

        self.horizontalLayout_25.addWidget(self.comboBox_structureType1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_caseType1 = QLabel(self.layoutWidget1)
        self.label_caseType1.setObjectName(u"label_caseType1")

        self.horizontalLayout_26.addWidget(self.label_caseType1)

        self.label_caseType1_2 = QLabel(self.layoutWidget1)
        self.label_caseType1_2.setObjectName(u"label_caseType1_2")
        sizePolicy4.setHeightForWidth(self.label_caseType1_2.sizePolicy().hasHeightForWidth())
        self.label_caseType1_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_26.addWidget(self.label_caseType1_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.checkBox_multipleNO_2 = QCheckBox(self.layoutWidget1)
        self.checkBox_multipleNO_2.setObjectName(u"checkBox_multipleNO_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.checkBox_multipleNO_2.sizePolicy().hasHeightForWidth())
        self.checkBox_multipleNO_2.setSizePolicy(sizePolicy5)
        self.checkBox_multipleNO_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_57.addWidget(self.checkBox_multipleNO_2)

        self.lineEdit_multipleNO_2 = QLineEdit(self.layoutWidget1)
        self.lineEdit_multipleNO_2.setObjectName(u"lineEdit_multipleNO_2")
        self.lineEdit_multipleNO_2.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.lineEdit_multipleNO_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_multipleNO_2.setSizePolicy(sizePolicy4)
        self.lineEdit_multipleNO_2.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_57.addWidget(self.lineEdit_multipleNO_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_workType1 = QLabel(self.layoutWidget1)
        self.label_workType1.setObjectName(u"label_workType1")

        self.horizontalLayout_27.addWidget(self.label_workType1)

        self.comboBox_workType1 = QComboBox(self.layoutWidget1)
        self.comboBox_workType1.addItem("")
        self.comboBox_workType1.addItem("")
        self.comboBox_workType1.setObjectName(u"comboBox_workType1")
        sizePolicy4.setHeightForWidth(self.comboBox_workType1.sizePolicy().hasHeightForWidth())
        self.comboBox_workType1.setSizePolicy(sizePolicy4)

        self.horizontalLayout_27.addWidget(self.comboBox_workType1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_coverType1 = QLabel(self.layoutWidget1)
        self.label_coverType1.setObjectName(u"label_coverType1")

        self.horizontalLayout_28.addWidget(self.label_coverType1)

        self.comboBox_coverType1 = QComboBox(self.layoutWidget1)
        self.comboBox_coverType1.addItem("")
        self.comboBox_coverType1.addItem("")
        self.comboBox_coverType1.addItem("")
        self.comboBox_coverType1.addItem("")
        self.comboBox_coverType1.setObjectName(u"comboBox_coverType1")
        sizePolicy4.setHeightForWidth(self.comboBox_coverType1.sizePolicy().hasHeightForWidth())
        self.comboBox_coverType1.setSizePolicy(sizePolicy4)

        self.horizontalLayout_28.addWidget(self.comboBox_coverType1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_Lenth1 = QLabel(self.layoutWidget1)
        self.label_Lenth1.setObjectName(u"label_Lenth1")

        self.horizontalLayout_29.addWidget(self.label_Lenth1)

        self.lineEdit_Lenth1 = QLineEdit(self.layoutWidget1)
        self.lineEdit_Lenth1.setObjectName(u"lineEdit_Lenth1")
        sizePolicy2.setHeightForWidth(self.lineEdit_Lenth1.sizePolicy().hasHeightForWidth())
        self.lineEdit_Lenth1.setSizePolicy(sizePolicy2)
        self.lineEdit_Lenth1.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_29.addWidget(self.lineEdit_Lenth1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_coverWidthName = QLabel(self.layoutWidget1)
        self.label_coverWidthName.setObjectName(u"label_coverWidthName")

        self.horizontalLayout_30.addWidget(self.label_coverWidthName)

        self.lineEdit_coverWidth = QLineEdit(self.layoutWidget1)
        self.lineEdit_coverWidth.setObjectName(u"lineEdit_coverWidth")
        sizePolicy2.setHeightForWidth(self.lineEdit_coverWidth.sizePolicy().hasHeightForWidth())
        self.lineEdit_coverWidth.setSizePolicy(sizePolicy2)
        self.lineEdit_coverWidth.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_30.addWidget(self.lineEdit_coverWidth)


        self.verticalLayout_6.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_coverThickName = QLabel(self.layoutWidget1)
        self.label_coverThickName.setObjectName(u"label_coverThickName")

        self.horizontalLayout_31.addWidget(self.label_coverThickName)

        self.comboBox_coverThick = QComboBox(self.layoutWidget1)
        self.comboBox_coverThick.addItem("")
        self.comboBox_coverThick.addItem("")
        self.comboBox_coverThick.setObjectName(u"comboBox_coverThick")
        sizePolicy4.setHeightForWidth(self.comboBox_coverThick.sizePolicy().hasHeightForWidth())
        self.comboBox_coverThick.setSizePolicy(sizePolicy4)

        self.horizontalLayout_31.addWidget(self.comboBox_coverThick)


        self.verticalLayout_6.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_grilleWidth = QLabel(self.layoutWidget1)
        self.label_grilleWidth.setObjectName(u"label_grilleWidth")
        self.label_grilleWidth.setEnabled(False)

        self.horizontalLayout_32.addWidget(self.label_grilleWidth)

        self.comboBox_grilleWidth = QComboBox(self.layoutWidget1)
        self.comboBox_grilleWidth.addItem("")
        self.comboBox_grilleWidth.addItem("")
        self.comboBox_grilleWidth.addItem("")
        self.comboBox_grilleWidth.setObjectName(u"comboBox_grilleWidth")
        self.comboBox_grilleWidth.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.comboBox_grilleWidth.sizePolicy().hasHeightForWidth())
        self.comboBox_grilleWidth.setSizePolicy(sizePolicy4)

        self.horizontalLayout_32.addWidget(self.comboBox_grilleWidth)


        self.verticalLayout_6.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_grilleType = QLabel(self.layoutWidget1)
        self.label_grilleType.setObjectName(u"label_grilleType")
        self.label_grilleType.setEnabled(False)

        self.horizontalLayout_33.addWidget(self.label_grilleType)

        self.comboBox_grilleType = QComboBox(self.layoutWidget1)
        self.comboBox_grilleType.addItem("")
        self.comboBox_grilleType.addItem("")
        self.comboBox_grilleType.setObjectName(u"comboBox_grilleType")
        self.comboBox_grilleType.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.comboBox_grilleType.sizePolicy().hasHeightForWidth())
        self.comboBox_grilleType.setSizePolicy(sizePolicy4)

        self.horizontalLayout_33.addWidget(self.comboBox_grilleType)


        self.verticalLayout_6.addLayout(self.horizontalLayout_33)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tableWidget_2 = QTableWidget(self.tab_8)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        if (self.tableWidget_2.rowCount() < 3):
            self.tableWidget_2.setRowCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem11)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 230, 231, 191))
        self.layoutWidget_8 = QWidget(self.tab_8)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(11, 11, 241, 211))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_27 = QLabel(self.layoutWidget_8)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_48.addWidget(self.label_27)

        self.comboBox_recoverType = QComboBox(self.layoutWidget_8)
        self.comboBox_recoverType.addItem("")
        self.comboBox_recoverType.addItem("")
        self.comboBox_recoverType.setObjectName(u"comboBox_recoverType")

        self.horizontalLayout_48.addWidget(self.comboBox_recoverType)

        self.label_62 = QLabel(self.layoutWidget_8)
        self.label_62.setObjectName(u"label_62")
        sizePolicy1.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy1)
        self.label_62.setMaximumSize(QSize(13, 16777215))

        self.horizontalLayout_48.addWidget(self.label_62)


        self.verticalLayout_3.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_37 = QLabel(self.layoutWidget_8)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_49.addWidget(self.label_37)

        self.label_caseType2_2 = QLabel(self.layoutWidget_8)
        self.label_caseType2_2.setObjectName(u"label_caseType2_2")
        sizePolicy.setHeightForWidth(self.label_caseType2_2.sizePolicy().hasHeightForWidth())
        self.label_caseType2_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_49.addWidget(self.label_caseType2_2)

        self.label_63 = QLabel(self.layoutWidget_8)
        self.label_63.setObjectName(u"label_63")
        sizePolicy1.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy1)
        self.label_63.setMaximumSize(QSize(13, 16777215))

        self.horizontalLayout_49.addWidget(self.label_63)


        self.verticalLayout_3.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_38 = QLabel(self.layoutWidget_8)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_50.addWidget(self.label_38)

        self.comboBox_materialType = QComboBox(self.layoutWidget_8)
        self.comboBox_materialType.addItem("")
        self.comboBox_materialType.addItem("")
        self.comboBox_materialType.setObjectName(u"comboBox_materialType")

        self.horizontalLayout_50.addWidget(self.comboBox_materialType)

        self.label_61 = QLabel(self.layoutWidget_8)
        self.label_61.setObjectName(u"label_61")
        sizePolicy1.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy1)
        self.label_61.setMaximumSize(QSize(13, 16777215))

        self.horizontalLayout_50.addWidget(self.label_61)


        self.verticalLayout_3.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_39 = QLabel(self.layoutWidget_8)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_51.addWidget(self.label_39)

        self.comboBox_recoverThick = QComboBox(self.layoutWidget_8)
        self.comboBox_recoverThick.addItem("")
        self.comboBox_recoverThick.addItem("")
        self.comboBox_recoverThick.setObjectName(u"comboBox_recoverThick")

        self.horizontalLayout_51.addWidget(self.comboBox_recoverThick)

        self.label_64 = QLabel(self.layoutWidget_8)
        self.label_64.setObjectName(u"label_64")
        sizePolicy1.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy1)
        self.label_64.setMaximumSize(QSize(13, 16777215))

        self.horizontalLayout_51.addWidget(self.label_64)


        self.verticalLayout_3.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_lengthFormula = QLabel(self.layoutWidget_8)
        self.label_lengthFormula.setObjectName(u"label_lengthFormula")

        self.horizontalLayout_52.addWidget(self.label_lengthFormula)

        self.lineEdit_lengthFormula = QLineEdit(self.layoutWidget_8)
        self.lineEdit_lengthFormula.setObjectName(u"lineEdit_lengthFormula")
        sizePolicy3.setHeightForWidth(self.lineEdit_lengthFormula.sizePolicy().hasHeightForWidth())
        self.lineEdit_lengthFormula.setSizePolicy(sizePolicy3)
        self.lineEdit_lengthFormula.setMaximumSize(QSize(106, 16777215))

        self.horizontalLayout_52.addWidget(self.lineEdit_lengthFormula)

        self.label_51 = QLabel(self.layoutWidget_8)
        self.label_51.setObjectName(u"label_51")
        sizePolicy1.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy1)
        self.label_51.setMaximumSize(QSize(13, 16777215))

        self.horizontalLayout_52.addWidget(self.label_51)


        self.verticalLayout_3.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_recoverWidth = QLabel(self.layoutWidget_8)
        self.label_recoverWidth.setObjectName(u"label_recoverWidth")

        self.horizontalLayout_53.addWidget(self.label_recoverWidth)

        self.lineEdit_recoverWidth = QLineEdit(self.layoutWidget_8)
        self.lineEdit_recoverWidth.setObjectName(u"lineEdit_recoverWidth")
        self.lineEdit_recoverWidth.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_recoverWidth.sizePolicy().hasHeightForWidth())
        self.lineEdit_recoverWidth.setSizePolicy(sizePolicy3)
        self.lineEdit_recoverWidth.setMaximumSize(QSize(106, 16777215))

        self.horizontalLayout_53.addWidget(self.lineEdit_recoverWidth)

        self.label_52 = QLabel(self.layoutWidget_8)
        self.label_52.setObjectName(u"label_52")
        sizePolicy1.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy1)
        self.label_52.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_53.addWidget(self.label_52)


        self.verticalLayout_3.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_42 = QLabel(self.layoutWidget_8)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_54.addWidget(self.label_42)

        self.pushButton_4 = QPushButton(self.layoutWidget_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy3.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy3)
        self.pushButton_4.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_54.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy3.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy3)
        self.pushButton_5.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_54.addWidget(self.pushButton_5)

        self.label_65 = QLabel(self.layoutWidget_8)
        self.label_65.setObjectName(u"label_65")
        sizePolicy1.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy1)
        self.label_65.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_54.addWidget(self.label_65)


        self.verticalLayout_3.addLayout(self.horizontalLayout_54)

        self.layoutWidget2 = QWidget(self.tab_8)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(5, 430, 231, 22))
        self.horizontalLayout_56 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.checkBox_colorCover = QCheckBox(self.layoutWidget2)
        self.checkBox_colorCover.setObjectName(u"checkBox_colorCover")
        self.checkBox_colorCover.setMaximumSize(QSize(16777215, 18))
        self.checkBox_colorCover.setChecked(False)

        self.horizontalLayout_56.addWidget(self.checkBox_colorCover)

        self.lineEdit_colorCover = QLineEdit(self.layoutWidget2)
        self.lineEdit_colorCover.setObjectName(u"lineEdit_colorCover")
        self.lineEdit_colorCover.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_colorCover.sizePolicy().hasHeightForWidth())
        self.lineEdit_colorCover.setSizePolicy(sizePolicy3)
        self.lineEdit_colorCover.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_56.addWidget(self.lineEdit_colorCover)

        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.layoutWidget_9 = QWidget(self.tab_9)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(0, 0, 259, 500))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_cuttingAC = QCheckBox(self.layoutWidget_9)
        self.checkBox_cuttingAC.setObjectName(u"checkBox_cuttingAC")
        self.checkBox_cuttingAC.setMaximumSize(QSize(16777215, 18))
        self.checkBox_cuttingAC.setChecked(True)

        self.horizontalLayout_7.addWidget(self.checkBox_cuttingAC)

        self.lineEdit_cuttingAC = QLineEdit(self.layoutWidget_9)
        self.lineEdit_cuttingAC.setObjectName(u"lineEdit_cuttingAC")
        self.lineEdit_cuttingAC.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_cuttingAC.sizePolicy().hasHeightForWidth())
        self.lineEdit_cuttingAC.setSizePolicy(sizePolicy3)
        self.lineEdit_cuttingAC.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_7.addWidget(self.lineEdit_cuttingAC)

        self.label_67 = QLabel(self.layoutWidget_9)
        self.label_67.setObjectName(u"label_67")
        sizePolicy4.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy4)
        self.label_67.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_7.addWidget(self.label_67)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.checkBox_camera = QCheckBox(self.layoutWidget_9)
        self.checkBox_camera.setObjectName(u"checkBox_camera")
        self.checkBox_camera.setChecked(True)

        self.horizontalLayout_18.addWidget(self.checkBox_camera)

        self.lineEdit_camera = QLineEdit(self.layoutWidget_9)
        self.lineEdit_camera.setObjectName(u"lineEdit_camera")
        self.lineEdit_camera.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_camera.sizePolicy().hasHeightForWidth())
        self.lineEdit_camera.setSizePolicy(sizePolicy3)
        self.lineEdit_camera.setMaximumSize(QSize(78, 20))

        self.horizontalLayout_18.addWidget(self.lineEdit_camera)

        self.label_68 = QLabel(self.layoutWidget_9)
        self.label_68.setObjectName(u"label_68")
        sizePolicy4.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy4)
        self.label_68.setMaximumSize(QSize(28, 16777215))

        self.horizontalLayout_18.addWidget(self.label_68)


        self.verticalLayout_10.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_trafficCtrl = QCheckBox(self.layoutWidget_9)
        self.checkBox_trafficCtrl.setObjectName(u"checkBox_trafficCtrl")
        self.checkBox_trafficCtrl.setMaximumSize(QSize(16777215, 18))
        self.checkBox_trafficCtrl.setChecked(True)

        self.horizontalLayout_8.addWidget(self.checkBox_trafficCtrl)

        self.lineEdit_trafficCtrl = QLineEdit(self.layoutWidget_9)
        self.lineEdit_trafficCtrl.setObjectName(u"lineEdit_trafficCtrl")
        self.lineEdit_trafficCtrl.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_trafficCtrl.sizePolicy().hasHeightForWidth())
        self.lineEdit_trafficCtrl.setSizePolicy(sizePolicy3)
        self.lineEdit_trafficCtrl.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_8.addWidget(self.lineEdit_trafficCtrl)

        self.label_69 = QLabel(self.layoutWidget_9)
        self.label_69.setObjectName(u"label_69")
        sizePolicy4.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy4)
        self.label_69.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_8.addWidget(self.label_69)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBox_supportLabor = QCheckBox(self.layoutWidget_9)
        self.checkBox_supportLabor.setObjectName(u"checkBox_supportLabor")
        self.checkBox_supportLabor.setChecked(True)

        self.horizontalLayout_9.addWidget(self.checkBox_supportLabor)

        self.lineEdit_supportLabor = QLineEdit(self.layoutWidget_9)
        self.lineEdit_supportLabor.setObjectName(u"lineEdit_supportLabor")
        self.lineEdit_supportLabor.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_supportLabor.sizePolicy().hasHeightForWidth())
        self.lineEdit_supportLabor.setSizePolicy(sizePolicy3)
        self.lineEdit_supportLabor.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_9.addWidget(self.lineEdit_supportLabor)

        self.label_70 = QLabel(self.layoutWidget_9)
        self.label_70.setObjectName(u"label_70")
        sizePolicy4.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy4)
        self.label_70.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_9.addWidget(self.label_70)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.checkBox_sectionalSteelFens = QCheckBox(self.layoutWidget_9)
        self.checkBox_sectionalSteelFens.setObjectName(u"checkBox_sectionalSteelFens")
        self.checkBox_sectionalSteelFens.setChecked(False)

        self.horizontalLayout_23.addWidget(self.checkBox_sectionalSteelFens)

        self.lineEdit_sectionalSteelFens = QLineEdit(self.layoutWidget_9)
        self.lineEdit_sectionalSteelFens.setObjectName(u"lineEdit_sectionalSteelFens")
        self.lineEdit_sectionalSteelFens.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_sectionalSteelFens.sizePolicy().hasHeightForWidth())
        self.lineEdit_sectionalSteelFens.setSizePolicy(sizePolicy3)
        self.lineEdit_sectionalSteelFens.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_23.addWidget(self.lineEdit_sectionalSteelFens)

        self.label_71 = QLabel(self.layoutWidget_9)
        self.label_71.setObjectName(u"label_71")
        sizePolicy4.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy4)
        self.label_71.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_23.addWidget(self.label_71)


        self.verticalLayout_10.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.checkBox_channelSteelFens = QCheckBox(self.layoutWidget_9)
        self.checkBox_channelSteelFens.setObjectName(u"checkBox_channelSteelFens")
        self.checkBox_channelSteelFens.setChecked(False)

        self.horizontalLayout_24.addWidget(self.checkBox_channelSteelFens)

        self.lineEdit_channelSteelFens = QLineEdit(self.layoutWidget_9)
        self.lineEdit_channelSteelFens.setObjectName(u"lineEdit_channelSteelFens")
        self.lineEdit_channelSteelFens.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_channelSteelFens.sizePolicy().hasHeightForWidth())
        self.lineEdit_channelSteelFens.setSizePolicy(sizePolicy3)
        self.lineEdit_channelSteelFens.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_24.addWidget(self.lineEdit_channelSteelFens)

        self.label_72 = QLabel(self.layoutWidget_9)
        self.label_72.setObjectName(u"label_72")
        sizePolicy4.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy4)
        self.label_72.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_24.addWidget(self.label_72)


        self.verticalLayout_10.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.checkBox_sprinklerTruck = QCheckBox(self.layoutWidget_9)
        self.checkBox_sprinklerTruck.setObjectName(u"checkBox_sprinklerTruck")
        self.checkBox_sprinklerTruck.setChecked(True)

        self.horizontalLayout_15.addWidget(self.checkBox_sprinklerTruck)

        self.lineEdit_sprinklerTruck = QLineEdit(self.layoutWidget_9)
        self.lineEdit_sprinklerTruck.setObjectName(u"lineEdit_sprinklerTruck")
        self.lineEdit_sprinklerTruck.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_sprinklerTruck.sizePolicy().hasHeightForWidth())
        self.lineEdit_sprinklerTruck.setSizePolicy(sizePolicy3)
        self.lineEdit_sprinklerTruck.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_15.addWidget(self.lineEdit_sprinklerTruck)

        self.label_73 = QLabel(self.layoutWidget_9)
        self.label_73.setObjectName(u"label_73")
        sizePolicy4.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy4)
        self.label_73.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_15.addWidget(self.label_73)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.checkBox_truckDriver = QCheckBox(self.layoutWidget_9)
        self.checkBox_truckDriver.setObjectName(u"checkBox_truckDriver")
        self.checkBox_truckDriver.setChecked(True)

        self.horizontalLayout_14.addWidget(self.checkBox_truckDriver)

        self.lineEdit_truckDriver = QLineEdit(self.layoutWidget_9)
        self.lineEdit_truckDriver.setObjectName(u"lineEdit_truckDriver")
        self.lineEdit_truckDriver.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_truckDriver.sizePolicy().hasHeightForWidth())
        self.lineEdit_truckDriver.setSizePolicy(sizePolicy3)
        self.lineEdit_truckDriver.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_14.addWidget(self.lineEdit_truckDriver)

        self.label_74 = QLabel(self.layoutWidget_9)
        self.label_74.setObjectName(u"label_74")
        sizePolicy4.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy4)
        self.label_74.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_14.addWidget(self.label_74)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.checkBox_craneTruck = QCheckBox(self.layoutWidget_9)
        self.checkBox_craneTruck.setObjectName(u"checkBox_craneTruck")
        self.checkBox_craneTruck.setChecked(True)

        self.horizontalLayout_16.addWidget(self.checkBox_craneTruck)

        self.lineEdit_craneTruck = QLineEdit(self.layoutWidget_9)
        self.lineEdit_craneTruck.setObjectName(u"lineEdit_craneTruck")
        self.lineEdit_craneTruck.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_craneTruck.sizePolicy().hasHeightForWidth())
        self.lineEdit_craneTruck.setSizePolicy(sizePolicy3)
        self.lineEdit_craneTruck.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_16.addWidget(self.lineEdit_craneTruck)

        self.label_75 = QLabel(self.layoutWidget_9)
        self.label_75.setObjectName(u"label_75")
        sizePolicy4.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy4)
        self.label_75.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_16.addWidget(self.label_75)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.checkBox_wheelLoaderTruck = QCheckBox(self.layoutWidget_9)
        self.checkBox_wheelLoaderTruck.setObjectName(u"checkBox_wheelLoaderTruck")
        self.checkBox_wheelLoaderTruck.setChecked(True)

        self.horizontalLayout_17.addWidget(self.checkBox_wheelLoaderTruck)

        self.lineEdit_wheelLoaderTruck = QLineEdit(self.layoutWidget_9)
        self.lineEdit_wheelLoaderTruck.setObjectName(u"lineEdit_wheelLoaderTruck")
        self.lineEdit_wheelLoaderTruck.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_wheelLoaderTruck.sizePolicy().hasHeightForWidth())
        self.lineEdit_wheelLoaderTruck.setSizePolicy(sizePolicy3)
        self.lineEdit_wheelLoaderTruck.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_17.addWidget(self.lineEdit_wheelLoaderTruck)

        self.label_76 = QLabel(self.layoutWidget_9)
        self.label_76.setObjectName(u"label_76")
        sizePolicy4.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy4)
        self.label_76.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_17.addWidget(self.label_76)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.checkBox_heavyMachineDriver = QCheckBox(self.layoutWidget_9)
        self.checkBox_heavyMachineDriver.setObjectName(u"checkBox_heavyMachineDriver")
        self.checkBox_heavyMachineDriver.setChecked(True)

        self.horizontalLayout_13.addWidget(self.checkBox_heavyMachineDriver)

        self.lineEdit_heavyMachineDriver = QLineEdit(self.layoutWidget_9)
        self.lineEdit_heavyMachineDriver.setObjectName(u"lineEdit_heavyMachineDriver")
        self.lineEdit_heavyMachineDriver.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_heavyMachineDriver.sizePolicy().hasHeightForWidth())
        self.lineEdit_heavyMachineDriver.setSizePolicy(sizePolicy3)
        self.lineEdit_heavyMachineDriver.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_13.addWidget(self.lineEdit_heavyMachineDriver)

        self.label_77 = QLabel(self.layoutWidget_9)
        self.label_77.setObjectName(u"label_77")
        sizePolicy4.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy4)
        self.label_77.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_13.addWidget(self.label_77)


        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.checkBox_emergencyRepair = QCheckBox(self.layoutWidget_9)
        self.checkBox_emergencyRepair.setObjectName(u"checkBox_emergencyRepair")
        self.checkBox_emergencyRepair.setChecked(True)

        self.horizontalLayout_11.addWidget(self.checkBox_emergencyRepair)

        self.lineEdit_emergencyRepair = QLineEdit(self.layoutWidget_9)
        self.lineEdit_emergencyRepair.setObjectName(u"lineEdit_emergencyRepair")
        self.lineEdit_emergencyRepair.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_emergencyRepair.sizePolicy().hasHeightForWidth())
        self.lineEdit_emergencyRepair.setSizePolicy(sizePolicy3)
        self.lineEdit_emergencyRepair.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_11.addWidget(self.lineEdit_emergencyRepair)

        self.label_78 = QLabel(self.layoutWidget_9)
        self.label_78.setObjectName(u"label_78")
        sizePolicy4.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy4)
        self.label_78.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_11.addWidget(self.label_78)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.checkBox_pump = QCheckBox(self.layoutWidget_9)
        self.checkBox_pump.setObjectName(u"checkBox_pump")
        self.checkBox_pump.setChecked(True)

        self.horizontalLayout_19.addWidget(self.checkBox_pump)

        self.lineEdit_pump = QLineEdit(self.layoutWidget_9)
        self.lineEdit_pump.setObjectName(u"lineEdit_pump")
        self.lineEdit_pump.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_pump.sizePolicy().hasHeightForWidth())
        self.lineEdit_pump.setSizePolicy(sizePolicy3)
        self.lineEdit_pump.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_19.addWidget(self.lineEdit_pump)

        self.label_79 = QLabel(self.layoutWidget_9)
        self.label_79.setObjectName(u"label_79")
        sizePolicy4.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy4)
        self.label_79.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_19.addWidget(self.label_79)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkBox_sandBag = QCheckBox(self.layoutWidget_9)
        self.checkBox_sandBag.setObjectName(u"checkBox_sandBag")
        self.checkBox_sandBag.setChecked(True)

        self.horizontalLayout_10.addWidget(self.checkBox_sandBag)

        self.lineEdit_sandBag = QLineEdit(self.layoutWidget_9)
        self.lineEdit_sandBag.setObjectName(u"lineEdit_sandBag")
        self.lineEdit_sandBag.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_sandBag.sizePolicy().hasHeightForWidth())
        self.lineEdit_sandBag.setSizePolicy(sizePolicy3)
        self.lineEdit_sandBag.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_10.addWidget(self.lineEdit_sandBag)

        self.label_80 = QLabel(self.layoutWidget_9)
        self.label_80.setObjectName(u"label_80")
        sizePolicy4.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy4)
        self.label_80.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_10.addWidget(self.label_80)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.checkBox_surveying = QCheckBox(self.layoutWidget_9)
        self.checkBox_surveying.setObjectName(u"checkBox_surveying")
        self.checkBox_surveying.setChecked(False)

        self.horizontalLayout_20.addWidget(self.checkBox_surveying)

        self.lineEdit_surveying = QLineEdit(self.layoutWidget_9)
        self.lineEdit_surveying.setObjectName(u"lineEdit_surveying")
        self.lineEdit_surveying.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_surveying.sizePolicy().hasHeightForWidth())
        self.lineEdit_surveying.setSizePolicy(sizePolicy3)
        self.lineEdit_surveying.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_20.addWidget(self.lineEdit_surveying)

        self.label_81 = QLabel(self.layoutWidget_9)
        self.label_81.setObjectName(u"label_81")
        sizePolicy4.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy4)
        self.label_81.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_20.addWidget(self.label_81)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.checkBox_humanSteelPlate = QCheckBox(self.layoutWidget_9)
        self.checkBox_humanSteelPlate.setObjectName(u"checkBox_humanSteelPlate")
        self.checkBox_humanSteelPlate.setChecked(False)

        self.horizontalLayout_21.addWidget(self.checkBox_humanSteelPlate)

        self.lineEdit_humanSteelPlate = QLineEdit(self.layoutWidget_9)
        self.lineEdit_humanSteelPlate.setObjectName(u"lineEdit_humanSteelPlate")
        self.lineEdit_humanSteelPlate.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_humanSteelPlate.sizePolicy().hasHeightForWidth())
        self.lineEdit_humanSteelPlate.setSizePolicy(sizePolicy3)
        self.lineEdit_humanSteelPlate.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_21.addWidget(self.lineEdit_humanSteelPlate)

        self.label_82 = QLabel(self.layoutWidget_9)
        self.label_82.setObjectName(u"label_82")
        sizePolicy4.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy4)
        self.label_82.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_21.addWidget(self.label_82)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.checkBox_tempSteelPlate = QCheckBox(self.layoutWidget_9)
        self.checkBox_tempSteelPlate.setObjectName(u"checkBox_tempSteelPlate")
        self.checkBox_tempSteelPlate.setChecked(False)

        self.horizontalLayout_22.addWidget(self.checkBox_tempSteelPlate)

        self.lineEdit_tempSteelPlate = QLineEdit(self.layoutWidget_9)
        self.lineEdit_tempSteelPlate.setObjectName(u"lineEdit_tempSteelPlate")
        self.lineEdit_tempSteelPlate.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_tempSteelPlate.sizePolicy().hasHeightForWidth())
        self.lineEdit_tempSteelPlate.setSizePolicy(sizePolicy3)
        self.lineEdit_tempSteelPlate.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_22.addWidget(self.lineEdit_tempSteelPlate)

        self.label_83 = QLabel(self.layoutWidget_9)
        self.label_83.setObjectName(u"label_83")
        sizePolicy4.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy4)
        self.label_83.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_22.addWidget(self.label_83)


        self.verticalLayout_10.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.checkBox_smallMachine = QCheckBox(self.layoutWidget_9)
        self.checkBox_smallMachine.setObjectName(u"checkBox_smallMachine")
        self.checkBox_smallMachine.setChecked(True)

        self.horizontalLayout_12.addWidget(self.checkBox_smallMachine)

        self.lineEdit_smallMachine = QLineEdit(self.layoutWidget_9)
        self.lineEdit_smallMachine.setObjectName(u"lineEdit_smallMachine")
        self.lineEdit_smallMachine.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.lineEdit_smallMachine.sizePolicy().hasHeightForWidth())
        self.lineEdit_smallMachine.setSizePolicy(sizePolicy3)
        self.lineEdit_smallMachine.setMaximumSize(QSize(92, 20))

        self.horizontalLayout_12.addWidget(self.lineEdit_smallMachine)

        self.label_84 = QLabel(self.layoutWidget_9)
        self.label_84.setObjectName(u"label_84")
        sizePolicy4.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy4)
        self.label_84.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_12.addWidget(self.label_84)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.tabWidget.addTab(self.tab_9, "")
        self.label_2 = QLabel(Notice)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(530, 30, 51, 16))
        self.lineEdit_position = QLineEdit(Notice)
        self.lineEdit_position.setObjectName(u"lineEdit_position")
        self.lineEdit_position.setGeometry(QRect(370, 150, 441, 21))
        self.layoutWidget3 = QWidget(Notice)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(300, 650, 239, 25))
        self.horizontalLayout_55 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_55.addWidget(self.label_10)

        self.pushButton_saveTemp = QPushButton(self.layoutWidget3)
        self.pushButton_saveTemp.setObjectName(u"pushButton_saveTemp")

        self.horizontalLayout_55.addWidget(self.pushButton_saveTemp)

        self.pushButton_loadTemp = QPushButton(self.layoutWidget3)
        self.pushButton_loadTemp.setObjectName(u"pushButton_loadTemp")

        self.horizontalLayout_55.addWidget(self.pushButton_loadTemp)

        self.layoutWidget_7 = QWidget(Notice)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(760, 120, 136, 23))
        self.horizontalLayout_58 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget_7)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_58.addWidget(self.label_9)

        self.lineEdit_mapNum = QLineEdit(self.layoutWidget_7)
        self.lineEdit_mapNum.setObjectName(u"lineEdit_mapNum")

        self.horizontalLayout_58.addWidget(self.lineEdit_mapNum)

        self.layoutWidget4 = QWidget(Notice)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(570, 650, 327, 25))
        self.horizontalLayout_59 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_59.addWidget(self.label_11)

        self.pushButton_output = QPushButton(self.layoutWidget4)
        self.pushButton_output.setObjectName(u"pushButton_output")

        self.horizontalLayout_59.addWidget(self.pushButton_output)

        self.pushButton_editExcel = QPushButton(self.layoutWidget4)
        self.pushButton_editExcel.setObjectName(u"pushButton_editExcel")

        self.horizontalLayout_59.addWidget(self.pushButton_editExcel)

        self.pushButton_editAutoCad = QPushButton(self.layoutWidget4)
        self.pushButton_editAutoCad.setObjectName(u"pushButton_editAutoCad")

        self.horizontalLayout_59.addWidget(self.pushButton_editAutoCad)

        self.layoutWidget5 = QWidget(Notice)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(300, 190, 77, 141))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget5)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_7.addWidget(self.pushButton)

        self.pushButton_recreate = QPushButton(self.layoutWidget5)
        self.pushButton_recreate.setObjectName(u"pushButton_recreate")

        self.verticalLayout_7.addWidget(self.pushButton_recreate)

        self.pushButton_moveUp = QPushButton(self.layoutWidget5)
        self.pushButton_moveUp.setObjectName(u"pushButton_moveUp")

        self.verticalLayout_7.addWidget(self.pushButton_moveUp)

        self.pushButton_delete = QPushButton(self.layoutWidget5)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.verticalLayout_7.addWidget(self.pushButton_delete)

        self.pushButton_clear = QPushButton(self.layoutWidget5)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.verticalLayout_7.addWidget(self.pushButton_clear)


        self.retranslateUi(Notice)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Notice)
    # setupUi

    def retranslateUi(self, Notice):
        Notice.setWindowTitle(QCoreApplication.translate("Notice", u"Notice", None))
        self.label_4.setText(QCoreApplication.translate("Notice", u"\u884c\u653f\u5206\u5340:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Notice", u"\u5de5\u9805\u540d\u7a31", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Notice", u"\u6578\u91cf", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Notice", u"\u55ae\u4f4d", None));
        self.lineEdit_expect.setText(QCoreApplication.translate("Notice", u"7", None))
        self.label_8.setText(QCoreApplication.translate("Notice", u"\u65e5\u66c6\u5929", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Notice", u"\u7d93\u7406", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Notice", u"\u5c0f\u5de6", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Notice", u"\u715c\u74bf", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Notice", u"\u96c5\u8431", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Notice", u"\u963f\u560e", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Notice", u"\u5ead\u744b", None))

        self.radioButton_survey.setText(QCoreApplication.translate("Notice", u"\u6703\u52d8\u65e5\u671f:", None))
        self.radioButton_start.setText(QCoreApplication.translate("Notice", u"\u958b\u5de5\u65e5\u671f:", None))
        self.radioButton_submit.setText(QCoreApplication.translate("Notice", u"\u7e73\u4ea4\u65e5\u671f:", None))
        self.label.setText(QCoreApplication.translate("Notice", u"      \u9810\u8a08\u5de5\u671f:", None))
        self.label_6.setText(QCoreApplication.translate("Notice", u"\u65bd\u5de5\u5730\u9ede:", None))
        self.label_5.setText(QCoreApplication.translate("Notice", u"\u7b2c", None))
        self.lineEdit_noticeNo.setText("")
        self.label_7.setText(QCoreApplication.translate("Notice", u"\u6b21\u901a\u5831\u55ae", None))
        self.radioButton_4.setText(QCoreApplication.translate("Notice", u"\u4e2d\u5c71\u677e\u5c71", None))
        self.radioButton_3.setText(QCoreApplication.translate("Notice", u"\u5317\u6295", None))
        self.radioButton_5.setText(QCoreApplication.translate("Notice", u"\u58eb\u6797\u5927\u540c", None))
        self.radioButton_6.setText(QCoreApplication.translate("Notice", u"\u5168\u5340\u6436\u4fee", None))
        self.radioButton.setText(QCoreApplication.translate("Notice", u"\u4e00\u822c\u6848", None))
        self.radioButton_2.setText(QCoreApplication.translate("Notice", u"\u6436\u4fee\u6848", None))
        self.label_3.setText(QCoreApplication.translate("Notice", u"\u6703\u52d8\u5c6c\u6027:", None))
        self.label_structureType0.setText(QCoreApplication.translate("Notice", u"\u69cb\u9020\u7269\u578b\u5f0f", None))
        self.comboBox_structureType0.setItemText(0, QCoreApplication.translate("Notice", u"\u5074\u6e9d", None))
        self.comboBox_structureType0.setItemText(1, QCoreApplication.translate("Notice", u"\u96c6\u6c34\u4e95", None))
        self.comboBox_structureType0.setItemText(2, QCoreApplication.translate("Notice", u"\u6697\u6e9d", None))
        self.comboBox_structureType0.setItemText(3, QCoreApplication.translate("Notice", u"\u92fc\u7b4b\u6df7\u51dd\u571f\u7ba1", None))

        self.label_57.setText("")
        self.label_caseType0.setText(QCoreApplication.translate("Notice", u"\u6848\u4ef6\u985e\u578b", None))
        self.label_caseType0_2.setText(QCoreApplication.translate("Notice", u"\u6436\u4fee\u6848", None))
        self.label_56.setText("")
        self.checkBox_multipleNO.setText(QCoreApplication.translate("Notice", u"\u591a\u9805\u7de8\u865f", None))
        self.label_55.setText("")
        self.label_workType0.setText(QCoreApplication.translate("Notice", u"\u65bd\u5de5\u985e\u578b", None))
        self.comboBox_workType0.setItemText(0, QCoreApplication.translate("Notice", u"\u66f4\u65b0", None))
        self.comboBox_workType0.setItemText(1, QCoreApplication.translate("Notice", u"\u65b0\u8a2d", None))

        self.label_58.setText("")
        self.label_oldType0.setText(QCoreApplication.translate("Notice", u"\u65e2\u6709\u578b\u5f0f", None))
        self.comboBox_oldType0.setItemText(0, QCoreApplication.translate("Notice", u"\u7121\u65e2\u6709\u8a2d\u65bd", None))
        self.comboBox_oldType0.setItemText(1, QCoreApplication.translate("Notice", u"\u77e9\u5f62\u6e9d", None))
        self.comboBox_oldType0.setItemText(2, QCoreApplication.translate("Notice", u"U\u578b\u6e9d", None))

        self.label_59.setText("")
        self.label_outerFrame0.setText(QCoreApplication.translate("Notice", u"\u5916\u6a21", None))
        self.comboBox_outerFrame.setItemText(0, QCoreApplication.translate("Notice", u"\u7121", None))
        self.comboBox_outerFrame.setItemText(1, QCoreApplication.translate("Notice", u"\u6709", None))

        self.label_60.setText("")
        self.label_length0.setText(QCoreApplication.translate("Notice", u"\u65bd\u4f5c\u9577\u5ea6", None))
        self.lineEdit_length0.setText("")
        self.label_49.setText(QCoreApplication.translate("Notice", u"m", None))
        self.label_depthName0.setText(QCoreApplication.translate("Notice", u"\u6e9d\u6df1(\u5e73\u5747\u6df1)", None))
        self.lineEdit_Depth0.setText(QCoreApplication.translate("Notice", u"40", None))
        self.label_45.setText(QCoreApplication.translate("Notice", u"cm", None))
        self.label_WidthName0.setText(QCoreApplication.translate("Notice", u"\u6e9d\u5bec", None))
        self.lineEdit_Width0.setText(QCoreApplication.translate("Notice", u"40", None))
        self.label_44.setText(QCoreApplication.translate("Notice", u"cm", None))
        self.label_WallThick0.setText(QCoreApplication.translate("Notice", u"\u6e9d\u7246\u539a", None))
        self.lineEdit_WallThick0.setText(QCoreApplication.translate("Notice", u"20", None))
        self.label_43.setText(QCoreApplication.translate("Notice", u"cm", None))
        self.checkBox_depthRange.setText(QCoreApplication.translate("Notice", u"\u6e9d\u6df1\u7bc4\u570d", None))
        self.lineEdit_depthRange1.setText(QCoreApplication.translate("Notice", u"40", None))
        self.label_53.setText(QCoreApplication.translate("Notice", u"~", None))
        self.lineEdit_depthRange2.setText(QCoreApplication.translate("Notice", u"40", None))
        self.label_54.setText(QCoreApplication.translate("Notice", u"cm~cm", None))
        self.label_oldDepth0.setText(QCoreApplication.translate("Notice", u"\u65e2\u6709\u6e9d\u6df1", None))
        self.label_47.setText(QCoreApplication.translate("Notice", u"cm", None))
        self.label_oldWidth0.setText(QCoreApplication.translate("Notice", u"\u65e2\u6709\u6e9d\u5bec", None))
        self.label_46.setText(QCoreApplication.translate("Notice", u"cm", None))
        self.label_oldWallThick0.setText(QCoreApplication.translate("Notice", u"\u65e2\u6709\u6e9d\u7246\u539a", None))
        self.label_48.setText(QCoreApplication.translate("Notice", u"cm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Notice", u"\u4e3b\u8981\u69cb\u9020\u7269", None))
        self.label_50.setText(QCoreApplication.translate("Notice", u"m", None))
        self.label_66.setText(QCoreApplication.translate("Notice", u"cm", None))
        self.label_structureType1.setText(QCoreApplication.translate("Notice", u"\u69cb\u9020\u7269\u578b\u5f0f", None))
        self.comboBox_structureType1.setItemText(0, QCoreApplication.translate("Notice", u"\u5074\u6e9d\u9802\u677f", None))
        self.comboBox_structureType1.setItemText(1, QCoreApplication.translate("Notice", u"\u96c6\u6c34\u4e95\u9802\u677f", None))
        self.comboBox_structureType1.setItemText(2, QCoreApplication.translate("Notice", u"\u6697\u6e9d\u9802\u677f", None))

        self.label_caseType1.setText(QCoreApplication.translate("Notice", u"\u6848\u4ef6\u985e\u578b", None))
        self.label_caseType1_2.setText(QCoreApplication.translate("Notice", u"\u6436\u4fee\u6848", None))
        self.checkBox_multipleNO_2.setText(QCoreApplication.translate("Notice", u"\u591a\u9805\u7de8\u865f", None))
        self.label_workType1.setText(QCoreApplication.translate("Notice", u"\u65bd\u5de5\u985e\u578b", None))
        self.comboBox_workType1.setItemText(0, QCoreApplication.translate("Notice", u"\u66f4\u65b0", None))
        self.comboBox_workType1.setItemText(1, QCoreApplication.translate("Notice", u"\u65b0\u8a2d", None))

        self.label_coverType1.setText(QCoreApplication.translate("Notice", u"\u9802\u677f\u578b\u5f0f", None))
        self.comboBox_coverType1.setItemText(0, QCoreApplication.translate("Notice", u"S1", None))
        self.comboBox_coverType1.setItemText(1, QCoreApplication.translate("Notice", u"S2", None))
        self.comboBox_coverType1.setItemText(2, QCoreApplication.translate("Notice", u"L1", None))
        self.comboBox_coverType1.setItemText(3, QCoreApplication.translate("Notice", u"L2", None))

        self.label_Lenth1.setText(QCoreApplication.translate("Notice", u"\u65bd\u4f5c\u9577\u5ea6", None))
        self.lineEdit_Lenth1.setText(QCoreApplication.translate("Notice", u"1", None))
        self.label_coverWidthName.setText(QCoreApplication.translate("Notice", u"\u9802\u677f\u5bec", None))
        self.lineEdit_coverWidth.setText(QCoreApplication.translate("Notice", u"80", None))
        self.label_coverThickName.setText(QCoreApplication.translate("Notice", u"\u9802\u677f\u539a", None))
        self.comboBox_coverThick.setItemText(0, QCoreApplication.translate("Notice", u"13cm", None))
        self.comboBox_coverThick.setItemText(1, QCoreApplication.translate("Notice", u"15cm", None))

        self.label_grilleWidth.setText(QCoreApplication.translate("Notice", u"\u683c\u67f5\u5bec", None))
        self.comboBox_grilleWidth.setItemText(0, QCoreApplication.translate("Notice", u"45cm", None))
        self.comboBox_grilleWidth.setItemText(1, QCoreApplication.translate("Notice", u"55cm", None))
        self.comboBox_grilleWidth.setItemText(2, QCoreApplication.translate("Notice", u"65cm", None))

        self.label_grilleType.setText(QCoreApplication.translate("Notice", u"\u683c\u67f5\u5f62\u5f0f", None))
        self.comboBox_grilleType.setItemText(0, QCoreApplication.translate("Notice", u"\u4e00\u822c\u578b", None))
        self.comboBox_grilleType.setItemText(1, QCoreApplication.translate("Notice", u"\u7d30\u76ee\u578b", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Notice", u"\u9802\u677f", None))
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Notice", u"\u9805\u76ee", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Notice", u"\u6578\u91cf \u7b97\u5f0f", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.label_27.setText(QCoreApplication.translate("Notice", u"\u5fa9\u820a\u65b9\u5f0f", None))
        self.comboBox_recoverType.setItemText(0, QCoreApplication.translate("Notice", u"\u8def\u9762\u5207\u5272", None))
        self.comboBox_recoverType.setItemText(1, QCoreApplication.translate("Notice", u"\u9053\u8def\u9291\u92ea", None))

        self.label_62.setText("")
        self.label_37.setText(QCoreApplication.translate("Notice", u"\u6848\u4ef6\u985e\u578b", None))
        self.label_caseType2_2.setText(QCoreApplication.translate("Notice", u"\u6436\u4fee\u6848", None))
        self.label_63.setText("")
        self.label_38.setText(QCoreApplication.translate("Notice", u"\u5fa9\u820a\u7528\u6599", None))
        self.comboBox_materialType.setItemText(0, QCoreApplication.translate("Notice", u"AC\u56de\u586b", None))
        self.comboBox_materialType.setItemText(1, QCoreApplication.translate("Notice", u"\u6a39\u8102\u6df7\u51dd\u571f", None))

        self.label_61.setText("")
        self.label_39.setText(QCoreApplication.translate("Notice", u"\u539a\u5ea6", None))
        self.comboBox_recoverThick.setItemText(0, QCoreApplication.translate("Notice", u"13cm", None))
        self.comboBox_recoverThick.setItemText(1, QCoreApplication.translate("Notice", u"15cm", None))

        self.label_64.setText("")
        self.label_lengthFormula.setText(QCoreApplication.translate("Notice", u"\u65bd\u4f5c\u9577\u5ea6", None))
        self.lineEdit_lengthFormula.setText(QCoreApplication.translate("Notice", u"1", None))
        self.label_51.setText(QCoreApplication.translate("Notice", u"m", None))
        self.label_recoverWidth.setText(QCoreApplication.translate("Notice", u"\u5207\u5272\u5bec\u5ea6", None))
        self.lineEdit_recoverWidth.setText(QCoreApplication.translate("Notice", u"10", None))
        self.label_52.setText(QCoreApplication.translate("Notice", u"cm", None))
        self.label_42.setText(QCoreApplication.translate("Notice", u"\u6a19\u7dda", None))
        self.pushButton_4.setText(QCoreApplication.translate("Notice", u"\u9078\u53d6\u6a19\u7dda", None))
        self.pushButton_5.setText(QCoreApplication.translate("Notice", u"\u522a\u9664\u6a19\u7dda", None))
        self.label_65.setText("")
        self.checkBox_colorCover.setText(QCoreApplication.translate("Notice", u"\u5f69\u8272\u92ea\u9762", None))
        self.lineEdit_colorCover.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("Notice", u"\u5fa9\u820a", None))
        self.checkBox_cuttingAC.setText(QCoreApplication.translate("Notice", u"\u5207\u5272\u701d\u9752\u6df7\u51dd\u571f(\u516c\u5f0f)", None))
        self.lineEdit_cuttingAC.setText("")
        self.label_67.setText(QCoreApplication.translate("Notice", u"\u33a1", None))
        self.checkBox_camera.setText(QCoreApplication.translate("Notice", u"\u651d\u5f71\u6a5f", None))
        self.lineEdit_camera.setText(QCoreApplication.translate("Notice", u"7", None))
        self.label_68.setText(QCoreApplication.translate("Notice", u"\u65e5/\u53f0", None))
        self.checkBox_trafficCtrl.setText(QCoreApplication.translate("Notice", u"\u7fa9\u4ea4\u7de8\u5217", None))
        self.lineEdit_trafficCtrl.setText(QCoreApplication.translate("Notice", u"1", None))
        self.label_69.setText(QCoreApplication.translate("Notice", u"\u6642", None))
        self.checkBox_supportLabor.setText(QCoreApplication.translate("Notice", u"\u914d\u5408\u6280\u8853\u4e4b\u52de\u5de5", None))
        self.lineEdit_supportLabor.setText(QCoreApplication.translate("Notice", u"8*3", None))
        self.label_70.setText(QCoreApplication.translate("Notice", u"\u6642", None))
        self.checkBox_sectionalSteelFens.setText(QCoreApplication.translate("Notice", u"\u578b\u92fc\u8b77\u6b04(\u516c\u5f0f)", None))
        self.lineEdit_sectionalSteelFens.setText("")
        self.label_71.setText(QCoreApplication.translate("Notice", u"m", None))
        self.checkBox_channelSteelFens.setText(QCoreApplication.translate("Notice", u"\u69fd\u92fc\u8b77\u6b04(\u516c\u5f0f)", None))
        self.lineEdit_channelSteelFens.setText("")
        self.label_72.setText(QCoreApplication.translate("Notice", u"m", None))
        self.checkBox_sprinklerTruck.setText(QCoreApplication.translate("Notice", u"\u7051\u6c34\u8eca", None))
        self.lineEdit_sprinklerTruck.setText(QCoreApplication.translate("Notice", u"4", None))
        self.label_73.setText(QCoreApplication.translate("Notice", u"\u6642", None))
        self.checkBox_truckDriver.setText(QCoreApplication.translate("Notice", u"\u99d5\u99db\uff0c\u5c0f\u8ca8\u8eca", None))
        self.lineEdit_truckDriver.setText(QCoreApplication.translate("Notice", u"4", None))
        self.label_74.setText(QCoreApplication.translate("Notice", u"\u6642", None))
        self.checkBox_craneTruck.setText(QCoreApplication.translate("Notice", u"\u540a\u5361\u8eca", None))
        self.lineEdit_craneTruck.setText(QCoreApplication.translate("Notice", u"4", None))
        self.label_75.setText(QCoreApplication.translate("Notice", u"\u6642", None))
        self.checkBox_wheelLoaderTruck.setText(QCoreApplication.translate("Notice", u"\u8f2a\u5f0f\u93df\u88dd\u8eca", None))
        self.lineEdit_wheelLoaderTruck.setText(QCoreApplication.translate("Notice", u"4", None))
        self.label_76.setText(QCoreApplication.translate("Notice", u"\u6642", None))
        self.checkBox_heavyMachineDriver.setText(QCoreApplication.translate("Notice", u"\u64cd\u4f5c\u624b\uff0c\u91cd\u6a5f\u68b0", None))
        self.lineEdit_heavyMachineDriver.setText(QCoreApplication.translate("Notice", u"4+4", None))
        self.label_77.setText(QCoreApplication.translate("Notice", u"\u6642", None))
        self.checkBox_emergencyRepair.setText(QCoreApplication.translate("Notice", u"\u7dca\u6025\u6436\u4fee\uff0c\u8def\u9762\u958b\u6316", None))
        self.lineEdit_emergencyRepair.setText(QCoreApplication.translate("Notice", u"1", None))
        self.label_78.setText(QCoreApplication.translate("Notice", u"\u8655", None))
        self.checkBox_pump.setText(QCoreApplication.translate("Notice", u"\u62bd\u6c34\u6a5f", None))
        self.lineEdit_pump.setText(QCoreApplication.translate("Notice", u"7", None))
        self.label_79.setText(QCoreApplication.translate("Notice", u"\u6642", None))
        self.checkBox_sandBag.setText(QCoreApplication.translate("Notice", u"\u570d\u6c34\u7802\u5305(\u516c\u5f0f)", None))
        self.lineEdit_sandBag.setText("")
        self.label_80.setText(QCoreApplication.translate("Notice", u"\u33a1", None))
        self.checkBox_surveying.setText(QCoreApplication.translate("Notice", u"\u65bd\u5de5\u6e2c\u91cf", None))
        self.lineEdit_surveying.setText(QCoreApplication.translate("Notice", u"1", None))
        self.label_81.setText(QCoreApplication.translate("Notice", u"\u6b21", None))
        self.checkBox_humanSteelPlate.setText(QCoreApplication.translate("Notice", u"\u4eba\u884c\u8de8\u8d8a\u92fc\u677f", None))
        self.lineEdit_humanSteelPlate.setText(QCoreApplication.translate("Notice", u"1", None))
        self.label_82.setText(QCoreApplication.translate("Notice", u"\u7d44", None))
        self.checkBox_tempSteelPlate.setText(QCoreApplication.translate("Notice", u"\u81e8\u6642\u8986\u84cb\u92fc\u677f(\u516c\u5f0f)", None))
        self.lineEdit_tempSteelPlate.setText("")
        self.label_83.setText(QCoreApplication.translate("Notice", u"\u33a1", None))
        self.checkBox_smallMachine.setText(QCoreApplication.translate("Notice", u"\u81e8\u6642\u8a2d\u65bd\uff0c\u5c0f\u578b\u6a5f\u5177", None))
        self.lineEdit_smallMachine.setText(QCoreApplication.translate("Notice", u"1", None))
        self.label_84.setText(QCoreApplication.translate("Notice", u"\u6b21", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("Notice", u"\u5176\u4ed6", None))
        self.label_2.setText(QCoreApplication.translate("Notice", u"\u6703\u52d8\u4eba\u54e1:", None))
        self.lineEdit_position.setText("")
        self.label_10.setText(QCoreApplication.translate("Notice", u"\u5de5\u9805\u8f38\u5165\u904e\u7a0b:", None))
        self.pushButton_saveTemp.setText(QCoreApplication.translate("Notice", u"\u66ab\u5b58", None))
        self.pushButton_loadTemp.setText(QCoreApplication.translate("Notice", u"\u532f\u5165", None))
        self.label_9.setText(QCoreApplication.translate("Notice", u"\u5730\u5f62\u5716\u7de8\u865f: N", None))
        self.lineEdit_mapNum.setText("")
        self.label_11.setText(QCoreApplication.translate("Notice", u"\u5de5\u9805\u8f38\u5165\u5b8c\u6210:", None))
        self.pushButton_output.setText(QCoreApplication.translate("Notice", u"\u8f09\u5165\u6a19\u6e96\u6a94", None))
        self.pushButton_editExcel.setText(QCoreApplication.translate("Notice", u"\u7de8\u8f2fExcel", None))
        self.pushButton_editAutoCad.setText(QCoreApplication.translate("Notice", u"\u7de8\u8f2fAutoCad", None))
        self.pushButton.setText(QCoreApplication.translate("Notice", u"\u65b0\u589e", None))
        self.pushButton_recreate.setText(QCoreApplication.translate("Notice", u"\u4fee\u6539", None))
        self.pushButton_moveUp.setText(QCoreApplication.translate("Notice", u"\u524d\u79fb", None))
        self.pushButton_delete.setText(QCoreApplication.translate("Notice", u"\u522a\u9664", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Notice", u"\u6e05\u9664", None))
    # retranslateUi

