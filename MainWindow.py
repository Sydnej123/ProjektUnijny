#!/usr/bin/python3

import sys

from PyQt5.QtCore import QTime, QDateTime
from PyQt5.QtGui import QIcon
from playsound import playsound
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QVBoxLayout,
                             QGroupBox, QLineEdit,
                             QDateTimeEdit, QComboBox, QTableWidget, QLabel, QPushButton)


def play_alert() -> None:
    playsound("./resources/sounds/alert.mp3")


class Notification:
    def __init__(self, title: str, description: str, alert_time: QTime):
        self.title = title
        self.description = description
        self.alert_time = alert_time


class CyclicalNotification(Notification):
    def __init__(self, title: str, description: str, alert_time: QTime, period: QTime):
        super(CyclicalNotification, self).__init__(title, description, alert_time)
        self.period = period


class OneTimeNotification(Notification):
    def __init__(self, title: str, description: str, alert_time: QTime):
        super(OneTimeNotification, self).__init__(title, description, alert_time)


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.notifications_table = QTableWidget()
        self.notification_title = QLineEdit()
        self.notification_description = QLineEdit()
        self.notification_type = QComboBox()
        self.one_time_notification_details = QComboBox()
        self.notification_date_time = QDateTimeEdit()
        self.add_notification_button = QPushButton()
        self.notification_list = []
        self.initialize_data()
        self.init_ui()

    def init_ui(self):

        super(MainWindow, self).setWindowIcon(QIcon("./resources/icons/icon.png"))
        vertical_box = QVBoxLayout()
        self.setLayout(vertical_box)
        notifications_group = QGroupBox()
        notifications_group.setCheckable(False)
        notifications_group.setTitle("Upcoming notifications.")
        vertical_box.addWidget(notifications_group)
        vertical_table_box = QVBoxLayout()
        notifications_group.setLayout(vertical_table_box)
        vertical_table_box.addWidget(self.notifications_table)
        self.notifications_table.setColumnCount(6)
        self.notifications_table.setRowCount(3)
        self.notifications_table.setHorizontalHeaderLabels(['Title', 'Description', 'Notification type', 'Time',
                                                            'Remaining time', 'Action'])
        push_button = QPushButton("Przycisk")
        push_button.setStyleSheet("QPushButton{ background-color: #ff1234 }")
        self.notifications_table.setCellWidget(0, 5, push_button)
        add_notification_group = QGroupBox()
        add_notification_group.setTitle("Add new notification.")
        add_notification_group.setCheckable(False)
        vertical_box.addWidget(add_notification_group)
        add_notification_group_layout = QVBoxLayout()
        add_notification_group.setLayout(add_notification_group_layout)
        add_notification_first_line = QHBoxLayout()
        add_notification_second_line = QHBoxLayout()
        add_notification_third_line = QHBoxLayout()
        add_notification_fourth_line = QHBoxLayout()
        add_notification_group_layout.addLayout(add_notification_first_line)
        add_notification_group_layout.addLayout(add_notification_second_line)
        add_notification_group_layout.addLayout(add_notification_third_line)
        add_notification_group_layout.addLayout(add_notification_fourth_line)
        self.notification_date_time.setDateTime(QDateTime.currentDateTime())
        notification_type_items = ["One-time notification", "Cyclical notification"]
        self.notification_type.addItems(notification_type_items)
        one_time_notification_details_types = ["At the exact time", "After a given time"]
        self.one_time_notification_details.addItems(one_time_notification_details_types)
        cyclical_notification_details = QComboBox()
        add_notification_first_line.addWidget(QLabel("Title:"))
        add_notification_first_line.addWidget(self.notification_title)
        add_notification_first_line.addStretch()
        add_notification_first_line.addWidget(QLabel("Notification type:"))
        add_notification_first_line.addWidget(self.notification_type)
        add_notification_second_line.addWidget(QLabel("Description"))
        add_notification_second_line.addWidget(self.notification_description)
        add_notification_second_line.addStretch()
        add_notification_second_line.addWidget(QLabel("Notification details"))
        add_notification_second_line.addWidget(self.one_time_notification_details)
        add_notification_third_line.addStretch()
        add_notification_third_line.addWidget(QLabel("Pick a time: "))
        add_notification_third_line.addWidget(self.notification_date_time)
        self.add_notification_button.clicked.connect(self.handle_add_button)
        self.add_notification_button.setText("Add")
        add_notification_fourth_line.addStretch()
        add_notification_fourth_line.addWidget(self.add_notification_button)
        self.setGeometry(600, 300, 600, 300)
        self.setWindowTitle("Reminder")
        self.show()

    def save_data(self) -> None:
        pass

    def initialize_data(self) -> None:
        pass

    def handle_add_button(self) -> None:
        pass

    def handle_notification_type_changed(self) -> None:
        pass

    def handle_notification_details_changed(self) -> None:
        pass

    def handle_time_changed(self) -> None:
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())