from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    """Defines the detailed user interface of the main window"""

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 240)
        font = QFont()
        font.setFamily(u"Malgun Gothic")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setLocale(QLocale(QLocale.Korean, QLocale.SouthKorea))
        self.input_height = QDoubleSpinBox(MainWindow)
        self.input_height.setObjectName(u"input_height")
        self.input_height.setGeometry(QRect(140, 20, 241, 30))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(10)
        self.input_height.setFont(font1)
        self.input_height.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.input_height.setMinimum(50.000000000000000)
        self.input_height.setMaximum(250.000000000000000)
        self.input_height.setValue(170.000000000000000)
        self.input_weight = QDoubleSpinBox(MainWindow)
        self.input_weight.setObjectName(u"input_weight")
        self.input_weight.setGeometry(QRect(140, 60, 241, 30))
        self.input_weight.setFont(font1)
        self.input_weight.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.input_weight.setMinimum(0.100000000000000)
        self.input_weight.setMaximum(250.000000000000000)
        self.input_weight.setValue(65.000000000000000)
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 81, 30))
        self.label.setFont(font)
        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 81, 30))
        self.label_2.setFont(font)
        self.label_3 = QLabel(MainWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 140, 111, 30))
        self.label_3.setFont(font)
        self.result_value = QLineEdit(MainWindow)
        self.result_value.setObjectName(u"result_value")
        self.result_value.setGeometry(QRect(262, 140, 119, 30))
        self.result_value.setFont(font1)
        self.result_value.setText(u"00.00 kg/m\u00b2")
        self.result_value.setMaxLength(12)
        self.result_value.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.result_value.setReadOnly(True)
        self.result_msg = QLineEdit(MainWindow)
        self.result_msg.setObjectName(u"result_msg")
        self.result_msg.setGeometry(QRect(140, 140, 119, 30))
        self.result_msg.setFont(font)
        self.result_msg.setText(u"\uc800\uccb4\uc911")
        self.result_msg.setMaxLength(12)
        self.result_msg.setAlignment(Qt.AlignCenter)
        self.result_msg.setReadOnly(True)
        self.result_slide = QSlider(MainWindow)
        self.result_slide.setObjectName(u"result_slide")
        self.result_slide.setEnabled(False)
        self.result_slide.setGeometry(QRect(20, 170, 361, 22))
        self.result_slide.setMinimum(15)
        self.result_slide.setMaximum(35)
        self.result_slide.setValue(15)
        self.result_slide.setOrientation(Qt.Horizontal)
        self.line = QFrame(MainWindow)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(76, 195, 5, 11))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(MainWindow)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(163, 195, 5, 11))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(MainWindow)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(198, 195, 5, 11))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(MainWindow)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(284, 195, 5, 11))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(MainWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 200, 41, 30))
        font2 = QFont()
        font2.setFamily(u"Malgun Gothic")
        font2.setPointSize(8)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(MainWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 200, 41, 30))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(MainWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(162, 200, 41, 30))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(MainWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(205, 200, 41, 41))
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.line_5 = QFrame(MainWindow)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(245, 195, 5, 11))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_8 = QLabel(MainWindow)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(246, 200, 41, 41))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(MainWindow)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(310, 200, 41, 41))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.calculate = QPushButton(MainWindow)
        self.calculate.setObjectName(u"calculate")
        self.calculate.setGeometry(QRect(280, 100, 101, 30))
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"\ube44\ub9cc\ub3c4 \uacc4\uc0b0\uae30", None))
        self.input_height.setSuffix(QCoreApplication.translate("MainWindow", u" cm", None))
        self.input_weight.setSuffix(QCoreApplication.translate("MainWindow", u" kg", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ud0a4", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ubab8\ubb34\uac8c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ube44\ub9cc\ub3c4(BMI)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" color:#4400cc;\">\uc800\uccb4\uc911</span></p></body></html>",
                                                        None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" color:#0000ff;\">\uc815\uc0c1</span></p></body></html>",
                                                        None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" color:#aa55ff;\">\uacfc\uccb4\uc911</span></p></body></html>",
                                                        None))
        self.label_7.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><span style=\" color:#ffcc00;\">\uacbd\ub3c4</span><br/><span style=\" color:#ffcc00;\">\ube44\ub9cc</span></body></html>",
                                                        None))
        self.label_8.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" color:#ff8800;\">\uc911\ub4f1\ub3c4<br/>\ube44\ub9cc</span></p></body></html>",
                                                        None))
        self.label_9.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" color:#ff0000;\">\uace0\ub3c4</span><br/><span style=\" color:#ff0000;\">\ube44\ub9cc</span></p></body></html>",
                                                        None))
        self.calculate.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc0b0(&C)", None))


class MainWindow(QWidget, Ui_MainWindow):
    """Defines the event handlers for the main window."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calculate.clicked.connect(self.calculateClicked)
        self.calculateClicked()

    def calculateClicked(self):
        """Calculate BMI and display it"""
        height: float = self.input_height.value() / 100.0
        weight: float = self.input_weight.value()

        bmi: float = weight / (height ** 2)
        self.result_value.setText(u"%0.2f kg/m\u00b2" % bmi)
        if bmi < 15:
            self.result_slide.setValue(15)
        elif bmi > 35:
            self.result_slide.setValue(35)
        else:
            self.result_slide.setValue(int(bmi))

        if bmi < 18.5:
            self.result_msg.setText(u"저체중")
        elif bmi < 23:
            self.result_msg.setText(u"정상")
        elif bmi < 25:
            self.result_msg.setText(u"과체중")
        elif bmi < 27.5:
            self.result_msg.setText(u"경도비만")
        elif bmi < 30:
            self.result_msg.setText(u"중등도비만")
        else:
            self.result_msg.setText(u"고도비만")
