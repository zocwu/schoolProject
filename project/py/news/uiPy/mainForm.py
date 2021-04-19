from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(642, 453)
        Form.setStyleSheet(u"")
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 110, 551, 221))
        self.sendButton = QPushButton(Form)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(490, 340, 89, 25))
        self.sendButton.setStyleSheet(u"background-color: white;\n"
"width: 75px;\n"
"height: 90px;\n"
"font-size: 14px;\n"
"font-weight: bold;")
        self.mainLabel = QLabel(Form)
        self.mainLabel.setObjectName(u"mainLabel")
        self.mainLabel.setGeometry(QRect(180, 20, 291, 51))
        self.mainLabel.setStyleSheet(u"font: 75 11pt \"Ubuntu Condensed\";\n"
"border: 3px solid rgb(136, 138, 133);\n"
"font-size: 20px;\n"
"")
        self.captionLabel = QLabel(Form)
        self.captionLabel.setObjectName(u"captionLabel")
        self.captionLabel.setGeometry(QRect(30, 340, 451, 91))
        self.captionLabel.setStyleSheet(u"font: 75 11pt \"Serif\";\n"
"border: 3px solid rgb(136, 138, 133);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"News", None))
        self.sendButton.setText(QCoreApplication.translate("Form", u"Send", None))
        self.mainLabel.setText(QCoreApplication.translate("Form", u"                    Input your news", None))
        self.captionLabel.setText(QCoreApplication.translate("Form", u"There will be status information", None))
    # retranslateUi

