# Form implementation generated from reading ui file 'C:\Users\admin\Documents\GitHub\ai-la-trieu-phu\ui\gameplay.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GamePlay(object):
    def setupUi(self, GamePlay):
        GamePlay.setObjectName("GamePlay")
        GamePlay.resize(1067, 764)
        self.centralwidget = QtWidgets.QWidget(parent=GamePlay)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.question_content = QtWidgets.QLabel(parent=self.widget)
        self.question_content.setStyleSheet("QLabel {\n"
"    font: 36pt \"Sitka\";\n"
"    font: 28pt \"Poor Richard\";\n"
"    border-radius: 25px;  /* Điều chỉnh độ bo tròn */\n"
"    background-color: #3498db; /* Màu nền */\n"
"    color: white; /* Màu chữ */\n"
"    padding: 10px;\n"
"    border: 2px solid #2980b9; /* Viền */\n"
"    font: 28pt \"Palatino Linotype\";\n"
"}\n"
"")
        self.question_content.setObjectName("question_content")
        self.gridLayout.addWidget(self.question_content, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget, 1, 0, 1, 5)
        self.widget_6 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.next_button = QtWidgets.QPushButton(parent=self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.next_button.setFont(font)
        self.next_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.next_button.setObjectName("next_button")
        self.gridLayout_6.addWidget(self.next_button, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_6, 2, 4, 1, 1)
        self.widget_7 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.goi_nguoi_than_button = QtWidgets.QPushButton(parent=self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.goi_nguoi_than_button.setFont(font)
        self.goi_nguoi_than_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.goi_nguoi_than_button.setStyleSheet("QPushButton {\n"
"    border-radius: 25px; /* Bo góc mềm mại */\n"
" /* Màu đỏ chủ đạo */\n"
"    \n"
"    background-color: rgb(255, 85, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    padding: 10px 20px; /* Khoảng cách nội dung thoải mái hơn */\n"
"    border: 2px solid rgb(180, 0, 0); /* Viền màu đỏ đậm */\n"
"    font-weight: bold; /* Chữ đậm hơn */\n"
"    font-size: 22px; /* Chữ lớn hơn để dễ nhìn */\n"
"    transition: background-color 0.3s, transform 0.1s; /* Hiệu ứng mượt mà */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     /* Màu đỏ sáng hơn khi hover */\n"
"    background-color: rgb(255, 162, 2);\n"
"    color: white; /* Chữ trắng khi hover để tạo độ tương phản */\n"
"    transform: scale(1.05); /* Hiệu ứng phóng to nhẹ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 0, 0); /* Màu đỏ sậm hơn khi nhấn */\n"
"    border: 2px solid rgb(140, 0, 0); /* Viền đậm hơn */\n"
"    transform: scale(0.95); /* Nhấn nút sẽ thu nhỏ nhẹ */\n"
"}\n"
"\n"
"QPushButton::icon {\n"
"    color: white; /* Màu icon trắng để nổi bật trên nền đỏ */\n"
"}\n"
"")
        self.goi_nguoi_than_button.setAutoRepeat(False)
        self.goi_nguoi_than_button.setAutoExclusive(False)
        self.goi_nguoi_than_button.setObjectName("goi_nguoi_than_button")
        self.gridLayout_5.addWidget(self.goi_nguoi_than_button, 0, 0, 1, 1)
        self.ti_le_50_50_button = QtWidgets.QPushButton(parent=self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.ti_le_50_50_button.setFont(font)
        self.ti_le_50_50_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ti_le_50_50_button.setStyleSheet("QPushButton {\n"
"    border-radius: 25px; /* Bo góc mềm mại */\n"
" /* Màu vàng chủ đạo */\n"
"    background-color: rgb(255, 255, 0);\n"
"    color: rgb(50, 50, 50); /* Màu chữ đậm, dễ đọc hơn */\n"
"    padding: 10px 20px; /* Khoảng cách nội dung thoải mái hơn */\n"
"    border: 2px solid rgb(200, 200, 0); /* Viền màu vàng đậm */\n"
"    font-weight: bold; /* Chữ đậm hơn */\n"
"    font-size: 22px; /* Chữ lớn hơn để dễ nhìn */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: white; /* Chữ trắng khi hover để tạo độ tương phản */\n"
"    transform: scale(1.05); /* Hiệu ứng phóng to nhẹ */\n"
"    \n"
"    background-color: rgb(213, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(190, 190, 0); /* Màu vàng sậm hơn khi nhấn */\n"
"    border: 2px solid rgb(170, 170, 0); /* Viền đậm hơn */\n"
"}\n"
"\n"
"QPushButton::icon {\n"
"    color: black; /* Màu icon đen để nổi bật */\n"
"}\n"
"")
        self.ti_le_50_50_button.setAutoRepeat(False)
        self.ti_le_50_50_button.setAutoExclusive(False)
        self.ti_le_50_50_button.setObjectName("ti_le_50_50_button")
        self.gridLayout_5.addWidget(self.ti_le_50_50_button, 0, 1, 1, 1)
        self.hoi_khan_gia_button = QtWidgets.QPushButton(parent=self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.hoi_khan_gia_button.setFont(font)
        self.hoi_khan_gia_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.hoi_khan_gia_button.setStyleSheet("QPushButton {\n"
"    border-radius: 25px; /* Bo góc mềm mại */\n"
"    background-color: rgb(120, 220, 100); /* Xanh lá nhạt, dịu mắt */\n"
"    color: rgb(30, 30, 30); /* Màu chữ tối để dễ đọc */\n"
"    padding: 10px 20px; /* Tăng khoảng cách giúp nút bấm rõ ràng */\n"
"    border: 2px solid rgb(50, 150, 50); /* Viền xanh đậm hơn để tạo độ nổi */\n"
"    font-weight: bold; /* Chữ đậm hơn để nổi bật */\n"
"    font-size: 22px; /* Chữ lớn hơn giúp dễ nhìn */\n"
"    transition: background-color 0.3s, transform 0.1s; /* Hiệu ứng mượt mà */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 0); /* Xanh lá đậm khi hover */\n"
"    color: white; /* Chữ trắng khi hover để tạo độ tương phản */\n"
"    transform: scale(1.05); /* Hiệu ứng phóng to nhẹ */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 130, 0); /* Xanh lá đậm hơn khi nhấn */\n"
"    border: 2px solid rgb(0, 100, 0); /* Viền đậm hơn để tạo hiệu ứng nhấn */\n"
"    transform: scale(0.95); /* Nhấn nút sẽ thu nhỏ nhẹ để cảm giác bấm thật hơn */\n"
"}\n"
"\n"
"QPushButton::icon {\n"
"    color: black; /* Icon màu đen để rõ hơn */\n"
"}\n"
"")
        self.hoi_khan_gia_button.setAutoRepeat(False)
        self.hoi_khan_gia_button.setAutoExclusive(False)
        self.hoi_khan_gia_button.setObjectName("hoi_khan_gia_button")
        self.gridLayout_5.addWidget(self.hoi_khan_gia_button, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.widget_7, 3, 0, 1, 5)
        self.widget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.dap_an_3_button = QtWidgets.QPushButton(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.dap_an_3_button.setFont(font)
        self.dap_an_3_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.dap_an_3_button.setStyleSheet("QPushButton {\n"
"    border-radius: 15px; /* Điều chỉnh độ bo tròn */\n"
"    background-color: #3498db; /* Màu nền */\n"
"    color: white; /* Màu chữ */\n"
"    padding: 10px 20px; /* Khoảng cách nội dung */\n"
"    border: 2px solid #2980b9; /* Viền */\n"
"    font-size: 16px; /* Cỡ chữ */\n"
"    font-weight: bold; /* Chữ đậm */\n"
"    transition: background-color 0.3s, transform 0.1s, box-shadow 0.2s; /* Hiệu ứng mượt */\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 25px; /* Nếu nút có chiều cao 50px */\n"
"}\n"
"\n"
"/* Hiệu ứng hover - Thêm bóng đổ để nút nổi lên */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* Màu xanh đậm hơn khi hover */\n"
"    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Tạo bóng đổ */\n"
"    transform: scale(1.05); /* Phóng to nhẹ khi di chuột vào */\n"
"}\n"
"\n"
"/* Hiệu ứng click */\n"
"QPushButton:pressed {\n"
"    background-color: #1f6690; /* Màu tối hơn khi nhấn */\n"
"    border: 2px solid #16527b; /* Viền tối hơn khi nhấn */\n"
"    transform: scale(0.92); /* Hiệu ứng co lại khi nhấn */\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); /* Bóng mờ nhẹ khi nhấn */\n"
"}\n"
"")
        self.dap_an_3_button.setAutoRepeat(False)
        self.dap_an_3_button.setAutoExclusive(False)
        self.dap_an_3_button.setObjectName("dap_an_3_button")
        self.gridLayout_4.addWidget(self.dap_an_3_button, 2, 0, 1, 1)
        self.dap_an_4_button = QtWidgets.QPushButton(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.dap_an_4_button.setFont(font)
        self.dap_an_4_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.dap_an_4_button.setStyleSheet("QPushButton {\n"
"    border-radius: 15px; /* Điều chỉnh độ bo tròn */\n"
"    background-color: #3498db; /* Màu nền */\n"
"    color: white; /* Màu chữ */\n"
"    padding: 10px 20px; /* Khoảng cách nội dung */\n"
"    border: 2px solid #2980b9; /* Viền */\n"
"    font-size: 16px; /* Cỡ chữ */\n"
"    font-weight: bold; /* Chữ đậm */\n"
"    transition: background-color 0.3s, transform 0.1s, box-shadow 0.2s; /* Hiệu ứng mượt */\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 25px; /* Nếu nút có chiều cao 50px */\n"
"}\n"
"\n"
"/* Hiệu ứng hover - Thêm bóng đổ để nút nổi lên */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* Màu xanh đậm hơn khi hover */\n"
"    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Tạo bóng đổ */\n"
"    transform: scale(1.05); /* Phóng to nhẹ khi di chuột vào */\n"
"}\n"
"\n"
"/* Hiệu ứng click */\n"
"QPushButton:pressed {\n"
"    background-color: #1f6690; /* Màu tối hơn khi nhấn */\n"
"    border: 2px solid #16527b; /* Viền tối hơn khi nhấn */\n"
"    transform: scale(0.92); /* Hiệu ứng co lại khi nhấn */\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); /* Bóng mờ nhẹ khi nhấn */\n"
"}\n"
"")
        self.dap_an_4_button.setAutoRepeat(False)
        self.dap_an_4_button.setAutoExclusive(False)
        self.dap_an_4_button.setObjectName("dap_an_4_button")
        self.gridLayout_4.addWidget(self.dap_an_4_button, 2, 1, 1, 1)
        self.dap_an_1_button = QtWidgets.QPushButton(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.dap_an_1_button.setFont(font)
        self.dap_an_1_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.dap_an_1_button.setStyleSheet("QPushButton {\n"
"    border-radius: 15px; /* Điều chỉnh độ bo tròn */\n"
"    background-color: #3498db; /* Màu nền */\n"
"    color: white; /* Màu chữ */\n"
"    padding: 10px 20px; /* Khoảng cách nội dung */\n"
"    border: 2px solid #2980b9; /* Viền */\n"
"    font-size: 16px; /* Cỡ chữ */\n"
"    font-weight: bold; /* Chữ đậm */\n"
"    transition: background-color 0.3s, transform 0.1s, box-shadow 0.2s; /* Hiệu ứng mượt */\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 25px; /* Nếu nút có chiều cao 50px */\n"
"}\n"
"\n"
"/* Hiệu ứng hover - Thêm bóng đổ để nút nổi lên */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* Màu xanh đậm hơn khi hover */\n"
"    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Tạo bóng đổ */\n"
"    transform: scale(1.05); /* Phóng to nhẹ khi di chuột vào */\n"
"}\n"
"\n"
"/* Hiệu ứng click */\n"
"QPushButton:pressed {\n"
"    background-color: #1f6690; /* Màu tối hơn khi nhấn */\n"
"    border: 2px solid #16527b; /* Viền tối hơn khi nhấn */\n"
"    transform: scale(0.92); /* Hiệu ứng co lại khi nhấn */\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); /* Bóng mờ nhẹ khi nhấn */\n"
"}\n"
"")
        self.dap_an_1_button.setAutoRepeat(False)
        self.dap_an_1_button.setAutoExclusive(False)
        self.dap_an_1_button.setObjectName("dap_an_1_button")
        self.gridLayout_4.addWidget(self.dap_an_1_button, 0, 0, 1, 1)
        self.dap_an_2_button = QtWidgets.QPushButton(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.dap_an_2_button.setFont(font)
        self.dap_an_2_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.dap_an_2_button.setStyleSheet("QPushButton {\n"
"    border-radius: 15px; /* Điều chỉnh độ bo tròn */\n"
"    background-color: #3498db; /* Màu nền */\n"
"    color: white; /* Màu chữ */\n"
"    padding: 10px 20px; /* Khoảng cách nội dung */\n"
"    border: 2px solid #2980b9; /* Viền */\n"
"    font-size: 16px; /* Cỡ chữ */\n"
"    font-weight: bold; /* Chữ đậm */\n"
"    transition: background-color 0.3s, transform 0.1s, box-shadow 0.2s; /* Hiệu ứng mượt */\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 25px; /* Nếu nút có chiều cao 50px */\n"
"}\n"
"\n"
"/* Hiệu ứng hover - Thêm bóng đổ để nút nổi lên */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* Màu xanh đậm hơn khi hover */\n"
"    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Tạo bóng đổ */\n"
"    transform: scale(1.05); /* Phóng to nhẹ khi di chuột vào */\n"
"}\n"
"\n"
"/* Hiệu ứng click */\n"
"QPushButton:pressed {\n"
"    background-color: #1f6690; /* Màu tối hơn khi nhấn */\n"
"    border: 2px solid #16527b; /* Viền tối hơn khi nhấn */\n"
"    transform: scale(0.92); /* Hiệu ứng co lại khi nhấn */\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); /* Bóng mờ nhẹ khi nhấn */\n"
"}\n"
"")
        self.dap_an_2_button.setAutoRepeat(False)
        self.dap_an_2_button.setAutoExclusive(False)
        self.dap_an_2_button.setObjectName("dap_an_2_button")
        self.gridLayout_4.addWidget(self.dap_an_2_button, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_4, 2, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 2, 1, 1)
        self.reward_label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.reward_label.setFont(font)
        self.reward_label.setStyleSheet("QLabel {\n"
"    font: 36pt \"Sitka\";\n"
"    font: 28pt \"Poor Richard\";\n"
"    border-radius: 25px;  /* Điều chỉnh độ bo tròn */\n"
"    background-color: brown; /* Màu nền */\n"
"    color: yellow; /* Màu chữ */\n"
"    padding: 10px;\n"
"    border: 2px solid #2980b9; /* Viền */\n"
"    font: 15pt \"Palatino Linotype\";\n"
"}\n"
"")
        self.reward_label.setObjectName("reward_label")
        self.gridLayout_7.addWidget(self.reward_label, 0, 3, 1, 2)
        self.label_reward = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_reward.setText("")
        self.label_reward.setObjectName("label_reward")
        self.gridLayout_7.addWidget(self.label_reward, 0, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.back_button = QtWidgets.QPushButton(parent=self.widget_2)
        self.back_button.setStyleSheet("QPushButton {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #FFD700; /* Màu vàng */\n"
"    background-color: #FFFFFF; /* Màu trắng */\n"
"    border: 3px solid #FFD700; /* Viền vàng */\n"
"    border-radius: 25px; /* Bo tròn */\n"
"    padding: 10px 20px;\n"
"    min-width: 120px;\n"
"    text-transform: uppercase;\n"
"    letter-spacing: 1px;\n"
"    outline: none;\n"
"    transition: all 0.3s ease-in-out;\n"
"}\n"
"\n"
"/* Hiệu ứng hover - Nền chuyển sang vàng nhạt pha trắng */\n"
"QPushButton:hover {\n"
"    background-color: #FFF8DC; /* Vàng nhạt lai với trắng */\n"
"    border: 3px solid #FFEE58; /* Viền vàng sáng hơn */\n"
"    box-shadow: 0px 0px 10px rgba(255, 215, 0, 0.6);\n"
"}\n"
"\n"
"/* Hiệu ứng khi nhấn */\n"
"QPushButton:pressed {\n"
"    background-color: #F5DEB3; /* Màu be vàng nhẹ hơn */\n"
"    border: 3px solid #FFCC00; /* Viền vàng đậm */\n"
"    box-shadow: 0px 0px 5px rgba(255, 215, 0, 0.5);\n"
"    transform: scale(0.95);\n"
"}\n"
"\n"
"/* Nút bị vô hiệu hóa */\n"
"QPushButton:disabled {\n"
"    background-color: #555555; /* Xám */\n"
"    border: 3px solid #777777;\n"
"    color: #999999;\n"
"}\n"
"")
        self.back_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\admin\\Documents\\GitHub\\ai-la-trieu-phu\\ui\\assets/image/back_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QtCore.QSize(70, 30))
        self.back_button.setObjectName("back_button")
        self.gridLayout_2.addWidget(self.back_button, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget_2, 0, 0, 1, 1)
        GamePlay.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=GamePlay)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1067, 21))
        self.menubar.setObjectName("menubar")
        GamePlay.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=GamePlay)
        self.statusbar.setObjectName("statusbar")
        GamePlay.setStatusBar(self.statusbar)

        self.retranslateUi(GamePlay)
        QtCore.QMetaObject.connectSlotsByName(GamePlay)

    def retranslateUi(self, GamePlay):
        _translate = QtCore.QCoreApplication.translate
        GamePlay.setWindowTitle(_translate("GamePlay", "GamePlay"))
        self.question_content.setText(_translate("GamePlay", "<html><head/><body><p><span style=\" font-size:16pt;\">Câu hỏi</span></p></body></html>"))
        self.next_button.setText(_translate("GamePlay", "Đi Tiếp"))
        self.goi_nguoi_than_button.setText(_translate("GamePlay", "Gọi người thân 📞"))
        self.ti_le_50_50_button.setText(_translate("GamePlay", "50:50 🔢"))
        self.hoi_khan_gia_button.setText(_translate("GamePlay", "Hỏi khán giả 👥"))
        self.dap_an_3_button.setText(_translate("GamePlay", "Đáp án 3"))
        self.dap_an_4_button.setText(_translate("GamePlay", "Đáp án 4"))
        self.dap_an_1_button.setText(_translate("GamePlay", "Đáp án 1"))
        self.dap_an_2_button.setText(_translate("GamePlay", "Đáp án 2"))
        self.reward_label.setText(_translate("GamePlay", "Tiền thưởng hiện tại: 0 VND"))
