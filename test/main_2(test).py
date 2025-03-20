import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QApplication
from ui.mainwindow import Ui_MainWindow
from ui.mainwindowext import MW_Extend, GamePlayWindow, Login, DatabaseManager


app = QApplication.instance()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    db_manager = DatabaseManager()
    main_window = MW_Extend()  # Tạo đối tượng chính trước
    login = Login(main_window, db_manager)  # Truyền main_window vào Login
    sys.exit(app.exec())

