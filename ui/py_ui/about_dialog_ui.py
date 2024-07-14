# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(550, 322)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(AboutDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(AboutDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.app_name_label = QLabel(self.frame_2)
        self.app_name_label.setObjectName(u"app_name_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.app_name_label.sizePolicy().hasHeightForWidth())
        self.app_name_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        self.app_name_label.setFont(font)

        self.gridLayout_2.addWidget(self.app_name_label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.copyright_label = QLabel(self.frame_2)
        self.copyright_label.setObjectName(u"copyright_label")
        sizePolicy1.setHeightForWidth(self.copyright_label.sizePolicy().hasHeightForWidth())
        self.copyright_label.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.copyright_label, 2, 0, 1, 1, Qt.AlignHCenter)

        self.app_version_label = QLabel(self.frame_2)
        self.app_version_label.setObjectName(u"app_version_label")
        sizePolicy.setHeightForWidth(self.app_version_label.sizePolicy().hasHeightForWidth())
        self.app_version_label.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.app_version_label, 1, 0, 1, 1, Qt.AlignHCenter)

        self.github_btn = QPushButton(self.frame_2)
        self.github_btn.setObjectName(u"github_btn")
        icon = QIcon()
        icon.addFile(u":/actionIcons/icons/logo-github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.github_btn.setIcon(icon)

        self.gridLayout_2.addWidget(self.github_btn, 3, 0, 1, 1, Qt.AlignHCenter)

        self.oslibs_groubbox = QGroupBox(self.frame_2)
        self.oslibs_groubbox.setObjectName(u"oslibs_groubbox")
        sizePolicy1.setHeightForWidth(self.oslibs_groubbox.sizePolicy().hasHeightForWidth())
        self.oslibs_groubbox.setSizePolicy(sizePolicy1)
        self.oslibs_groubbox.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.oslibs_groubbox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.open_source_te = QTextEdit(self.oslibs_groubbox)
        self.open_source_te.setObjectName(u"open_source_te")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.open_source_te.sizePolicy().hasHeightForWidth())
        self.open_source_te.setSizePolicy(sizePolicy2)
        self.open_source_te.setMaximumSize(QSize(16777215, 90))
        self.open_source_te.setContextMenuPolicy(Qt.NoContextMenu)
        self.open_source_te.setStyleSheet(u"background-color: transparent")
        self.open_source_te.setReadOnly(True)
        self.open_source_te.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.open_source_te)


        self.gridLayout_2.addWidget(self.oslibs_groubbox, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)

        self.icon_frame = QFrame(AboutDialog)
        self.icon_frame.setObjectName(u"icon_frame")
        self.icon_frame.setFrameShape(QFrame.NoFrame)
        self.icon_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.icon_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.app_icon = QLabel(self.icon_frame)
        self.app_icon.setObjectName(u"app_icon")
        sizePolicy.setHeightForWidth(self.app_icon.sizePolicy().hasHeightForWidth())
        self.app_icon.setSizePolicy(sizePolicy)
        self.app_icon.setMinimumSize(QSize(128, 128))

        self.gridLayout_3.addWidget(self.app_icon, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.icon_frame, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(AboutDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.retranslateUi(AboutDialog)
        self.buttonBox.accepted.connect(AboutDialog.accept)
        self.buttonBox.rejected.connect(AboutDialog.reject)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        self.app_name_label.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">PyBeam QA</span></p></body></html>", None))
        self.copyright_label.setText(QCoreApplication.translate("AboutDialog", u"Copyright \u00a9 2023-2024 Kagiso Lebang", None))
        self.app_version_label.setText(QCoreApplication.translate("AboutDialog", u"version a.b.c", None))
        self.github_btn.setText(QCoreApplication.translate("AboutDialog", u"Github", None))
        self.oslibs_groubbox.setTitle(QCoreApplication.translate("AboutDialog", u"Open source libraries", None))
        pass
    # retranslateUi

