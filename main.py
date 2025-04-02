from application import Application
from sql_connect import DataBase
from task_engine import Task

from PySide6.QtWidgets import QApplication
from user_interface import Ui
import sys

if __name__ == '__main__':
    appp = QApplication(sys.argv)
    db = DataBase(
        database='task_tracker',
        user='docker',
        password='docker',
        host='localhost'
    )
    if db.is_connected():

        task = Task()
        ui = Ui()
        app = Application(
            db,
            ui,
            task
        )

        app.start()
        sys.exit(appp.exec())





