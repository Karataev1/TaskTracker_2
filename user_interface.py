from form_tasklist import Ui_MainWindow
from form_addtask import Ui_AddTaskForm
from form_edittask import Ui_EditTaskForm
from PySide6.QtWidgets import QMainWindow

class Ui:
    def __init__(self):

        self.task = None
        self.ui_selected_task_index = None # Держит в себе ID выбранного элемента для изменения задачи
        self.task_ids_from_the_database : dict[str, list] = {"ItemTaskId": []} # Хранит ID задач из базы данных

        self.task_list = None
        self.add_task = None
        self.edit_task = None


    def install_forms(self):
        from class_tasklist import TaskListUI
        self.task_list = TaskListUI(self, self.task)

        from class_addtask import AddTaskUI
        self.add_task = AddTaskUI(self, self.task, self.task_list)

        from class_edittask import EditTaskUI
        self.edit_task = EditTaskUI(self, self.task, self.task_list)


    def show_form(self,form='task_list'):

        form_name = {
            'task_list': lambda: self.task_list.ui_form.show(),
            'add_task': lambda: self.add_task.ui_form.show(),
            'edit_task': lambda: self.edit_task.ui_form.show()

        }
        show_form = form_name.get(form)
        show_form()



class Ui_TaskList(QMainWindow):
    def __init__(self):
        super(Ui_TaskList, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Ui_AddTask(QMainWindow):
    def __init__(self,parent=None):
        super(Ui_AddTask, self).__init__(parent)
        self.ui = Ui_AddTaskForm()
        self.ui.setupUi(self)


class Ui_EditTask(QMainWindow):
    def __init__(self,parent=None):
        super(Ui_EditTask, self).__init__(parent)
        self.ui = Ui_EditTaskForm()
        self.ui.setupUi(self)



