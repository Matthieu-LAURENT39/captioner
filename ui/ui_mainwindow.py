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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox,
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

from widgets import ColorPickerWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 433)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setAutoRepeat(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.imageLabel)

        self.captionEdit = QPlainTextEdit(self.centralwidget)
        self.captionEdit.setObjectName(u"captionEdit")

        self.verticalLayout.addWidget(self.captionEdit)

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

        self.marginLayout = QFormLayout()
        self.marginLayout.setObjectName(u"marginLayout")
        self.marginLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.marginLabel = QLabel(self.centralwidget)
        self.marginLabel.setObjectName(u"marginLabel")

        self.marginLayout.setWidget(0, QFormLayout.LabelRole, self.marginLabel)

        self.marginSpinBox = QSpinBox(self.centralwidget)
        self.marginSpinBox.setObjectName(u"marginSpinBox")
        self.marginSpinBox.setMaximum(99999)

        self.marginLayout.setWidget(0, QFormLayout.FieldRole, self.marginSpinBox)


        self.borderControlsLayout.addLayout(self.marginLayout)

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

        self.markdownModeCheckBox = QCheckBox(self.centralwidget)
        self.markdownModeCheckBox.setObjectName(u"markdownModeCheckBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.markdownModeCheckBox.sizePolicy().hasHeightForWidth())
        self.markdownModeCheckBox.setSizePolicy(sizePolicy1)

        self.borderControlsLayout.addWidget(self.markdownModeCheckBox)


        self.verticalLayout.addLayout(self.borderControlsLayout)

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


        self.verticalLayout.addLayout(self.textControlsLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)

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
        self.imageLabel.setText("")
        self.sizeLabel.setText(QCoreApplication.translate("MainWindow", u"Border size", None))
        self.sizeSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" px", None))
        self.marginLabel.setText(QCoreApplication.translate("MainWindow", u"Margin", None))
        self.marginSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" px", None))
        self.backgroundColorLabel.setText(QCoreApplication.translate("MainWindow", u"Background color", None))
        self.directionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Right", None))
        self.directionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Left", None))
        self.directionComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Up", None))
        self.directionComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Down", None))

        self.markdownModeCheckBox.setText(QCoreApplication.translate("MainWindow", u"Markdown mode", None))
#if QT_CONFIG(shortcut)
        self.markdownModeCheckBox.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.textColorlabel.setText(QCoreApplication.translate("MainWindow", u"Text color", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

