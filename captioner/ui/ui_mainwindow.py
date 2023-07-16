# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFontComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QSizePolicy, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

from captioner.widgets import ColorPickerWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(854, 448)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setAutoRepeat(False)
        self.actionMarkdownMode = QAction(MainWindow)
        self.actionMarkdownMode.setObjectName(u"actionMarkdownMode")
        self.actionMarkdownMode.setCheckable(True)
        self.actionAutoRender = QAction(MainWindow)
        self.actionAutoRender.setObjectName(u"actionAutoRender")
        self.actionAutoRender.setCheckable(True)
        self.actionAutoRender.setChecked(True)
        self.actionRender = QAction(MainWindow)
        self.actionRender.setObjectName(u"actionRender")
        self.actionSourceCode = QAction(MainWindow)
        self.actionSourceCode.setObjectName(u"actionSourceCode")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionDrawMargins = QAction(MainWindow)
        self.actionDrawMargins.setObjectName(u"actionDrawMargins")
        self.actionDrawMargins.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"font: 48pt;")
        self.imageLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.imageLabel)

        self.captionEdit = QPlainTextEdit(self.centralwidget)
        self.captionEdit.setObjectName(u"captionEdit")

        self.verticalLayout.addWidget(self.captionEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.leftControlsLayout = QVBoxLayout()
        self.leftControlsLayout.setObjectName(u"leftControlsLayout")
        self.borderControlsLayout = QHBoxLayout()
        self.borderControlsLayout.setObjectName(u"borderControlsLayout")
        self.borderSizeLayout = QFormLayout()
        self.borderSizeLayout.setObjectName(u"borderSizeLayout")
        self.borderSizeLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.sizeLabel = QLabel(self.centralwidget)
        self.sizeLabel.setObjectName(u"sizeLabel")

        self.borderSizeLayout.setWidget(0, QFormLayout.LabelRole, self.sizeLabel)

        self.sizeSpinBox = QSpinBox(self.centralwidget)
        self.sizeSpinBox.setObjectName(u"sizeSpinBox")
        self.sizeSpinBox.setMaximum(999999)

        self.borderSizeLayout.setWidget(0, QFormLayout.FieldRole, self.sizeSpinBox)


        self.borderControlsLayout.addLayout(self.borderSizeLayout)

        self.backgroundColorLayout = QFormLayout()
        self.backgroundColorLayout.setObjectName(u"backgroundColorLayout")
        self.backgroundColorLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.backgroundColorLabel = QLabel(self.centralwidget)
        self.backgroundColorLabel.setObjectName(u"backgroundColorLabel")

        self.backgroundColorLayout.setWidget(0, QFormLayout.LabelRole, self.backgroundColorLabel)

        self.backgroundColorPicker = ColorPickerWidget(self.centralwidget)
        self.backgroundColorPicker.setObjectName(u"backgroundColorPicker")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backgroundColorPicker.sizePolicy().hasHeightForWidth())
        self.backgroundColorPicker.setSizePolicy(sizePolicy)
        self.backgroundColorPicker.setMinimumSize(QSize(20, 20))
        self.backgroundColorPicker.setFrameShape(QFrame.StyledPanel)
        self.backgroundColorPicker.setFrameShadow(QFrame.Raised)

        self.backgroundColorLayout.setWidget(0, QFormLayout.FieldRole, self.backgroundColorPicker)


        self.borderControlsLayout.addLayout(self.backgroundColorLayout)

        self.directionComboBox = QComboBox(self.centralwidget)
        self.directionComboBox.addItem("")
        self.directionComboBox.addItem("")
        self.directionComboBox.addItem("")
        self.directionComboBox.addItem("")
        self.directionComboBox.setObjectName(u"directionComboBox")

        self.borderControlsLayout.addWidget(self.directionComboBox)


        self.leftControlsLayout.addLayout(self.borderControlsLayout)

        self.textControlsLayout = QHBoxLayout()
        self.textControlsLayout.setObjectName(u"textControlsLayout")
        self.textColorLayout = QFormLayout()
        self.textColorLayout.setObjectName(u"textColorLayout")
        self.textColorLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.textColorlabel = QLabel(self.centralwidget)
        self.textColorlabel.setObjectName(u"textColorlabel")

        self.textColorLayout.setWidget(0, QFormLayout.LabelRole, self.textColorlabel)

        self.textColorPicker = ColorPickerWidget(self.centralwidget)
        self.textColorPicker.setObjectName(u"textColorPicker")
        sizePolicy.setHeightForWidth(self.textColorPicker.sizePolicy().hasHeightForWidth())
        self.textColorPicker.setSizePolicy(sizePolicy)
        self.textColorPicker.setMinimumSize(QSize(20, 20))
        self.textColorPicker.setFrameShape(QFrame.StyledPanel)
        self.textColorPicker.setFrameShadow(QFrame.Raised)

        self.textColorLayout.setWidget(0, QFormLayout.FieldRole, self.textColorPicker)


        self.textControlsLayout.addLayout(self.textColorLayout)

        self.fontComboBox = QFontComboBox(self.centralwidget)
        self.fontComboBox.setObjectName(u"fontComboBox")
        font = QFont()
        font.setPointSize(16)
        self.fontComboBox.setCurrentFont(font)

        self.textControlsLayout.addWidget(self.fontComboBox)

        self.fontSizeSpinBox = QSpinBox(self.centralwidget)
        self.fontSizeSpinBox.setObjectName(u"fontSizeSpinBox")
        self.fontSizeSpinBox.setMinimum(1)
        self.fontSizeSpinBox.setMaximum(99999)
        self.fontSizeSpinBox.setValue(16)

        self.textControlsLayout.addWidget(self.fontSizeSpinBox)


        self.leftControlsLayout.addLayout(self.textControlsLayout)


        self.horizontalLayout.addLayout(self.leftControlsLayout)

        self.marginControlsLayout = QGridLayout()
        self.marginControlsLayout.setObjectName(u"marginControlsLayout")
        self.leftMarginLabel = QLabel(self.centralwidget)
        self.leftMarginLabel.setObjectName(u"leftMarginLabel")

        self.marginControlsLayout.addWidget(self.leftMarginLabel, 1, 0, 1, 1)

        self.rightMarginLabel = QLabel(self.centralwidget)
        self.rightMarginLabel.setObjectName(u"rightMarginLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rightMarginLabel.sizePolicy().hasHeightForWidth())
        self.rightMarginLabel.setSizePolicy(sizePolicy1)

        self.marginControlsLayout.addWidget(self.rightMarginLabel, 2, 0, 1, 1)

        self.leftMarginSpinBox = QSpinBox(self.centralwidget)
        self.leftMarginSpinBox.setObjectName(u"leftMarginSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftMarginSpinBox.sizePolicy().hasHeightForWidth())
        self.leftMarginSpinBox.setSizePolicy(sizePolicy2)
        self.leftMarginSpinBox.setMaximum(99999)

        self.marginControlsLayout.addWidget(self.leftMarginSpinBox, 1, 1, 1, 1)

        self.rightMarginSpinBox = QSpinBox(self.centralwidget)
        self.rightMarginSpinBox.setObjectName(u"rightMarginSpinBox")
        sizePolicy2.setHeightForWidth(self.rightMarginSpinBox.sizePolicy().hasHeightForWidth())
        self.rightMarginSpinBox.setSizePolicy(sizePolicy2)
        self.rightMarginSpinBox.setMaximum(99999)

        self.marginControlsLayout.addWidget(self.rightMarginSpinBox, 2, 1, 1, 1)

        self.topMarginLayout = QHBoxLayout()
        self.topMarginLayout.setObjectName(u"topMarginLayout")
        self.topMarginLabel = QLabel(self.centralwidget)
        self.topMarginLabel.setObjectName(u"topMarginLabel")

        self.topMarginLayout.addWidget(self.topMarginLabel)

        self.topMarginSpinBox = QSpinBox(self.centralwidget)
        self.topMarginSpinBox.setObjectName(u"topMarginSpinBox")
        self.topMarginSpinBox.setMaximum(99999)

        self.topMarginLayout.addWidget(self.topMarginSpinBox)


        self.marginControlsLayout.addLayout(self.topMarginLayout, 1, 2, 1, 1)


        self.horizontalLayout.addLayout(self.marginControlsLayout)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 854, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionMarkdownMode)
        self.menuEdit.addAction(self.actionDrawMargins)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAutoRender)
        self.menuEdit.addAction(self.actionRender)
        self.menuAbout.addAction(self.actionSourceCode)
        self.menuAbout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Captioner", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionMarkdownMode.setText(QCoreApplication.translate("MainWindow", u"Markdown mode", None))
#if QT_CONFIG(shortcut)
        self.actionMarkdownMode.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionAutoRender.setText(QCoreApplication.translate("MainWindow", u"Auto-render", None))
        self.actionRender.setText(QCoreApplication.translate("MainWindow", u"Render", None))
#if QT_CONFIG(shortcut)
        self.actionRender.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionSourceCode.setText(QCoreApplication.translate("MainWindow", u"Source code", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionDrawMargins.setText(QCoreApplication.translate("MainWindow", u"Draw margins", None))
        self.imageLabel.setText(QCoreApplication.translate("MainWindow", u"Open an image, or\n"
"drag-and-drop one here!", None))
        self.sizeLabel.setText(QCoreApplication.translate("MainWindow", u"Border size", None))
        self.sizeSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" px", None))
        self.backgroundColorLabel.setText(QCoreApplication.translate("MainWindow", u"Background color", None))
        self.directionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Right", None))
        self.directionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Left", None))
        self.directionComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Up", None))
        self.directionComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Down", None))

        self.textColorlabel.setText(QCoreApplication.translate("MainWindow", u"Text color", None))
        self.leftMarginLabel.setText(QCoreApplication.translate("MainWindow", u"Left margin", None))
        self.rightMarginLabel.setText(QCoreApplication.translate("MainWindow", u"Right margin", None))
        self.leftMarginSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" px", None))
        self.rightMarginSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" px", None))
        self.topMarginLabel.setText(QCoreApplication.translate("MainWindow", u"Top margin", None))
        self.topMarginSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" px", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

