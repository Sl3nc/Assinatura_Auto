# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_ass.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(538, 446)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QSize(0, 15))
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setMargin(5)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setMargin(5)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 15))
        self.line_2.setMaximumSize(QSize(16777214, 16777215))
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT"])
        font1.setPointSize(20)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_4.setMargin(0)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo_hori = QLabel(self.frame_2)
        self.logo_hori.setObjectName(u"logo_hori")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.logo_hori.sizePolicy().hasHeightForWidth())
        self.logo_hori.setSizePolicy(sizePolicy5)
        self.logo_hori.setMinimumSize(QSize(500, 100))
        self.logo_hori.setMaximumSize(QSize(1000, 200))
        self.logo_hori.setTextFormat(Qt.TextFormat.RichText)
        self.logo_hori.setPixmap(QPixmap(u"../img/ass-hori.png"))
        self.logo_hori.setScaledContents(True)
        self.logo_hori.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.logo_hori)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)
        font2 = QFont()
        font2.setFamilies([u"Arial Rounded MT Bold"])
        font2.setPointSize(28)
        self.label.setFont(font2)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lab_load = QLabel(self.frame)
        self.lab_load.setObjectName(u"lab_load")

        self.horizontalLayout.addWidget(self.lab_load)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy7)
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.pushButton.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 538, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Setor correspondente :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nome do colaborador:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Favor preencha o formul\u00e1rio:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Manual de uso", None))
        self.logo_hori.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Gerador de assinatura", None))
        self.lab_load.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Gerar Assinatura", None))
    # retranslateUi

