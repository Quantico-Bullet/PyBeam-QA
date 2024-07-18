# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'picket_fence_offsets_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_PFOffsetDialog(object):
    def setupUi(self, PFOffsetDialog):
        if not PFOffsetDialog.objectName():
            PFOffsetDialog.setObjectName(u"PFOffsetDialog")
        PFOffsetDialog.resize(369, 400)
        self.gridLayout = QGridLayout(PFOffsetDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttons_spacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.buttons_spacer, 3, 0, 1, 1)

        self.button_box = QDialogButtonBox(PFOffsetDialog)
        self.button_box.setObjectName(u"button_box")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setStyleSheet(u"")
        self.button_box.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)

        self.gridLayout.addWidget(self.button_box, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.picket_num_label = QLabel(PFOffsetDialog)
        self.picket_num_label.setObjectName(u"picket_num_label")

        self.horizontalLayout_2.addWidget(self.picket_num_label)

        self.picket_num_cb = QComboBox(PFOffsetDialog)
        self.picket_num_cb.setObjectName(u"picket_num_cb")

        self.horizontalLayout_2.addWidget(self.picket_num_cb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(PFOffsetDialog)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)


        self.retranslateUi(PFOffsetDialog)
        self.button_box.accepted.connect(PFOffsetDialog.accept)
        self.button_box.rejected.connect(PFOffsetDialog.reject)

        QMetaObject.connectSlotsByName(PFOffsetDialog)
    # setupUi

    def retranslateUi(self, PFOffsetDialog):
        self.picket_num_label.setText(QCoreApplication.translate("PFOffsetDialog", u"Picket No:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PFOffsetDialog", u"Index", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PFOffsetDialog", u"Left Picket (A)", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PFOffsetDialog", u"Right Picket (B)", None));
        pass
    # retranslateUi

