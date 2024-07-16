from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
import sys
import sqlite3


class Ui_Login(QtWidgets.QWidget):
    getID = "test"
    switch_window = QtCore.pyqtSignal()
    teacher_window = QtCore.pyqtSignal()
    student_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Login = self
        Login.setObjectName("Login")
        Login.resize(600, 400)
        Login.setMinimumSize(QtCore.QSize(600, 400))
        Login.setMaximumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        Login.setFont(font)
        self.welcome_title = QtWidgets.QLabel(Login)
        self.welcome_title.setGeometry(QtCore.QRect(100, 20, 400, 75))
        self.welcome_title.setMinimumSize(QtCore.QSize(300, 75))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.welcome_title.setFont(font)
        self.welcome_title.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.welcome_title.setTextFormat(QtCore.Qt.PlainText)
        self.welcome_title.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_title.setWordWrap(False)
        self.welcome_title.setIndent(0)
        self.welcome_title.setObjectName("welcome_title")
        self.ID_label = QtWidgets.QLabel(Login)
        self.ID_label.setGeometry(QtCore.QRect(100, 125, 75, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        self.ID_label.setFont(font)
        self.ID_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ID_label.setObjectName("ID_label")
        self.PW_label = QtWidgets.QLabel(Login)
        self.PW_label.setGeometry(QtCore.QRect(100, 175, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        self.PW_label.setFont(font)
        self.PW_label.setObjectName("PW_label")
        self.ID_input = QtWidgets.QLineEdit(Login)
        self.ID_input.setGeometry(QtCore.QRect(225, 125, 275, 30))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        self.ID_input.setFont(font)
        self.ID_input.setObjectName("ID_input")
        self.PW_input = QtWidgets.QLineEdit(Login)
        self.PW_input.setGeometry(QtCore.QRect(225, 175, 275, 30))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        self.PW_input.setFont(font)
        self.PW_input.setObjectName("PW_input")
        self.PW_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LoginButton = QtWidgets.QPushButton(Login)
        self.LoginButton.setGeometry(QtCore.QRect(225, 300, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        self.LoginButton.setFont(font)
        self.LoginButton.setObjectName("LoginButton")
        self.LoginButton.clicked.connect(self.CheckLogin)
        self.Login_Error_Label = QtWidgets.QLabel(Login)
        self.Login_Error_Label.setVisible(False)
        self.Login_Error_Label.setGeometry(QtCore.QRect(130, 250, 340, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Franklin Gothic Book")
        self.Login_Error_Label.setFont(font)
        self.Login_Error_Label.setStyleSheet("color: rgb(250, 0, 0);")
        self.Login_Error_Label.setObjectName("Login_Error_Label")
        self.Login_Error_Label.setFont(font)
        self.Author_Info_Label = QtWidgets.QLabel(Login)
        self.Author_Info_Label.setGeometry(QtCore.QRect(10, 360, 580, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("黑体")
        self.Author_Info_Label.setFont(font)
        self.Author_Info_Label.setStyleSheet("color: rgb(0, 0, 250);")
        self.Author_Info_Label.setObjectName("Author_Info_Label")
        self.Author_Info_Label.setFont(font)
        self.Author_Info_Label.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def CheckLogin(self):
        global db
        global userID
        global userChar
        getID = self.ID_input.text()
        getPW = self.PW_input.text()
        cursor = db.cursor()
        if getID != "":
            sql = "select * from user_info where ID=" + getID + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) > 0 and str(results[0][2]) == getPW:
                userID = getID
                self.Login_Error_Label.setVisible(False)
                char = results[0][1]
                userChar = char
                if char == "Admin":
                    self.switch_window.emit()
                elif char == "Teacher":
                    self.teacher_window.emit()
                elif char == "Student":
                    self.student_window.emit()
            else:
                self.Login_Error_Label.setVisible(True)
        else:
            self.Login_Error_Label.setVisible(True)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.welcome_title.setText(_translate("Login", "Welcome to MIS for Computer Science\n"
                                                       "College of SCUT"))
        self.ID_label.setText(_translate("Login", "User ID"))
        self.PW_label.setText(_translate("Login", "Password"))
        self.LoginButton.setText(_translate("Login", "Login"))
        self.Login_Error_Label.setText(_translate("Login", "Error: Inexistence ID or wrong password"))
        self.Author_Info_Label.setText(_translate("Login", "Author: Tang Kin Long 2022级计算机科学与技术（全英创新班）"))


class Ui_Admin_Win(QtWidgets.QWidget):
    logout_window = QtCore.pyqtSignal()
    PW_Modify_Button = QtCore.pyqtSignal()
    Goto_Query_Button = QtCore.pyqtSignal()
    Student_Modify_Button = QtCore.pyqtSignal()
    Course_Modify_Button = QtCore.pyqtSignal()
    Choose_Modify_Button = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Admin_Win = self
        Admin_Win.setObjectName("Admin_Win")
        Admin_Win.resize(800, 700)
        Admin_Win.setMinimumSize(QtCore.QSize(800, 700))
        Admin_Win.setMaximumSize(QtCore.QSize(800, 700))
        self.Admin_Identify = QtWidgets.QLabel(Admin_Win)
        self.Admin_Identify.setGeometry(QtCore.QRect(110, 20, 600, 100))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(24)
        self.Admin_Identify.setFont(font)
        self.Admin_Identify.setAlignment(QtCore.Qt.AlignCenter)
        self.Admin_Identify.setObjectName("Admin_Identify")
        self.Course_Admin = QtWidgets.QPushButton(Admin_Win)
        self.Course_Admin.setGeometry(QtCore.QRect(100, 210, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Course_Admin.setFont(font)
        self.Course_Admin.setObjectName("Course_Admin")
        self.Course_Admin.clicked.connect(self.Course_Modify_Button.emit)
        self.Choosing_Admin = QtWidgets.QPushButton(Admin_Win)
        self.Choosing_Admin.setGeometry(QtCore.QRect(100, 300, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Choosing_Admin.setFont(font)
        self.Choosing_Admin.setObjectName("Choosing_Admin")
        self.Choosing_Admin.clicked.connect(self.Choose_Modify_Button.emit)
        self.Query_Entry = QtWidgets.QPushButton(Admin_Win)
        self.Query_Entry.setGeometry(QtCore.QRect(100, 390, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Query_Entry.setFont(font)
        self.Query_Entry.setObjectName("Query_Entry")
        self.Query_Entry.clicked.connect(self.Goto_Query_Button.emit)
        self.PW_Modify_Entry = QtWidgets.QPushButton(Admin_Win)
        self.PW_Modify_Entry.setGeometry(QtCore.QRect(100, 480, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.PW_Modify_Entry.setFont(font)
        self.PW_Modify_Entry.setObjectName("PW_Modify_Entry")
        self.PW_Modify_Entry.clicked.connect(self.PW_Modify_Button.emit)
        self.Stu_Admin = QtWidgets.QPushButton(Admin_Win)
        self.Stu_Admin.setGeometry(QtCore.QRect(100, 120, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Stu_Admin.setFont(font)
        self.Stu_Admin.setObjectName("Stu_Admin")
        self.Stu_Admin.clicked.connect(self.Student_Modify_Button.emit)
        self.Logout_Entry = QtWidgets.QPushButton(Admin_Win)
        self.Logout_Entry.setGeometry(QtCore.QRect(100, 570, 600, 70))

        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Logout_Entry.setFont(font)
        self.Logout_Entry.setObjectName("Logout_Entry")
        self.Logout_Entry.clicked.connect(self.logout_window.emit)

        self.retranslateUi(Admin_Win)
        QtCore.QMetaObject.connectSlotsByName(Admin_Win)

    def retranslateUi(self, Admin_Win):
        _translate = QtCore.QCoreApplication.translate
        Admin_Win.setWindowTitle(_translate("Admin_Win", "Administrator"))
        self.Admin_Identify.setText(_translate("Admin_Win", "User: Admin" + str(userID)))
        self.Course_Admin.setText(_translate("Admin_Win", "Modify Course Information"))
        self.Choosing_Admin.setText(_translate("Admin_Win", "Modify Choosing Information"))
        self.Query_Entry.setText(_translate("Admin_Win", "Specific Query"))
        self.PW_Modify_Entry.setText(_translate("Admin_Win", "Modify Password"))
        self.Stu_Admin.setText(_translate("Admin_Win", "Modify Student Information"))
        self.Logout_Entry.setText(_translate("Admin_Win", "Logout"))


class Ui_Teacher_Win(QtWidgets.QWidget):
    logout_window = QtCore.pyqtSignal()
    PW_Modify_Button = QtCore.pyqtSignal()
    Goto_Query_Button = QtCore.pyqtSignal()
    Score_Modify_Button = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Teacher_Win = self
        Teacher_Win.setObjectName("Teacher_Win")
        Teacher_Win.resize(800, 500)
        Teacher_Win.setMinimumSize(QtCore.QSize(800, 500))
        Teacher_Win.setMaximumSize(QtCore.QSize(800, 500))
        self.Teacher_Identify = QtWidgets.QLabel(Teacher_Win)
        self.Teacher_Identify.setGeometry(QtCore.QRect(110, 20, 600, 100))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(24)
        self.Teacher_Identify.setFont(font)
        self.Teacher_Identify.setAlignment(QtCore.Qt.AlignCenter)
        self.Teacher_Identify.setObjectName("Teacher_Identify")
        self.Score_Teacher = QtWidgets.QPushButton(Teacher_Win)
        self.Score_Teacher.setGeometry(QtCore.QRect(100, 120, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Score_Teacher.setFont(font)
        self.Score_Teacher.setObjectName("Score_Teacher")
        self.Score_Teacher.clicked.connect(self.Score_Modify_Button.emit)
        self.Query_Entry = QtWidgets.QPushButton(Teacher_Win)
        self.Query_Entry.setGeometry(QtCore.QRect(100, 210, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Query_Entry.setFont(font)
        self.Query_Entry.setObjectName("Query_Entry")
        self.Query_Entry.clicked.connect(self.Goto_Query_Button.emit)
        self.PW_Modify_Entry = QtWidgets.QPushButton(Teacher_Win)
        self.PW_Modify_Entry.setGeometry(QtCore.QRect(100, 300, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.PW_Modify_Entry.setFont(font)
        self.PW_Modify_Entry.setObjectName("PW_Modify_Entry")
        self.PW_Modify_Entry.clicked.connect(self.PW_Modify_Button.emit)
        self.Logout_Entry = QtWidgets.QPushButton(Teacher_Win)
        self.Logout_Entry.setGeometry(QtCore.QRect(100, 390, 600, 70))

        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Logout_Entry.setFont(font)
        self.Logout_Entry.setObjectName("Logout_Entry")
        self.Logout_Entry.clicked.connect(self.logout_window.emit)

        self.retranslateUi(Teacher_Win)
        QtCore.QMetaObject.connectSlotsByName(Teacher_Win)

    def retranslateUi(self, Teacher_Win):
        _translate = QtCore.QCoreApplication.translate
        Teacher_Win.setWindowTitle(_translate("Teacher_Win", "Teacher"))
        self.Teacher_Identify.setText(_translate("Teacher_Win", "User: Teacher" + str(userID)))
        self.Score_Teacher.setText(_translate("Teacher_Win", "Modify Score"))
        self.Query_Entry.setText(_translate("Teacher_Win", "Specific Query"))
        self.PW_Modify_Entry.setText(_translate("Teacher_Win", "Modify Password"))
        self.Logout_Entry.setText(_translate("Teacher_Win", "Logout"))


class Ui_Student_Win(QtWidgets.QWidget):
    logout_window = QtCore.pyqtSignal()
    PW_Modify_Button = QtCore.pyqtSignal()
    Goto_Query_Button = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Student_Win = self
        Student_Win.setObjectName("Student_Win")
        Student_Win.resize(800, 400)
        Student_Win.setMinimumSize(QtCore.QSize(800, 400))
        Student_Win.setMaximumSize(QtCore.QSize(800, 400))
        self.Student_Identify = QtWidgets.QLabel(Student_Win)
        self.Student_Identify.setGeometry(QtCore.QRect(110, 20, 600, 100))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(24)
        self.Student_Identify.setFont(font)
        self.Student_Identify.setAlignment(QtCore.Qt.AlignCenter)
        self.Student_Identify.setObjectName("Student_Identify")
        self.Query_Entry = QtWidgets.QPushButton(Student_Win)
        self.Query_Entry.setGeometry(QtCore.QRect(100, 120, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Query_Entry.setFont(font)
        self.Query_Entry.setObjectName("Query_Entry")
        self.Query_Entry.clicked.connect(self.Goto_Query_Button.emit)
        self.PW_Modify_Entry = QtWidgets.QPushButton(Student_Win)
        self.PW_Modify_Entry.setGeometry(QtCore.QRect(100, 210, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.PW_Modify_Entry.setFont(font)
        self.PW_Modify_Entry.setObjectName("PW_Modify_Entry")
        self.PW_Modify_Entry.clicked.connect(self.PW_Modify_Button.emit)
        self.Logout_Entry = QtWidgets.QPushButton(Student_Win)
        self.Logout_Entry.setGeometry(QtCore.QRect(100, 300, 600, 70))

        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Logout_Entry.setFont(font)
        self.Logout_Entry.setObjectName("Logout_Entry")
        self.Logout_Entry.clicked.connect(self.logout_window.emit)

        self.retranslateUi(Student_Win)
        QtCore.QMetaObject.connectSlotsByName(Student_Win)

    def retranslateUi(self, Student_Win):
        _translate = QtCore.QCoreApplication.translate
        Student_Win.setWindowTitle(_translate("Student_Win", "Student"))
        self.Student_Identify.setText(_translate("Student_Win", "User: Student" + str(userID)))
        self.Query_Entry.setText(_translate("Student_Win", "Specific Query"))
        self.PW_Modify_Entry.setText(_translate("Student_Win", "Modify Password"))
        self.Logout_Entry.setText(_translate("_Win", "Logout"))


class Ui_PW_Modify(QtWidgets.QWidget):
    cancel_back = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        PW_Modify = self
        PW_Modify.setObjectName("PW_Modify")
        PW_Modify.resize(600, 400)
        PW_Modify.setMinimumSize(QtCore.QSize(600, 400))
        PW_Modify.setMaximumSize(QtCore.QSize(600, 400))
        self.PW_Notice = QtWidgets.QLabel(PW_Modify)
        self.PW_Notice.setGeometry(QtCore.QRect(100, 20, 400, 75))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        self.PW_Notice.setFont(font)
        self.PW_Notice.setAlignment(QtCore.Qt.AlignCenter)
        self.PW_Notice.setObjectName("PW_Notice")
        self.Old_PW_Label = QtWidgets.QLabel(PW_Modify)
        self.Old_PW_Label.setGeometry(QtCore.QRect(80, 110, 140, 35))
        self.Old_PW_Label.setFont(font)
        self.Old_PW_Label.setObjectName("Old_PW_Label")
        self.New_PW_Label = QtWidgets.QLabel(PW_Modify)
        self.New_PW_Label.setGeometry(QtCore.QRect(75, 165, 150, 35))
        self.New_PW_Label.setFont(font)
        self.New_PW_Label.setObjectName("New_PW_Label")
        self.Double_PW_Label = QtWidgets.QLabel(PW_Modify)
        self.Double_PW_Label.setGeometry(QtCore.QRect(85, 220, 130, 35))
        self.Double_PW_Label.setFont(font)
        self.Double_PW_Label.setObjectName("Double_PW_Label")
        self.Old_PW_Input = QtWidgets.QLineEdit(PW_Modify)
        self.Old_PW_Input.setGeometry(QtCore.QRect(230, 110, 290, 35))
        self.Old_PW_Input.setFont(font)
        self.Old_PW_Input.setObjectName("Old_PW_Input")
        self.Old_PW_Input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.New_PW_Input = QtWidgets.QLineEdit(PW_Modify)
        self.New_PW_Input.setGeometry(QtCore.QRect(230, 165, 290, 35))
        self.New_PW_Input.setFont(font)
        self.New_PW_Input.setObjectName("New_PW_Input")
        self.New_PW_Input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Double_PW_Input = QtWidgets.QLineEdit(PW_Modify)
        self.Double_PW_Input.setGeometry(QtCore.QRect(230, 220, 290, 35))
        self.Double_PW_Input.setFont(font)
        self.Double_PW_Input.setObjectName("Double_PW_Input")
        self.Double_PW_Input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Modify_PW_Confirm = QtWidgets.QPushButton(PW_Modify)
        self.Modify_PW_Confirm.setGeometry(QtCore.QRect(90, 330, 160, 45))
        self.Modify_PW_Confirm.setFont(font)
        self.Modify_PW_Confirm.setObjectName("Modify_PW_Confirm")
        self.Modify_PW_Confirm.clicked.connect(self.Check_PW_Modify)
        self.PW_Cancel = QtWidgets.QPushButton(PW_Modify)
        self.PW_Cancel.setGeometry(QtCore.QRect(350, 330, 160, 45))
        self.PW_Cancel.setFont(font)
        self.PW_Cancel.setObjectName("PW_Cancel")
        self.PW_Cancel.clicked.connect(self.cancel_back.emit)
        self.Error_Modifiy_Label = QtWidgets.QLabel(PW_Modify)
        self.Error_Modifiy_Label.setGeometry(QtCore.QRect(70, 275, 480, 40))
        font.setPointSize(10)
        self.Error_Modifiy_Label.setFont(font)
        self.Error_Modifiy_Label.setStyleSheet("color:rgb(255, 0, 0);")
        self.Error_Modifiy_Label.setVisible(False)
        self.Error_Modifiy_Label.setObjectName("Error_Modify_Label")

        self.retranslateUi(PW_Modify)
        QtCore.QMetaObject.connectSlotsByName(PW_Modify)

    def Check_PW_Modify(self):
        global userID
        global db
        getOldPW = self.Old_PW_Input.text()
        getNewPW = self.New_PW_Input.text()
        getDouble = self.Double_PW_Input.text()
        cursor = db.cursor()
        sql = "select * from user_info where ID=" + userID + ";"
        cursor.execute(sql)
        results = cursor.fetchall()
        realOldPW = str(results[0][2])
        if realOldPW == getOldPW and getNewPW == getDouble:
            sql = "update user_info set Passwords=" + getNewPW + " where ID=" + userID
            cursor.execute(sql)
            db.commit()
            self.cancel_back.emit()
        else:
            self.Error_Modifiy_Label.setVisible(True)

    def retranslateUi(self, PW_Modify):
        _translate = QtCore.QCoreApplication.translate
        PW_Modify.setWindowTitle(_translate("PW_Modify", "Modify Password"))
        self.PW_Notice.setText(_translate("PW_Modify", "Please Correctly Enter Old Password \n"
                                                       "and Remember New Password"))
        self.Old_PW_Label.setText(_translate("PW_Modify", "Old Password"))
        self.New_PW_Label.setText(_translate("PW_Modify", "New Password"))
        self.Double_PW_Label.setText(_translate("PW_Modify", "Input Again"))
        self.Modify_PW_Confirm.setText(_translate("PW_Modify", "Confirm"))
        self.PW_Cancel.setText(_translate("PW_Modify", "Cancel"))
        self.Error_Modifiy_Label.setText(
            _translate("PW_Modify", "Error: Wrong Old Password or Different New Password "))


class Ui_Query(QtWidgets.QWidget):
    Query_back = QtCore.pyqtSignal()
    Query_to_Student = QtCore.pyqtSignal()
    Query_to_Score = QtCore.pyqtSignal()
    Query_to_Course = QtCore.pyqtSignal()
    Query_to_teaching = QtCore.pyqtSignal()
    Query_to_Average = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Query_Win = self
        Query_Win.setObjectName("Query_Win")
        Query_Win.resize(800, 700)
        Query_Win.setMinimumSize(QtCore.QSize(800, 700))
        Query_Win.setMaximumSize(QtCore.QSize(800, 700))
        self.Query_Identify = QtWidgets.QLabel(Query_Win)
        self.Query_Identify.setGeometry(QtCore.QRect(110, 20, 600, 100))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(24)
        self.Query_Identify.setFont(font)
        self.Query_Identify.setAlignment(QtCore.Qt.AlignCenter)
        self.Query_Identify.setObjectName("Query_Identify")
        self.Course_Score = QtWidgets.QPushButton(Query_Win)
        self.Course_Score.setGeometry(QtCore.QRect(100, 210, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Course_Score.setFont(font)
        self.Course_Score.setObjectName("Course_Score")
        self.Course_Score.clicked.connect(self.Query_to_Score.emit)
        self.Course_Open = QtWidgets.QPushButton(Query_Win)
        self.Course_Open.setGeometry(QtCore.QRect(100, 300, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Course_Open.setFont(font)
        self.Course_Open.setObjectName("Course_Open")
        self.Course_Open.clicked.connect(self.Query_to_Course.emit)
        self.Course_Teach = QtWidgets.QPushButton(Query_Win)
        self.Course_Teach.setGeometry(QtCore.QRect(100, 390, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Course_Teach.setFont(font)
        self.Course_Teach.setObjectName("Course_Teach")
        self.Course_Teach.clicked.connect(self.Query_to_teaching.emit)
        self.Average_Score = QtWidgets.QPushButton(Query_Win)
        self.Average_Score.setGeometry(QtCore.QRect(100, 480, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Average_Score.setFont(font)
        self.Average_Score.setObjectName("Average_Score")
        self.Average_Score.clicked.connect(self.Query_to_Average.emit)
        self.stuChoose = QtWidgets.QPushButton(Query_Win)
        self.stuChoose.setGeometry(QtCore.QRect(100, 120, 600, 70))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.stuChoose.setFont(font)
        self.stuChoose.setObjectName("stuChoose")
        self.stuChoose.clicked.connect(self.Query_to_Student.emit)
        self.Logout_Entry = QtWidgets.QPushButton(Query_Win)
        self.Logout_Entry.setGeometry(QtCore.QRect(100, 570, 600, 70))

        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(18)
        self.Logout_Entry.setFont(font)
        self.Logout_Entry.setObjectName("Logout_Entry")
        self.Logout_Entry.clicked.connect(self.Query_back.emit)

        self.retranslateUi(Query_Win)
        QtCore.QMetaObject.connectSlotsByName(Query_Win)

    def retranslateUi(self, Admin_Win):
        _translate = QtCore.QCoreApplication.translate
        Admin_Win.setWindowTitle(_translate("Query_Win", "Specific Query"))
        self.Query_Identify.setText(_translate("Query_Win", "Choose Query Function"))
        self.Course_Score.setText(_translate("Query_Win", "Course Score"))
        self.Course_Open.setText(_translate("Query_Win", "Course or Course Choosing Info."))
        self.Course_Teach.setText(_translate("Query_Win", "Teaching Information"))
        self.Average_Score.setText(_translate("Query_Win", "Average Score"))
        self.stuChoose.setText(_translate("Query_Win", "Student Course Choosing Info."))
        self.Logout_Entry.setText(_translate("Query_Win", "Back Menu"))


class Ui_Query_Teaching(QtWidgets.QWidget):
    Goback_Query = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Query_Teaching = self
        Query_Teaching.setObjectName("Query_Teaching")
        Query_Teaching.resize(800, 700)
        Query_Teaching.setMinimumSize(QtCore.QSize(800, 700))
        Query_Teaching.setMaximumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        Query_Teaching.setFont(font)
        self.Teaching_Table = QtWidgets.QTableWidget(Query_Teaching)
        self.Teaching_Table.setGeometry(QtCore.QRect(50, 200, 700, 400))
        self.Teaching_Table.setMinimumSize(QtCore.QSize(700, 400))
        self.Teaching_Table.setMaximumSize(QtCore.QSize(700, 400))
        self.Teaching_Table.setRowCount(0)
        self.Teaching_Table.setObjectName("Teaching_Table")
        self.Teaching_Table.setColumnCount(0)
        self.Teaching_Table.setFont(font)
        self.Teaching_Table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Query_Teaching_Button = QtWidgets.QPushButton(Query_Teaching)
        self.Query_Teaching_Button.setGeometry(QtCore.QRect(600, 53, 150, 64))
        self.Query_Teaching_Button.setMinimumSize(QtCore.QSize(150, 70))
        self.Query_Teaching_Button.setMaximumSize(QtCore.QSize(150, 70))
        self.Query_Teaching_Button.setObjectName("Query_Teaching_Button")
        self.Query_Teaching_Button.clicked.connect(self.Query_Teaching_SQL)
        self.Query_Teaching_Button.setFont(font)
        self.Query_back = QtWidgets.QPushButton(Query_Teaching)
        self.Query_back.setGeometry(QtCore.QRect(325, 615, 150, 70))
        self.Query_back.setMinimumSize(QtCore.QSize(150, 70))
        self.Query_back.setMaximumSize(QtCore.QSize(150, 70))
        self.Query_back.setObjectName("Query_back")
        self.Query_back.clicked.connect(self.Goback_Query.emit)
        self.Query_back.setFont(font)
        self.TName_label = QtWidgets.QLabel(Query_Teaching)
        self.TName_label.setGeometry(QtCore.QRect(50, 30, 191, 40))
        self.TName_label.setObjectName("TName_label")
        self.TName_label.setFont(font)
        self.TID_label = QtWidgets.QLabel(Query_Teaching)
        self.TID_label.setGeometry(QtCore.QRect(50, 98, 221, 40))
        self.TID_label.setObjectName("TID_label")
        self.TID_label.setFont(font)
        self.TName_input = QtWidgets.QLineEdit(Query_Teaching)
        self.TName_input.setGeometry(QtCore.QRect(250, 35, 300, 36))
        self.TName_input.setMinimumSize(QtCore.QSize(300, 36))
        self.TName_input.setMaximumSize(QtCore.QSize(300, 36))
        self.TName_input.setObjectName("TName_input")
        self.TName_input.setFont(font)
        self.TID_input = QtWidgets.QLineEdit(Query_Teaching)
        self.TID_input.setGeometry(QtCore.QRect(250, 99, 300, 36))
        self.TID_input.setMinimumSize(QtCore.QSize(300, 36))
        self.TID_input.setMaximumSize(QtCore.QSize(300, 36))
        self.TID_input.setObjectName("TID_input")
        self.TID_input.setFont(font)
        self.Result_label = QtWidgets.QLabel(Query_Teaching)
        self.Result_label.setGeometry(QtCore.QRect(250, 150, 300, 36))
        self.Result_label.setObjectName("Result_label")
        self.Result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Result_label.setFont(font)

        self.retranslateUi(Query_Teaching)
        QtCore.QMetaObject.connectSlotsByName(Query_Teaching)
        self._translate = QtCore.QCoreApplication.translate

    def retranslateUi(self, Query_Teaching):
        _translate = QtCore.QCoreApplication.translate
        Query_Teaching.setWindowTitle(_translate("Query_Teaching", "Teaching Information"))
        self.Query_Teaching_Button.setText(_translate("Query_Teaching", "Query"))
        self.Query_back.setText(_translate("Query_Teaching", "Back"))
        self.TName_label.setText(_translate("Query_Teaching", "Teacher Name:"))
        self.TID_label.setText(_translate("Query_Teaching", "Teacher ID:"))
        self.Result_label.setText(_translate("Result_Label", "Number of result: 0"))

    def Query_Teaching_SQL(self):
        getTName = str(self.TName_input.text())
        getTID = self.TID_input.text()
        cursor = db.cursor()
        if getTName == "" and getTID == "":
            sql = "select * from teacher;"
        elif getTName == "":
            sql = "select * from teacher where tID=" + getTID + ";"
        elif getTID == "":
            sql = "select * from teacher where tName='" + getTName + "';"
        else:
            sql = "select * from teacher where tID=" + getTID + " and tName='" + getTName + "';"
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            self.Teaching_Table.clear()
            self.Teaching_Table.setColumnCount(0)
            self.Teaching_Table.setRowCount(0)
            col_result = cursor.description
            self.row = len(results)  # 取得记录个数，用于设置表格的行数
            self.vol = len(results[0])  # 取得字段数，用于设置表格的列数
            self.Result_label.setText(
                QtCore.QCoreApplication.translate("Result_Label", "Number of result: ") + str(self.row))
            col_result = list(col_result)
            a = 0
            self.Teaching_Table.setColumnCount(self.vol)
            self.Teaching_Table.setRowCount(self.row)
            for i in col_result:
                item = QtWidgets.QTableWidgetItem()
                self.Teaching_Table.setHorizontalHeaderItem(a, item)
                item = self.Teaching_Table.horizontalHeaderItem(a)
                item.setText(self._translate("Teaching_Table", i[0]))
                a = a + 1
            results = list(results)
            for i in range(len(results)):
                results[i] = list(results[i])
            for i in range(self.row):
                for j in range(self.vol):
                    item = QtWidgets.QTableWidgetItem()
                    self.Teaching_Table.setItem(i, j, item)
                    item = self.Teaching_Table.item(i, j)
                    item.setText(self._translate("Teaching_Table", str(results[i][j])))
        else:
            self.Teaching_Table.clear()
            self.Teaching_Table.setColumnCount(0)
            self.Teaching_Table.setRowCount(0)
            self.Result_label.setText(QtCore.QCoreApplication.translate("Result_Label", "Number of result: 0"))


class Ui_Query_Average(QtWidgets.QWidget):
    Goback_Query = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Query_Average = self
        Query_Average.setObjectName("Query_Average")
        Query_Average.resize(800, 700)
        Query_Average.setMinimumSize(QtCore.QSize(800, 700))
        Query_Average.setMaximumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        Query_Average.setFont(font)
        self.Average_Table = QtWidgets.QTableWidget(Query_Average)
        self.Average_Table.setGeometry(QtCore.QRect(50, 250, 700, 350))
        self.Average_Table.setMinimumSize(QtCore.QSize(700, 350))
        self.Average_Table.setMaximumSize(QtCore.QSize(700, 350))
        self.Average_Table.setRowCount(0)
        self.Average_Table.setObjectName("Average_Table")
        self.Average_Table.setColumnCount(0)
        self.Average_Table.setFont(font)
        self.Average_Table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Query_Average_Button = QtWidgets.QPushButton(Query_Average)
        self.Query_Average_Button.setGeometry(QtCore.QRect(600, 78, 150, 64))
        self.Query_Average_Button.setMinimumSize(QtCore.QSize(150, 70))
        self.Query_Average_Button.setMaximumSize(QtCore.QSize(150, 70))
        self.Query_Average_Button.setObjectName("Query_Average_Button")
        self.Query_Average_Button.clicked.connect(self.Query_Average_SQL)
        self.Query_Average_Button.setFont(font)
        self.Query_back = QtWidgets.QPushButton(Query_Average)
        self.Query_back.setGeometry(QtCore.QRect(325, 615, 150, 70))
        self.Query_back.setMinimumSize(QtCore.QSize(150, 70))
        self.Query_back.setMaximumSize(QtCore.QSize(150, 70))
        self.Query_back.setObjectName("Query_back")
        self.Query_back.clicked.connect(self.Goback_Query.emit)
        self.Query_back.setFont(font)
        self.SName_label = QtWidgets.QLabel(Query_Average)
        self.SName_label.setGeometry(QtCore.QRect(50, 30, 191, 40))
        self.SName_label.setObjectName("SName_label")
        self.SName_label.setFont(font)
        self.SID_label = QtWidgets.QLabel(Query_Average)
        self.SID_label.setGeometry(QtCore.QRect(50, 70, 221, 40))
        self.SID_label.setObjectName("SID_label")
        self.SID_label.setFont(font)
        self.class_label = QtWidgets.QLabel(Query_Average)
        self.class_label.setGeometry(QtCore.QRect(50, 110, 221, 40))
        self.class_label.setObjectName("class_label")
        self.class_label.setFont(font)
        self.course_label = QtWidgets.QLabel(Query_Average)
        self.course_label.setGeometry(QtCore.QRect(50, 150, 221, 40))
        self.course_label.setObjectName("course_label")
        self.course_label.setFont(font)
        self.SName_input = QtWidgets.QLineEdit(Query_Average)
        self.SName_input.setGeometry(QtCore.QRect(250, 32, 300, 36))
        self.SName_input.setMinimumSize(QtCore.QSize(300, 36))
        self.SName_input.setMaximumSize(QtCore.QSize(300, 36))
        self.SName_input.setObjectName("SName_input")
        self.SName_input.setFont(font)
        self.SID_input = QtWidgets.QLineEdit(Query_Average)
        self.SID_input.setGeometry(QtCore.QRect(250, 72, 300, 36))
        self.SID_input.setMinimumSize(QtCore.QSize(300, 36))
        self.SID_input.setMaximumSize(QtCore.QSize(300, 36))
        self.SID_input.setObjectName("SID_input")
        self.SID_input.setFont(font)
        self.class_input = QtWidgets.QLineEdit(Query_Average)
        self.class_input.setGeometry(QtCore.QRect(250, 112, 300, 36))
        self.class_input.setMinimumSize(QtCore.QSize(300, 36))
        self.class_input.setMaximumSize(QtCore.QSize(300, 36))
        self.class_input.setObjectName("class_input")
        self.class_input.setFont(font)
        self.course_input = QtWidgets.QLineEdit(Query_Average)
        self.course_input.setGeometry(QtCore.QRect(250, 152, 300, 36))
        self.course_input.setMinimumSize(QtCore.QSize(300, 36))
        self.course_input.setMaximumSize(QtCore.QSize(300, 36))
        self.course_input.setObjectName("course_input")
        self.course_input.setFont(font)

        self.Result_label = QtWidgets.QLabel(Query_Average)
        self.Result_label.setGeometry(QtCore.QRect(250, 200, 300, 36))
        self.Result_label.setObjectName("Result_label")
        self.Result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Result_label.setFont(font)

        self.retranslateUi(Query_Average)
        QtCore.QMetaObject.connectSlotsByName(Query_Average)
        self._translate = QtCore.QCoreApplication.translate

    def retranslateUi(self, Query_Average):
        _translate = QtCore.QCoreApplication.translate
        Query_Average.setWindowTitle(_translate("Query_Average", "Average Score"))
        self.Query_Average_Button.setText(_translate("Query_Average", "Query"))
        self.Query_back.setText(_translate("Query_Average", "Back"))
        self.SName_label.setText(_translate("Query_Average", "Student Name:"))
        self.SID_label.setText(_translate("Query_Average", "Student ID:"))
        self.class_label.setText(_translate("Query_Average", "Class:"))
        self.course_label.setText(_translate("Query_Average", "Course:"))
        self.Result_label.setText(_translate("Result_Label", "Number of result: 0"))

    def Query_Average_SQL(self):
        self.Average_Table.clear()
        self.Average_Table.setColumnCount(0)
        self.Average_Table.setRowCount(0)
        self.Result_label.setText(QtCore.QCoreApplication.translate("Result_Label", "Number of result: 0"))
        getSName = str(self.SName_input.text())
        getSID = self.SID_input.text()
        getClass = self.class_input.text()
        getCourse = self.course_input.text()
        cursor = db.cursor()

        inputstate = -1
        basesql = "select avg(score) as 'average score' from course join course_choosing join student using(sID) where student.sID=course_choosing.sID and course.cID=course_choosing.cID and course_choosing.score!=-1 "
        if getSName == "" and getSID == "":
            if getClass == "" and getCourse == "":
                inputstate = 1
                sql = basesql + ";"
            elif getClass == "":
                inputstate = 2
                sql = basesql + " and course.cName='" + getCourse + "';"
            elif getCourse == "":
                inputstate = 3
                sql = basesql + " and student.class='" + getClass + "';"
            else:
                inputstate = 4
                sql = basesql + " and course.cName='" + getCourse + "' and student.class='" + getClass + "';"
        else:
            if getSName == "":
                inputstate = 5
                sql = basesql + " and student.sID='" + getSID + "';"
            elif getSID == "":
                inputstate = 6
                sql = basesql + " and student.sName='" + getSName + "';"
            else:
                inputstate = 7
                sql = basesql + " and student.sID='" + getSID + "' and student.sName='" + getSName + "';"

        cursor.execute(sql)
        results = cursor.fetchall()
        ans_avg = str(results[0][0])
        if len(results) > 0:
            self.Average_Table.setColumnCount(5)
            self.Average_Table.setRowCount(1)
            self.row = 1  # 取得记录个数，用于设置表格的行数
            self.vol = 5  # 取得字段数，用于设置表格的列数
            self.Result_label.setText(
                QtCore.QCoreApplication.translate("Result_Label", "Number of result: ") + str(self.row))
            headlist = ["Student ID", "Student Name", "Class", "Course", "Average Score"]
            for i in range(5):
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setHorizontalHeaderItem(i, item)
                item = self.Average_Table.horizontalHeaderItem(i)
                item.setText(self._translate("Average_Table", headlist[i]))

            if inputstate == 1:
                for i in range(4):
                    item = QtWidgets.QTableWidgetItem()
                    self.Average_Table.setItem(0, i, item)
                    item = self.Average_Table.item(0, i)
                    item.setText(self._translate("Average_Table", "All"))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 4, item)
                item = self.Average_Table.item(0, 4)
                item.setText(self._translate("Average_Table", ans_avg))
            elif inputstate == 2:
                for i in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.Average_Table.setItem(0, i, item)
                    item = self.Average_Table.item(0, i)
                    item.setText(self._translate("Average_Table", "All"))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 3, item)
                item = self.Average_Table.item(0, 3)
                item.setText(self._translate("Average_Table", getCourse))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 4, item)
                item = self.Average_Table.item(0, 4)
                item.setText(self._translate("Average_Table", ans_avg))
            elif inputstate == 3:
                for i in [0, 1, 3]:
                    item = QtWidgets.QTableWidgetItem()
                    self.Average_Table.setItem(0, i, item)
                    item = self.Average_Table.item(0, i)
                    item.setText(self._translate("Average_Table", "All"))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 2, item)
                item = self.Average_Table.item(0, 2)
                item.setText(self._translate("Average_Table", getClass))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 4, item)
                item = self.Average_Table.item(0, 4)
                item.setText(self._translate("Average_Table", ans_avg))
            elif inputstate == 4:
                for i in [0, 1]:
                    item = QtWidgets.QTableWidgetItem()
                    self.Average_Table.setItem(0, i, item)
                    item = self.Average_Table.item(0, i)
                    item.setText(self._translate("Average_Table", "All"))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 2, item)
                item = self.Average_Table.item(0, 2)
                item.setText(self._translate("Average_Table", getClass))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 3, item)
                item = self.Average_Table.item(0, 3)
                item.setText(self._translate("Average_Table", getCourse))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 4, item)
                item = self.Average_Table.item(0, 4)
                item.setText(self._translate("Average_Table", ans_avg))
            elif inputstate == 5:
                sql = "select sName from student where sID='" + getSID + "';"
                cursor.execute(sql)
                findSName = cursor.fetchall()
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 0, item)
                item = self.Average_Table.item(0, 0)
                item.setText(self._translate("Average_Table", getSID))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 1, item)
                item = self.Average_Table.item(0, 1)
                item.setText(self._translate("Average_Table", findSName[0][0]))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 2, item)
                item = self.Average_Table.item(0, 2)
                item.setText(self._translate("Average_Table", "All"))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 3, item)
                item = self.Average_Table.item(0, 3)
                item.setText(self._translate("Average_Table", "All"))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 4, item)
                item = self.Average_Table.item(0, 4)
                item.setText(self._translate("Average_Table", ans_avg))

            elif inputstate == 6:
                sql = "select sID from student where sName='" + getSName + "';"
                cursor.execute(sql)
                findSID = cursor.fetchall()
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 0, item)
                item = self.Average_Table.item(0, 0)
                item.setText(self._translate("Average_Table", findSID[0][0]))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 1, item)
                item = self.Average_Table.item(0, 1)
                item.setText(self._translate("Average_Table", getSName))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 2, item)
                item = self.Average_Table.item(0, 2)
                item.setText(self._translate("Average_Table", "All"))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 3, item)
                item = self.Average_Table.item(0, 3)
                item.setText(self._translate("Average_Table", "All"))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 4, item)
                item = self.Average_Table.item(0, 4)
                item.setText(self._translate("Average_Table", ans_avg))
            elif inputstate == 7:
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 0, item)
                item = self.Average_Table.item(0, 0)
                item.setText(self._translate("Average_Table", getSID))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 1, item)
                item = self.Average_Table.item(0, 1)
                item.setText(self._translate("Average_Table", getSName))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 2, item)
                item = self.Average_Table.item(0, 2)
                item.setText(self._translate("Average_Table", "All"))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 3, item)
                item = self.Average_Table.item(0, 3)
                item.setText(self._translate("Average_Table", "All"))
                item = QtWidgets.QTableWidgetItem()
                self.Average_Table.setItem(0, 4, item)
                item = self.Average_Table.item(0, 4)
                item.setText(self._translate("Average_Table", ans_avg))


class Ui_Query_Course(QtWidgets.QWidget):
    Goback_Query = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Query_Course = self
        Query_Course.setObjectName("Query_Course")
        Query_Course.resize(800, 700)
        Query_Course.setMinimumSize(QtCore.QSize(800, 700))
        Query_Course.setMaximumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        Query_Course.setFont(font)
        self.Course_Table = QtWidgets.QTableWidget(Query_Course)
        self.Course_Table.setGeometry(QtCore.QRect(50, 200, 700, 400))
        self.Course_Table.setMinimumSize(QtCore.QSize(700, 400))
        self.Course_Table.setMaximumSize(QtCore.QSize(700, 400))
        self.Course_Table.setRowCount(0)
        self.Course_Table.setObjectName("Course_Table")
        self.Course_Table.setColumnCount(0)
        self.Course_Table.setFont(font)
        self.Course_Table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Query_Course_Button = QtWidgets.QPushButton(Query_Course)
        self.Query_Course_Button.setGeometry(QtCore.QRect(600, 53, 150, 64))
        self.Query_Course_Button.setMinimumSize(QtCore.QSize(150, 70))
        self.Query_Course_Button.setMaximumSize(QtCore.QSize(150, 70))
        self.Query_Course_Button.setObjectName("Query_Course_Button")
        self.Query_Course_Button.clicked.connect(self.Query_Course_SQL)
        self.Query_Course_Button.setFont(font)
        self.Query_back = QtWidgets.QPushButton(Query_Course)
        self.Query_back.setGeometry(QtCore.QRect(325, 615, 150, 70))
        self.Query_back.setMinimumSize(QtCore.QSize(150, 70))
        self.Query_back.setMaximumSize(QtCore.QSize(150, 70))
        self.Query_back.setObjectName("Query_back")
        self.Query_back.clicked.connect(self.Goback_Query.emit)
        self.Query_back.setFont(font)
        self.CName_label = QtWidgets.QLabel(Query_Course)
        self.CName_label.setGeometry(QtCore.QRect(50, 30, 191, 40))
        self.CName_label.setObjectName("CName_label")
        self.CName_label.setFont(font)
        self.CID_label = QtWidgets.QLabel(Query_Course)
        self.CID_label.setGeometry(QtCore.QRect(50, 98, 221, 40))
        self.CID_label.setObjectName("CID_label")
        self.CID_label.setFont(font)
        self.CName_input = QtWidgets.QLineEdit(Query_Course)
        self.CName_input.setGeometry(QtCore.QRect(250, 35, 300, 36))
        self.CName_input.setMinimumSize(QtCore.QSize(300, 36))
        self.CName_input.setMaximumSize(QtCore.QSize(300, 36))
        self.CName_input.setObjectName("CName_input")
        self.CName_input.setFont(font)
        self.CID_input = QtWidgets.QLineEdit(Query_Course)
        self.CID_input.setGeometry(QtCore.QRect(250, 99, 300, 36))
        self.CID_input.setMinimumSize(QtCore.QSize(300, 36))
        self.CID_input.setMaximumSize(QtCore.QSize(300, 36))
        self.CID_input.setObjectName("CID_input")
        self.CID_input.setFont(font)
        self.Result_label = QtWidgets.QLabel(Query_Course)
        self.Result_label.setGeometry(QtCore.QRect(250, 150, 300, 36))
        self.Result_label.setObjectName("Result_label")
        self.Result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Result_label.setFont(font)

        self.retranslateUi(Query_Course)
        QtCore.QMetaObject.connectSlotsByName(Query_Course)
        self._translate = QtCore.QCoreApplication.translate

    def retranslateUi(self, Query_Course):
        _translate = QtCore.QCoreApplication.translate
        Query_Course.setWindowTitle(_translate("Query_Teaching", "Course and Course Choosing Information"))
        self.Query_Course_Button.setText(_translate("Query_Teaching", "Query"))
        self.Query_back.setText(_translate("Query_Teaching", "Back"))
        self.CName_label.setText(_translate("Query_Teaching", "Course Name:"))
        self.CID_label.setText(_translate("Query_Teaching", "Course ID:"))
        self.Result_label.setText(_translate("Result_Label", "Number of result: 0"))

    def Query_Course_SQL(self):
        getCName = str(self.CName_input.text())
        getCID = self.CID_input.text()
        cursor = db.cursor()
        sql1 = "select ccID 'Course ID',cName 'Course Name',tName 'Teacher Name',credit,grade,canceled_year,ssID 'Student ID',sName 'Student Name' from course c, course_choosing cc, teacher t, student s where c.tID=t.tID and c.cID=cc.cID and cc.sID=s.sID"
        sql2 = " order by ccID"
        if getCName == "" and getCID == "":
            sql = sql1 + sql2
        elif getCName == "":
            sql = sql1 + " and ccID=" + getCID + sql2
        elif getCID == "":
            sql = sql1 + " and cName='" + getCName + "'" + sql2
        else:
            sql = sql1 + " and ccID=" + getCID + " and cName='" + getCName + "'" + sql2
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            self.Course_Table.clear()
            self.Course_Table.setColumnCount(0)
            self.Course_Table.setRowCount(0)
            col_result = cursor.description
            self.row = len(results)  # 取得记录个数，用于设置表格的行数
            self.vol = len(results[0])  # 取得字段数，用于设置表格的列数
            self.Result_label.setText(
                QtCore.QCoreApplication.translate("Result_Label", "Number of result: ") + str(self.row))
            col_result = list(col_result)
            a = 0
            self.Course_Table.setColumnCount(self.vol)
            self.Course_Table.setRowCount(self.row)
            for i in col_result:
                item = QtWidgets.QTableWidgetItem()
                self.Course_Table.setHorizontalHeaderItem(a, item)
                item = self.Course_Table.horizontalHeaderItem(a)
                item.setText(self._translate("Course_Table", i[0]))
                a = a + 1
            results = list(results)
            for i in range(len(results)):
                results[i] = list(results[i])
            for i in range(self.row):
                for j in range(self.vol):
                    item = QtWidgets.QTableWidgetItem()
                    self.Course_Table.setItem(i, j, item)
                    item = self.Course_Table.item(i, j)
                    item.setText(self._translate("Course_Table", str(results[i][j])))
        else:
            self.Course_Table.clear()
            self.Course_Table.setColumnCount(0)
            self.Course_Table.setRowCount(0)
            self.Result_label.setText(QtCore.QCoreApplication.translate("Result_Label", "Number of result: 0"))


class Ui_Query_Student(QtWidgets.QWidget):
    Goback_Query = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Query_Student = self
        Query_Student.setObjectName("Query_Student")
        Query_Student.resize(800, 700)
        Query_Student.setMinimumSize(QtCore.QSize(800, 700))
        Query_Student.setMaximumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        Query_Student.setFont(font)
        self.Student_Table = QtWidgets.QTableWidget(Query_Student)
        self.Student_Table.setGeometry(QtCore.QRect(50, 200, 700, 400))
        self.Student_Table.setMinimumSize(QtCore.QSize(700, 400))
        self.Student_Table.setMaximumSize(QtCore.QSize(700, 400))
        self.Student_Table.setRowCount(0)
        self.Student_Table.setObjectName("Student_Table")
        self.Student_Table.setColumnCount(0)
        self.Student_Table.setFont(font)
        self.Student_Table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Query_Student_Button = QtWidgets.QPushButton(Query_Student)
        self.Query_Student_Button.setGeometry(QtCore.QRect(600, 53, 150, 64))
        self.Query_Student_Button.setMinimumSize(QtCore.QSize(150, 70))
        self.Query_Student_Button.setMaximumSize(QtCore.QSize(150, 70))
        self.Query_Student_Button.setObjectName("Query_Course_Button")
        self.Query_Student_Button.clicked.connect(self.Query_Student_SQL)
        self.Query_Student_Button.setFont(font)
        self.Query_back = QtWidgets.QPushButton(Query_Student)
        self.Query_back.setGeometry(QtCore.QRect(325, 615, 150, 70))
        self.Query_back.setMinimumSize(QtCore.QSize(150, 70))
        self.Query_back.setMaximumSize(QtCore.QSize(150, 70))
        self.Query_back.setObjectName("Query_back")
        self.Query_back.clicked.connect(self.Goback_Query.emit)
        self.Query_back.setFont(font)
        self.SName_label = QtWidgets.QLabel(Query_Student)
        self.SName_label.setGeometry(QtCore.QRect(50, 30, 191, 40))
        self.SName_label.setObjectName("CName_label")
        self.SName_label.setFont(font)
        self.SID_label = QtWidgets.QLabel(Query_Student)
        self.SID_label.setGeometry(QtCore.QRect(50, 98, 221, 40))
        self.SID_label.setObjectName("CID_label")
        self.SID_label.setFont(font)
        self.SName_input = QtWidgets.QLineEdit(Query_Student)
        self.SName_input.setGeometry(QtCore.QRect(250, 35, 300, 36))
        self.SName_input.setMinimumSize(QtCore.QSize(300, 36))
        self.SName_input.setMaximumSize(QtCore.QSize(300, 36))
        self.SName_input.setObjectName("CName_input")
        self.SName_input.setFont(font)
        self.SID_input = QtWidgets.QLineEdit(Query_Student)
        self.SID_input.setGeometry(QtCore.QRect(250, 99, 300, 36))
        self.SID_input.setMinimumSize(QtCore.QSize(300, 36))
        self.SID_input.setMaximumSize(QtCore.QSize(300, 36))
        self.SID_input.setObjectName("CID_input")
        self.SID_input.setFont(font)
        self.Result_label = QtWidgets.QLabel(Query_Student)
        self.Result_label.setGeometry(QtCore.QRect(250, 150, 300, 36))
        self.Result_label.setObjectName("Result_label")
        self.Result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Result_label.setFont(font)

        self.retranslateUi(Query_Student)
        QtCore.QMetaObject.connectSlotsByName(Query_Student)
        self._translate = QtCore.QCoreApplication.translate

    def retranslateUi(self, Query_Student):
        _translate = QtCore.QCoreApplication.translate
        Query_Student.setWindowTitle(_translate("Query_Student", "Student Course Choosing Information"))
        self.Query_Student_Button.setText(_translate("Query_Student", "Query"))
        self.Query_back.setText(_translate("Query_Student", "Back"))
        self.SName_label.setText(_translate("Query_Student", "Student Name:"))
        self.SID_label.setText(_translate("Query_Student", "Student ID:"))
        self.Result_label.setText(_translate("Result_Label", "Number of result: 0"))

    def Query_Student_SQL(self):
        getSName = str(self.SName_input.text())
        getSID = self.SID_input.text()
        cursor = db.cursor()
        sql1 = "select ssID 'Student ID',sName 'Student Name',ccID 'Course ID',cName 'Course Name',tName 'Teacher Name',credit,grade,canceled_year from course c, course_choosing cc, teacher t, student s where c.tID=t.tID and c.cID=cc.cID and cc.sID=s.sID"
        sql2 = " order by ssID"
        if getSName == "" and getSID == "":
            sql = sql1 + sql2
        elif getSName == "":
            sql = sql1 + " and ssID=" + getSID + sql2
        elif getSID == "":
            sql = sql1 + " and sName='" + getSName + "'" + sql2
        else:
            sql = sql1 + " and ssID=" + getSID + " and sName='" + getSName + "'" + sql2
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            self.Student_Table.clear()
            self.Student_Table.setColumnCount(0)
            self.Student_Table.setRowCount(0)
            col_result = cursor.description
            self.row = len(results)  # 取得记录个数，用于设置表格的行数
            self.vol = len(results[0])  # 取得字段数，用于设置表格的列数
            self.Result_label.setText(
                QtCore.QCoreApplication.translate("Result_Label", "Number of result: ") + str(self.row))
            col_result = list(col_result)
            a = 0
            self.Student_Table.setColumnCount(self.vol)
            self.Student_Table.setRowCount(self.row)
            for i in col_result:
                item = QtWidgets.QTableWidgetItem()
                self.Student_Table.setHorizontalHeaderItem(a, item)
                item = self.Student_Table.horizontalHeaderItem(a)
                item.setText(self._translate("Student_Table", i[0]))
                a = a + 1
            results = list(results)
            for i in range(len(results)):
                results[i] = list(results[i])
            for i in range(self.row):
                for j in range(self.vol):
                    item = QtWidgets.QTableWidgetItem()
                    self.Student_Table.setItem(i, j, item)
                    item = self.Student_Table.item(i, j)
                    item.setText(self._translate("Student_Table", str(results[i][j])))
        else:
            self.Student_Table.clear()
            self.Student_Table.setColumnCount(0)
            self.Student_Table.setRowCount(0)
            self.Result_label.setText(QtCore.QCoreApplication.translate("Result_Label", "Number of result: 0"))


class Ui_Query_Score(QtWidgets.QWidget):
    Goback_Query = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Query_Score = self
        Query_Score.setObjectName("Query_Score")
        Query_Score.resize(800, 700)
        Query_Score.setMinimumSize(QtCore.QSize(800, 700))
        Query_Score.setMaximumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        Query_Score.setFont(font)
        self.Score_Table = QtWidgets.QTableWidget(Query_Score)
        self.Score_Table.setGeometry(QtCore.QRect(50, 250, 700, 350))
        self.Score_Table.setMinimumSize(QtCore.QSize(700, 350))
        self.Score_Table.setMaximumSize(QtCore.QSize(700, 350))
        self.Score_Table.setRowCount(0)
        self.Score_Table.setObjectName("Score_Table")
        self.Score_Table.setColumnCount(0)
        self.Score_Table.setFont(font)
        self.Score_Table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Query_Score_Button = QtWidgets.QPushButton(Query_Score)
        self.Query_Score_Button.setGeometry(QtCore.QRect(600, 78, 150, 64))
        self.Query_Score_Button.setMinimumSize(QtCore.QSize(150, 70))
        self.Query_Score_Button.setMaximumSize(QtCore.QSize(150, 70))
        self.Query_Score_Button.setObjectName("Query_Score_Button")
        self.Query_Score_Button.clicked.connect(self.Query_Score_SQL)
        self.Query_Score_Button.setFont(font)
        self.Query_back = QtWidgets.QPushButton(Query_Score)
        self.Query_back.setGeometry(QtCore.QRect(325, 615, 150, 70))
        self.Query_back.setMinimumSize(QtCore.QSize(150, 70))
        self.Query_back.setMaximumSize(QtCore.QSize(150, 70))
        self.Query_back.setObjectName("Query_back")
        self.Query_back.clicked.connect(self.Goback_Query.emit)
        self.Query_back.setFont(font)
        self.SName_label = QtWidgets.QLabel(Query_Score)
        self.SName_label.setGeometry(QtCore.QRect(50, 30, 191, 40))
        self.SName_label.setObjectName("SName_label")
        self.SName_label.setFont(font)
        self.SID_label = QtWidgets.QLabel(Query_Score)
        self.SID_label.setGeometry(QtCore.QRect(50, 70, 221, 40))
        self.SID_label.setObjectName("SID_label")
        self.SID_label.setFont(font)
        self.cName_label = QtWidgets.QLabel(Query_Score)
        self.cName_label.setGeometry(QtCore.QRect(50, 110, 221, 40))
        self.cName_label.setObjectName("cName_label")
        self.cName_label.setFont(font)
        self.courseID_label = QtWidgets.QLabel(Query_Score)
        self.courseID_label.setGeometry(QtCore.QRect(50, 150, 221, 40))
        self.courseID_label.setObjectName("courseID_label")
        self.courseID_label.setFont(font)
        self.SName_input = QtWidgets.QLineEdit(Query_Score)
        self.SName_input.setGeometry(QtCore.QRect(250, 32, 300, 36))
        self.SName_input.setMinimumSize(QtCore.QSize(300, 36))
        self.SName_input.setMaximumSize(QtCore.QSize(300, 36))
        self.SName_input.setObjectName("SName_input")
        self.SName_input.setFont(font)
        self.SID_input = QtWidgets.QLineEdit(Query_Score)
        self.SID_input.setGeometry(QtCore.QRect(250, 72, 300, 36))
        self.SID_input.setMinimumSize(QtCore.QSize(300, 36))
        self.SID_input.setMaximumSize(QtCore.QSize(300, 36))
        self.SID_input.setObjectName("SID_input")
        self.SID_input.setFont(font)
        self.cName_input = QtWidgets.QLineEdit(Query_Score)
        self.cName_input.setGeometry(QtCore.QRect(250, 112, 300, 36))
        self.cName_input.setMinimumSize(QtCore.QSize(300, 36))
        self.cName_input.setMaximumSize(QtCore.QSize(300, 36))
        self.cName_input.setObjectName("cName_input")
        self.cName_input.setFont(font)
        self.courseID_input = QtWidgets.QLineEdit(Query_Score)
        self.courseID_input.setGeometry(QtCore.QRect(250, 152, 300, 36))
        self.courseID_input.setMinimumSize(QtCore.QSize(300, 36))
        self.courseID_input.setMaximumSize(QtCore.QSize(300, 36))
        self.courseID_input.setObjectName("courseID_input")
        self.courseID_input.setFont(font)

        self.Result_label = QtWidgets.QLabel(Query_Score)
        self.Result_label.setGeometry(QtCore.QRect(250, 200, 300, 36))
        self.Result_label.setObjectName("Result_label")
        self.Result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Result_label.setFont(font)

        self.retranslateUi(Query_Score)
        QtCore.QMetaObject.connectSlotsByName(Query_Score)
        self._translate = QtCore.QCoreApplication.translate

    def retranslateUi(self, Query_Score):
        _translate = QtCore.QCoreApplication.translate
        Query_Score.setWindowTitle(_translate("Query_Score", "Course Score"))
        self.Query_Score_Button.setText(_translate("Query_Score", "Query"))
        self.Query_back.setText(_translate("Query_Score", "Back"))
        self.SName_label.setText(_translate("Query_Score", "Student Name:"))
        self.SID_label.setText(_translate("Query_Score", "Student ID:"))
        self.cName_label.setText(_translate("Query_Score", "Course Name:"))
        self.courseID_label.setText(_translate("Query_Score", "Course ID:"))
        self.Result_label.setText(_translate("Result_Label", "Number of result: 0"))

    def Query_Score_SQL(self):
        getSName = str(self.SName_input.text())
        getSID = self.SID_input.text()
        getCName = self.cName_input.text()
        getCID = self.courseID_input.text()
        cursor = db.cursor()
        sql1 = "select ssID 'Student ID',sName 'Student Name',ccID 'Course ID',cName 'Course Name',score from course c,student s,course_choosing cc where c.cID=cc.cID and s.sID=cc.sID"
        sql2 = " order by ssID;"
        if getSName == "" and getSID == "" and getCName == "" and getCID == "":
            sql = sql1 + sql2
        elif getSName == "" and getSID == "" and getCName == "" and getCID != "":
            sql = sql1 + " and c.cID=" + getCID + sql2
        elif getSName == "" and getSID == "" and getCName != "" and getCID == "":
            sql = sql1 + " and c.cName='" + getCName + "'" + sql2
        elif getSName == "" and getSID == "" and getCName != "" and getCID != "":
            sql = sql1 + " and c.cID=" + getCID + " and c.cName='" + getCName + "'" + sql2
        elif getSName == "" and getSID != "" and getCName == "" and getCID == "":
            sql = sql1 + " and s.sID=" + getSID + sql2
        elif getSName == "" and getSID != "" and getCName == "" and getCID != "":
            sql = sql1 + " and s.sID=" + getSID + " and c.cID=" + getCID + sql2
        elif getSName == "" and getSID != "" and getCName != "" and getCID == "":
            sql = sql1 + " and s.sID=" + getSID + " and c.cName='" + getCName + "'" + sql2
        elif getSName == "" and getSID != "" and getCName != "" and getCID != "":
            sql = sql1 + " and s.sID=" + getSID + " and c.cName='" + getCName + "' and c.cID=" + getCID + sql2
        elif getSName != "" and getSID == "" and getCName == "" and getCID == "":
            sql = sql1 + " and s.sName='" + getSName + "'" + sql2
        elif getSName != "" and getSID == "" and getCName == "" and getCID != "":
            sql = sql1 + " and s.sName='" + getSName + "' and c.cID=" + getCID + sql2
        elif getSName != "" and getSID == "" and getCName != "" and getCID == "":
            sql = sql1 + " and s.sName='" + getSName + "' and c.cName='" + getCName + "'" + sql2
        elif getSName != "" and getSID == "" and getCName != "" and getCID != "":
            sql = sql1 + " and s.sName='" + getSName + "' and c.cName='" + getCName + "' and c.cID=" + getCID + sql2
        elif getSName != "" and getSID != "" and getCName == "" and getCID == "":
            sql = sql1 + " and s.sName='" + getSName + "' and s.sID=" + getSID + sql2
        elif getSName != "" and getSID != "" and getCName == "" and getCID != "":
            sql = sql1 + " and s.sName='" + getSName + "' and s.sID=" + getSID + " and c.cID=" + getCID + sql2
        elif getSName != "" and getSID != "" and getCName != "" and getCID == "":
            sql = sql1 + " and s.sName='" + getSName + "' and s.sID=" + getSID + " and c.cName='" + getCName + "'" + sql2
        elif getSName != "" and getSID != "" and getCName != "" and getCID != "":
            sql = sql1 + " and s.sName='" + getSName + "' and s.sID=" + getSID + " and c.cName='" + getCName + "' and c.cID=" + getCID + sql2
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            self.Score_Table.clear()
            self.Score_Table.setColumnCount(0)
            self.Score_Table.setRowCount(0)
            col_result = cursor.description
            self.row = len(results)  # 取得记录个数，用于设置表格的行数
            self.vol = len(results[0])  # 取得字段数，用于设置表格的列数
            self.Result_label.setText(
                QtCore.QCoreApplication.translate("Result_Label", "Number of result: ") + str(self.row))
            col_result = list(col_result)
            a = 0
            self.Score_Table.setColumnCount(self.vol)
            self.Score_Table.setRowCount(self.row)
            for i in col_result:
                item = QtWidgets.QTableWidgetItem()
                self.Score_Table.setHorizontalHeaderItem(a, item)
                item = self.Score_Table.horizontalHeaderItem(a)
                item.setText(self._translate("Score_Table", i[0]))
                a = a + 1
            results = list(results)
            for i in range(len(results)):
                results[i] = list(results[i])
            for i in range(self.row):
                for j in range(self.vol):
                    item = QtWidgets.QTableWidgetItem()
                    self.Score_Table.setItem(i, j, item)
                    item = self.Score_Table.item(i, j)
                    item.setText(self._translate("Student_Table", str(results[i][j])))
        else:
            self.Score_Table.clear()
            self.Score_Table.setColumnCount(0)
            self.Score_Table.setRowCount(0)
            self.Result_label.setText(QtCore.QCoreApplication.translate("Result_Label", "Number of result: 0"))


class Ui_Admin_Student(QtWidgets.QWidget):
    Student_Goback_Admin = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Admin_Student = self
        Admin_Student.setObjectName("Admin_Student")
        Admin_Student.resize(800, 700)
        Admin_Student.setMinimumSize(QtCore.QSize(800, 700))
        Admin_Student.setMaximumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        Admin_Student.setFont(font)
        self.Student_Modify_Info = QtWidgets.QTableWidget(Admin_Student)
        self.Student_Modify_Info.setGeometry(QtCore.QRect(50, 510, 700, 100))
        self.Student_Modify_Info.setMinimumSize(QtCore.QSize(700, 100))
        self.Student_Modify_Info.setMaximumSize(QtCore.QSize(700, 100))
        self.Student_Modify_Info.setObjectName("Student_Modify_Info")
        self.Student_Modify_Info.setColumnCount(0)
        self.Student_Modify_Info.setRowCount(0)
        self.Student_Modify_Info.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Query_back = QtWidgets.QPushButton(Admin_Student)
        self.Query_back.setGeometry(QtCore.QRect(320, 620, 150, 70))
        self.Query_back.setMinimumSize(QtCore.QSize(160, 70))
        self.Query_back.setMaximumSize(QtCore.QSize(160, 70))
        self.Query_back.setObjectName("Query_back")
        self.Query_back.clicked.connect(self.Student_Goback_Admin.emit)
        self.sID_label = QtWidgets.QLabel(Admin_Student)
        self.sID_label.setGeometry(QtCore.QRect(50, 20, 160, 30))
        self.sID_label.setObjectName("sID_label")
        self.sName_label = QtWidgets.QLabel(Admin_Student)
        self.sName_label.setGeometry(QtCore.QRect(50, 70, 160, 30))
        self.sName_label.setObjectName("sName_label")
        self.Seperator = QtWidgets.QFrame(Admin_Student)
        self.Seperator.setGeometry(QtCore.QRect(50, 115, 700, 20))
        self.Seperator.setFrameShape(QtWidgets.QFrame.HLine)
        self.Seperator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Seperator.setObjectName("Seperator")
        self.new_SID_label = QtWidgets.QLabel(Admin_Student)
        self.new_SID_label.setGeometry(QtCore.QRect(50, 150, 160, 30))
        self.new_SID_label.setObjectName("new_SID_label")
        self.new_SName_label = QtWidgets.QLabel(Admin_Student)
        self.new_SName_label.setGeometry(QtCore.QRect(50, 200, 160, 30))
        self.new_SName_label.setObjectName("new_SName_label")
        self.new_sex_label = QtWidgets.QLabel(Admin_Student)
        self.new_sex_label.setGeometry(QtCore.QRect(50, 260, 160, 30))
        self.new_sex_label.setObjectName("new_sex_label")
        self.new_enAge_label = QtWidgets.QLabel(Admin_Student)
        self.new_enAge_label.setGeometry(QtCore.QRect(50, 310, 160, 30))
        self.new_enAge_label.setObjectName("new_enAge_label")
        self.new_enYear_label = QtWidgets.QLabel(Admin_Student)
        self.new_enYear_label.setGeometry(QtCore.QRect(50, 370, 160, 30))
        self.new_enYear_label.setObjectName("new_enYear_label")
        self.new_class_label = QtWidgets.QLabel(Admin_Student)
        self.new_class_label.setGeometry(QtCore.QRect(50, 420, 160, 30))
        self.new_class_label.setObjectName("new_class_label")
        self.sID_input = QtWidgets.QLineEdit(Admin_Student)
        self.sID_input.setGeometry(QtCore.QRect(250, 15, 300, 36))
        self.sID_input.setObjectName("sID_input")
        self.sName_input = QtWidgets.QLineEdit(Admin_Student)
        self.sName_input.setGeometry(QtCore.QRect(250, 70, 300, 36))
        self.sName_input.setObjectName("sName_input")
        self.new_sID_input = QtWidgets.QLineEdit(Admin_Student)
        self.new_sID_input.setGeometry(QtCore.QRect(250, 145, 300, 36))
        self.new_sID_input.setObjectName("new_sID_input")
        self.new_sName_input = QtWidgets.QLineEdit(Admin_Student)
        self.new_sName_input.setGeometry(QtCore.QRect(250, 200, 300, 36))
        self.new_sName_input.setObjectName("new_sName_input")
        self.new_sex_input = QtWidgets.QLineEdit(Admin_Student)
        self.new_sex_input.setGeometry(QtCore.QRect(250, 255, 300, 36))
        self.new_sex_input.setObjectName("new_sex_input")
        self.new_enAge_input = QtWidgets.QLineEdit(Admin_Student)
        self.new_enAge_input.setGeometry(QtCore.QRect(250, 310, 300, 36))
        self.new_enAge_input.setObjectName("new_enAge_input")
        self.new_enYear_input = QtWidgets.QLineEdit(Admin_Student)
        self.new_enYear_input.setGeometry(QtCore.QRect(250, 365, 300, 36))
        self.new_enYear_input.setObjectName("new_enYear_input")
        self.new_class_input = QtWidgets.QLineEdit(Admin_Student)
        self.new_class_input.setGeometry(QtCore.QRect(250, 420, 300, 36))
        self.new_class_input.setObjectName("new_class_input")
        self.Focus_Item = QtWidgets.QPushButton(Admin_Student)
        self.Focus_Item.setGeometry(QtCore.QRect(600, 25, 150, 70))
        self.Focus_Item.setObjectName("Focus_Item")
        self.Focus_Item.clicked.connect(self.focus_man)
        self.Delete_Button = QtWidgets.QPushButton(Admin_Student)
        self.Delete_Button.setGeometry(QtCore.QRect(600, 140, 150, 70))
        self.Delete_Button.setObjectName("Delete_Button")
        self.Delete_Button.clicked.connect(self.delete_student_info)
        self.Insert_Button = QtWidgets.QPushButton(Admin_Student)
        self.Insert_Button.setGeometry(QtCore.QRect(600, 220, 150, 70))
        self.Insert_Button.setObjectName("Insert_Button")
        self.Insert_Button.clicked.connect(self.insert_student_info)
        self.Update_Button = QtWidgets.QPushButton(Admin_Student)
        self.Update_Button.setGeometry(QtCore.QRect(600, 300, 150, 70))
        self.Update_Button.setObjectName("Update_Button")
        self.Update_Button.clicked.connect(self.update_student_info)
        self.error_display_label = QtWidgets.QLabel(Admin_Student)
        self.error_display_label.setGeometry(QtCore.QRect(50, 470, 700, 30))
        self.error_display_label.setObjectName("error_display_label")
        self.error_display_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_display_label.setVisible(False)
        self.error_display_label.setStyleSheet("color:rgb(255, 0, 0);")
        self.focusSID = ""
        self.retranslateUi(Admin_Student)
        QtCore.QMetaObject.connectSlotsByName(Admin_Student)

    def retranslateUi(self, Admin_Student):
        _translate = QtCore.QCoreApplication.translate
        Admin_Student.setWindowTitle(_translate("Admin_Student", "Administrator Modify Student Information"))
        self.Query_back.setText(_translate("Admin_Student", "Back"))
        self.sID_label.setText(_translate("Admin_Student", "Student ID:"))
        self.sName_label.setText(_translate("Admin_Student", "Student Name:"))
        self.new_SID_label.setText(_translate("Admin_Student", "*Student ID:"))
        self.new_SName_label.setText(_translate("Admin_Student", "*Student Name:"))
        self.new_sex_label.setText(_translate("Admin_Student", "*Sex:"))
        self.new_enAge_label.setText(_translate("Admin_Student", "*Entrance Age:"))
        self.new_enYear_label.setText(_translate("Admin_Student", "*Entrance Year:"))
        self.new_class_label.setText(_translate("Admin_Student", "*Class:"))
        self.Focus_Item.setText(_translate("Admin_Student", "Focus"))
        self.Delete_Button.setText(_translate("Admin_Student", "Delete"))
        self.Insert_Button.setText(_translate("Admin_Student", "Insert"))
        self.Update_Button.setText(_translate("Admin_Student", "Update"))
        self.error_display_label.setText(_translate("Admin_Student", "Error Display"))
        self._translate = QtCore.QCoreApplication.translate

    def focus_man(self):
        getSID = self.sID_input.text()
        getSName = self.sName_input.text()
        self.focusSID = ""
        cursor = db.cursor()
        if getSID == "" and getSName == "":
            sql = "select * from student;"
        if getSID == "" and getSName != "":
            sql = "select * from student where sName='" + getSName + "';"
        if getSID != "" and getSName == "":
            sql = "select * from student where sID=" + getSID + ";"
        if getSID != "" and getSName != "":
            sql = "select * from student where sName='" + getSName + "' and sID=" + getSID + ";"
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            if len(results) == 1:
                self.focusSID = results[0][0]
                self.error_display_label.setVisible(True)
                self.error_display_label.setText("Successful Catch.")
                self.new_sID_input.setText(results[0][0])
                self.new_sName_input.setText(results[0][1])
                self.new_sex_input.setText(results[0][2])
                self.new_enAge_input.setText(str(results[0][3]))
                self.new_enYear_input.setText(str(results[0][4]))
                self.new_class_input.setText(results[0][5])
            else:
                self.new_sID_input.setText("")
                self.new_sName_input.setText("")
                self.new_sex_input.setText("")
                self.new_enAge_input.setText("")
                self.new_enYear_input.setText("")
                self.new_class_input.setText("")
                self.error_display_label.setVisible(True)
                self.error_display_label.setText("Already Catch All. Please Focus On One Item.")
            self.Student_Modify_Info.clear()
            self.Student_Modify_Info.setColumnCount(0)
            self.Student_Modify_Info.setRowCount(0)
            col_result = cursor.description
            self.row = len(results)  # 取得记录个数，用于设置表格的行数
            self.vol = len(results[0]) - 1  # 取得字段数，用于设置表格的列数
            col_result = list(col_result)
            a = 0
            self.Student_Modify_Info.setColumnCount(self.vol)
            self.Student_Modify_Info.setRowCount(self.row)
            for i in col_result[:len(col_result) - 1]:
                item = QtWidgets.QTableWidgetItem()
                self.Student_Modify_Info.setHorizontalHeaderItem(a, item)
                item = self.Student_Modify_Info.horizontalHeaderItem(a)
                item.setText(self._translate("Student_Modify_Info", i[0]))
                a = a + 1
            results = list(results)
            for i in range(len(results)):
                results[i] = list(results[i])
            for i in range(self.row):
                for j in range(self.vol):
                    item = QtWidgets.QTableWidgetItem()
                    self.Student_Modify_Info.setItem(i, j, item)
                    item = self.Student_Modify_Info.item(i, j)
                    item.setText(self._translate("Student_Table", str(results[i][j])))
        else:
            self.new_sID_input.setText("")
            self.new_sName_input.setText("")
            self.new_sex_input.setText("")
            self.new_enAge_input.setText("")
            self.new_enYear_input.setText("")
            self.new_class_input.setText("")
            self.error_display_label.setText("Error: Item Not Exist. Fail to Catch.")
            self.error_display_label.setVisible(True)
            self.Student_Modify_Info.clear()
            self.Student_Modify_Info.setColumnCount(0)
            self.Student_Modify_Info.setRowCount(0)

    def update_student_info(self):
        if self.focusSID == "":
            self.error_display_label.setText("Please Focus One Item First.")
            self.error_display_label.setVisible(True)
        elif self.new_sex_input.text() != "male" and self.new_sex_input.text() != "female" and self.new_sex_input.text() != "Male" and self.new_sex_input.text() != "Female":
            self.error_display_label.setText("Error: Sex must be male or female.")
            self.error_display_label.setVisible(True)
        elif (self.new_enAge_input.text()).isdigit() == False or int(self.new_enAge_input.text()) < 10 or int(
                self.new_enAge_input.text()) > 50:
            self.error_display_label.setText("Error: Entrance Age should between 10 and 50.")
            self.error_display_label.setVisible(True)
        elif (self.new_sID_input.text()).isdigit() == False or len(self.new_sID_input.text()) != 10:
            self.error_display_label.setText("Error: Student ID length should be 10.")
            self.error_display_label.setVisible(True)
        elif self.new_sName_input.text() == "" or self.new_class_input.text() == "" or (
        self.new_enYear_input.text()).isdigit() == False:
            self.error_display_label.setText("Error: Exist Empty or Illegal Information.")
            self.error_display_label.setVisible(True)
        else:
            if self.focusSID != self.new_sID_input.text():
                cursor = db.cursor()
                sql = "SELECT COUNT(*) FROM student WHERE sID = " + self.new_sID_input.text() + ";"
                cursor.execute(sql)
                results = cursor.fetchall()
                if results[0][0] >= 1:
                    self.error_display_label.setText("Error: Student ID is already exist.")
                    self.error_display_label.setVisible(True)
                    return

            cursor = db.cursor()
            sql = "update student set sName='" + self.new_sName_input.text() + "' where sID=" + self.focusSID
            cursor.execute(sql)
            sql = "update student set sex='" + self.new_sex_input.text() + "' where sID=" + self.focusSID
            cursor.execute(sql)
            sql = "update student set entrance_age='" + self.new_enAge_input.text() + "' where sID=" + self.focusSID
            cursor.execute(sql)
            sql = "update student set entrance_year='" + self.new_enYear_input.text() + "' where sID=" + self.focusSID
            cursor.execute(sql)
            sql = "update student set class='" + self.new_class_input.text() + "' where sID=" + self.focusSID
            cursor.execute(sql)
            sql = "update student set ssID='" + self.new_sID_input.text() + "' where sID=" + self.focusSID
            cursor.execute(sql)
            sql = "update student set sID='" + self.new_sID_input.text() + "' where sID=" + self.focusSID
            cursor.execute(sql)
            sql = "update course_choosing set sID='" + self.new_sID_input.text() + "' where sID=" + self.focusSID
            cursor.execute(sql)
            sql = "update user_info set ID='" + self.new_sID_input.text() + "' where ID=" + self.focusSID
            cursor.execute(sql)
            db.commit()
            self.error_display_label.setText("Successful Update.")
            self.error_display_label.setVisible(True)

    def insert_student_info(self):

        if self.focusSID != "":
            self.error_display_label.setText("Don't Focus For Insertion.")
            self.error_display_label.setVisible(True)
        elif self.new_sex_input.text() != "male" and self.new_sex_input.text() != "female" and self.new_sex_input.text() != "Male" and self.new_sex_input.text() != "Female":
            self.error_display_label.setText("Error: Sex must be male or female.")
            self.error_display_label.setVisible(True)
        elif (self.new_enAge_input.text()).isdigit() == False or int(self.new_enAge_input.text()) < 10 or int(
                self.new_enAge_input.text()) > 50:
            self.error_display_label.setText("Error: Entrance Age should between 10 and 50.")
            self.error_display_label.setVisible(True)
        elif (self.new_sID_input.text()).isdigit() == False or len(self.new_sID_input.text()) != 10:
            self.error_display_label.setText("Error: Student ID length should be 10.")
            self.error_display_label.setVisible(True)
        elif self.new_sName_input.text() == "" or self.new_class_input.text() == "" or (
        self.new_enYear_input.text()).isdigit() == False:
            self.error_display_label.setText("Error: Exist Empty or Illegal Information.")
            self.error_display_label.setVisible(True)
        else:
            cursor = db.cursor()
            sql = "SELECT COUNT(*) FROM student WHERE sID = " + self.new_sID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if results[0][0] > 0:
                self.error_display_label.setText("Error: Student ID is already exist.")
                self.error_display_label.setVisible(True)
            else:
                cursor = db.cursor()
                sql = "insert into student values(" + self.new_sID_input.text() + ",'" + self.new_sName_input.text() + "','" + self.new_sex_input.text() + "'," + self.new_enAge_input.text() + "," + self.new_enYear_input.text() + ",'" + self.new_class_input.text() + "'," + self.new_sID_input.text() + ");"
                cursor.execute(sql)
                sql = "insert into user_info values(" + self.new_sID_input.text() + ",'Student',123456);"
                cursor.execute(sql)
                db.commit()
                self.error_display_label.setText("Successful Insertion.")
                self.error_display_label.setVisible(True)

    def delete_student_info(self):
        if self.focusSID == "":
            self.error_display_label.setText("Please Focus One Item First.")
            self.error_display_label.setVisible(True)
        else:
            cursor = db.cursor()
            sql = "SELECT COUNT(*) FROM student WHERE sID = " + self.focusSID + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if results[0][0] == 0:
                self.error_display_label.setText("Error: Student ID don't exist.")
                self.error_display_label.setVisible(True)
            else:
                cursor = db.cursor()
                sql = "delete from student where sID=" + self.focusSID + ";"
                cursor.execute(sql)
                sql = "delete from course_choosing where sID=" + self.focusSID + ";"
                cursor.execute(sql)
                sql = "delete from user_info where ID=" + self.focusSID + ";"
                cursor.execute(sql)
                db.commit()
                self.error_display_label.setText("Successful Deletion")
                self.error_display_label.setVisible(True)


class Ui_Admin_Course(QtWidgets.QWidget):
    Course_Goback_Admin = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Admin_Course = self
        Admin_Course.setObjectName("Admin_Course")
        Admin_Course.resize(800, 700)
        Admin_Course.setMinimumSize(QtCore.QSize(800, 700))
        Admin_Course.setMaximumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        Admin_Course.setFont(font)
        self.Course_Modify_Info = QtWidgets.QTableWidget(Admin_Course)
        self.Course_Modify_Info.setGeometry(QtCore.QRect(50, 510, 700, 100))
        self.Course_Modify_Info.setMinimumSize(QtCore.QSize(700, 100))
        self.Course_Modify_Info.setMaximumSize(QtCore.QSize(700, 100))
        self.Course_Modify_Info.setObjectName("Course_Modify_Info")
        self.Course_Modify_Info.setColumnCount(0)
        self.Course_Modify_Info.setRowCount(0)
        self.Course_Modify_Info.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Query_back = QtWidgets.QPushButton(Admin_Course)
        self.Query_back.setGeometry(QtCore.QRect(320, 620, 150, 70))
        self.Query_back.setMinimumSize(QtCore.QSize(160, 70))
        self.Query_back.setMaximumSize(QtCore.QSize(160, 70))
        self.Query_back.setObjectName("Query_back")
        self.Query_back.clicked.connect(self.Course_Goback_Admin.emit)
        self.cID_label = QtWidgets.QLabel(Admin_Course)
        self.cID_label.setGeometry(QtCore.QRect(50, 20, 160, 30))
        self.cID_label.setObjectName("cID_label")
        self.cName_label = QtWidgets.QLabel(Admin_Course)
        self.cName_label.setGeometry(QtCore.QRect(50, 70, 160, 30))
        self.cName_label.setObjectName("cName_label")
        self.Seperator = QtWidgets.QFrame(Admin_Course)
        self.Seperator.setGeometry(QtCore.QRect(50, 115, 700, 20))
        self.Seperator.setFrameShape(QtWidgets.QFrame.HLine)
        self.Seperator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Seperator.setObjectName("Seperator")
        self.new_CID_label = QtWidgets.QLabel(Admin_Course)
        self.new_CID_label.setGeometry(QtCore.QRect(50, 150, 160, 30))
        self.new_CID_label.setObjectName("new_CID_label")
        self.new_CName_label = QtWidgets.QLabel(Admin_Course)
        self.new_CName_label.setGeometry(QtCore.QRect(50, 200, 160, 30))
        self.new_CName_label.setObjectName("new_CName_label")
        self.new_tID_label = QtWidgets.QLabel(Admin_Course)
        self.new_tID_label.setGeometry(QtCore.QRect(50, 260, 160, 30))
        self.new_tID_label.setObjectName("new_tID_label")
        self.new_credit_label = QtWidgets.QLabel(Admin_Course)
        self.new_credit_label.setGeometry(QtCore.QRect(50, 310, 160, 30))
        self.new_credit_label.setObjectName("new_credit_label")
        self.new_grade_label = QtWidgets.QLabel(Admin_Course)
        self.new_grade_label.setGeometry(QtCore.QRect(50, 370, 160, 30))
        self.new_grade_label.setObjectName("new_grade_label")
        self.new_cancelyear_label = QtWidgets.QLabel(Admin_Course)
        self.new_cancelyear_label.setGeometry(QtCore.QRect(50, 420, 170, 30))
        self.new_cancelyear_label.setObjectName("new_cancelyear_label")
        self.cID_input = QtWidgets.QLineEdit(Admin_Course)
        self.cID_input.setGeometry(QtCore.QRect(250, 15, 300, 36))
        self.cID_input.setObjectName("cID_input")
        self.cName_input = QtWidgets.QLineEdit(Admin_Course)
        self.cName_input.setGeometry(QtCore.QRect(250, 70, 300, 36))
        self.cName_input.setObjectName("cName_input")
        self.new_cID_input = QtWidgets.QLineEdit(Admin_Course)
        self.new_cID_input.setGeometry(QtCore.QRect(250, 145, 300, 36))
        self.new_cID_input.setObjectName("new_cID_input")
        self.new_cName_input = QtWidgets.QLineEdit(Admin_Course)
        self.new_cName_input.setGeometry(QtCore.QRect(250, 200, 300, 36))
        self.new_cName_input.setObjectName("new_cName_input")
        self.new_tID_input = QtWidgets.QLineEdit(Admin_Course)
        self.new_tID_input.setGeometry(QtCore.QRect(250, 255, 300, 36))
        self.new_tID_input.setObjectName("new_tID_input")
        self.new_credit_input = QtWidgets.QLineEdit(Admin_Course)
        self.new_credit_input.setGeometry(QtCore.QRect(250, 310, 300, 36))
        self.new_credit_input.setObjectName("new_credit_input")
        self.new_grade_input = QtWidgets.QLineEdit(Admin_Course)
        self.new_grade_input.setGeometry(QtCore.QRect(250, 365, 300, 36))
        self.new_grade_input.setObjectName("new_grade_input")
        self.new_cancelyear_input = QtWidgets.QLineEdit(Admin_Course)
        self.new_cancelyear_input.setGeometry(QtCore.QRect(250, 420, 300, 36))
        self.new_cancelyear_input.setObjectName("new_cancelyear_input")
        self.Focus_Item = QtWidgets.QPushButton(Admin_Course)
        self.Focus_Item.setGeometry(QtCore.QRect(600, 25, 150, 70))
        self.Focus_Item.setObjectName("Focus_Item")
        self.Focus_Item.clicked.connect(self.focus_course)
        self.Delete_Button = QtWidgets.QPushButton(Admin_Course)
        self.Delete_Button.setGeometry(QtCore.QRect(600, 140, 150, 70))
        self.Delete_Button.setObjectName("Delete_Button")
        self.Delete_Button.clicked.connect(self.delete_course_info)
        self.Insert_Button = QtWidgets.QPushButton(Admin_Course)
        self.Insert_Button.setGeometry(QtCore.QRect(600, 220, 150, 70))
        self.Insert_Button.setObjectName("Insert_Button")
        self.Insert_Button.clicked.connect(self.insert_course_info)
        self.Update_Button = QtWidgets.QPushButton(Admin_Course)
        self.Update_Button.setGeometry(QtCore.QRect(600, 300, 150, 70))
        self.Update_Button.setObjectName("Update_Button")
        self.Update_Button.clicked.connect(self.update_course_info)
        self.error_display_label = QtWidgets.QLabel(Admin_Course)
        self.error_display_label.setGeometry(QtCore.QRect(50, 470, 700, 30))
        self.error_display_label.setObjectName("error_display_label")
        self.error_display_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_display_label.setVisible(False)
        self.error_display_label.setStyleSheet("color:rgb(255, 0, 0);")
        self.focusCID = ""
        self.retranslateUi(Admin_Course)
        QtCore.QMetaObject.connectSlotsByName(Admin_Course)

    def retranslateUi(self, Admin_Course):
        _translate = QtCore.QCoreApplication.translate
        Admin_Course.setWindowTitle(_translate("Admin_Course", "Administrator Modify Course Information"))
        self.Query_back.setText(_translate("Admin_Course", "Back"))
        self.cID_label.setText(_translate("Admin_Course", "Course ID:"))
        self.cName_label.setText(_translate("Admin_Course", "Course Name:"))
        self.new_CID_label.setText(_translate("Admin_Course", "*Course ID:"))
        self.new_CName_label.setText(_translate("Admin_Course", "*Course Name:"))
        self.new_tID_label.setText(_translate("Admin_Course", "*Teacher ID:"))
        self.new_credit_label.setText(_translate("Admin_Course", "*Credit:"))
        self.new_grade_label.setText(_translate("Admin_Course", "*Grade:"))
        self.new_cancelyear_label.setText(_translate("Admin_Course", "*Canceled Year:"))
        self.Focus_Item.setText(_translate("Admin_Course", "Focus"))
        self.Delete_Button.setText(_translate("Admin_Course", "Delete"))
        self.Insert_Button.setText(_translate("Admin_Course", "Insert"))
        self.Update_Button.setText(_translate("Admin_Course", "Update"))
        self.error_display_label.setText(_translate("Admin_Course", "Error Display"))
        self._translate = QtCore.QCoreApplication.translate

    def focus_course(self):
        getCID = self.cID_input.text()
        getCName = self.cName_input.text()
        self.focusCID = ""
        cursor = db.cursor()
        if getCID == "" and getCName == "":
            sql = "select * from course;"
        if getCID == "" and getCName != "":
            sql = "select * from course where cName='" + getCName + "';"
        if getCID != "" and getCName == "":
            sql = "select * from course where cID=" + getCID + ";"
        if getCID != "" and getCName != "":
            sql = "select * from course where cName='" + getCName + "' and cID=" + getCID + ";"
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            if len(results) == 1:
                self.focusCID = results[0][0]
                self.error_display_label.setVisible(True)
                self.error_display_label.setText("Successful Catch.")
                self.new_cID_input.setText(results[0][0])
                self.new_cName_input.setText(results[0][1])
                self.new_tID_input.setText(results[0][2])
                self.new_credit_input.setText(str(results[0][3]))
                self.new_grade_input.setText(str(results[0][4]))
                self.new_cancelyear_input.setText(str(results[0][5]))
            else:
                self.new_cID_input.setText("")
                self.new_cName_input.setText("")
                self.new_tID_input.setText("")
                self.new_credit_input.setText("")
                self.new_grade_input.setText("")
                self.new_cancelyear_input.setText("")
                self.error_display_label.setVisible(True)
                self.error_display_label.setText("Already Catch All. Please Focus On One Item.")
            self.Course_Modify_Info.clear()
            self.Course_Modify_Info.setColumnCount(0)
            self.Course_Modify_Info.setRowCount(0)
            col_result = cursor.description
            self.row = len(results)  # 取得记录个数，用于设置表格的行数
            self.vol = len(results[0]) - 1  # 取得字段数，用于设置表格的列数
            col_result = list(col_result)
            a = 0
            self.Course_Modify_Info.setColumnCount(self.vol)
            self.Course_Modify_Info.setRowCount(self.row)
            for i in col_result[:len(col_result) - 1]:
                item = QtWidgets.QTableWidgetItem()
                self.Course_Modify_Info.setHorizontalHeaderItem(a, item)
                item = self.Course_Modify_Info.horizontalHeaderItem(a)
                item.setText(self._translate("Course_Modify_Info", i[0]))
                a = a + 1
            results = list(results)
            for i in range(len(results)):
                results[i] = list(results[i])
            for i in range(self.row):
                for j in range(self.vol):
                    item = QtWidgets.QTableWidgetItem()
                    self.Course_Modify_Info.setItem(i, j, item)
                    item = self.Course_Modify_Info.item(i, j)
                    item.setText(self._translate("Course_Table", str(results[i][j])))
        else:
            self.new_cID_input.setText("")
            self.new_cName_input.setText("")
            self.new_tID_input.setText("")
            self.new_credit_input.setText("")
            self.new_grade_input.setText("")
            self.new_cancelyear_input.setText("")
            self.error_display_label.setText("Error: Item Not Exist. Fail to Catch.")
            self.error_display_label.setVisible(True)
            self.Course_Modify_Info.clear()
            self.Course_Modify_Info.setColumnCount(0)
            self.Course_Modify_Info.setRowCount(0)

    def update_course_info(self):
        if self.focusCID == "":
            self.error_display_label.setText("Please Focus One Item First.")
            self.error_display_label.setVisible(True)
        elif (self.new_tID_input.text()).isdigit() == False or len(self.new_tID_input.text()) != 5:
            self.error_display_label.setText("Error: Teacher ID length should be 5.")
            self.error_display_label.setVisible(True)
        elif (self.new_cID_input.text()).isdigit() == False or len(self.new_cID_input.text()) != 7:
            self.error_display_label.setText("Error: Course ID length should be 7.")
            self.error_display_label.setVisible(True)
        elif self.new_cName_input.text() == "" or self.new_credit_input.text() == "" or (
        self.new_credit_input.text()).isdigit() == False or self.new_grade_input.text() == "" or (
        self.new_grade_input.text()).isdigit() == False:
            self.error_display_label.setText("Error: Exist Empty or Illegal Information.")
            self.error_display_label.setVisible(True)
        elif self.new_cancelyear_input.text() != "" and (self.new_cancelyear_input.text()).isdigit() == True and int(
                self.new_grade_input.text()) > int(self.new_cancelyear_input.text()):
            self.error_display_label.setText("Error: Course Canceled Year Below Grade.")
            self.error_display_label.setVisible(True)
        else:
            if self.focusCID != self.new_cID_input:
                cursor = db.cursor()
                sql = "SELECT COUNT(*) FROM course WHERE cID = " + self.new_cID_input.text() + ";"
                cursor.execute(sql)
                results = cursor.fetchall()
                if results[0][0] > 1:
                    self.error_display_label.setText("Error: Course ID is already exist.")
                    self.error_display_label.setVisible(True)
                    return
            cursor = db.cursor()
            sql = "SELECT COUNT(*) FROM teacher WHERE tID = " + self.new_tID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if results[0][0] == 0:
                self.error_display_label.setText("Error: New Teacher ID Not Exist.")
                self.error_display_label.setVisible(True)
                return
            sql = "SELECT Courses FROM teacher WHERE tID = " + self.new_tID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            matchflag = -1
            for i in results:
                if i[0] == self.new_cName_input.text():
                    matchflag = 1
                    break
            if matchflag == -1:
                self.error_display_label.setText("Error: New Class Name Not Match Teacher.")
                self.error_display_label.setVisible(True)
                return
            sql = "select count(*) from course_choosing where choose_year<" + self.new_grade_input.text() + " or choose_year>" + self.new_cancelyear_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if results[0][0] > 0:
                self.error_display_label.setText("Error: Some Choosing Year Out Of Grade-Canceled Year Range.")
                self.error_display_label.setVisible(True)
                return
            sql = "update course set cName='" + self.new_cName_input.text() + "' where cID=" + self.focusCID
            cursor.execute(sql)
            sql = "update course set tID='" + self.new_tID_input.text() + "' where cID=" + self.focusCID
            cursor.execute(sql)
            sql = "update course set credit='" + self.new_credit_input.text() + "' where cID=" + self.focusCID
            cursor.execute(sql)
            sql = "update course set grade='" + self.new_grade_input.text() + "' where cID=" + self.focusCID
            cursor.execute(sql)
            sql = "update course set canceled_year='" + self.new_cancelyear_input.text() + "' where cID=" + self.focusCID
            cursor.execute(sql)
            sql = "update course set ccID='" + self.new_cID_input.text() + "' where cID=" + self.focusCID
            cursor.execute(sql)
            sql = "update course set cID='" + self.new_cID_input.text() + "' where cID=" + self.focusCID
            cursor.execute(sql)
            sql = "update course_choosing set cID='" + self.new_cID_input.text() + "' where cID=" + self.focusCID
            cursor.execute(sql)
            db.commit()
            self.error_display_label.setText("Successful Update.")
            self.error_display_label.setVisible(True)

    def insert_course_info(self):
        if self.focusCID != "":
            self.error_display_label.setText("Don't Focus For Insertion.")
            self.error_display_label.setVisible(True)
        elif (self.new_tID_input.text()).isdigit() == False or len(self.new_tID_input.text()) != 5:
            self.error_display_label.setText("Error: Teacher ID length should be 5.")
            self.error_display_label.setVisible(True)
        elif (self.new_cID_input.text()).isdigit() == False or len(self.new_cID_input.text()) != 7:
            self.error_display_label.setText("Error: Course ID length should be 7.")
            self.error_display_label.setVisible(True)
        elif self.new_cName_input.text() == "" or self.new_credit_input.text() == "" or (
        self.new_credit_input.text()).isdigit() == False or self.new_grade_input.text() == "" or (
        self.new_grade_input.text()).isdigit() == False:
            self.error_display_label.setText("Error: Exist Empty or Illegal Information.")
            self.error_display_label.setVisible(True)
        elif self.new_cancelyear_input.text() != "" and (self.new_cancelyear_input.text()).isdigit() == True and int(
                self.new_grade_input.text()) > int(self.new_cancelyear_input.text()):
            self.error_display_label.setText("Error: Course Canceled Year Below Grade.")
            self.error_display_label.setVisible(True)
        else:
            cursor = db.cursor()
            sql = "SELECT COUNT(*) FROM course WHERE cID = " + self.new_cID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if results[0][0] > 0:
                self.error_display_label.setText("Error: Course ID is already exist.")
                self.error_display_label.setVisible(True)
            else:
                cursor = db.cursor()
                sql = "SELECT COUNT(*) FROM teacher WHERE tID = " + self.new_tID_input.text() + ";"
                cursor.execute(sql)
                results = cursor.fetchall()
                if results[0][0] == 0:
                    self.error_display_label.setText("Error: New Teacher ID Not Exist.")
                    self.error_display_label.setVisible(True)
                    return
                sql = "SELECT Courses FROM teacher WHERE tID = " + self.new_tID_input.text() + ";"
                cursor.execute(sql)
                results = cursor.fetchall()
                matchflag = -1
                for i in results:
                    if i[0] == self.new_cName_input.text():
                        matchflag = 1
                        break
                if matchflag == -1:
                    self.error_display_label.setText("Error: New Class Name Not Match Teacher.")
                    self.error_display_label.setVisible(True)
                    return
                sql = "insert into course values(" + self.new_cID_input.text() + ",'" + self.new_cName_input.text() + "','" + self.new_tID_input.text() + "'," + self.new_credit_input.text() + "," + self.new_grade_input.text() + ",'" + self.new_cancelyear_input.text() + "'," + self.new_cID_input.text() + ");"
                cursor.execute(sql)
                db.commit()
                self.error_display_label.setText("Successful Insertion.")
                self.error_display_label.setVisible(True)

    def delete_course_info(self):
        if self.focusCID == "":
            self.error_display_label.setText("Please Focus One Item First.")
            self.error_display_label.setVisible(True)
        else:
            cursor = db.cursor()
            sql = "SELECT COUNT(*) FROM course WHERE cID = " + self.focusCID + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if results[0][0] == 0:
                self.error_display_label.setText("Error: Course ID don't exist.")
                self.error_display_label.setVisible(True)
            else:
                cursor = db.cursor()
                sql = "delete from course where cID=" + self.focusCID + ";"
                cursor.execute(sql)
                sql = "delete from course_choosing where cID=" + self.focusCID + ";"
                cursor.execute(sql)
                db.commit()
                self.error_display_label.setText("Successful Deletion")
                self.error_display_label.setVisible(True)


class Ui_Admin_Choose(QtWidgets.QWidget):
    Choose_Goback_Admin = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Admin_Choose = self
        Admin_Choose.setObjectName("Admin_Choose")
        Admin_Choose.resize(800, 700)
        Admin_Choose.setMinimumSize(QtCore.QSize(800, 700))
        Admin_Choose.setMaximumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        Admin_Choose.setFont(font)
        self.Choose_Modify_Info = QtWidgets.QTableWidget(Admin_Choose)
        self.Choose_Modify_Info.setGeometry(QtCore.QRect(50, 510, 700, 100))
        self.Choose_Modify_Info.setMinimumSize(QtCore.QSize(700, 100))
        self.Choose_Modify_Info.setMaximumSize(QtCore.QSize(700, 100))
        self.Choose_Modify_Info.setObjectName("Choose_Modify_Info")
        self.Choose_Modify_Info.setColumnCount(0)
        self.Choose_Modify_Info.setRowCount(0)
        self.Choose_Modify_Info.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Query_back = QtWidgets.QPushButton(Admin_Choose)
        self.Query_back.setGeometry(QtCore.QRect(320, 620, 150, 70))
        self.Query_back.setMinimumSize(QtCore.QSize(160, 70))
        self.Query_back.setMaximumSize(QtCore.QSize(160, 70))
        self.Query_back.setObjectName("Query_back")
        self.Query_back.clicked.connect(self.Choose_Goback_Admin.emit)
        self.sID_label = QtWidgets.QLabel(Admin_Choose)
        self.sID_label.setGeometry(QtCore.QRect(50, 20, 160, 30))
        self.sID_label.setObjectName("sID_label")
        self.sName_label = QtWidgets.QLabel(Admin_Choose)
        self.sName_label.setGeometry(QtCore.QRect(50, 70, 160, 30))
        self.sName_label.setObjectName("sName_label")
        self.Seperator = QtWidgets.QFrame(Admin_Choose)
        self.Seperator.setGeometry(QtCore.QRect(50, 225, 700, 20))
        self.Seperator.setFrameShape(QtWidgets.QFrame.HLine)
        self.Seperator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Seperator.setObjectName("Seperator")
        self.cID_label = QtWidgets.QLabel(Admin_Choose)
        self.cID_label.setGeometry(QtCore.QRect(50, 130, 160, 30))
        self.cID_label.setObjectName("cID_label")
        self.cName_label = QtWidgets.QLabel(Admin_Choose)
        self.cName_label.setGeometry(QtCore.QRect(50, 180, 160, 30))
        self.cName_label.setObjectName("cName_label")
        self.new_sID_label = QtWidgets.QLabel(Admin_Choose)
        self.new_sID_label.setGeometry(QtCore.QRect(50, 260, 160, 30))
        self.new_sID_label.setObjectName("new_sID_label")
        self.new_cID_label = QtWidgets.QLabel(Admin_Choose)
        self.new_cID_label.setGeometry(QtCore.QRect(50, 310, 160, 30))
        self.new_cID_label.setObjectName("new_cID_label")
        self.new_tID_label = QtWidgets.QLabel(Admin_Choose)
        self.new_tID_label.setGeometry(QtCore.QRect(50, 370, 160, 30))
        self.new_tID_label.setObjectName("new_tID_label")
        self.new_chosenyear_label = QtWidgets.QLabel(Admin_Choose)
        self.new_chosenyear_label.setGeometry(QtCore.QRect(50, 420, 170, 30))
        self.new_chosenyear_label.setObjectName("new_chosenyear_label")
        self.sID_input = QtWidgets.QLineEdit(Admin_Choose)
        self.sID_input.setGeometry(QtCore.QRect(250, 15, 300, 36))
        self.sID_input.setObjectName("sID_input")
        self.sName_input = QtWidgets.QLineEdit(Admin_Choose)
        self.sName_input.setGeometry(QtCore.QRect(250, 70, 300, 36))
        self.sName_input.setObjectName("sName_input")
        self.cID_input = QtWidgets.QLineEdit(Admin_Choose)
        self.cID_input.setGeometry(QtCore.QRect(250, 125, 300, 36))
        self.cID_input.setObjectName("cID_input")
        self.cName_input = QtWidgets.QLineEdit(Admin_Choose)
        self.cName_input.setGeometry(QtCore.QRect(250, 180, 300, 36))
        self.cName_input.setObjectName("cName_input")
        self.new_sID_input = QtWidgets.QLineEdit(Admin_Choose)
        self.new_sID_input.setGeometry(QtCore.QRect(250, 255, 300, 36))
        self.new_sID_input.setObjectName("new_sID_input")
        self.new_cID_input = QtWidgets.QLineEdit(Admin_Choose)
        self.new_cID_input.setGeometry(QtCore.QRect(250, 310, 300, 36))
        self.new_cID_input.setObjectName("new_cID_input")
        self.new_tID_input = QtWidgets.QLineEdit(Admin_Choose)
        self.new_tID_input.setGeometry(QtCore.QRect(250, 365, 300, 36))
        self.new_tID_input.setObjectName("new_tID_input")
        self.new_chosenyear_input = QtWidgets.QLineEdit(Admin_Choose)
        self.new_chosenyear_input.setGeometry(QtCore.QRect(250, 420, 300, 36))
        self.new_chosenyear_input.setObjectName("new_chosenyear_input")
        self.Focus_Item = QtWidgets.QPushButton(Admin_Choose)
        self.Focus_Item.setGeometry(QtCore.QRect(600, 80, 150, 70))
        self.Focus_Item.setObjectName("Focus_Item")
        self.Focus_Item.clicked.connect(self.focus_choose)
        self.Delete_Button = QtWidgets.QPushButton(Admin_Choose)
        self.Delete_Button.setGeometry(QtCore.QRect(600, 240, 150, 70))
        self.Delete_Button.setObjectName("Delete_Button")
        self.Delete_Button.clicked.connect(self.delete_choose_info)
        self.Insert_Button = QtWidgets.QPushButton(Admin_Choose)
        self.Insert_Button.setGeometry(QtCore.QRect(600, 320, 150, 70))
        self.Insert_Button.setObjectName("Insert_Button")
        self.Insert_Button.clicked.connect(self.insert_choose_info)
        self.Update_Button = QtWidgets.QPushButton(Admin_Choose)
        self.Update_Button.setGeometry(QtCore.QRect(600, 400, 150, 70))
        self.Update_Button.setObjectName("Update_Button")
        self.Update_Button.clicked.connect(self.update_choose_info)
        self.error_display_label = QtWidgets.QLabel(Admin_Choose)
        self.error_display_label.setGeometry(QtCore.QRect(50, 470, 700, 30))
        self.error_display_label.setObjectName("error_display_label")
        self.error_display_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_display_label.setVisible(False)
        self.error_display_label.setStyleSheet("color:rgb(255, 0, 0);")
        self.focusChoose = ["", ""]
        self.retranslateUi(Admin_Choose)
        QtCore.QMetaObject.connectSlotsByName(Admin_Choose)

    def retranslateUi(self, Admin_Choose):
        _translate = QtCore.QCoreApplication.translate
        Admin_Choose.setWindowTitle(_translate("Admin_Choose", "Administrator Modify Course Choosing Information"))
        self.Query_back.setText(_translate("Admin_Choose", "Back"))
        self.sID_label.setText(_translate("Admin_Choose", "Student ID:"))
        self.sName_label.setText(_translate("Admin_Choose", "Student Name:"))
        self.cID_label.setText(_translate("Admin_Choose", "Course ID:"))
        self.cName_label.setText(_translate("Admin_Choose", "Course Name:"))
        self.new_sID_label.setText(_translate("Admin_Choose", "*Student ID:"))
        self.new_cID_label.setText(_translate("Admin_Choose", "*Course ID:"))
        self.new_tID_label.setText(_translate("Admin_Choose", "*Teacher ID:"))
        self.new_chosenyear_label.setText(_translate("Admin_Choose", "*Chosen Year:"))
        self.Focus_Item.setText(_translate("Admin_Choose", "Focus"))
        self.Delete_Button.setText(_translate("Admin_Choose", "Delete"))
        self.Insert_Button.setText(_translate("Admin_Choose", "Insert"))
        self.Update_Button.setText(_translate("Admin_Choose", "Update"))
        self.error_display_label.setText(_translate("Admin_Choose", "Error Display"))
        self._translate = QtCore.QCoreApplication.translate

    def focus_choose(self):
        self.focusChoose = ["", ""]
        cursor = db.cursor()
        getSID = ""
        getCID = ""
        if self.sName_input.text() != "":
            sql = "select sID from student where sName='" + self.sName_input.text() + "';"
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 1: getSID = results[0][0]
        if self.cName_input.text() != "":
            sql = "select cID from course where cName='" + self.cName_input.text() + "';"
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 1: getCID = results[0][0]
        sql1 = "select * from course_choosing"
        if self.sName_input.text() == "" and self.sID_input.text() == "" and self.cName_input.text() == "" and self.cID_input.text() == "":
            sql = sql1 + ";"
        elif self.sName_input.text() == "" and self.sID_input.text() == "" and self.cName_input.text() == "" and self.cID_input.text() != "":
            sql = sql1 + " where cID=" + self.cID_input.text() + ";"
        elif self.sName_input.text() == "" and self.sID_input.text() == "" and self.cName_input.text() != "" and self.cID_input.text() == "":
            sql = sql1 + " where cID='" + getCID + "';"
        elif self.sName_input.text() == "" and self.sID_input.text() == "" and self.cName_input.text() != "" and self.cID_input.text() != "":
            sql = sql1 + " where cID='" + getCID + "' and cID=" + self.cID_input.text() + ";"
        elif self.sName_input.text() == "" and self.sID_input.text() != "" and self.cName_input.text() == "" and self.cID_input.text() == "":
            sql = sql1 + " where sID=" + self.sID_input.text() + ";"
        elif self.sName_input.text() == "" and self.sID_input.text() != "" and self.cName_input.text() == "" and self.cID_input.text() != "":
            sql = sql1 + " where sID=" + self.sID_input.text() + " and cID=" + self.cID_input.text() + ";"
        elif self.sName_input.text() == "" and self.sID_input.text() != "" and self.cName_input.text() != "" and self.cID_input.text() == "":
            sql = sql1 + " where sID=" + self.sID_input.text() + " and cID='" + getCID + "';"
        elif self.sName_input.text() == "" and self.sID_input.text() != "" and self.cName_input.text() != "" and self.cID_input.text() != "":
            sql = sql1 + " where sID=" + self.sID_input.text() + " and cID=" + self.cID_input.text() + "and cID='" + getCID + "';"
        elif self.sName_input.text() != "" and self.sID_input.text() == "" and self.cName_input.text() == "" and self.cID_input.text() == "":
            sql = sql1 + " where sID='" + getSID + "';"
        elif self.sName_input.text() != "" and self.sID_input.text() == "" and self.cName_input.text() == "" and self.cID_input.text() != "":
            sql = sql1 + " where sID='" + getSID + "' and cID=" + self.cID_input.text() + ";"
        elif self.sName_input.text() != "" and self.sID_input.text() == "" and self.cName_input.text() != "" and self.cID_input.text() == "":
            sql = sql1 + " where sID='" + getSID + "' and cID='" + getCID + "';"
        elif self.sName_input.text() != "" and self.sID_input.text() == "" and self.cName_input.text() != "" and self.cID_input.text() != "":
            sql = sql1 + " where sID='" + getSID + "' and cID='" + getCID + "' and cID=" + self.cID_input.text() + ";"
        elif self.sName_input.text() != "" and self.sID_input.text() != "" and self.cName_input.text() == "" and self.cID_input.text() == "":
            sql = sql1 + " where sID='" + getSID + "' and sID=" + self.sID_input.text() + ";"
        elif self.sName_input.text() != "" and self.sID_input.text() != "" and self.cName_input.text() == "" and self.cID_input.text() != "":
            sql = sql1 + " where sID='" + getSID + "' and sID='" + self.sID_input.text() + "' and cID=" + self.cID_input.text() + ";"
        elif self.sName_input.text() != "" and self.sID_input.text() != "" and self.cName_input.text() != "" and self.cID_input.text() == "":
            sql = sql1 + " where sID='" + getSID + "' and sID='" + self.sID_input.text() + "' and cID='" + getCID + "';"
        elif self.sName_input.text() != "" and self.sID_input.text() != "" and self.cName_input.text() != "" and self.cID_input.text() != "":
            sql = sql1 + " where sID='" + getSID + "' and sID='" + self.sID_input.text() + "' and cID='" + getCID + "' and cID=" + self.cID_input.text() + ";"
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            if len(results) == 1:
                self.focusChoose = [results[0][0], results[0][1]]
                self.error_display_label.setVisible(True)
                self.error_display_label.setText("Successful Catch.")
                self.new_sID_input.setText(results[0][0])
                self.new_cID_input.setText(results[0][1])
                self.new_tID_input.setText(str(results[0][2]))
                self.new_chosenyear_input.setText(str(results[0][3]))
            else:
                self.new_sID_input.setText("")
                self.new_cID_input.setText("")
                self.new_tID_input.setText("")
                self.new_chosenyear_input.setText("")
                self.error_display_label.setVisible(True)
                self.error_display_label.setText("Already Catch All. Please Focus On One Item.")
            self.Choose_Modify_Info.clear()
            self.Choose_Modify_Info.setColumnCount(0)
            self.Choose_Modify_Info.setRowCount(0)
            col_result = cursor.description
            self.row = len(results)  # 取得记录个数，用于设置表格的行数
            self.vol = len(results[0]) - 1  # 取得字段数，用于设置表格的列数
            col_result = list(col_result)
            a = 0
            self.Choose_Modify_Info.setColumnCount(self.vol)
            self.Choose_Modify_Info.setRowCount(self.row)
            for i in col_result[:len(col_result) - 1]:
                item = QtWidgets.QTableWidgetItem()
                self.Choose_Modify_Info.setHorizontalHeaderItem(a, item)
                item = self.Choose_Modify_Info.horizontalHeaderItem(a)
                item.setText(self._translate("Choose_Modify_Info", i[0]))
                a = a + 1
            results = list(results)
            for i in range(len(results)):
                results[i] = list(results[i])
            for i in range(self.row):
                for j in range(self.vol):
                    item = QtWidgets.QTableWidgetItem()
                    self.Choose_Modify_Info.setItem(i, j, item)
                    item = self.Choose_Modify_Info.item(i, j)
                    item.setText(self._translate("Choose_Table", str(results[i][j])))
        else:
            self.new_sID_input.setText("")
            self.new_cID_input.setText("")
            self.new_tID_input.setText("")
            self.new_chosenyear_input.setText("")
            self.error_display_label.setText("Error: Item Not Exist. Fail to Catch.")
            self.error_display_label.setVisible(True)
            self.Choose_Modify_Info.clear()
            self.Choose_Modify_Info.setColumnCount(0)
            self.Choose_Modify_Info.setRowCount(0)

    def update_choose_info(self):
        cursor = db.cursor()
        if self.focusChoose == ["", ""]:
            self.error_display_label.setText("Please Focus One Item First.")
            self.error_display_label.setVisible(True)
            return
        elif self.new_sID_input.text() == "" or self.new_cID_input.text() == "" or self.new_tID_input.text() == "" or self.new_chosenyear_input.text() == "":
            self.error_display_label.setText("Exist Empty Information.")
            self.error_display_label.setVisible(True)
            return
        else:
            sql = "select * from student where sID=" + self.new_sID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 0:
                self.error_display_label.setText("Student ID Not Exist.")
                self.error_display_label.setVisible(True)
                return
            sql = "select * from course where cID=" + self.new_cID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 0:
                self.error_display_label.setText("Course ID Not Exist.")
                self.error_display_label.setVisible(True)
                return
            sql = "select * from teacher where cID=" + self.new_cID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            matchflag = -1
            for i in results:
                if i[0] == self.new_tID_input.text():
                    matchflag = 1
                    break
            if matchflag == -1:
                self.error_display_label.setText("No Matching Teacher For Course.")
                self.error_display_label.setVisible(True)
                return
            sql = "select * from course where cID=" + self.new_cID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if int(self.new_chosenyear_input.text()) < int(results[0][4]):
                self.error_display_label.setText("Illegal Chosen Year.")
                self.error_display_label.setVisible(True)
                return
            if results[0][5] != '':
                if int(results[0][5]) < int(self.new_chosenyear_input.text()):
                    self.error_display_label.setText("Illegal Chosen Year.")
                    self.error_display_label.setVisible(True)
                    return
            sql = "select count(*) from course_choosing where sID=" + self.new_sID_input.text() + " and cID=" + self.new_cID_input.text() + " and tID=" + self.new_tID_input.text() + " and choose_year=" + self.new_chosenyear_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if results[0][0] > 0:
                self.error_display_label.setText("Exist Same Item.")
                self.error_display_label.setVisible(True)
                return
            sql = "update course_choosing set sID=" + self.new_sID_input.text() + " where sID=" + self.focusChoose[
                0] + " and cID=" + self.focusChoose[1] + ";"
            cursor.execute(sql)
            sql = "update course_choosing set cID=" + self.new_cID_input.text() + " where sID=" + self.new_sID_input.text() + " and cID=" + \
                  self.focusChoose[1] + ";"
            cursor.execute(sql)
            sql = "update course_choosing set tID=" + self.new_tID_input.text() + " where sID=" + self.new_sID_input.text() + " and cID=" + self.new_cID_input.text() + ";"
            cursor.execute(sql)
            sql = "update course_choosing set choose_year=" + self.new_chosenyear_input.text() + " where sID=" + self.new_sID_input.text() + " and cID=" + self.new_cID_input.text() + ";"
            cursor.execute(sql)
            db.commit()
            self.error_display_label.setText("Successful Update.")
            self.error_display_label.setVisible(True)
        self.focusChoose = ["", ""]

    def insert_choose_info(self):
        cursor = db.cursor()
        if self.focusChoose != ["", ""]:
            self.error_display_label.setText("Don't Focus For Insertion.")
            self.error_display_label.setVisible(True)
            return
        elif self.new_sID_input.text() == "" or self.new_cID_input.text() == "" or self.new_tID_input.text() == "" or self.new_chosenyear_input.text() == "":
            self.error_display_label.setText("Exist Empty Information.")
            self.error_display_label.setVisible(True)
            return
        else:
            sql = "select * from student where sID=" + self.new_sID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 0:
                self.error_display_label.setText("Student ID Not Exist.")
                self.error_display_label.setVisible(True)
                return
            sql = "select * from course where cID=" + self.new_cID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 0:
                self.error_display_label.setText("Course ID Not Exist.")
                self.error_display_label.setVisible(True)
                return
            sql = "select * from teacher where cID=" + self.new_cID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            matchflag = -1
            for i in results:
                if i[0] == self.new_tID_input.text():
                    matchflag = 1
                    break
            if matchflag == -1:
                self.error_display_label.setText("No Matching Teacher For Course.")
                self.error_display_label.setVisible(True)
                return
            sql = "select * from course where cID=" + self.new_cID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if int(self.new_chosenyear_input.text()) < int(results[0][4]):
                self.error_display_label.setText("Illegal Chosen Year.")
                self.error_display_label.setVisible(True)
                return
            if results[0][5] != '':
                if int(results[0][5]) < int(self.new_chosenyear_input.text()):
                    self.error_display_label.setText("Illegal Chosen Year.")
                    self.error_display_label.setVisible(True)
                    return
            sql = "select count(*) from course_choosing where sID=" + self.new_sID_input.text() + " and cID=" + self.new_cID_input.text() + " and tID=" + self.new_tID_input.text() + ";"
            cursor.execute(sql)
            results = cursor.fetchall()
            if results[0][0] > 0:
                self.error_display_label.setText("Exist Same Item.")
                self.error_display_label.setVisible(True)
                return
            sql = "insert into course_choosing values (" + self.new_sID_input.text() + "," + self.new_cID_input.text() + "," + self.new_tID_input.text() + "," + self.new_chosenyear_input.text() + ",-1)"
            cursor.execute(sql)
            db.commit()
            self.error_display_label.setText("Successful Insert.")
            self.error_display_label.setVisible(True)

    def delete_choose_info(self):
        cursor = db.cursor()
        if self.focusChoose == ["", ""]:
            self.error_display_label.setText("Please Focus One Item First.")
            self.error_display_label.setVisible(True)
            return
        else:
            sql = "delete from course_choosing where sID=" + self.focusChoose[0] + " and cID=" + self.focusChoose[
                1] + ";"
            cursor.execute(sql)
            db.commit()
            self.error_display_label.setText("Successful Deletetion.")
            self.error_display_label.setVisible(True)


class Ui_Teacher_Score(QtWidgets.QWidget):
    Score_Goback_Teacher = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Teacher_Score = self
        Teacher_Score.setObjectName("Teacher_Score")
        Teacher_Score.resize(800, 700)
        Teacher_Score.setMinimumSize(QtCore.QSize(800, 700))
        Teacher_Score.setMaximumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        Teacher_Score.setFont(font)
        self.Score_Modify_Info = QtWidgets.QTableWidget(Teacher_Score)
        self.Score_Modify_Info.setGeometry(QtCore.QRect(50, 320, 700, 270))
        self.Score_Modify_Info.setMinimumSize(QtCore.QSize(700, 270))
        self.Score_Modify_Info.setMaximumSize(QtCore.QSize(700, 270))
        self.Score_Modify_Info.setObjectName("Score_Modify_Info")
        self.Score_Modify_Info.setColumnCount(0)
        self.Score_Modify_Info.setRowCount(0)
        self.Score_Modify_Info.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Query_back = QtWidgets.QPushButton(Teacher_Score)
        self.Query_back.setGeometry(QtCore.QRect(320, 610, 150, 70))
        self.Query_back.setMinimumSize(QtCore.QSize(160, 70))
        self.Query_back.setMaximumSize(QtCore.QSize(160, 70))
        self.Query_back.setObjectName("Query_back")
        self.Query_back.clicked.connect(self.Score_Goback_Teacher.emit)
        self.sID_label = QtWidgets.QLabel(Teacher_Score)
        self.sID_label.setGeometry(QtCore.QRect(50, 20, 160, 30))
        self.sID_label.setObjectName("sID_label")
        self.Seperator = QtWidgets.QFrame(Teacher_Score)
        self.Seperator.setGeometry(QtCore.QRect(50, 175, 700, 20))
        self.Seperator.setFrameShape(QtWidgets.QFrame.HLine)
        self.Seperator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Seperator.setObjectName("Seperator")
        self.cID_label = QtWidgets.QLabel(Teacher_Score)
        self.cID_label.setGeometry(QtCore.QRect(50, 70, 160, 30))
        self.cID_label.setObjectName("cID_label")
        self.chosenyear_label = QtWidgets.QLabel(Teacher_Score)
        self.chosenyear_label.setGeometry(QtCore.QRect(50, 120, 160, 30))
        self.chosenyear_label.setObjectName("chosenyear_label")
        self.new_score_label = QtWidgets.QLabel(Teacher_Score)
        self.new_score_label.setGeometry(QtCore.QRect(50, 217, 160, 30))
        self.new_score_label.setObjectName("new_score_label")
        self.sID_input = QtWidgets.QLineEdit(Teacher_Score)
        self.sID_input.setGeometry(QtCore.QRect(250, 15, 300, 36))
        self.sID_input.setObjectName("sID_input")
        self.cID_input = QtWidgets.QLineEdit(Teacher_Score)
        self.cID_input.setGeometry(QtCore.QRect(250, 70, 300, 36))
        self.cID_input.setObjectName("cID_input")
        self.chosenyear_input = QtWidgets.QLineEdit(Teacher_Score)
        self.chosenyear_input.setGeometry(QtCore.QRect(250, 125, 300, 36))
        self.chosenyear_input.setObjectName("chosenyear_input")
        self.new_score_input = QtWidgets.QLineEdit(Teacher_Score)
        self.new_score_input.setGeometry(QtCore.QRect(250, 217, 300, 36))
        self.new_score_input.setObjectName("new_score_input")
        self.Focus_Item = QtWidgets.QPushButton(Teacher_Score)
        self.Focus_Item.setGeometry(QtCore.QRect(600, 50, 150, 70))
        self.Focus_Item.setObjectName("Focus_Item")
        self.Focus_Item.clicked.connect(self.focus_score)
        self.Update_Button = QtWidgets.QPushButton(Teacher_Score)
        self.Update_Button.setGeometry(QtCore.QRect(600, 200, 150, 70))
        self.Update_Button.setObjectName("Update_Button")
        self.Update_Button.clicked.connect(self.update_score_info)
        self.error_display_label = QtWidgets.QLabel(Teacher_Score)
        self.error_display_label.setGeometry(QtCore.QRect(50, 275, 700, 30))
        self.error_display_label.setObjectName("error_display_label")
        self.error_display_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_display_label.setVisible(False)
        self.error_display_label.setStyleSheet("color:rgb(255, 0, 0);")
        self.focusChoose = ["", ""]
        self.retranslateUi(Teacher_Score)
        self.focusScore = ["", "", ""]
        QtCore.QMetaObject.connectSlotsByName(Teacher_Score)

    def retranslateUi(self, Teacher_Score):
        _translate = QtCore.QCoreApplication.translate
        Teacher_Score.setWindowTitle(_translate("Teacher_Score", "Teacher Modify Score"))
        self.Query_back.setText(_translate("Teacher_Score", "Back"))
        self.sID_label.setText(_translate("Teacher_Score", "Student ID:"))
        self.cID_label.setText(_translate("Teacher_Score", "Course ID:"))
        self.chosenyear_label.setText(_translate("Teacher_Score", "Chosen Year:"))
        self.new_score_label.setText(_translate("Teacher_Score", "*Score:"))
        self.Focus_Item.setText(_translate("Teacher_Score", "Focus"))
        self.Update_Button.setText(_translate("Teacher_Score", "Update"))
        self.error_display_label.setText(_translate("Teacher_Score", "Error Display"))
        self._translate = QtCore.QCoreApplication.translate

    def focus_score(self):
        self.focusScore = ["", "", ""]
        cursor = db.cursor()
        sql1 = "select * from course_choosing"
        if self.sID_input.text() == "" and self.cID_input.text() == "" and self.chosenyear_input.text() == "":
            sql = sql1 + ";"
        elif self.sID_input.text() == "" and self.cID_input.text() == "" and self.chosenyear_input.text() != "":
            sql = sql1 + " where choose_year=" + self.chosenyear_input.text() + ";"
        elif self.sID_input.text() == "" and self.cID_input.text() != "" and self.chosenyear_input.text() == "":
            sql = sql1 + " where cID=" + self.cID_input.text() + ";"
        elif self.sID_input.text() == "" and self.cID_input.text() != "" and self.chosenyear_input.text() != "":
            sql = sql1 + " where cID=" + self.cID_input.text() + " and choose_year=" + self.chosenyear_input.text() + ";"
        elif self.sID_input.text() != "" and self.cID_input.text() == "" and self.chosenyear_input.text() == "":
            sql = sql1 + " where sID=" + self.sID_input.text() + ";"
        elif self.sID_input.text() != "" and self.cID_input.text() == "" and self.chosenyear_input.text() != "":
            sql = sql1 + " where sID=" + self.sID_input.text() + " and choose_year=" + self.chosenyear_input.text() + ";"
        elif self.sID_input.text() != "" and self.cID_input.text() != "" and self.chosenyear_input.text() == "":
            sql = sql1 + " where sID=" + self.sID_input.text() + " and cID=" + self.cID_input.text() + ";"
        elif self.sID_input.text() != "" and self.cID_input.text() != "" and self.chosenyear_input.text() != "":
            sql = sql1 + " where sID=" + self.sID_input.text() + " and cID=" + self.cID_input.text() + " and choose_year=" + self.chosenyear_input.text() + ";"
        cursor.execute(sql)
        results = cursor.fetchall()
        if len(results) > 0:
            if len(results) == 1:
                self.focusScore = [results[0][0], results[0][1], results[0][3]]
                self.error_display_label.setVisible(True)
                self.error_display_label.setText("Successful Catch.")
                self.new_score_input.setText(str(results[0][4]))
            else:
                self.new_score_input.setText("")
                self.error_display_label.setVisible(True)
                self.error_display_label.setText("Already Catch All. Please Focus On One Item.")
            self.Score_Modify_Info.clear()
            self.Score_Modify_Info.setColumnCount(0)
            self.Score_Modify_Info.setRowCount(0)
            col_result = cursor.description
            self.row = len(results)  # 取得记录个数，用于设置表格的行数
            self.vol = len(results[0])  # 取得字段数，用于设置表格的列数
            col_result = list(col_result)
            a = 0
            self.Score_Modify_Info.setColumnCount(self.vol)
            self.Score_Modify_Info.setRowCount(self.row)
            for i in col_result[:len(col_result)]:
                item = QtWidgets.QTableWidgetItem()
                self.Score_Modify_Info.setHorizontalHeaderItem(a, item)
                item = self.Score_Modify_Info.horizontalHeaderItem(a)
                item.setText(self._translate("Score_Modify_Info", i[0]))
                a = a + 1
            results = list(results)
            for i in range(len(results)):
                results[i] = list(results[i])
            for i in range(self.row):
                for j in range(self.vol):
                    item = QtWidgets.QTableWidgetItem()
                    self.Score_Modify_Info.setItem(i, j, item)
                    item = self.Score_Modify_Info.item(i, j)
                    item.setText(self._translate("Score_Table", str(results[i][j])))
        else:
            self.new_score_input.setText("")
            self.error_display_label.setText("Error: Item Not Exist. Fail to Catch.")
            self.error_display_label.setVisible(True)
            self.Score_Modify_Info.clear()
            self.Score_Modify_Info.setColumnCount(0)
            self.Score_Modify_Info.setRowCount(0)

    def update_score_info(self):
        if self.focusScore == ["", "", ""]:
            self.error_display_label.setVisible(True)
            self.error_display_label.setText("Please Focus One Item First.")
            return
        elif self.new_score_input.text() == "" or self.new_score_input.text().isdigit() == False:
            self.error_display_label.setVisible(True)
            self.error_display_label.setText("Error: Empty or Illegal New Score.")
            return
        elif int(self.new_score_input.text()) > 100 or int(self.new_score_input.text()) < 0:
            self.error_display_label.setVisible(True)
            self.error_display_label.setText("Error: New Score Out of Range 0 to 100.")
            return
        else:
            print(self.focusScore)
            sql = "update course_choosing set score=" + self.new_score_input.text() + " where sID=" + self.focusScore[
                0] + " and cID=" + self.focusScore[1] + " and choose_year=" + str(self.focusScore[2]) + ";"
            print(sql)
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
            self.error_display_label.setVisible(True)
            self.error_display_label.setText("Successful Update.")


class Controller:

    def show_login(self):
        self.login = Ui_Login()
        self.login.switch_window.connect(self.show_admin)
        self.login.teacher_window.connect(self.show_teacher)
        self.login.student_window.connect(self.show_student)
        self.login.show()

    def show_admin(self):
        self.admin_window = Ui_Admin_Win()
        self.admin_window.logout_window.connect(self.back_login)
        self.admin_window.PW_Modify_Button.connect(self.show_PW_Modify)
        self.admin_window.Goto_Query_Button.connect(self.show_Query_Win)
        self.admin_window.Student_Modify_Button.connect(self.show_Student_Modify)
        self.admin_window.Course_Modify_Button.connect(self.show_Course_Modify)
        self.admin_window.Choose_Modify_Button.connect(self.show_Choose_Modify)
        self.admin_window.show()
        self.login.close()

    def show_teacher(self):
        self.teacher_window = Ui_Teacher_Win()
        self.teacher_window.logout_window.connect(self.back_login)
        self.teacher_window.PW_Modify_Button.connect(self.show_PW_Modify)
        self.teacher_window.Goto_Query_Button.connect(self.show_Query_Win)
        self.teacher_window.Score_Modify_Button.connect(self.show_Score_Modify)
        self.teacher_window.show()
        self.login.close()

    def show_student(self):
        self.student_window = Ui_Student_Win()
        self.student_window.logout_window.connect(self.back_login)
        self.student_window.PW_Modify_Button.connect(self.show_PW_Modify)
        self.student_window.Goto_Query_Button.connect(self.show_Query_Win)
        self.student_window.show()
        self.login.close()

    def show_PW_Modify(self):
        self.PW_Modify_Win = Ui_PW_Modify()
        self.PW_Modify_Win.cancel_back.connect(self.Modify_PW_Back)
        if userChar == "Admin":
            self.admin_window.close()
        elif userChar == "Teacher":
            self.teacher_window.close()
        elif userChar == "Student":
            self.student_window.close()
        self.PW_Modify_Win.show()

    def Modify_PW_Back(self):
        self.PW_Modify_Win.close()
        if userChar == "Admin":
            self.show_admin()
        elif userChar == "Teacher":
            self.show_teacher()
        elif userChar == "Student":
            self.show_student()

    def back_login(self):
        if userChar == "Admin":
            self.admin_window.close()
        elif userChar == "Teacher":
            self.teacher_window.close()
        elif userChar == "Student":
            self.student_window.close()
        self.show_login()

    def PW_Modify_Cancel(self):
        self.PW_Modify_Win.close()
        if userChar == "Admin":
            self.show_admin()
        elif userChar == "Teacher":
            self.show_teacher()
        elif userChar == "Student":
            self.show_student()

    def show_Query_Win(self):
        self.Specific_Query_Win = Ui_Query()
        self.Specific_Query_Win.Query_back.connect(self.Query_Back_Menu)
        self.Specific_Query_Win.Query_to_Student.connect(self.show_query_student)
        self.Specific_Query_Win.Query_to_Score.connect(self.show_query_score)
        self.Specific_Query_Win.Query_to_Course.connect(self.show_query_course)
        self.Specific_Query_Win.Query_to_teaching.connect(self.show_query_teach)
        self.Specific_Query_Win.Query_to_Average.connect(self.show_query_average)
        if userChar == "Admin":
            self.admin_window.close()
        elif userChar == "Teacher":
            self.teacher_window.close()
        elif userChar == "Student":
            self.student_window.close()
        self.Specific_Query_Win.show()

    def Query_Back_Menu(self):
        self.Specific_Query_Win.close()
        if userChar == "Admin":
            self.show_admin()
        elif userChar == "Teacher":
            self.show_teacher()
        elif userChar == "Student":
            self.show_student()

    def show_query_teach(self):
        self.Query_teach_win = Ui_Query_Teaching()
        self.Query_teach_win.Goback_Query.connect(self.teach_back_query)
        self.Specific_Query_Win.close()
        self.Query_teach_win.show()

    def teach_back_query(self):
        self.Query_teach_win.close()
        self.show_Query_Win()

    def show_query_average(self):
        self.Query_average_win = Ui_Query_Average()
        self.Query_average_win.Goback_Query.connect(self.average_back_query)
        self.Specific_Query_Win.close()
        self.Query_average_win.show()

    def average_back_query(self):
        self.Query_average_win.close()
        self.show_Query_Win()

    def show_query_course(self):
        self.Query_course_win = Ui_Query_Course()
        self.Query_course_win.Goback_Query.connect(self.course_back_query)
        self.Specific_Query_Win.close()
        self.Query_course_win.show()

    def course_back_query(self):
        self.Query_course_win.close()
        self.show_Query_Win()

    def show_query_student(self):
        self.Query_student_win = Ui_Query_Student()
        self.Query_student_win.Goback_Query.connect(self.student_back_query)
        self.Specific_Query_Win.close()
        self.Query_student_win.show()

    def student_back_query(self):
        self.Query_student_win.close()
        self.show_Query_Win()

    def show_query_score(self):
        self.Query_score_win = Ui_Query_Score()
        self.Query_score_win.Goback_Query.connect(self.score_back_query)
        self.Specific_Query_Win.close()
        self.Query_score_win.show()

    def score_back_query(self):
        self.Query_score_win.close()
        self.show_Query_Win()

    def show_Student_Modify(self):
        self.student_modify_win = Ui_Admin_Student()
        self.student_modify_win.Student_Goback_Admin.connect(self.student_back_admin)
        self.admin_window.close()
        self.student_modify_win.show()

    def student_back_admin(self):
        self.student_modify_win.close()
        self.show_admin()

    def show_Course_Modify(self):
        self.course_modify_win = Ui_Admin_Course()
        self.course_modify_win.Course_Goback_Admin.connect(self.course_back_admin)
        self.admin_window.close()
        self.course_modify_win.show()

    def course_back_admin(self):
        self.course_modify_win.close()
        self.show_admin()

    def show_Choose_Modify(self):
        self.choose_modify_win = Ui_Admin_Choose()
        self.choose_modify_win.Choose_Goback_Admin.connect(self.choose_back_admin)
        self.admin_window.close()
        self.choose_modify_win.show()

    def choose_back_admin(self):
        self.choose_modify_win.close()
        self.show_admin()

    def show_Score_Modify(self):
        self.score_modify_win = Ui_Teacher_Score()
        self.score_modify_win.Score_Goback_Teacher.connect(self.score_back_teacher)
        self.teacher_window.close()
        self.score_modify_win.show()

    def score_back_teacher(self):
        self.score_modify_win.close()
        self.show_teacher()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


userID = ""
userChar = ""
if __name__ == '__main__':
    db = sqlite3.connect('experiment_2.db')
    main()
