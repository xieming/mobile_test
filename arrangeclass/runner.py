from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from globals import set_env, Teacher

from arrangeclass import Ui_MainWindow
from pages import web_page
import time
import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        if self.radioButton.isChecked():
            self.env = "uat"
            print("Default env is {}".format(self.env))
        if self.radioButton_4.isChecked():
            self.type = "GL"
            print("Default type is {}".format(self.type))
        if self.radioButton_6.isChecked():
            current_teacher = Teacher().current_teacher(self.env, "A")
            self.memberid = current_teacher[0:current_teacher.index(",")]
            self.teacher_name = current_teacher[current_teacher.index(","):]
            print("Default teacher_name{}, Member id {}".format(self.teacher_name, self.memberid))
        if self.radioButton_10.isChecked():
            self.level = "BEG"
            print("Default level is {}".format(self.level))

        # if not self.checkBox.isChecked():
        #     self.dateTimeEdit.setEnabled(False)
        #     self.dateTimeEdit_2.setEnabled(False)

    @pyqtSlot()
    def on_radioButton_clicked(self):

        self.env = "uat"
        self.radioButton_9.setDisabled(False)
        print("current env is: {}".format(self.env))

    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        self.env = "qa"
        self.radioButton_9.setDisabled(True)

        print("current env is: {}".format(self.env))

    @pyqtSlot()
    def on_radioButton_3_clicked(self):
        self.env = "staging"
        self.radioButton_9.setDisabled(True)
        print("current env is: {}".format(self.env))

    # PL, GL
    @pyqtSlot()
    def on_radioButton_4_clicked(self):

        self.type = "gl"
        print("current type is: {}".format(self.type))

    @pyqtSlot()
    def on_radioButton_5_clicked(self):

        self.type = "pl"
        print("current type is: {}".format(self.type))

    @pyqtSlot()
    def on_radioButton_15_clicked(self):

        self.type = "cp20"
        print("current type is: {}".format(self.type))

    # Teachers
    @pyqtSlot()
    def on_radioButton_6_clicked(self):

        current_teacher = Teacher().current_teacher(self.env, "A")
        self.memberid = current_teacher[0:current_teacher.index(",")]
        self.teacher_name = current_teacher[current_teacher.index(","):]
        print("Current teacher_name{}, Member id {}".format(self.teacher_name, self.memberid))

    @pyqtSlot()
    def on_radioButton_7_clicked(self):
        current_teacher = Teacher().current_teacher(self.env, "B")
        self.memberid = current_teacher[0:current_teacher.index(",")]
        self.teacher_name = current_teacher[current_teacher.index(","):]
        print("Current teacher_name{}, Member id {}".format(self.teacher_name, self.memberid))

    @pyqtSlot()
    def on_radioButton_8_clicked(self):
        current_teacher = Teacher().current_teacher(self.env, "C")
        self.memberid = current_teacher[0:current_teacher.index(",")]
        self.teacher_name = current_teacher[current_teacher.index(","):]
        print("Current teacher_name{}, Member id {}".format(self.teacher_name, self.memberid))

    @pyqtSlot()
    def on_radioButton_9_clicked(self):
        current_teacher = Teacher().current_teacher(self.env, "D")
        self.memberid = current_teacher[0:current_teacher.index(",")]
        self.teacher_name = current_teacher[current_teacher.index(","):]
        print("Current teacher_name{}, Member id {}".format(self.teacher_name, self.memberid))

    # Level
    @pyqtSlot()
    def on_radioButton_10_clicked(self):
        self.level = "BEG"
        print("Current level is: {}".format(self.level))

    @pyqtSlot()
    def on_radioButton_11_clicked(self):
        self.level = "ELE"
        print("Current level is: {}".format(self.level))

    @pyqtSlot()
    def on_radioButton_12_clicked(self):
        self.level = "INT"
        print("Current level is: {}".format(self.level))

    @pyqtSlot()
    def on_radioButton_13_clicked(self):
        self.level = "UPINT"
        print("Current level is: {}".format(self.level))

    @pyqtSlot()
    def on_radioButton_14_clicked(self):
        self.level = "ADV"
        print("Current level is: {}".format(self.level))


    def on_checkBox_toggled(self):
        self.start_time = time.strptime(self.dateTimeEdit.text(), '%Y-%m-%d %H:%M:%S')
        print(self.start_time)

        self.end_time = time.strptime(self.dateTimeEdit_2.text(), '%Y-%m-%d %H:%M:%S')
        print(self.end_time)


    @pyqtSlot()
    def on_pushButton_clicked(self):
        host, admin = set_env(self.env)
        if self.checkBox.isChecked():

            page = web_page(host, admin, self.memberid, self.type, self.level, self.start_time, self.end_time)
            page.open_page_with_admin()
            page.arrange_class()

        else:
            page = web_page(host, admin, self.memberid, self.type, self.level)
            page.open_page_with_admin()
            page.arrange_class()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
