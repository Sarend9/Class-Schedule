# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowshOocsk.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QAbstractItemView, QCalendarWidget, QComboBox,
                               QDateEdit, QFormLayout, QGroupBox, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QSizePolicy, QTableWidget, QTimeEdit, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1079, 519)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.calendar = QWidget(self.centralwidget)
        self.calendar.setObjectName(u"calendar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy)
        self.calendarLayout = QVBoxLayout(self.calendar)
        self.calendarLayout.setObjectName(u"calendarLayout")
        self.label_calendar = QLabel(self.calendar)
        self.label_calendar.setObjectName(u"label_calendar")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_calendar.setFont(font)

        self.calendarLayout.addWidget(self.label_calendar)

        self.calendarWidget = QCalendarWidget(self.calendar)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy1)

        self.calendarLayout.addWidget(self.calendarWidget)

        self.addEntryGroupBox = QGroupBox(self.calendar)
        self.addEntryGroupBox.setObjectName(u"addEntryGroupBox")
        font1 = QFont()
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.addEntryGroupBox.setFont(font1)
        self.addEntryGroupBox.setAutoFillBackground(False)
        self.formLayout = QFormLayout(self.addEntryGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_subject = QLabel(self.addEntryGroupBox)
        self.label_subject.setObjectName(u"label_subject")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_subject)

        self.subjectComboBox = QComboBox(self.addEntryGroupBox)
        self.subjectComboBox.setObjectName(u"subjectComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.subjectComboBox.sizePolicy().hasHeightForWidth())
        self.subjectComboBox.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.subjectComboBox)

        self.label_group = QLabel(self.addEntryGroupBox)
        self.label_group.setObjectName(u"label_group")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_group)

        self.groupComboBox = QComboBox(self.addEntryGroupBox)
        self.groupComboBox.setObjectName(u"groupComboBox")
        sizePolicy2.setHeightForWidth(self.groupComboBox.sizePolicy().hasHeightForWidth())
        self.groupComboBox.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.groupComboBox)

        self.label_date = QLabel(self.addEntryGroupBox)
        self.label_date.setObjectName(u"label_date")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_date)

        self.dateEdit = QDateEdit(self.addEntryGroupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy2.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy2)
        self.dateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateEdit)

        self.label_start_time = QLabel(self.addEntryGroupBox)
        self.label_start_time.setObjectName(u"label_start_time")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_start_time)

        self.startTimeEdit = QTimeEdit(self.addEntryGroupBox)
        self.startTimeEdit.setObjectName(u"startTimeEdit")
        sizePolicy2.setHeightForWidth(self.startTimeEdit.sizePolicy().hasHeightForWidth())
        self.startTimeEdit.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.startTimeEdit)

        self.label_end_time = QLabel(self.addEntryGroupBox)
        self.label_end_time.setObjectName(u"label_end_time")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_end_time)

        self.endTimeEdit = QTimeEdit(self.addEntryGroupBox)
        self.endTimeEdit.setObjectName(u"endTimeEdit")
        sizePolicy2.setHeightForWidth(self.endTimeEdit.sizePolicy().hasHeightForWidth())
        self.endTimeEdit.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.endTimeEdit)

        self.label_teacher = QLabel(self.addEntryGroupBox)
        self.label_teacher.setObjectName(u"label_teacher")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_teacher)

        self.teacherComboBox = QComboBox(self.addEntryGroupBox)
        self.teacherComboBox.setObjectName(u"teacherComboBox")
        sizePolicy2.setHeightForWidth(self.teacherComboBox.sizePolicy().hasHeightForWidth())
        self.teacherComboBox.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.teacherComboBox)

        self.label_room = QLabel(self.addEntryGroupBox)
        self.label_room.setObjectName(u"label_room")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_room)

        self.roomComboBox = QComboBox(self.addEntryGroupBox)
        self.roomComboBox.setObjectName(u"roomComboBox")
        sizePolicy2.setHeightForWidth(self.roomComboBox.sizePolicy().hasHeightForWidth())
        self.roomComboBox.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.roomComboBox)

        self.addEntryButton = QPushButton(self.addEntryGroupBox)
        self.addEntryButton.setObjectName(u"addEntryButton")
        sizePolicy2.setHeightForWidth(self.addEntryButton.sizePolicy().hasHeightForWidth())
        self.addEntryButton.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.SpanningRole, self.addEntryButton)

        self.calendarLayout.addWidget(self.addEntryGroupBox)

        self.horizontalLayout.addWidget(self.calendar)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.selectedDateSchedule = QGroupBox(self.widget)
        self.selectedDateSchedule.setObjectName(u"selectedDateSchedule")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.selectedDateSchedule.setFont(font2)
        self.verticalLayout_2 = QVBoxLayout(self.selectedDateSchedule)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.dailyScheduleTable = QTableWidget(self.selectedDateSchedule)
        self.dailyScheduleTable.setObjectName(u"dailyScheduleTable")
        sizePolicy3.setHeightForWidth(self.dailyScheduleTable.sizePolicy().hasHeightForWidth())
        self.dailyScheduleTable.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.dailyScheduleTable.setFont(font3)
        self.dailyScheduleTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.dailyScheduleTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.dailyScheduleTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_2.addWidget(self.dailyScheduleTable)

        self.deleteDailyEntryButton = QPushButton(self.selectedDateSchedule)
        self.deleteDailyEntryButton.setObjectName(u"deleteDailyEntryButton")
        self.deleteDailyEntryButton.setFont(font3)

        self.verticalLayout_2.addWidget(self.deleteDailyEntryButton)

        self.verticalLayout.addWidget(self.selectedDateSchedule)

        self.scheduleDisplay = QGroupBox(self.widget)
        self.scheduleDisplay.setObjectName(u"scheduleDisplay")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setKerning(True)
        self.scheduleDisplay.setFont(font4)
        self.scheduleDisplayLayout = QVBoxLayout(self.scheduleDisplay)
        self.scheduleDisplayLayout.setObjectName(u"scheduleDisplayLayout")
        self.scheduleDisplayLayout.setContentsMargins(9, 9, 9, 9)
        self.filterGroupBox = QGroupBox(self.scheduleDisplay)
        self.filterGroupBox.setObjectName(u"filterGroupBox")
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(False)
        font5.setKerning(True)
        self.filterGroupBox.setFont(font5)
        self.horizontalLayout_2 = QHBoxLayout(self.filterGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchLineEdit = QLineEdit(self.filterGroupBox)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setFont(font5)

        self.horizontalLayout_2.addWidget(self.searchLineEdit)

        self.applyFilterButton = QPushButton(self.filterGroupBox)
        self.applyFilterButton.setObjectName(u"applyFilterButton")
        self.applyFilterButton.setFont(font5)

        self.horizontalLayout_2.addWidget(self.applyFilterButton)

        self.clearFilterButton = QPushButton(self.filterGroupBox)
        self.clearFilterButton.setObjectName(u"clearFilterButton")
        self.clearFilterButton.setFont(font5)

        self.horizontalLayout_2.addWidget(self.clearFilterButton)

        self.scheduleDisplayLayout.addWidget(self.filterGroupBox)

        self.allScheduleTable = QTableWidget(self.scheduleDisplay)
        self.allScheduleTable.setObjectName(u"allScheduleTable")
        self.allScheduleTable.setFont(font5)
        self.allScheduleTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.allScheduleTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.allScheduleTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.scheduleDisplayLayout.addWidget(self.allScheduleTable)

        self.deleteAllEntryButton = QPushButton(self.scheduleDisplay)
        self.deleteAllEntryButton.setObjectName(u"deleteAllEntryButton")
        self.deleteAllEntryButton.setFont(font5)

        self.scheduleDisplayLayout.addWidget(self.deleteAllEntryButton)

        self.verticalLayout.addWidget(self.scheduleDisplay)

        self.horizontalLayout.addWidget(self.widget)

        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c \u0437\u0430\u043d\u044f\u0442\u0438\u0439",
                                                             None))
        self.label_calendar.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0430\u0442\u0443:",
                                                               None))
        self.addEntryGroupBox.setTitle(QCoreApplication.translate("MainWindow",
                                                                  u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0437\u0430\u043f\u0438\u0441\u044c",
                                                                  None))
        self.label_subject.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442:", None))
        self.label_group.setText(
            QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430:", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430:", None))
        self.label_start_time.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430:",
                                                                 None))
        self.startTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm", None))
        self.label_end_time.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0412\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f:",
                                                               None))
        self.endTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm", None))
        self.label_teacher.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c:",
                                                              None))
        self.label_room.setText(
            QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f:", None))
        self.addEntryButton.setText(QCoreApplication.translate("MainWindow",
                                                               u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c",
                                                               None))
        self.selectedDateSchedule.setTitle(QCoreApplication.translate("MainWindow",
                                                                      u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0443\u044e \u0434\u0430\u0442\u0443:",
                                                                      None))
        self.deleteDailyEntryButton.setText(QCoreApplication.translate("MainWindow",
                                                                       u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0443\u044e \u0437\u0430\u043f\u0438\u0441\u044c (\u043d\u0430 \u0434\u0430\u0442\u0443)",
                                                                       None))
        self.scheduleDisplay.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f:",
                                       None))
        self.filterGroupBox.setTitle(QCoreApplication.translate("MainWindow",
                                                                u"\u0424\u0438\u043b\u044c\u0442\u0440 \u0438 \u043f\u043e\u0438\u0441\u043a",
                                                                None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443, \u0433\u0440\u0443\u043f\u043f\u0435, \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044e,\n"
                                                                          "                                                                    \u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u0438...\n"
                                                                          "                                                                ",
                                                                          None))
        self.applyFilterButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.clearFilterButton.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.deleteAllEntryButton.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u0443\u044e \u0437\u0430\u043f\u0438\u0441\u044c (\u0438\u0437 \u0432\u0441\u0435\u0445)",
                                                                     None))
    # retranslateUi
