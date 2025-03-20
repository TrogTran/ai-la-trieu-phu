import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from .mainwindow import Ui_MainWindow  # Chỉ cần import 1 lần
from .gameplay import Ui_GamePlay  # Import đúng cách
from .Login import Ui_Login
from .register import Ui_Register
import ctypes
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl, QTimer
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow, QPushButton
import os, pygame
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt  # Đảm bảo đã import Qt
from pymongo import MongoClient, errors
import bcrypt
import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox
from PyQt6 import uic
from PyQt6.QtMultimedia import QSoundEffect  # Đã có sẵn, dùng cho hiệu ứng âm thanh
import json  # Để đọc file câu hỏi từ ngân hàng
#Tạo lớp DatabaseManager để quản lý kết nối MongoDB
class DatabaseManager:
    def __init__(self):
        try:
            self.client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
            self.client.server_info()  # Kiểm tra kết nối
            self.db = self.client["login_data"]
            self.users_collection = self.db["username_and_password"]
            self.progress_collection = self.db["player_progress"]
            self.questions_collection = self.db["questions_bank"]
        except errors.ServerSelectionTimeoutError:
            raise Exception("Không thể kết nối đến MongoDB. Vui lòng kiểm tra lại!")

    def get_client(self):
        return self.client

    def get_db(self):
        return self.db

    def get_users_collection(self):
        return self.users_collection

    def get_progress_collection(self):
        return self.progress_collection

    def get_questions_collection(self):
        return self.questions_collection
#Cửa sổ register
class RegisterWindow(QMainWindow, Ui_Register):
    def __init__(self, login_window, db_manager):
        super().__init__()
        self.setupUi(self)
        self.db_manager = db_manager  # Lưu db_manager
        self.users_collection = self.db_manager.get_users_collection()
        # Thêm hình nền
        self.background_label = QLabel(self)
        self.set_background()
        self.login_window = login_window

        # Kết nối nút Register với hàm xử lý đăng ký
        self.pushButton_register.clicked.connect(self.register_user)
        self.pushButton_back.clicked.connect(self.Return_Login)

                            # # Kết nối MongoDB với xử lý lỗi
                            # try:
                            #     self.client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
                            #     self.db = self.client["login_data"]  # Đổi tên database
                            #     self.users_collection = self.db["username_and_password"]  # Đổi tên collection
                            #     # Kiểm tra kết nối MongoDB
                            #     self.client.server_info()
                            # except errors.ServerSelectionTimeoutError:
                            #     QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến MongoDB. Hãy kiểm tra lại!")
                            #     self.close()  # Đóng cửa sổ nếu không có kết nối

    def register_user(self):
        """Xử lý đăng ký tài khoản"""
        username = self.lineEdit_register_username.text().strip()
        password = self.lineEdit_register_password.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ Username và Password!")
            return

        # Kiểm tra username đã tồn tại chưa
        if self.users_collection.find_one({"username": username}):
            QMessageBox.warning(self, "Lỗi", "Username đã tồn tại! Hãy chọn username khác.")
            return

        # Mã hóa mật khẩu và lưu
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        try:
            self.users_collection.insert_one({
                "username": username,
                "password": hashed_password
            })
            QMessageBox.information(self, "Thành công", "Đăng ký thành công, vui lòng nhấn nút BACK để đăng nhập!")
            self.lineEdit_register_username.clear()
            self.lineEdit_register_password.clear()
        except errors.PyMongoError as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi lưu dữ liệu vào MongoDB: {str(e)}")


    def Return_Login(self):
        self.close()
        self.login_window.show()

    def set_background(self):
        """ Thiết lập hình nền bằng QLabel """
        image_path = os.path.join(os.path.dirname(__file__), "assets/image/imgailatrieuphu1.jpg")

        if not os.path.exists(image_path):
            print("Không tìm thấy ảnh nền!")
            return

        # Đặt QLabel làm nền
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        # Cập nhật hình nền sau khi cửa sổ hiển thị
        QtCore.QTimer.singleShot(100, self.update_background)

        # Đưa QLabel ra sau các widget khác
        self.background_label.lower()

    def update_background(self):
        """ Cập nhật lại hình nền khi thay đổi kích thước """
        image_path = os.path.join(os.path.dirname(__file__), "assets/image/imgailatrieuphu1.jpg")

        if os.path.exists(image_path):
            # Lấy kích thước cửa sổ
            window_width = self.width()
            window_height = self.height()

            # Load ảnh và scale theo tỉ lệ giữ nguyên (KeepAspectRatio)
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(window_width, window_height, Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)

            # Tính toán tọa độ để căn giữa
            x = (window_width - scaled_pixmap.width()) // 2
            y = (window_height - scaled_pixmap.height()) // 2

            # Hiển thị hình ảnh lên QLabel
            self.background_label.setPixmap(scaled_pixmap)
            self.background_label.setGeometry(x, y, scaled_pixmap.width(), scaled_pixmap.height())  # Đặt lại vị trí

    def resizeEvent(self, event):
        """ Cập nhật hình nền khi thay đổi kích thước cửa sổ """
        self.update_background()
        super().resizeEvent(event)

#Cửa sổ login
class Login(QMainWindow, Ui_Login):
    def __init__(self, main_window, db_manager):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.db_manager = db_manager  # Lưu db_manager
        self.users_collection = self.db_manager.get_users_collection()  # Sử dụng db_manager
        self.background_label = QLabel(self)
        self.set_background()
        self.pushButton_register.clicked.connect(self.show_register)
        self.pushButton_forgot_password.clicked.connect(self.forgot_password)


                                # try:
                                #     self.client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
                                #     self.db = self.client["login_data"]  # Database giống với RegisterWindow
                                #     self.users_collection = self.db["username_and_password"]  # Collection giống với RegisterWindow
                                #     self.client.server_info()  # Kiểm tra kết nối
                                # except errors.ServerSelectionTimeoutError:
                                #     QMessageBox.critical(self, "Lỗi", "Không thể kết nối đến MongoDB. Hãy kiểm tra lại!")
                                #     self.close()

            # Kết nối nút login với hàm xử lý đăng nhập
        self.pushButton_login.clicked.connect(self.login_user)

    def login_user(self):
        """Xử lý đăng nhập"""
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()

        user = self.db_manager.get_users_collection().find_one({"username": username})

        if not user:
            QMessageBox.warning(self, "Lỗi", "Username không tồn tại!")
            return

        if bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
            QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
            self.open_main_window()
        else:
            QMessageBox.warning(self, "Lỗi", "Sai mật khẩu! Vui lòng thử lại.")

    def open_main_window(self):
        self.close()
        self.main_window.show()
    def show_register(self):
        self.register_window = RegisterWindow(self, self.db_manager)  # Tạo cửa sổ đăng ký
        self.register_window.show()  # Hiển thị cửa sổ đăng ký
        self.close()

    def set_background(self):
        """ Thiết lập hình nền bằng QLabel """
        image_path = os.path.join(os.path.dirname(__file__), "assets/image/imgailatrieuphu1.jpg")

        if not os.path.exists(image_path):
            print("Không tìm thấy ảnh nền!")
            return

        # Đặt QLabel làm nền
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        # Cập nhật hình nền sau khi cửa sổ hiển thị
        QtCore.QTimer.singleShot(100, self.update_background)

        # Đưa QLabel ra sau các widget khác
        self.background_label.lower()

    def update_background(self):
        """ Cập nhật lại hình nền khi thay đổi kích thước """
        image_path = os.path.join(os.path.dirname(__file__), "assets/image/imgailatrieuphu1.jpg")

        if os.path.exists(image_path):
            # Lấy kích thước cửa sổ
            window_width = self.width()
            window_height = self.height()

            # Load ảnh và scale theo tỉ lệ giữ nguyên (KeepAspectRatio)
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(window_width, window_height, Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)

            # Tính toán tọa độ để căn giữa
            x = (window_width - scaled_pixmap.width()) // 2
            y = (window_height - scaled_pixmap.height()) // 2

            # Hiển thị hình ảnh lên QLabel
            self.background_label.setPixmap(scaled_pixmap)
            self.background_label.setGeometry(x, y, scaled_pixmap.width(), scaled_pixmap.height())  # Đặt lại vị trí

    def resizeEvent(self, event):
        """ Cập nhật hình nền khi thay đổi kích thước cửa sổ """
        self.update_background()
        super().resizeEvent(event)

    def forgot_password(self):
        """Xử lý đổi mật khẩu trong SettingsWindow"""

        # Nhập username
        username, ok = QtWidgets.QInputDialog.getText(self, "Đổi Mật Khẩu", "Nhập Username:")
        if not ok or not username.strip():
            return


        # Nhập mật khẩu mới
        new_password, ok = QtWidgets.QInputDialog.getText(
            self, "Đổi Mật Khẩu", "Nhập mật khẩu mới:", QtWidgets.QLineEdit.EchoMode.Password
        )
        if not ok or not new_password.strip():
            return

        # Xác nhận mật khẩu mới
        confirm_password, ok = QtWidgets.QInputDialog.getText(
            self, "Đổi Mật Khẩu", "Xác nhận mật khẩu mới:", QtWidgets.QLineEdit.EchoMode.Password
        )
        if not ok or new_password != confirm_password:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Mật khẩu xác nhận không khớp!")
            return

        # Kiểm tra username có tồn tại không
        user = self.users_collection.find_one({"username": username})
        if not user:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Username không tồn tại!")
            return

        # Băm mật khẩu mới và cập nhật vào MongoDB
        hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        try:
            self.users_collection.update_one({"username": username}, {"$set": {"password": hashed_new_password}})
            QtWidgets.QMessageBox.information(self, "Thành công", "Mật khẩu đã được cập nhật thành công!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi", f"Lỗi khi cập nhật mật khẩu: {str(e)}")

# Cửa sổ Gameplay
class GamePlayWindow(QMainWindow, Ui_GamePlay):
    def __init__(self, main_window, db_manager, username):
        super().__init__()
        self.setupUi(self)
        self.db_manager = db_manager
        self.username = username
        self.background_label = QLabel(self)
        self.set_background()
        self.main_window = main_window
        self.back_button.clicked.connect(self.Return_MainWindow)
        self.progress_collection = self.db_manager.get_progress_collection()
        self.questions_collection = self.db_manager.get_questions_collection()

        # Khởi tạo âm thanh
        self.correct_sound = QSoundEffect()
        self.correct_sound.setSource(QUrl.fromLocalFile("assets/sound/correct.wav"))
        self.wrong_sound = QSoundEffect()
        self.wrong_sound.setSource(QUrl.fromLocalFile("assets/sound/wrong.mp3"))

        # Danh sách phần thưởng
        self.rewards = [10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000,
                        20000000, 50000000, 100000000, 200000000, 500000000]
        self.language = "vi"

        # Khởi tạo các biến trạng thái trợ giúp
        self.used_50_50 = False
        self.used_goi_nguoi_than = False
        self.used_hoi_khan_gia = False

        # Khởi tạo biến gameplay
        self.current_question = 0
        self.correct_answers = 0
        self.reward = 0

        # Liên kết các nút đáp án
        self.dap_an_1_button.clicked.connect(lambda: self.kiem_tra_dap_an(0))
        self.dap_an_2_button.clicked.connect(lambda: self.kiem_tra_dap_an(1))
        self.dap_an_3_button.clicked.connect(lambda: self.kiem_tra_dap_an(2))
        self.dap_an_4_button.clicked.connect(lambda: self.kiem_tra_dap_an(3))
        self.ti_le_50_50_button.clicked.connect(self.su_dung_50_50)
        self.goi_nguoi_than_button.clicked.connect(self.goi_nguoi_than)
        self.hoi_khan_gia_button.clicked.connect(self.hoi_khan_gia)

        # Thêm nút "Đi tiếp" bằng code
        self.next_button.clicked.connect(self.tiep_tuc_cau_hoi)
        self.next_button.setVisible(False)


        # Tải câu hỏi và tiến độ
        if not self.load_questions():
            return
        self.load_progress()
        self.hien_cau_hoi()

    def load_questions(self):
        try:
            self.cau_hoi = list(self.questions_collection.find({"language": self.language}))
            print(f"Loaded {len(self.cau_hoi)} questions for language '{self.language}'")
            if not self.cau_hoi:
                QMessageBox.critical(self, "Lỗi",
                                     f"Không có câu hỏi nào cho ngôn ngữ '{self.language}' trong cơ sở dữ liệu!")
                self.close()
                return False
            return True
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tải câu hỏi: {str(e)}")
            self.close()
            return False

    def load_progress(self):
        progress = self.progress_collection.find_one({"username": self.username})
        if progress:
            self.current_question = progress.get("current_question", 0)
            self.correct_answers = progress.get("correct_answers", 0)
            self.reward = progress.get("reward", 0)
        else:
            self.current_question = 0
            self.correct_answers = 0
            self.reward = 0
            self.save_progress()

    def save_progress(self):
        try:
            self.progress_collection.update_one(
                {"username": self.username},
                {"$set": {"current_question": self.current_question, "correct_answers": self.correct_answers,
                          "reward": self.reward}},
                upsert=True
            )
        except Exception as e:
            print(f"Error saving progress: {str(e)}")

    def hien_cau_hoi(self):
        if not self.cau_hoi:
            QMessageBox.critical(self, "Lỗi", "Không có câu hỏi nào để hiển thị!")
            self.close()
            return
        if self.current_question < len(self.cau_hoi):
            question_data = self.cau_hoi[self.current_question]
            self.question_content.setText(question_data["question"])
            self.dap_an_1_button.setText(question_data["answers"][0])
            self.dap_an_2_button.setText(question_data["answers"][1])
            self.dap_an_3_button.setText(question_data["answers"][2])
            self.dap_an_4_button.setText(question_data["answers"][3])
            self.reward_label.setText(f"Tiền thưởng hiện tại: {self.reward:,} VND")  # Chỉ dùng reward_label
            self.dap_an_1_button.setVisible(True)
            self.dap_an_2_button.setVisible(True)
            self.dap_an_3_button.setVisible(True)
            self.dap_an_4_button.setVisible(True)
            self.dap_an_1_button.setStyleSheet("")
            self.dap_an_2_button.setStyleSheet("")
            self.dap_an_3_button.setStyleSheet("")
            self.dap_an_4_button.setStyleSheet("")
            self.update_help_buttons()
            self.next_button.setVisible(False)
        else:
            self.hien_thong_bao()

    def kiem_tra_dap_an(self, answer_index):
        question_data = self.cau_hoi[self.current_question]
        buttons = [self.dap_an_1_button, self.dap_an_2_button, self.dap_an_3_button, self.dap_an_4_button]
        print(f"Selected: {answer_index}, Correct: {question_data['correct']}")
        if answer_index == question_data["correct"]:
            print("Correct answer!")
            self.correct_answers += 1
            self.reward = self.rewards[self.correct_answers - 1] if self.correct_answers <= len(self.rewards) else \
                self.rewards[-1]
            try:
                self.correct_sound.play()
            except Exception as e:
                print(f"Error playing correct sound: {str(e)}")
            # Áp dụng stylesheet đầy đủ
            buttons[answer_index].setStyleSheet("""
                background-color: green;
                color: white;
                font-size: 15px;
                border-radius: 15px;
                border: 2px solid #2980b9;
                padding: 10px 20px;
            """)
            buttons[answer_index].update()  # Buộc cập nhật giao diện
            self.reward_label.setText(f"Tiền thưởng hiện tại: {self.reward:,} VND")
            self.next_button.setVisible(True)
            QTimer.singleShot(100, lambda: [btn.setEnabled(False) for btn in buttons])
        else:
            print("Wrong answer!")
            buttons[answer_index].setStyleSheet("""
                background-color: red;
                color: white;
                font-size: 15px;
                border-radius: 15px;
                border: 2px solid #2980b9;
                padding: 10px 20px;
            """)
            buttons[answer_index].update()
            try:
                self.wrong_sound.play()
            except Exception as e:
                print(f"Error playing wrong sound: {str(e)}")
            self.hien_thong_bao_sai()

    def tiep_tuc_cau_hoi(self):
        self.current_question += 1
        self.save_progress()
        self.hien_cau_hoi()
        buttons = [self.dap_an_1_button, self.dap_an_2_button, self.dap_an_3_button, self.dap_an_4_button]
        for btn in buttons:
            btn.setEnabled(True)

    def hien_thong_bao(self):
        msg = QMessageBox()
        msg.setText(
            f"Chúc mừng! Bạn đã trả lời đúng {self.correct_answers}/{len(self.cau_hoi)} câu. Phần thưởng: {self.reward:,} VND")
        msg.exec()
        self.reset_game()

    def hien_thong_bao_sai(self):
        msg = QMessageBox()
        msg.setText(
            f"Đáp án sai! Bạn đã trả lời đúng {self.correct_answers}/{len(self.cau_hoi)} câu. Phần thưởng: {self.reward:,} VND")
        msg.exec()
        self.reset_game()

    def reset_game(self):
        self.current_question = 0
        self.correct_answers = 0
        self.reward = 0
        self.used_50_50 = False
        self.used_goi_nguoi_than = False
        self.used_hoi_khan_gia = False
        self.save_progress()
        self.hien_cau_hoi()

    def update_help_buttons(self):
        self.ti_le_50_50_button.setVisible(not self.used_50_50)
        self.goi_nguoi_than_button.setVisible(not self.used_goi_nguoi_than)
        self.hoi_khan_gia_button.setVisible(not self.used_hoi_khan_gia)

    def resizeEvent(self, event):
        # self.next_button.setGeometry(self.width() - 150, self.height() - 100, 100, 40)
        # self.reward_label.setGeometry(10, 10, 300, 30)
        self.update_background()
        super().resizeEvent(event)

    # Các phương thức khác như su_dung_50_50, goi_nguoi_than, hoi_khan_gia, set_background giữ nguyên
    def su_dung_50_50(self):
        """Xóa ngẫu nhiên 2 đáp án sai và ẩn nút 50:50"""
        question_data = self.cau_hoi[self.current_question]
        correct_answer = question_data["correct"]

        # Lấy danh sách các vị trí đáp án sai
        wrong_answers = [i for i in range(4) if i != correct_answer]
        random.shuffle(wrong_answers)  # Xáo trộn danh sách để chọn ngẫu nhiên

        # Ẩn 2 đáp án sai bằng setVisible
        buttons = [self.dap_an_1_button, self.dap_an_2_button, self.dap_an_3_button, self.dap_an_4_button]
        buttons[wrong_answers[0]].setVisible(False)
        buttons[wrong_answers[1]].setVisible(False)

        # Ẩn nút 50:50 vĩnh viễn
        self.ti_le_50_50_button.setVisible(False)  # ẩn nút
        self.used_50_50 = True  # ghi nhận nút 50:50 đã sử dụng

    def goi_nguoi_than(self):
        """Gợi ý ngẫu nhiên 1 đáp án"""
        question_data = self.cau_hoi[self.current_question]
        random_answer = random.choice(question_data["answers"])  # chọn bất kì 1 trong 4 đáp án

        msg = QMessageBox()
        msg.setWindowTitle("Gợi ý từ người thân")
        msg.setText(f"Theo tôi thì bạn nên chọn đáp án: {random_answer}")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()  # hiển thị hộp thoại

        # Ẩn nút Gọi người thân vĩnh viễn
        self.goi_nguoi_than_button.setVisible(False)  # ẩn
        self.used_goi_nguoi_than = True  # ghi nhận đã sử dụng

    def hoi_khan_gia(self):
        """Hiển thị tỉ lệ phần trăm khán giả chọn các đáp án"""
        question_data = self.cau_hoi[self.current_question]
        correct_answer = question_data["correct"]

        # Chọn phần trăm ngẫu nhiên cho đáp án đúng (49% - 70%)
        correct_percentage = random.randint(49, 70)
        remaining_percentage = 100 - correct_percentage  # Phần trăm dành cho các đáp án sai

        # Lấy danh sách đáp án sai
        wrong_answers = [i for i in range(4) if i != correct_answer]

        # Chia đều phần trăm sai và điều chỉnh nhỏ ngẫu nhiên
        wrong_percentages = self.chia_ti_le_phan_tram(remaining_percentage, len(wrong_answers))

        # Lưu kết quả vào dictionary
        final_percentages = {correct_answer: correct_percentage}
        for idx, percent in zip(wrong_answers, wrong_percentages):
            final_percentages[idx] = percent

        # Hiển thị kết quả
        text = "\n".join(
            [f"{question_data['answers'][idx]}: {final_percentages[idx]}%" for idx in range(4)]
        )

        msg = QMessageBox()
        msg.setWindowTitle("Khán giả bình chọn")
        msg.setText(text)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

        # Ẩn nút Hỏi khán giả vĩnh viễn
        self.hoi_khan_gia_button.setVisible(False)
        self.used_hoi_khan_gia = True

    def chia_ti_le_phan_tram(self, remaining_percentage, so_dap_an_sai):
        """Chia phần trăm còn lại cho các đáp án sai sao cho tổng đúng"""

        # Chia đều trước, rồi điều chỉnh ngẫu nhiên
        base = remaining_percentage // so_dap_an_sai
        percentages = [base] * so_dap_an_sai

        # Phân phối phần dư để đảm bảo tổng đúng
        du = remaining_percentage - sum(percentages)

        for i in range(du):
            percentages[i % so_dap_an_sai] += 1  # Phân bổ phần dư ngẫu nhiên

        random.shuffle(percentages)  # Xáo trộn để tránh quá đều
        return percentages

    def set_background(self):
        """ Thiết lập hình nền bằng QLabel """
        image_path = os.path.join(os.path.dirname(__file__), "assets/image/imgailatrieuphu1.jpg")

        if not os.path.exists(image_path):
            print("Không tìm thấy ảnh nền!")
            return

        # Đặt QLabel làm nền
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        # Cập nhật hình nền sau khi cửa sổ hiển thị
        QtCore.QTimer.singleShot(100, self.update_background)

        # Đưa QLabel ra sau các widget khác
        self.background_label.lower()

    def update_background(self):
        """ Cập nhật lại hình nền khi thay đổi kích thước """
        image_path = os.path.join(os.path.dirname(__file__), "assets/image/imgailatrieuphu1.jpg")

        if os.path.exists(image_path):
            # Lấy kích thước cửa sổ
            window_width = self.width()
            window_height = self.height()

            # Load ảnh và scale theo tỉ lệ giữ nguyên (KeepAspectRatio)
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(window_width, window_height, Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)

            # Tính toán tọa độ để căn giữa
            x = (window_width - scaled_pixmap.width()) // 2
            y = (window_height - scaled_pixmap.height()) // 2

            # Hiển thị hình ảnh lên QLabel
            self.background_label.setPixmap(scaled_pixmap)
            self.background_label.setGeometry(x, y, scaled_pixmap.width(), scaled_pixmap.height())  # Đặt lại vị trí

    def Return_MainWindow(self):
        self.close()  # Đóng cửa sổ gameplay
        self.main_window.show()  # Hiển thị lại cửa sổ chính


# Cửa sổ MainWindow
class MW_Extend(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_manager = DatabaseManager()
        self.login_window = Login(self, self.db_manager)
        self.settings_window = SettingsWindow(self, self.db_manager)
        self.login_window.show()
        self.hide()
        self.background_label = QLabel(self)
        self.set_background()
        self.push_button_bat_dau.clicked.connect(self.showGameplay)
        self.push_button_cai_dat.clicked.connect(self.showSettings)
        self.push_button_thoat.clicked.connect(self.confirm_exit)
        self.push_button_lich_su_choi.clicked.connect(self.show_history)
        

        # Khởi tạo pygame.mixer để phát nhạc
        pygame.mixer.init()

        # Lấy đường dẫn tương đối tới file nhạc
        music_path = os.path.join(os.path.dirname(__file__), "assets/music/back_ground_game.mp3")

        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.5)  # Đặt âm lượng (0.0 - 1.0)
        pygame.mixer.music.play(-1)  # Phát lặp vô hạn

    def show_history(self):
        try:
            username = self.login_window.lineEdit_username.text().strip()
            if not username:
                QMessageBox.warning(self, "Lỗi", "Vui lòng đăng nhập để xem lịch sử!")
                return
            progress = self.db_manager.get_progress_collection().find_one({"username": username})
            if progress:
                message = (f"Lịch sử chơi của {username}:\n"
                           f"Câu hỏi hiện tại: {progress.get('current_question', 0)}\n"
                           f"Số câu đúng: {progress.get('correct_answers', 0)}\n"
                           f"Phần thưởng: {progress.get('reward', 0):,} VND")
                QMessageBox.information(self, "Lịch sử", message)
            else:
                QMessageBox.information(self, "Lịch sử", f"Chưa có lịch sử chơi cho {username}!")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tải lịch sử: {str(e)}")
    def set_background(self):
        """ Thiết lập hình nền bằng QLabel """
        image_path = os.path.join(os.path.dirname(__file__), "assets/image/imgailatrieuphu1.jpg")

        if not os.path.exists(image_path):
            print("Không tìm thấy ảnh nền!")
            return

        # Đặt QLabel làm nền
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        # Cập nhật hình nền sau khi cửa sổ hiển thị
        QtCore.QTimer.singleShot(100, self.update_background)

        # Đưa QLabel ra sau các widget khác
        self.background_label.lower()

    def update_background(self):
        """ Cập nhật lại hình nền khi thay đổi kích thước """
        image_path = os.path.join(os.path.dirname(__file__), "assets/image/imgailatrieuphu1.jpg")

        if os.path.exists(image_path):
            # Lấy kích thước cửa sổ
            window_width = self.width()
            window_height = self.height()

            # Load ảnh và scale theo tỉ lệ giữ nguyên (KeepAspectRatio)
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(window_width, window_height, Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)

            # Tính toán tọa độ để căn giữa
            x = (window_width - scaled_pixmap.width()) // 2
            y = (window_height - scaled_pixmap.height()) // 2

            # Hiển thị hình ảnh lên QLabel
            self.background_label.setPixmap(scaled_pixmap)
            self.background_label.setGeometry(x, y, scaled_pixmap.width(), scaled_pixmap.height())  # Đặt lại vị trí

    def resizeEvent(self, event):
        """ Cập nhật hình nền khi thay đổi kích thước cửa sổ """
        self.update_background()
        super().resizeEvent(event)

    def stop_music(self):
        pygame.mixer.music.stop()  # Dừng nhạc nền

    def confirm_exit(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Xác nhận thoát")
        msg_box.setText("Bạn không muốn làm tỷ phú à?")
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        reply = msg_box.exec()

        if reply == QMessageBox.StandardButton.Yes:
            pygame.mixer.music.stop()
            pygame.quit()  # Dừng tất cả tiến trình PyGame
            QtWidgets.QApplication.quit()  # Đóng toàn bộ Qt
            sys.exit(0)
            sys.exit(1)# Thoát hoàn toàn chương trình

    def closeEvent(self, event):
        self.confirm_exit()  # Gọi xác nhận thoát
        event.ignore()  # Ngăn Qt đóng cửa sổ nếu người dùng nhấn "No"

    def showGameplay(self):
        if not hasattr(self, 'gameplay_window') or self.gameplay_window is None:
            self.gameplay_window = GamePlayWindow(self, self.db_manager, self.login_window.lineEdit_username.text())
        self.hide()
        self.gameplay_window.show()

    def showSettings(self):
        if not hasattr(self, 'settings_window') or self.settings_window is None:
            self.settings_window = SettingsWindow(self, self.db_manager)
        self.hide()
        self.settings_window.show()

    def logout_user(self):
        """Hàm đăng xuất"""
        self.hide()  # Ẩn cửa sổ chính
        self.login_window.show()  # Hiển thị lại cửa sổ đăng nhập

        # Xóa dữ liệu nhập trong ô QLineEdit
        self.login_window.lineEdit_username.clear()
        self.login_window.lineEdit_password.clear()

    def update_theme(self, theme: str):
        """Cập nhật giao diện theo chế độ đã chọn"""
        if theme == "Tối":
            self.setStyleSheet("background-color: #2E2E2E; color: white;")
        elif theme == "Sáng":
            self.setStyleSheet("background-color: white; color: black;")
        else:  # Mặc định
            self.setStyleSheet("")


import ctypes
from PyQt6 import QtWidgets, QtCore
import sys
if sys.platform.startswith('win'):
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    from comtypes import CLSCTX_ALL
from pymongo import MongoClient, errors

class SettingsWindow(QtWidgets.QWidget):
    theme_changed = QtCore.pyqtSignal(str)  # Tín hiệu gửi trạng thái sáng/tối

    def __init__(self, main_window, db_manager):
        super().__init__()
        self.setWindowTitle("Cài Đặt")
        self.main_window = main_window
        self.db_manager = db_manager  # Lưu db_manager
        self.users_collection = self.db_manager.get_users_collection()

        # Khởi tạo layout
        layout = QtWidgets.QVBoxLayout()

        # Thanh trượt điều chỉnh âm lượng
        self.volume_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(self.get_system_volume())  # Lấy âm lượng hiện tại
        self.volume_slider.valueChanged.connect(self.set_system_volume)

        self.volume_label = QtWidgets.QLabel(f"Âm lượng: {self.volume_slider.value()}%")
        self.volume_slider.valueChanged.connect(
            lambda: self.volume_label.setText(f"Âm lượng: {self.volume_slider.value()}%"))

        # ComboBox để chọn giao diện
        self.theme_selector = QtWidgets.QComboBox()
        self.theme_selector.addItems(["Mặc định", "Sáng", "Tối"])
        self.theme_selector.currentTextChanged.connect(self.change_theme)

        # Nút đổi mật khẩu
        self.change_password_button = QtWidgets.QPushButton("Đổi Mật Khẩu")
        self.change_password_button.clicked.connect(self.change_password)

        # Nút đăng xuất
        self.logout_button = QtWidgets.QPushButton("Đăng Xuất")
        self.logout_button.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        self.logout_button.clicked.connect(self.logout)

        # Nút quản lý câu hỏi
        self.question_manager_button = QtWidgets.QPushButton("Quản lý câu hỏi")
        self.question_manager_button.clicked.connect(self.manage_questions)

        # ComboBox chọn ngôn ngữ
        self.language_selector = QtWidgets.QComboBox()
        self.language_selector.addItems(["Tiếng Việt", "English"])
        self.language_selector.currentTextChanged.connect(self.change_language)

        # Thêm các widget vào layout
        layout.addWidget(self.volume_label)
        layout.addWidget(self.volume_slider)
        layout.addWidget(QtWidgets.QLabel("Chọn giao diện:"))
        layout.addWidget(self.theme_selector)
        layout.addWidget(self.change_password_button)
        layout.addWidget(self.logout_button)
        layout.addWidget(self.question_manager_button)
        layout.addWidget(QtWidgets.QLabel("Chọn ngôn ngữ:"))
        layout.addWidget(self.language_selector)

        # Gán layout cho widget
        self.setLayout(layout)

    # Các phương thức khác giữ nguyên, không thay đổi
    def manage_questions(self):
        self.question_window = QuestionManagerWindow(self.main_window, self.db_manager)  # Sửa để truyền db_manager
        self.question_window.show()

    def change_language(self, lang):
        lang_map = {"Tiếng Việt": "vi", "English": "en"}
        if hasattr(self.main_window, 'gameplay_window') and self.main_window.gameplay_window:
            self.main_window.gameplay_window.language = lang_map[lang]
            self.main_window.gameplay_window.load_questions()
            self.main_window.gameplay_window.hien_cau_hoi()

    def get_system_volume(self):
        if not sys.platform.startswith('win'):
            return 50
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)
        return int(volume.GetMasterVolumeLevelScalar() * 100)

    def set_system_volume(self, value):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)
        volume.SetMasterVolumeLevelScalar(value / 100, None)

    def change_theme(self, theme):
        self.theme_changed.emit(theme)

    def change_password(self):
        username, ok = QtWidgets.QInputDialog.getText(self, "Đổi Mật Khẩu", "Nhập Username:")
        if not ok or not username.strip():
            return
        current_password, ok = QtWidgets.QInputDialog.getText(
            self, "Đổi Mật Khẩu", "Nhập mật khẩu hiện tại:", QtWidgets.QLineEdit.EchoMode.Password
        )
        if not ok or not current_password.strip():
            return
        new_password, ok = QtWidgets.QInputDialog.getText(
            self, "Đổi Mật Khẩu", "Nhập mật khẩu mới:", QtWidgets.QLineEdit.EchoMode.Password
        )
        if not ok or not new_password.strip():
            return
        confirm_password, ok = QtWidgets.QInputDialog.getText(
            self, "Đổi Mật Khẩu", "Xác nhận mật khẩu mới:", QtWidgets.QLineEdit.EchoMode.Password
        )
        if not ok or new_password != confirm_password:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Mật khẩu xác nhận không khớp!")
            return
        user = self.users_collection.find_one({"username": username})
        if not user:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Username không tồn tại!")
            return
        if not bcrypt.checkpw(current_password.encode('utf-8'), user["password"].encode('utf-8')):
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Sai mật khẩu hiện tại!")
            return
        hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        try:
            self.users_collection.update_one({"username": username}, {"$set": {"password": hashed_new_password}})
            QtWidgets.QMessageBox.information(self, "Thành công", "Mật khẩu đã được cập nhật thành công!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi", f"Lỗi khi cập nhật mật khẩu: {str(e)}")

    def logout(self):
        confirm = QMessageBox.question(
            self, "Xác nhận đăng xuất", "Bạn có chắc chắn muốn đăng xuất?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            self.main_window.logout_user()
            self.close()


class QuestionManagerWindow(QtWidgets.QWidget):
    def __init__(self, main_window, db_manager):
        super().__init__()
        self.setWindowTitle("Quản lý ngân hàng câu hỏi")
        self.main_window = main_window
        self.db_manager = db_manager
        self.questions_collection = self.db_manager.get_questions_collection()
        # # self.client = MongoClient("mongodb://localhost:27017/")
        # self.db = self.client["login_data"]
        # self.questions_collection = self.db["questions_bank"]

        layout = QtWidgets.QVBoxLayout()

        # Nhập câu hỏi
        self.question_input = QtWidgets.QLineEdit()
        self.question_input.setPlaceholderText("Nhập câu hỏi")
        layout.addWidget(self.question_input)

        # Nhập đáp án
        self.answer_inputs = [QtWidgets.QLineEdit() for _ in range(4)]
        for i, input in enumerate(self.answer_inputs):
            input.setPlaceholderText(f"Đáp án {i + 1}")
            layout.addWidget(input)

        # Chọn đáp án đúng
        self.correct_selector = QtWidgets.QComboBox()
        self.correct_selector.addItems(["Đáp án 1", "Đáp án 2", "Đáp án 3", "Đáp án 4"])
        layout.addWidget(self.correct_selector)

        # Chọn ngôn ngữ
        self.lang_selector = QtWidgets.QComboBox()
        self.lang_selector.addItems(["vi", "en"])
        layout.addWidget(self.lang_selector)

        # Nút thêm câu hỏi
        self.add_button = QtWidgets.QPushButton("Thêm câu hỏi")
        self.add_button.clicked.connect(self.add_question)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_question(self):
        question = self.question_input.text().strip()
        answers = [input.text().strip() for input in self.answer_inputs]
        correct = self.correct_selector.currentIndex()
        language = self.lang_selector.currentText()

        if not question or not all(answers):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        self.questions_collection.insert_one({
            "question": question,
            "answers": answers,
            "correct": correct,
            "language": language
        })
        QMessageBox.information(self, "Thành công", "Câu hỏi đã được thêm!")
        self.question_input.clear()
        for input in self.answer_inputs:
            input.clear()