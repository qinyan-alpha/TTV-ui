# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demoui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(1800, 1000))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: r"
                        "gb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#leftbotton_logo .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#leftbotton_logo .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#ti"
                        "tleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extr"
                        "a Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPu"
                        "shButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ////////////////////"
                        "/////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-to"
                        "p-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QS"
                        "crollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: no"
                        "ne;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub"
                        "-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt"
                        ".png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	b"
                        "order-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0p"
                        "x;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	bor"
                        "der-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMinimumSize(QSize(1000, 0))
        self.bgApp.setMaximumSize(QSize(1800, 1000))
        self.bgApp.setFrameShape(QFrame.StyledPanel)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftbotton_logo = QFrame(self.leftMenuBg)
        self.leftbotton_logo.setObjectName(u"leftbotton_logo")
        self.leftbotton_logo.setEnabled(True)
        self.leftbotton_logo.setMinimumSize(QSize(0, 40))
        self.leftbotton_logo.setMaximumSize(QSize(16777215, 55))
        self.leftbotton_logo.setStyleSheet(u"#leftbotton_logo .QPushButton {		\n"
"	background-color: rgb(220, 147, 249);\n"
"	background-position:center;\n"
"    background-repeat: no-repeat;\n"
"	border-radius: 25px;\n"
"}\n"
"#leftbotton_logo .QPushButton:hover {\n"
"	background-color: rgb(240, 200, 249);\n"
"}")
        self.leftbotton_logo.setFrameShape(QFrame.StyledPanel)
        self.leftbotton_logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.leftbotton_logo)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(4, 0, 0, 0)
        self.pushButton = QPushButton(self.leftbotton_logo)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(50, 50))
        self.pushButton.setStyleSheet(u"background-image: url(:/icon/uiimage/button/icons/cil-media-play.png);\n"
"")
        self.pushButton.setIconSize(QSize(60, 60))

        self.verticalLayout_6.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.leftbotton_logo)

        self.topMenu = QFrame(self.leftMenuBg)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 80))
        self.topMenu.setMaximumSize(QSize(16777215, 80))
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.topMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.btn_home_2 = QPushButton(self.topMenu)
        self.btn_home_2.setObjectName(u"btn_home_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home_2.sizePolicy().hasHeightForWidth())
        self.btn_home_2.setSizePolicy(sizePolicy)
        self.btn_home_2.setMinimumSize(QSize(0, 45))
        self.btn_home_2.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.btn_home_2.setFont(font)
        self.btn_home_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_home_2.setStyleSheet(u"background-image: url(:/icon/uiimage/button/icons/cil-home.png);")

        self.verticalLayout.addWidget(self.btn_home_2)


        self.verticalLayout_2.addWidget(self.topMenu)

        self.leftbotton_setting_2 = QFrame(self.leftMenuBg)
        self.leftbotton_setting_2.setObjectName(u"leftbotton_setting_2")
        self.leftbotton_setting_2.setFrameShape(QFrame.StyledPanel)
        self.leftbotton_setting_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.leftbotton_setting_2)

        self.bottomMenu = QFrame(self.leftMenuBg)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setMinimumSize(QSize(0, 50))
        self.bottomMenu.setMaximumSize(QSize(16777215, 50))
        self.bottomMenu.setFrameShape(QFrame.StyledPanel)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icon/uiimage/button/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalLayout_2.addWidget(self.bottomMenu)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_2.setStretch(3, 1)

        self.horizontalLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setMinimumSize(QSize(940, 0))
        self.contentBox.setFrameShape(QFrame.StyledPanel)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.contentBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(940, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.StyledPanel)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        self.leftBox.setFrameShape(QFrame.StyledPanel)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.leftBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(4, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setFont(font)

        self.verticalLayout_7.addWidget(self.titleRightInfo)


        self.horizontalLayout_4.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 0))
        self.rightButtons.setMaximumSize(QSize(150, 16777215))
        self.rightButtons.setFrameShape(QFrame.StyledPanel)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.changeoutboderAppBtn = QPushButton(self.rightButtons)
        self.changeoutboderAppBtn.setObjectName(u"changeoutboderAppBtn")
        self.changeoutboderAppBtn.setMinimumSize(QSize(28, 28))
        self.changeoutboderAppBtn.setMaximumSize(QSize(28, 28))
        self.changeoutboderAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icon/uiimage/button/icons/cil-library.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changeoutboderAppBtn.setIcon(icon)
        self.changeoutboderAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.changeoutboderAppBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout_4.addWidget(self.rightButtons)


        self.verticalLayout_4.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setMinimumSize(QSize(940, 0))
        self.contentBottom.setFrameShape(QFrame.StyledPanel)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.mian = QFrame(self.contentBottom)
        self.mian.setObjectName(u"mian")
        self.mian.setMinimumSize(QSize(940, 0))
        self.mian.setFrameShape(QFrame.StyledPanel)
        self.mian.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.mian)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.mian)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setMinimumSize(QSize(940, 0))
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(940, 0))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setMinimumSize(QSize(940, 0))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(False)
        self.page_1.setFont(font2)
        self.page_1.setStyleSheet(u"QWidget {\n"
"    color: rgb(221, 221, 221);\n"
"    font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;}")
        self.horizontalLayout_13 = QHBoxLayout(self.page_1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 9, 0)
        self.scrollArea_2 = QScrollArea(self.page_1)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollArea{background-color:rgb(47,54,60)}\n"
"\n"
"QScrollArea{border:0px}")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -15, 923, 828))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_17 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.textframe = QFrame(self.frame_17)
        self.textframe.setObjectName(u"textframe")
        self.textframe.setMinimumSize(QSize(0, 200))
        self.textframe.setFrameShape(QFrame.StyledPanel)
        self.textframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.textframe)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.frame_12 = QFrame(self.textframe)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_35.addWidget(self.frame_12)

        self.textEdit = QTextEdit(self.textframe)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setAutoFillBackground(False)

        self.horizontalLayout_35.addWidget(self.textEdit)

        self.frame_8 = QFrame(self.textframe)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_35.addWidget(self.frame_8)


        self.horizontalLayout_28.addWidget(self.textframe)


        self.verticalLayout_18.addWidget(self.frame_17)

        self.func = QFrame(self.scrollAreaWidgetContents_2)
        self.func.setObjectName(u"func")
        self.func.setFrameShape(QFrame.StyledPanel)
        self.func.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.func)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_15 = QFrame(self.func)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(50, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_15)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.play = QPushButton(self.frame_15)
        self.play.setObjectName(u"play")
        self.play.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-image: url(:/icon/uiimage/button/icons/cil-media-play.png);\n"
"background-position: center;")

        self.verticalLayout_20.addWidget(self.play)

        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(50, 40))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")

        self.verticalLayout_20.addWidget(self.frame_21)


        self.horizontalLayout_25.addWidget(self.frame_15)

        self.infer_play = QFrame(self.func)
        self.infer_play.setObjectName(u"infer_play")
        self.infer_play.setFrameShape(QFrame.StyledPanel)
        self.infer_play.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.infer_play)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.wavslider = QSlider(self.infer_play)
        self.wavslider.setObjectName(u"wavslider")
        self.wavslider.setMinimum(0)
        self.wavslider.setMaximum(100)
        self.wavslider.setOrientation(Qt.Horizontal)

        self.verticalLayout_17.addWidget(self.wavslider)

        self.frame_19 = QFrame(self.infer_play)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_24.addWidget(self.frame_20)

        self.frame_18 = QFrame(self.frame_19)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, -1, 0)
        self.inferbutton = QPushButton(self.frame_18)
        self.inferbutton.setObjectName(u"inferbutton")
        self.inferbutton.setMinimumSize(QSize(0, 0))
        self.inferbutton.setMaximumSize(QSize(16777215, 16777215))
        self.inferbutton.setStyleSheet(u"QPushButton:hover {\n"
"       background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton {\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(132, 99, 218);\n"
"}\n"
"QPushButton {\n"
"    color: rgb(221, 221, 221);\n"
"    font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"")

        self.verticalLayout_21.addWidget(self.inferbutton)

        self.show_time = QLabel(self.frame_18)
        self.show_time.setObjectName(u"show_time")
        self.show_time.setMinimumSize(QSize(0, 0))
        self.show_time.setMaximumSize(QSize(16777215, 16777215))
        self.show_time.setStyleSheet(u"font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.show_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.show_time)


        self.horizontalLayout_24.addWidget(self.frame_18)

        self.frame_26 = QFrame(self.frame_19)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_24.addWidget(self.frame_26)


        self.verticalLayout_17.addWidget(self.frame_19)


        self.horizontalLayout_25.addWidget(self.infer_play)

        self.frame_16 = QFrame(self.func)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(50, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.save = QPushButton(self.frame_16)
        self.save.setObjectName(u"save")
        self.save.setMinimumSize(QSize(0, 40))
        self.save.setStyleSheet(u"background-image: url(:/icon/uiimage/button/icons/cil-save.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")

        self.verticalLayout_19.addWidget(self.save)

        self.frame_22 = QFrame(self.frame_16)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(50, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.frame_22)


        self.horizontalLayout_25.addWidget(self.frame_16)


        self.verticalLayout_18.addWidget(self.func)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")

        self.verticalLayout_18.addWidget(self.pushButton_2)

        self.inferparsersetting = QFrame(self.scrollAreaWidgetContents_2)
        self.inferparsersetting.setObjectName(u"inferparsersetting")
        self.inferparsersetting.setMinimumSize(QSize(680, 0))
        self.inferparsersetting.setMaximumSize(QSize(16777215, 16777215))
        self.inferparsersetting.setFrameShape(QFrame.StyledPanel)
        self.inferparsersetting.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.inferparsersetting)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.inferparsersetting)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(380, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.inferparsersetting1 = QLabel(self.frame_6)
        self.inferparsersetting1.setObjectName(u"inferparsersetting1")
        self.inferparsersetting1.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.inferparsersetting1.setFont(font3)
        self.inferparsersetting1.setStyleSheet(u"color: rgb(221, 221, 221);\n"
"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"")

        self.verticalLayout_15.addWidget(self.inferparsersetting1)

        self.inferparser = QFrame(self.frame_6)
        self.inferparser.setObjectName(u"inferparser")
        self.inferparser.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setItalic(False)
        self.inferparser.setFont(font4)
        self.inferparser.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;    \n"
"    font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"QComboBox{\n"
"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"\n"
"")
        self.inferparser.setFrameShape(QFrame.StyledPanel)
        self.inferparser.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.inferparser)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.inferparser)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.comboBox_4 = QComboBox(self.inferparser)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(170, 0))
        self.comboBox_4.setMaximumSize(QSize(170, 16777215))
        self.comboBox_4.setFont(font4)
        self.comboBox_4.setEditable(False)

        self.horizontalLayout_11.addWidget(self.comboBox_4)


        self.verticalLayout_15.addWidget(self.inferparser)

        self.inferparser_2 = QFrame(self.frame_6)
        self.inferparser_2.setObjectName(u"inferparser_2")
        self.inferparser_2.setMaximumSize(QSize(16777215, 16777215))
        self.inferparser_2.setFont(font4)
        self.inferparser_2.setStyleSheet(u"background-color: #282F38;\n"
"border-radius: 10px;    \n"
"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"\n"
"\n"
"")
        self.inferparser_2.setFrameShape(QFrame.StyledPanel)
        self.inferparser_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.inferparser_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.inferparser_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"border: 0.2px solid black;\n"
"border-radius: 5px")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.frame = QFrame(self.inferparser_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.rate1 = QLabel(self.frame)
        self.rate1.setObjectName(u"rate1")

        self.horizontalLayout_6.addWidget(self.rate1)

        self.horizontalSlider1 = QSlider(self.frame)
        self.horizontalSlider1.setObjectName(u"horizontalSlider1")
        self.horizontalSlider1.setMinimumSize(QSize(140, 0))
        self.horizontalSlider1.setMaximumSize(QSize(140, 16777215))
        self.horizontalSlider1.setMaximum(10)
        self.horizontalSlider1.setPageStep(0)
        self.horizontalSlider1.setValue(2)
        self.horizontalSlider1.setSliderPosition(2)
        self.horizontalSlider1.setTracking(False)
        self.horizontalSlider1.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.horizontalSlider1)


        self.horizontalLayout_7.addWidget(self.frame)


        self.verticalLayout_15.addWidget(self.inferparser_2)

        self.inferparser_3 = QFrame(self.frame_6)
        self.inferparser_3.setObjectName(u"inferparser_3")
        self.inferparser_3.setMaximumSize(QSize(16777215, 16777215))
        self.inferparser_3.setFont(font4)
        self.inferparser_3.setStyleSheet(u"background-color: #282F38;\n"
"border-radius: 10px;    \n"
"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"\n"
"\n"
"")
        self.inferparser_3.setFrameShape(QFrame.StyledPanel)
        self.inferparser_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.inferparser_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_7 = QLabel(self.inferparser_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"border: 0.2px solid black;\n"
"border-radius: 5px")

        self.horizontalLayout_12.addWidget(self.label_7)

        self.frame_2 = QFrame(self.inferparser_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setMaximumSize(QSize(200, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.rate2 = QLabel(self.frame_2)
        self.rate2.setObjectName(u"rate2")

        self.horizontalLayout_15.addWidget(self.rate2)

        self.horizontalSlider2 = QSlider(self.frame_2)
        self.horizontalSlider2.setObjectName(u"horizontalSlider2")
        self.horizontalSlider2.setMinimumSize(QSize(140, 0))
        self.horizontalSlider2.setMaximumSize(QSize(140, 16777215))
        self.horizontalSlider2.setMaximum(20)
        self.horizontalSlider2.setPageStep(0)
        self.horizontalSlider2.setValue(10)
        self.horizontalSlider2.setSliderPosition(10)
        self.horizontalSlider2.setTracking(False)
        self.horizontalSlider2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.horizontalSlider2)


        self.horizontalLayout_12.addWidget(self.frame_2)


        self.verticalLayout_15.addWidget(self.inferparser_3)

        self.inferparser_4 = QFrame(self.frame_6)
        self.inferparser_4.setObjectName(u"inferparser_4")
        self.inferparser_4.setMaximumSize(QSize(16777215, 16777215))
        self.inferparser_4.setFont(font4)
        self.inferparser_4.setStyleSheet(u"background-color: #282F38;\n"
"border-radius: 10px;    \n"
"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"\n"
"\n"
"")
        self.inferparser_4.setFrameShape(QFrame.StyledPanel)
        self.inferparser_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.inferparser_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.inferparser_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"border: 0.2px solid black;\n"
"border-radius: 5px")

        self.horizontalLayout_16.addWidget(self.label_8)

        self.frame_3 = QFrame(self.inferparser_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 0))
        self.frame_3.setMaximumSize(QSize(200, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.rate3 = QLabel(self.frame_3)
        self.rate3.setObjectName(u"rate3")

        self.horizontalLayout_18.addWidget(self.rate3)

        self.horizontalSlider3 = QSlider(self.frame_3)
        self.horizontalSlider3.setObjectName(u"horizontalSlider3")
        self.horizontalSlider3.setMinimumSize(QSize(140, 0))
        self.horizontalSlider3.setMaximumSize(QSize(140, 16777215))
        self.horizontalSlider3.setMaximum(20)
        self.horizontalSlider3.setPageStep(0)
        self.horizontalSlider3.setValue(9)
        self.horizontalSlider3.setSliderPosition(9)
        self.horizontalSlider3.setTracking(False)
        self.horizontalSlider3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_18.addWidget(self.horizontalSlider3)


        self.horizontalLayout_16.addWidget(self.frame_3)


        self.verticalLayout_15.addWidget(self.inferparser_4)

        self.inferparser_5 = QFrame(self.frame_6)
        self.inferparser_5.setObjectName(u"inferparser_5")
        self.inferparser_5.setMaximumSize(QSize(16777215, 16777215))
        self.inferparser_5.setFont(font4)
        self.inferparser_5.setStyleSheet(u"background-color: #282F38;\n"
"border-radius: 10px;    \n"
"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"\n"
"\n"
"")
        self.inferparser_5.setFrameShape(QFrame.StyledPanel)
        self.inferparser_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.inferparser_5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_9 = QLabel(self.inferparser_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"border: 0.2px solid black;\n"
"border-radius: 5px")

        self.horizontalLayout_19.addWidget(self.label_9)

        self.frame_4 = QFrame(self.inferparser_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setMaximumSize(QSize(200, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.rate4 = QLabel(self.frame_4)
        self.rate4.setObjectName(u"rate4")

        self.horizontalLayout_21.addWidget(self.rate4)

        self.horizontalSlider4 = QSlider(self.frame_4)
        self.horizontalSlider4.setObjectName(u"horizontalSlider4")
        self.horizontalSlider4.setMinimumSize(QSize(140, 0))
        self.horizontalSlider4.setMaximumSize(QSize(140, 16777215))
        self.horizontalSlider4.setMaximum(20)
        self.horizontalSlider4.setPageStep(0)
        self.horizontalSlider4.setValue(9)
        self.horizontalSlider4.setSliderPosition(9)
        self.horizontalSlider4.setTracking(False)
        self.horizontalSlider4.setOrientation(Qt.Horizontal)

        self.horizontalLayout_21.addWidget(self.horizontalSlider4)


        self.horizontalLayout_19.addWidget(self.frame_4)


        self.verticalLayout_15.addWidget(self.inferparser_5)

        self.inferparser_6 = QFrame(self.frame_6)
        self.inferparser_6.setObjectName(u"inferparser_6")
        self.inferparser_6.setMaximumSize(QSize(16777215, 16777215))
        self.inferparser_6.setFont(font4)
        self.inferparser_6.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;    \n"
"    font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"QComboBox{\n"
"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"\n"
"")
        self.inferparser_6.setFrameShape(QFrame.StyledPanel)
        self.inferparser_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.inferparser_6)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_10 = QLabel(self.inferparser_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.label_10)

        self.comboBox_5 = QComboBox(self.inferparser_6)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(170, 0))
        self.comboBox_5.setMaximumSize(QSize(170, 16777215))
        self.comboBox_5.setFont(font4)
        self.comboBox_5.setEditable(False)

        self.horizontalLayout_22.addWidget(self.comboBox_5)


        self.verticalLayout_15.addWidget(self.inferparser_6)


        self.horizontalLayout_23.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.inferparsersetting)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(380, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_7)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 20))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(-540, 60, 881, 81))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_9)

        self.inferparsersetting_2 = QLabel(self.frame_7)
        self.inferparsersetting_2.setObjectName(u"inferparsersetting_2")
        self.inferparsersetting_2.setMinimumSize(QSize(0, 0))
        self.inferparsersetting_2.setFont(font3)
        self.inferparsersetting_2.setLayoutDirection(Qt.LeftToRight)
        self.inferparsersetting_2.setStyleSheet(u"color: rgb(221, 221, 221);\n"
"font: 14pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"")
        self.inferparsersetting_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.inferparsersetting_2)


        self.horizontalLayout_23.addWidget(self.frame_7)


        self.verticalLayout_18.addWidget(self.inferparsersetting)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_13.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.page_1)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.page_setting.setFont(font5)
        self.page_setting.setStyleSheet(u"QWidget {\n"
"    color: rgb(221, 221, 221);\n"
"    font: 10pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"QLineEdit{\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;}")
        self.verticalLayout_10 = QVBoxLayout(self.page_setting)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, -1, 0)
        self.scrollArea = QScrollArea(self.page_setting)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setStyleSheet(u"QScrollArea{background-color:rgb(47,54,60)}\n"
"\n"
"QScrollArea{border:0px}")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 884, 879))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.setting_drivers = QFrame(self.scrollAreaWidgetContents)
        self.setting_drivers.setObjectName(u"setting_drivers")
        self.setting_drivers.setStyleSheet(u"QFrame{background-color:rgb(47,54,60)}")
        self.setting_drivers.setFrameShape(QFrame.StyledPanel)
        self.setting_drivers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.setting_drivers)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.driver = QLabel(self.setting_drivers)
        self.driver.setObjectName(u"driver")
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        self.driver.setFont(font6)
        self.driver.setStyleSheet(u"QLabel {\n"
"    color: rgb(221, 221, 221);\n"
"    font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.driver)

        self.driver_starts = QFrame(self.setting_drivers)
        self.driver_starts.setObjectName(u"driver_starts")
        self.driver_starts.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.driver_starts.setFrameShape(QFrame.StyledPanel)
        self.driver_starts.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.driver_starts)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_2 = QLabel(self.driver_starts)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.devicecomboBox = QComboBox(self.driver_starts)
        self.devicecomboBox.addItem("")
        self.devicecomboBox.setObjectName(u"devicecomboBox")
        self.devicecomboBox.setFont(font5)
        self.devicecomboBox.setEditable(False)

        self.horizontalLayout_9.addWidget(self.devicecomboBox)


        self.verticalLayout_13.addWidget(self.driver_starts)

        self.frame_5 = QFrame(self.setting_drivers)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.inferway = QComboBox(self.frame_5)
        self.inferway.addItem("")
        self.inferway.addItem("")
        self.inferway.setObjectName(u"inferway")
        self.inferway.setFont(font5)
        self.inferway.setEditable(False)

        self.horizontalLayout_8.addWidget(self.inferway)


        self.verticalLayout_13.addWidget(self.frame_5)


        self.verticalLayout_11.addWidget(self.setting_drivers)

        self.setting_drivers_2 = QFrame(self.scrollAreaWidgetContents)
        self.setting_drivers_2.setObjectName(u"setting_drivers_2")
        self.setting_drivers_2.setStyleSheet(u"QFrame{background-color:rgb(47,54,60)}")
        self.setting_drivers_2.setFrameShape(QFrame.StyledPanel)
        self.setting_drivers_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.setting_drivers_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.driver_2 = QLabel(self.setting_drivers_2)
        self.driver_2.setObjectName(u"driver_2")
        self.driver_2.setFont(font6)
        self.driver_2.setStyleSheet(u"QLabel {\n"
"    color: rgb(221, 221, 221);\n"
"    font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.driver_2)

        self.driver_starts_2 = QFrame(self.setting_drivers_2)
        self.driver_starts_2.setObjectName(u"driver_starts_2")
        self.driver_starts_2.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.driver_starts_2.setFrameShape(QFrame.StyledPanel)
        self.driver_starts_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.driver_starts_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.driver_starts_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.comboBox_3 = QComboBox(self.driver_starts_2)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setFont(font5)
        self.comboBox_3.setEditable(False)

        self.horizontalLayout_10.addWidget(self.comboBox_3)


        self.verticalLayout_12.addWidget(self.driver_starts_2)

        self.frame_10 = QFrame(self.setting_drivers_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.label_11)

        self.model_information = QLabel(self.frame_10)
        self.model_information.setObjectName(u"model_information")

        self.horizontalLayout_20.addWidget(self.model_information)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.frame_25 = QFrame(self.setting_drivers_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_14 = QLabel(self.frame_25)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"")

        self.horizontalLayout_29.addWidget(self.label_14)


        self.verticalLayout_12.addWidget(self.frame_25)


        self.verticalLayout_11.addWidget(self.setting_drivers_2)

        self.setting_drivers_3 = QFrame(self.scrollAreaWidgetContents)
        self.setting_drivers_3.setObjectName(u"setting_drivers_3")
        self.setting_drivers_3.setMaximumSize(QSize(16777215, 200))
        self.setting_drivers_3.setStyleSheet(u"QFrame{background-color:rgb(47,54,60)}")
        self.setting_drivers_3.setFrameShape(QFrame.StyledPanel)
        self.setting_drivers_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.setting_drivers_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.driver_4 = QLabel(self.setting_drivers_3)
        self.driver_4.setObjectName(u"driver_4")
        self.driver_4.setMinimumSize(QSize(0, 0))
        self.driver_4.setFont(font6)
        self.driver_4.setStyleSheet(u"QLabel {\n"
"    color: rgb(221, 221, 221);\n"
"    font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"")

        self.verticalLayout_14.addWidget(self.driver_4)

        self.frame_11 = QFrame(self.setting_drivers_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.openweb = QFrame(self.frame_11)
        self.openweb.setObjectName(u"openweb")
        self.openweb.setFrameShape(QFrame.StyledPanel)
        self.openweb.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.openweb)


        self.verticalLayout_14.addWidget(self.frame_11)

        self.frame_24 = QFrame(self.setting_drivers_3)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 16777215))
        self.frame_24.setStyleSheet(u"QFrame{\n"
"    background-color: #282F38;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_28 = QFrame(self.frame_24)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_28)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font5)
        self.label_13.setStyleSheet(u"")

        self.horizontalLayout_27.addWidget(self.label_13)

        self.lineEdit = QLineEdit(self.frame_28)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_27.addWidget(self.lineEdit)


        self.horizontalLayout_17.addWidget(self.frame_28)

        self.update = QPushButton(self.frame_24)
        self.update.setObjectName(u"update")
        self.update.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_17.addWidget(self.update)


        self.verticalLayout_14.addWidget(self.frame_24)


        self.verticalLayout_11.addWidget(self.setting_drivers_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_setting)

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.pagesContainer)


        self.verticalLayout_5.addWidget(self.mian)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(940, 0))
        self.bottomBar.setFrameShape(QFrame.StyledPanel)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.creditsLabel)

        self.frame_13 = QFrame(self.bottomBar)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(40, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_13)

        self.stateshow = QLabel(self.bottomBar)
        self.stateshow.setObjectName(u"stateshow")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setBold(False)
        font7.setItalic(False)
        self.stateshow.setFont(font7)
        self.stateshow.setStyleSheet(u"font-size: 11px; \n"
"color: rgb(113, 126, 149);")
        self.stateshow.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.stateshow)

        self.frame_23 = QFrame(self.bottomBar)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(40, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_23)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(0, 0))
        self.version.setMaximumSize(QSize(100, 16777215))
        self.version.setTextFormat(Qt.PlainText)
        self.version.setScaledContents(False)
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.version.setWordWrap(False)
        self.version.setMargin(0)

        self.horizontalLayout_3.addWidget(self.version)


        self.verticalLayout_5.addWidget(self.bottomBar)

        self.verticalLayout_5.setStretch(0, 20)

        self.verticalLayout_4.addWidget(self.contentBottom)


        self.horizontalLayout.addWidget(self.contentBox)


        self.verticalLayout_3.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"text to voice", None))
        self.pushButton.setText("")
        self.btn_home_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Text to voice</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.changeoutboderAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.changeoutboderAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5f85\u8f6c\u5316\u6587\u5b57", None))
        self.play.setText("")
        self.inferbutton.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u7406", None))
        self.show_time.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0/0</p></body></html>", None))
        self.save.setText("")
        self.pushButton_2.setText("")
        self.inferparsersetting1.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8bf4\u8bdd\u4eba", None))
        self.comboBox_4.setCurrentText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SDP/DP\u6df7\u5408\u6bd4\u7387", None))
        self.rate1.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u60c5\u611f", None))
        self.rate2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u7d20\u957f\u5ea6", None))
        self.rate3.setText(QCoreApplication.translate("MainWindow", u"0.9", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u901f", None))
        self.rate4.setText(QCoreApplication.translate("MainWindow", u"0.9", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8bed\u8a00", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"ZH", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"JP", None))

        self.comboBox_5.setCurrentText(QCoreApplication.translate("MainWindow", u"ZH", None))
        self.inferparsersetting_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; vertical-align:super;\">\u53c2\u6570\u89e3\u91ca</span></p><p align=\"justify\"><span style=\" font-size:16pt; font-weight:700; vertical-align:super;\">\u8f93\u5165\u6587\u672c\u6846\uff1a\u53ea\u80fd\u5408\u6210\u4e2d\u6587\u5b57\u7b26\u548c\u90e8\u5206\u6807\u70b9\u7b26\u53f7\uff0c</span></p><p align=\"justify\"><span style=\" font-size:16pt; font-weight:700; vertical-align:super;\">\u4e0d\u80fd\u5408\u6210\u82f1\u6587\u548c\u6570\u5b57\uff0c\u8fd9\u4e9b\u4e0d\u80fd\u8f6c\u5316</span></p><p align=\"justify\"><span style=\" font-size:16pt; font-weight:700; vertical-align:super;\">\u5b57\u7b26\u8bf7\u8f6c\u5316\u4e3a\u53d1\u97f3\u76f8\u8fd1\u7684\u6c49\u5b57</span></p><p align=\"justify\"><span style=\" font-size:16pt; font-weight:700; vertical-align:super;\">SDP/DP\u6df7\u5408\u6bd4\uff1aSDP\u5728\u5408\u6210\u65f6\u7684\u6bd4\u91cd\uff0c\u7406\u8bba\u4e0a\u6b64\u6bd4\u7387\u8d8a\u9ad8\uff0c</span></p><p align=\"justify\"><span style=\" fon"
                        "t-size:16pt; font-weight:700; vertical-align:super;\">\u5408\u6210\u7684\u8bed\u8c03\u65b9\u5dee\u8d8a\u5927\u3002</span></p><p align=\"justify\"><span style=\" font-size:16pt; font-weight:700; vertical-align:super;\">\u60c5\u611f\uff1a\u63a7\u5236\u60c5\u611f\u53d8\u5316\u7a0b\u5ea6\uff0c\u9ed8\u8ba4\u57280.2</span></p><p align=\"justify\"><span style=\" font-size:16pt; font-weight:700; vertical-align:super;\">\u97f3\u901f\u957f\u5ea6\uff1a\u63a7\u5236\u97f3\u8282\u53d1\u97f3\u957f\u5ea6\u53d8\u5316\u7a0b\u5ea6\uff0c\u9ed8\u8ba4\u4e3a0.9.</span></p><p align=\"justify\"><br/></p></body></html>", None))
        self.driver.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u8bbe\u5907\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528\u8bbe\u5907", None))
        self.devicecomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u9009\u62e9", None))

        self.devicecomboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u9009\u62e9", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u534a\u7cbe\u5ea6\u8ba1\u7b97(\u4ec5\u82f1\u4f1f\u8fbe\u663e\u5361\u53ef\u7528)", None))
        self.inferway.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.inferway.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))

        self.inferway.setCurrentText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.driver_2.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u9009\u62e9", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5f53\u524d\u6a21\u578b", None))
        self.comboBox_3.setCurrentText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u4fe1\u606f\u4e3a", None))
        self.model_information.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6a21\u578b\u4e0b\u8f7d\uff1a<a href=\"https://huggingface.co/qinyan/TTV-log-model-for-vits/tree/main/mhyhhh\"><span style=\" text-decoration: underline; color:#ffffff;\">qinyan/TTV-log-model-for-vits at main (huggingface.co)</span></a></p></body></html>", None))
        self.driver_4.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u8bad\u7ec3\u97f3\u9891\u548c\u95ee\u9898\u53cd\u9988", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8bf7\u8bbf\u95ee\u6211\u7684GITHUB\u4e3b\u9875\u8fdb\u884c\u8054\u7cfb\u548c\u63d0\u4ea4\uff1a<a href=\"https://github.com/qinyan-alpha/TTV-ui\"><span style=\" text-decoration: underline; color:#ffffff;\">qinyan-alpha/TTV-ui (github.com)</span></a></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8bbe\u7f6e\u4ee3\u7406\u8def\u5f84\uff1a</p></body></html>", None))
        self.update.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"by zhenziyi", None))
        self.stateshow.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u72b6\u6001\u680f\uff1a\u663e\u793a\u7a0b\u5e8f\u8fd0\u884c\u72b6\u6001</p></body></html>", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"version: 1.00", None))
    # retranslateUi

