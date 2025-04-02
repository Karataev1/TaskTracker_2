from sql_connect import DataBase
from user_interface import Ui
from task_engine import Task

class Application:

    def __init__(self,
                 db: DataBase,
                 ui: Ui,
                 task: Task):

        self.ui = ui
        self.task = task
        self.task.database = db
        self.ui.task = task


    def start(self):

        self.ui.install_forms()
        self.ui.show_form('task_list')
        self.ui.task_list.update_list()